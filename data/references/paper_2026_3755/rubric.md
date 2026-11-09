# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes the discretization contribution \(L^2A_\Delta\), where \(A_\Delta=\Delta^2T^{-1}\int_0^{T+\Delta}m_\mu(s)\,ds+\sigma^2D\Delta\), using valid conditional averaging, SDE increment moments, and time integration. The requisite moment integrability must be justified; a valid finite-horizon argument from global Lipschitzness and \(m_\mu(0)<\infty\) suffices.
- **3 points:** Establishes the exact conditional-mean relation needed to transfer denoiser accuracy into the contribution \(b_\Delta(\tau)^2\varepsilon_{\rm score}(\tau)\). The oracle projection argument, or a direct conditional-bias argument using the same coefficient identity and conditional Jensen, is acceptable. The accuracy assumption is the stated total prediction error, not an assumed excess-risk bound.
- **3 points:** Verifies the estimator's Lipschitz constant and bounds the difference between its conditional-forward and Gaussian expectations by \(L_{\rm est}(\tau)^2[2\alpha_\tau^2A_\Delta+(1-\sigma_\tau)^2D]\) after time averaging. A direct coupling proof or a correctly applied vector-valued transport bound is acceptable. The vanishing cross term must follow from forward-noise independence, and the increment estimate must justify the factor \(2A_\Delta\).
- **2 points:** Uses the correct conditional-iid sampling law to obtain \(D L_{\rm est}(\tau)^2/K\), and combines the contributions to prove the exact final bound. Gaussian Poincare with verified hypotheses, or the independent-copy variance identity and Lipschitzness, is acceptable.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's exact intermediate notation, number of intermediate quantities, or choice of named inequalities. The decomposition is a proof device, not an additional target requirement. A named result receives credit only when its relevant statement and applicable hypotheses support the quantitative consequence used.

The denoiser is fixed, forward noise is independent of the SDE, and the entire Monte Carlo sampling vector is independent of the evaluation trajectory. Do not interpret unconditional iid Gaussian marginals alone as sufficient for a conditional-iid variance calculation.

Do not require a second moment for \(Y_0\), stationarity, independence of successive observed increments, Gaussian true SDE increments, or a finite-sample guarantee for the training procedure. The moment hypothesis concerns \(\mu(Y_t)\), and the denoiser accuracy assumption is time averaged. Conditional \(L^2\) calculations for almost every conditioning time are sufficient. No uniform bound on \(L_D(\tau)\) across noise levels or dimensions is assumed.

The final theorem, including all four displayed contributions, the averaging over process and Monte Carlo randomness, and every parameter dependency, must be supported. No proof obligation remains unresolved in the reference proof.
