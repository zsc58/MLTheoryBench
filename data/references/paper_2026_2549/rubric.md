# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Verifies the density representation of eta_r using the sigma-finite reference measures, handles the m_r=0 and m_r=infinity null sets, and proves eta_rK_r=pi_r, pi_{r-1}P_{r-1}=eta_{r-1}, and eta_0K_0=pi_0.
- **3 points:** Defines or uses the displayed extended stage target and proposal, computes their Radon-Nikodym ratio by explicit cancellation, obtains W_r=(Z_r/Z_{r-1})ell(x)^(lambda_{r-1}-lambda_r), explains why the common stage constant cancels, and shows normalized weighting maps pi_r to pi_{r-1}.
- **3 points:** Gives a valid finite-stage induction through independent reconstruction, bounded-potential weighting, the explicit zero-total-weight fallback, consistency-preserving or absent resampling, and re-noising. The proof must establish vanishing maximum particle weights or an equivalent dispersion condition before invoking conditional mutation variance bounds.
- **2 points:** Applies terminal exact reconstruction, identifies pi_0 with the posterior, and concludes convergence in probability for every bounded measurable test function and hence weak convergence, without treating the two notions as logically equivalent in general.

# Evaluator Notes

Accept a complete valid alternative proof. Require the stage target/proposal ratio or an equivalent rigorous derivation of the exact incremental factor. Require all stages of the induction, a valid mutation-consistency argument, the terminal reconstruction, and treatment of finite-sample zero normalization. Do not require the incidental notation or ordering used by the reference proof.
