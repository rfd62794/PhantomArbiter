# Portability Specs: PhantomArbiter Browser Integration

This document serves as the technical source of truth for porting the PhantomArbiter high-performance engine to a web-based environment.

## 1. Network Requirements (Market Connectivity)

To maintain real-time edge, the following endpoints must be accessible from the browser:

| Category | Protocol | Source | Purpose |
| :--- | :--- | :--- | :--- |
| **Market Data** | WSS | Raydium, Orca, Jupiter | Real-time pool state updates |
| **RPC** | HTTPS | Helius, Triton, Quicknode | Transaction submission & state verification |
| **Bundles** | HTTPS/GRPC | Jito | MEV-protected bundle submission |

> [!IMPORTANT]
> Browser-based WebSockets may require CORS-enabled proxying if direct access to RPC WSS is restricted by the provider.

## 2. Dependency Hardening (Rust vs. WASM)

| Rust Dependency | WASM Equivalent / Strategy | Compatibility Notes |
| :--- | :--- | :--- |
| `pyo3` | `pyodide` / `emscripten` | Requires careful FFI mapping to JavaScript. |
| `solana-sdk` | `@solana/web3.js` or `wasm-solana` | Core types port easily; networking must use `web-sys`. |
| `tokio` | `wasm-bindgen-futures` | Standard `tokio` multi-threading is NOT supported in WASM. |
| `reqwest` | `web-sys::fetch` | Compatible with `wasm-bindgen` feature flags. |
| `rayon` | **FALLBACK TO SERIAL** | WASM does not support standard threads without specialized runners. |
| `bincode` / `serde` | Native Rust WASM | 100% compatible. |

## 3. Compute Resource Analysis

Transaction signing and serialization in Rust (ported to WASM) offers significantly lower latency compared to pure JavaScript implementations. 

**Estimated Overhead:**
- **Serialization:** < 1ms (WASM) vs 3-5ms (JS)
- **Signing (Ed25519):** 0.2ms (WASM)
- **Memory Footprint:** ~50MB (Shared memory heap)

## 4. API & WebSocket Inventory

### RPC Channels
- `getLatestBlockhash` (High Priority)
- `simulateTransaction` (Pre-flight Risk)
- `sendTransaction` (Failover Path)

### WebSocket Subscriptions
- `logsSubscribe` (Raydium program ID)
- `accountSubscribe` (Pool State)
- `programSubscribe` (Arbitrage Opportunity Discovery)
