# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **EWMA reduction and setup (2 points):** Correctly obtains the constant-coefficient recurrence s_k=rho_i s_{k-1}+(1-rho_i)E_{i,k} from the scale update and uses 0<rho_i<1.
2. **Asymptotic unbiasedness (3 points):** Derives the mean recursion or an equivalent geometric-sum expression and proves convergence of E[s_k] to sigma_i^2 under weak stationarity.
3. **Steady-state variance (3 points):** Uses temporal independence to derive and solve V_k=rho_i^2V_{k-1}+(1-rho_i)^2eta_i^4, obtaining ((1-rho_i)/(1+rho_i))eta_i^4. Merely naming an EWMA variance formula is insufficient.
4. **Parameter form and tracking time (2 points):** Substitutes rho_i=nu_i^-/(nu_i^-+1) to obtain eta_i^4/(2nu_i^-+1), and identifies the e-folding time constant T_i=-1/log rho_i.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Apply the temporal-independence condition only to the variance claim; weak stationarity suffices for the mean claim. Propagate a missing EWMA reduction to later steps only when the corresponding downstream calculation is genuinely unsupported.

The initialization is a fixed finite constant, so V_0=0 and independence from initialization is automatic. A proof may retain V_0 symbolically in the variance recursion, provided its treatment is consistent with this initialization. No additional initialization moment assumption is required. The formulas include eta_i^4=0; a separate case split is unnecessary when the derivation already covers it.
