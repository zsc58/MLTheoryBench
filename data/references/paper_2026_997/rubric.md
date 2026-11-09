# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derives the first-mean evolution from the SDE or KFP equation, either as m_t-m_s=∫_s^t E[u_r(X_r)]dr or as its justified almost-everywhere differential version.
- **4 points:** Differentiates the HJB consistently with u=-∇J, explains the gradient-field/Hessian-symmetry calculation, and combines the resulting vector evolution with Itô's formula. Obtains either E[u_t(X_t)]-E[u_s(X_s)]=∫_s^t E[∇U_r(X_r)]dr or the corresponding justified mean-acceleration identity.
- **2 points:** Computes ∇U_t(x)=beta_t(x-m_t) from the finite-valued quadratic integral and uses the population mean/self-consistency relation to make the expected force vanish. Concludes constancy of the expected control or the equivalent zero mean acceleration in an appropriate integral or almost-everywhere sense.
- **2 points:** Obtains the affine interior mean, justifies its identification with the endpoint means using the supplied endpoint regularity, and identifies nu_t with m_t for every t in [0,1].

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The public assumptions supply the analytic admissibility conditions; solvers need not prove bridge existence or derive those assumptions from the endpoint laws.

The schedule is measurable, not necessarily continuous or differentiable. An integral or almost-everywhere argument is fully sufficient. Do not require pointwise existence of a second time derivative everywhere. A proof written in differential notation can receive full credit when its integral/almost-everywhere interpretation is clear and it does not assume extra schedule smoothness. A proof that covers only smooth schedules without extending to the stated regime leaves a gap.

The finite-valued potential assumption supplies the interior moment needed to expand its defining integral. Do not demand finite second moments of the endpoint laws, Gaussian endpoints, a delta initial law, or a piecewise-constant schedule.

The endpoint conditions must identify the same affine path obtained in the interior. A brief invocation of the supplied L1 endpoint continuity is sufficient; an otherwise complete proof that omits this explicit invocation has at most a readily repairable omission.

Treat omission of the HJB differentiation/cancellation or of the quadratic expected-force calculation as a theorem-critical gap unless a valid alternative argument supplies the same conclusion. Merely naming Itô calculus or a Burgers/HJB identity without establishing the needed relation earns no credit for that step. No Green-function or specialized guided-diffusion result is required.
