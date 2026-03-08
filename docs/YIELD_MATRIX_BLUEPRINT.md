# DASHBOARD BLUEPRINT: Card 7 - The Institutional Yield Matrix

This component showcases protocol-level yield intelligence, transitioning the portfolio from "Bot" to "Quant Finance Engine."

## 🎨 Visual Identity: --neon-gold
- **Primary Accent**: `#FFD700` (Gold)
- **Alt Accent**: `#00FF00` (Neon Green for APR > 20%)
- **Background**: Glassmorphism (`rgba(10, 10, 20, 0.85)`)

## 📊 Data Mapping: Yield Stats
| Field | ID | Source | Logic |
| :--- | :--- | :--- | :--- |
| **Hourly Rate** | `drift-rate-h` | Drift API | Raw hourly funding % |
| **Annual APR** | `drift-apr` | `calculate_funding_apr` | $rate \times 24 \times 365.25$ |
| **Compounded APY** | `drift-apy` | `calculate_funding_apy` | $(1+rate)^{8766}-1$ |
| **Basis Spread** | `drift-basis` | `calculate_basis_yield` | $(Mark - Oracle) / Oracle$ |
| **Rebate Pool** | `drift-rebate` | Drift Account Data | Capped Symmetric Status |

## 🚨 Indicator Logic: "The Ignite"
When the APY exceeds 50% (Crowded Bearish Shift):
1. Card border pulses with `box-shadow: 0 0 25px var(--neon-gold)`.
2. A "SQUEEZE RISK" badge appears in the top-right corner.
3. The "Sentinel" utility emits a `YIELD_SPIKE` signal.

## 📝 Technical Disclaimer
"Yield calculations assume constant hourly funding rates. Actual returns may vary based on Drift protocol caps and rebate pool health."
