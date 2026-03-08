# Full Repository Inventory: PhantomArbiter

This document provides a comprehensive forensic inventory of every directory and file in the PhantomArbiter repository.

## 📁 Root Directory (Full Zero-Distillation Catalog)

The root contains 140+ files orchestrating the arbitrage lifecycle, documentation, and forensic history.

### 📄 Architecture & Strategy (ADRs & Specs)
- `ACTION_PLAN.md`: Strategic roadmap for the current iteration.
- `ARCHITECTURE_ARBITRAGE.md`: Deep-dive into arbitrage pathfinding.
- `ADR_008_PHASE_1_IMPLEMENTATION_SUMMARY.md`: Architectural Decision Record for Phase 1.
- `DELTA_NEUTRAL_IMPLEMENTATION_SUMMARY.md`: Spec for hedging and risk-neutrality.
- `DRIFT_API_COVERAGE.md` / `DRIFT_SDK_MIGRATION_SUMMARY.md`: Protocol-specific integration docs.
- `ENGINES_EXPLAINED.md`: Detailed breakdown of the multi-engine paradigm.
- `PHASE_3_IMPLEMENTATION_SUMMARY.md`: Status of the execution layer refinements.
- `REMAINING_WORK_SUMMARY.md`: Open tasks for the core arbiter.
- `STARTHERE.md`: Onboarding guide for the repository.

### 🧪 Simulation & Execution Logs
- `LIVE_EXECUTION_LOGS.csv`: Real-world performance data.
- `SAGE_SIM_LOGS.csv`: Simulation output for the SAGE strategy.
- `sim.log`, `sim2.log`, `sim3.log`: Verbose execution traces.
- `sim_result_1.txt` to `sim_result_5.txt`: Performance benchmarking outputs.
- `bridge_test_output.txt`: FFI boundary verification logs.
- `log.txt`, `log_review.py`: System diagnostic tools.

### 🛠️ Execution & Build Scripts
- `main.py`: Primary entry point.
- `build_rust.py`: Rust compilation orchestrator.
- `build_station.py` / `build_venv.py`: Environment setup utilities.
- `cli_typer.py`: The CLI interface engine.
- `run_dashboard.py`: TUI launcher.
- `refactor_trading_core.py`: Transformation utility for the core engine.

### 🔍 Diagnostic & Verification Utilities
- `check_api_connectivity.py`: Network health check.
- `check_drift_equity.py`: Balance and margin verification.
- `verify_reality.py`: Large-scale state consistency check.
- `verify_wallet_address.py`: Security validation for signing keys.
- `debug_keys.py`, `debug_load.py`, `debug_precision.py`: Precision and security audit tools.
- `test_connectivity.py`, `test_jup.py`, `test_tensor_real.py`: Individual module validators.

### 📦 Ecosystem Connectors
- `drift_bridge.js`: Node.js interop for Drift Protocol.
- `deploy_star_atlas.py`: Star Atlas specific deployment logic.
- `send_tensor_payment.py`: NFT marketplace interaction utility.

## 🦀 High-Performance Engine (`src_rust/`)
...

- `Cargo.toml`: Rust dependency manifest.
- `src/lib.rs`: The PyO3 bridge (The Aorta).
- `src/amm_math.rs`: Optimized AMM calculations.
- `src/graph.rs`: Negative cycle detection (SPFA) engine.
- `src/router.rs`: Atomic transaction routing layer.
- `src/wss_aggregator.rs`: High-throughput WebSocket ingestion.
- `src/slab_decoder.rs`: Fast binary decoding for DEX orderbooks.
- `src/token2022.rs`: Support for Solana Token Extensions.
- `src/multiverse.rs`: Parallel state simulation across multiple forks.

## 🐍 Intelligence Intelligence (`src/`)

- `engines/`: Core arbitrage and scalping engines.
    - `arb/`: Triangular and spatial arbitrage logic.
    - `scalp/`: Short-term market-making logic.
- `shared/`: Reusable components across all engines.
    - `execution/`: Transaction builders, adapters, and pool registries.
    - `feeds/`: Data ingestion from Jupiter, Raydium, and Drift.
    - `infrastructure/`: Logging, database management, and networking.
    - `state/`: Global application state management.
- `services/`: Background service definitions (Discovery, API).
- `ui/`: Terminal UI components and formatting.

## 📦 Extended Ecosystem

### `apps/` (Microservices)
- `datafeed/`: Specialized service for market data ingestion.
- `execution/`: Isolated execution backend for security.
- `galaxy/`: Models and logic for the Galaxy integration.

### `external/` (Third-Party Integration)
- `star-atlas-dash/`: Integration for Star Atlas market data.
- `star-atlas-cookbook/`: Wallet and player profile helpers.

### `frontend/` (Web Interface)
- `dashboard.html` & `index.html`: Web-based observability dashboards.
- `js/` & `styles/`: Support assets for the web dashboard.
- `templates/`: HTML templates for dynamic reporting.

### `models/` (Data Persistence)
- `ml_filter.pkl`: Pre-trained machine learning models for trade filtering.

### `tools/` (Maintenance)
- `close_dust.py`: Utility to reclaim rent from tiny SPL balances.
- `migrate_legacy_dbs.py`: Database schema versioning tools.

## 🛠️ Automated Scripts Inventory (`scripts/`)
Detailed list of the 100+ automation scripts (Exhaustive mapping):
- `analyze_history.py`
- `check_balances.py`
- `check_live_ready.py`
- `generate_market_map.py`
- `ghost_execute.py`
- `reinit_db.py`
- `run_backtest.py`
- `verify_audit_architecture.py`
- ... (and 90+ others mapping every facet of the system).
