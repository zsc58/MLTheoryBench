# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Bandit gradient and moment identities (2 points).** Correctly uses U(y*)=1/2 and U(a)=-1/2 for failures to derive the stated plain failure moment and the gated per-action expression.
2. **Asymmetric gate bound and geometric suppression (3 points).** Derives the negative-tail sigmoid bound w(a)<=pi(a)^(1/(2 eta)) and propagates it through the perpendicular projection to obtain the weighted gated second-moment bound. Merely naming a sigmoid or gating method is insufficient.
3. **Contamination decomposition (3 points).** Expands expectations under mu=(1-rho)pi+rho nu, identifies the overlap moment M_{nu,eta}^perp(pi) controlling the gated contamination, and identifies the plain contamination term (rho/4)S_nu.
4. **Near-optimal asymptotics and contrast (2 points).** Proves ||phi_pi(a)||<=2 and M<=4(max_{a != y*}pi(a))^(1/eta)<=4 delta^(1/eta), yielding vanishing gated contamination; under S_nu>=gamma, proves the plain lower bound rho gamma/4 and the non-vanishing contrast.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Propagate a missing gate bound or contamination decomposition to downstream claims only when those claims are genuinely unsupported.
