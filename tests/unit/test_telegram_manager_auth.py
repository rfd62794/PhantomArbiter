"""
TelegramManager command authorization.

Every command handler must only run for the configured TELEGRAM_CHAT_ID;
other senders are ignored (logged by id only), and commands are disabled
entirely when no chat id is configured.
"""

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.shared.notification import telegram_manager as tm

AUTHORIZED_CHAT = "12345"


def _make_manager(monkeypatch, chat_id=AUTHORIZED_CHAT):
    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", "test-token")
    if chat_id is None:
        monkeypatch.delenv("TELEGRAM_CHAT_ID", raising=False)
    else:
        monkeypatch.setenv("TELEGRAM_CHAT_ID", chat_id)
    return tm.TelegramManager(command_queue=MagicMock())


def _make_update(chat_id, user_id=999):
    update = MagicMock()
    update.effective_chat.id = int(chat_id)
    update.effective_user.id = user_id
    update.message.reply_text = AsyncMock()
    return update


def test_authorized_chat_runs_handler(monkeypatch):
    manager = _make_manager(monkeypatch)
    handler = AsyncMock(return_value="ran")
    handler.__name__ = "_cmd_stop"

    update = _make_update(AUTHORIZED_CHAT)
    result = asyncio.run(manager._authorized(handler)(update, MagicMock()))

    assert result == "ran"
    handler.assert_awaited_once()


@pytest.mark.parametrize("command", ["_cmd_stop", "_cmd_clean", "_cmd_status", "_cmd_help"])
def test_unauthorized_chat_is_ignored_and_logged(monkeypatch, command):
    manager = _make_manager(monkeypatch)
    manager.command_queue = MagicMock()
    guarded = manager._authorized(getattr(manager, command))

    update = _make_update("67890", user_id=424242)
    context = MagicMock()
    context.args = ["all"]

    with patch.object(tm.Logger, "warning") as mock_warning:
        asyncio.run(guarded(update, context))

    update.message.reply_text.assert_not_called()
    manager.command_queue.put.assert_not_called()
    mock_warning.assert_called_once()
    assert "424242" in mock_warning.call_args[0][0]


def test_commands_not_registered_without_chat_id(monkeypatch):
    manager = _make_manager(monkeypatch, chat_id=None)
    manager.application = MagicMock()

    manager._register_commands()

    manager.application.add_handler.assert_not_called()


def test_guard_fails_closed_if_chat_id_cleared(monkeypatch):
    manager = _make_manager(monkeypatch)
    handler = AsyncMock()
    handler.__name__ = "_cmd_clean"
    guarded = manager._authorized(handler)

    manager.chat_id = None
    asyncio.run(guarded(_make_update(AUTHORIZED_CHAT), MagicMock()))

    handler.assert_not_awaited()


def test_all_registered_handlers_are_guarded(monkeypatch):
    manager = _make_manager(monkeypatch)
    manager.application = MagicMock()

    manager._register_commands()

    handlers = [c.args[0] for c in manager.application.add_handler.call_args_list]
    assert {next(iter(h.commands)) for h in handlers} == {"status", "stop", "help", "clean"}
    for h in handlers:
        # functools.wraps exposes the original bound method via __wrapped__
        assert hasattr(h.callback, "__wrapped__")
