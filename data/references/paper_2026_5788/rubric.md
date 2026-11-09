# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points: Coordinate kernel.** Correctly collects the coordinate-dependent energy terms, including the factor \(2\alpha_d-2\) from the symmetric log-amplitude interaction, and obtains the planar kernel \(|x_d|^{2\alpha_d-2}\exp(-\beta_d|x_d|^2+\operatorname{Re}(\overline{g_d}x_d))\). The argument must also recognize why \(\beta_d>0\) and \(\alpha_d>0\) give coordinate integrability.
- **3 points: Planar distribution identification.** Completes the complex square with \(m_d=g_d/(2\beta_d)\) and \(s_d^2=1/\beta_d\), then establishes the correct normalizing constant for the power-weighted complex Gaussian density. Merely naming the family without matching its kernel and parameters does not earn full credit.
- **2 points: Phase conditional.** Conditions on the radius and derives the normalized von Mises density with center \(\phi_d\) and concentration \(a_dr\), including a correct treatment of the zero-field case.
- **2 points: Magnitude marginal.** Uses the polar Jacobian and angular Bessel integral to derive the stated generalized Rician density with radial noncentrality \(\nu_d=|m_d|\). Omitting the Jacobian or using the complex value \(m_d\) as a radial parameter is a theorem-critical error in this step.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the reference proof's incidental presentation choices. A normalization calculation may use an equivalent standard integral identity instead of a power-series derivation. If the planar conditional is independently established despite an error in its derivation, score subsequent valid phase and magnitude calculations on their own merits.
