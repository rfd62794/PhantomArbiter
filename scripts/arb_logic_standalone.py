"""
Arb Logic Standalone (Forensic Extraction)
==========================================
Decoupled math logic from PhantomArbiter for portability and verification.
Extracted from: src_rust/src/lib.rs and src/engines/arb/scanner.py.
"""

import math
import time
from typing import List, Dict, Optional

# --- SECTION 1: CORE MATH (From Rust lib.rs) ---

def calculate_net_profit(
    spread_raw: float,
    trade_size: float,
    jito_tip: float,
    route_friction: float,
) -> float:
    """Go/No-Go Decision Engine for Net Profit. Ported from Rust."""
    gross = trade_size * (spread_raw / 100.0)
    net = gross - jito_tip - route_friction
    return net

def estimate_compute_units(
    ops: List[str],
    num_accounts: int,
    num_signers: int,
    safety_margin_percent: float,
) -> int:
    """High-Fidelity Compute Unit Estimator. Ported from Rust."""
    estimated_cu = 0.0

    # 1. Signature Cost
    estimated_cu += num_signers * 1500.0

    # 2. Serialization Overhead
    estimated_cu += num_accounts * 850.0

    # 3. Instruction Simulation
    for op in ops:
        costs = {
            "transfer_sol": 500.0,
            "transfer_spl": 4500.0,
            "create_ata": 25000.0,
            "close_account": 3000.0,
            "memo": 100.0,
            "raydium_swap_v4": 80000.0,
            "raydium_swap_cpcc": 120000.0,
            "orca_whirlpool_swap": 145000.0,
            "meteora_dlmm_swap": 70000.0,
            "jupiter_aggregator": 180000.0,
            "phoenix_swap": 25000.0,
        }
        estimated_cu += costs.get(op, 10000.0)

    # 4. Safety Margin
    estimated_cu *= 1.0 + (safety_margin_percent / 100.0)

    if estimated_cu < 5000.0:
        estimated_cu = 5000.0

    return int(math.ceil(estimated_cu))

# --- SECTION 2: STRATEGY MATH (From Python scanner.py) ---

def calculate_optimal_size(
    spread_pct: float,
    impact_factor: float,
    min_size: float = 10.0,
    max_size: float = 1000.0
) -> float:
    """Calculate optimal trade size using calculus. Ported from Python."""
    if impact_factor <= 0:
        return max_size

    # x_opt = Spread / (2 * Impact)
    s = spread_pct / 100
    optimal_size = s / (2 * impact_factor)

    return max(min_size, min(optimal_size, max_size))

# --- SECTION 3: MOCK DATA & SIMULATION ---

def simulate_opportunity():
    """Run a bit-perfect simulation of the arb logic."""
    print("--- 🔬 PhantomArbiter Logic Simulation ---")
    
    # Mock Pool Setup (Mirroring Real Structures)
    pool_a = {
        "dex": "RAYDIUM",
        "liquidity_usd": 150000,
        "price": 95.0, # BUY
    }
    pool_b = {
        "dex": "ORCA",
        "liquidity_usd": 120000,
        "price": 96.5, # SELL
    }

    # Parameters
    spread_pct = ((pool_b["price"] - pool_a["price"]) / pool_a["price"]) * 100
    impact_factor = 1e-5 * (100000 / max(pool_a["liquidity_usd"], 10000))
    
    print(f"Spread Detected: {spread_pct:.3f}%")
    print(f"Impact Factor: {impact_factor:.2e}")

    # 1. Optimal Sizing
    size = calculate_optimal_size(spread_pct, impact_factor)
    print(f"Optimal Trade Size: ${size:,.2f}")

    # 2. Net Profit Calculation (with friction)
    jito_tip = 0.001 * 95.0 # ~0.1 USD tip in SOL
    friction = 0.05 # Mock fixed friction
    net_profit = calculate_net_profit(spread_pct, size, jito_tip, friction)
    
    print(f"Est. Net Profit: ${net_profit:,.4f}")
    
    # 3. Compute Unit Estimation
    ops = ["raydium_swap_v4", "orca_whirlpool_swap", "transfer_spl"]
    cu = estimate_compute_units(ops, num_accounts=12, num_signers=1, safety_margin_percent=10.0)
    print(f"Est. Compute Units: {cu:,} CU")

    if net_profit > 0:
        print("\n✅ DECISION: [EXECUTABLE]")
    else:
        print("\n❌ DECISION: [THIN/NEGATIVE]")

if __name__ == "__main__":
    simulate_opportunity()
