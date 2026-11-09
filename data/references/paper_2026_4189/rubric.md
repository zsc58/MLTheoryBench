# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **Step 1 (2 points):** Uses nonnegativity and $F_c(\pi_d)=0$ to establish zero averaged conditional mutual information in every model. Correctly distinguishes the fixed-value quantity $I_m(D;\phi\mid\theta=t,\pi_d)$ from the scalar conditional mutual information averaged over $\theta$. It is equivalent to show that the fixed-value quantity vanishes for $p(\theta)$-almost every $t$.
- **Step 2 (3 points):** Correctly invokes the zero-CMI characterization to derive conditional independence of $D$ and $\phi$ given $\theta$, with appropriate almost-sure qualification.
- **Step 3 (3 points):** Combines conditional independence with the factorized prior to prove posterior invariance to $\phi$, by Bayes' rule or an equivalent joint-law argument. Establishes $p_m(\phi,D\mid\pi_d)=p_m(\phi)p_m(D\mid\pi_d)$ so posterior invariance holds under the product law required by the target. The shared $(\theta,D)$ marginal also permits a common posterior $p(\theta\mid D,\pi_d)$ across models.
- **Step 4 (2 points):** Integrates the invariant posterior against the fixed $p(z\mid\theta)$ and concludes predictive equality for every $z$ and for $p_m(\phi_1)p_m(\phi_2)p_m(D\mid\pi_d)$-almost every $(\phi_1,\phi_2,D)$, separately in every model. Handles the two exceptional conditioning-pair sets correctly, explicitly or by an equivalent valid almost-sure argument.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. In particular, a proof may work model by model and need not exploit the shared marginal to prove an additional cross-model conclusion. It may use scalar conditional mutual information directly without introducing a fixed-value information function, provided the averaging convention is correct.

Treat omitted null-set qualifications as a minor issue when the underlying argument is correct. Failure to establish posterior invariance or predictive parity is a theorem-critical gap. Equality almost everywhere is not equality everywhere in the support, and arbitrary posterior versions on null datasets need not satisfy pointwise parity. Do not demand a simultaneous exceptional set across models. No strict positivity assumption, finite model class, nondegenerate prior, positive sample size, or additional covariate condition is needed.
