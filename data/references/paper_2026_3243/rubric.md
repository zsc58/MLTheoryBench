# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Proves the latent conditional pushforward equals the conditioned process law.
- **2 points:** Derives \(\rho_t=r\psi/Z\) and \(\nabla\log\rho_t=g-u\) from the Gaussian bridge for positive times.
- **5 points:** Derives the reverse drift and validly identifies the SDE’s reverse marginals—for example, by applying time reversal with its hypotheses checked and using uniqueness in law, or by establishing that the SDE’s marginals have densities before invoking density-valued Fokker--Planck uniqueness.
- **1 point:** Justifies the time-zero law using a continuous endpoint solution and \(\rho_t\Rightarrow\rho_0\), then concludes the process conditional law.

# Evaluator Notes

Accept any complete mathematically valid alternative proof; do not award substantial credit for merely naming a method. A calculation that \(q_s=\rho_{t_1-s}\) solves the reverse Fokker--Planck equation is not, by itself, enough to apply uniqueness restricted to density-valued solutions to an SDE whose marginal densities have not been established. The endpoint claim does not require \(g(0,\cdot)\) to exist.
