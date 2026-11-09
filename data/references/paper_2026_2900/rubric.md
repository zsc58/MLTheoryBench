# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Uses the stated operator, baseline, and residual correctly and verifies integrability. In particular, delta and r_t in L2 give integrability of delta r_t, while the growth bounds and the target moment give integrability of the directional derivative.
- **3 points:** Justifies the weighted boundary limit, or supplies a complete alternative integration-by-parts justification. For the Gaussian surface argument, includes the head growth, field growth, and surface factor, and gives an integrable dominating function under the explicit target moment. Pointwise conditional Gaussian decay alone is insufficient.
- **3 points:** Derives E_p[delta r]=-E_p[<grad delta,v>] using a valid integration-by-parts argument and proves the exact identity E_p[(delta-r)^2]=L_t(delta)+E_p[r^2]. Covers both model settings; one correctly parameterized Gaussian-mixture argument may cover both.
- **2 points:** Establishes equality of minimizer sets without asserting unconditional existence. When r_t belongs to H, proves existence and recovery in L2, then concludes b_t+delta_t^*=div v_t almost surely for each permitted time and model setting.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices, duplicated diffusion and flow calculations, or a Gaussian-tail estimate if another fully justified argument proves the required identity from the stated assumptions. In particular, a justified localization argument is acceptable.

Treat an unsupported interchange of a mixture expectation and a boundary limit, or minimizer equivalence asserted without a valid risk identity, as a theorem-critical gap. Do not accept the assertion that every Gaussian mixture has Gaussian unconditional tails. Stein-class membership of v alone does not establish the weighted identity for delta v.

The theorem is at each fixed time. Do not demand uniform constants, a uniform lower bound on conditional variance, a common null set for all times, or a result about time-averaged training. The argument must remain valid for D=1, zero growth degrees, and a zero Gaussian-mixture mean coefficient. A class not containing r_t need not have a minimizer and need not recover r_t.

The source appendix's omitted factors R are corrected in the private reference materials. A solver need not discuss these source errors; assess the submitted mathematics against the public task.
