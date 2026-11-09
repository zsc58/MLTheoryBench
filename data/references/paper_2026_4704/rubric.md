# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Proves existence and uniqueness of the KL minimizer over the stated radial class. A normalized candidate and an exact relative-entropy comparison are sufficient. A compactness proof must justify that the limiting competitor has finite second moment rather than simply claiming the entire finite-second-moment class is weakly closed. Strict convexity and convexity of the radial class, or the equality condition for relative entropy, establish uniqueness.
- **2 points:** Identifies the optimizer as the density proportional to $e^{-\bar V}$, with $\bar V$ the spherical average of $V$. Accept either a justified Euler-Lagrange argument with positivity and global optimality addressed, or the equivalent identity $\mathrm{KL}(\mu\|\pi)=\mathrm{KL}(\mu\|\pi_*^{\rm rad})+\log Z-\log Z_*$. These two points assess identification, separately from the existence and uniqueness conclusions.
- **2 points:** Verifies that the spherical average preserves the $\ell$-strong convexity and $L$-smoothness bounds in the full spatial Hessian, including radial and tangential directions and the extension at the origin.
- **1 point:** Correctly establishes the radial optimal-map representative and applies Brenier and two-sided Caffarelli bounds, or another valid argument, to obtain $L^{-1/2}\le\Psi'(r)\le\ell^{-1/2}$ for every positive radius. Classical differentiation must be justified for the chosen representative, not inferred solely from almost-everywhere uniqueness.
- **3 points:** Completes a valid second-derivative argument with the stated uniform dependence on $\kappa,\ell,d,r$. For the reference route, this includes the correctly oriented identity $f_\rho(r)=f_*(\Psi(r))\Psi'(r)$, the estimate $|F_*'(s)|\le C(L+d/s^2)|s-r_*|$, the mode control $|\Psi(\sqrt{d-1})-r_*|\le2/\sqrt\ell$, and the final combination of these bounds. The half-line moment argument must be proved or obtained from a correctly stated applicable standard result; an integration-by-parts proof verifies the endpoint at zero using $d\ge2$.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, first variation, or compactness if another argument establishes the same conclusions. A single entropy-comparison argument may legitimately earn both the existence/uniqueness points and the optimizer-identification points when it proves both sets of claims.

The external standard Brenier and Caffarelli results may be invoked without reproving them, provided their relevant hypotheses and conclusions are used correctly. No specialized algorithmic approximation or optimization result is required.

The second-derivative estimate may use any explicitly universal numerical constant. The reference proof obtains $C=8$, but that value is not required. An equivalent estimate with $\sqrt{d-1}$ in place of $\sqrt d$ is acceptable when the equivalence is justified. Stronger valid estimates are also acceptable.

Do not accept a parameter-free replacement of $L+d/s^2$ by $1+d/s^2$ unless a valid scaling argument supplies the missing parameter factors. The task imposes no normalization on $\ell$ or $L$ beyond $0<\ell\le L$.

Do not require $\psi(r)=\Psi(r)/r$ to be strictly monotone: that sentence in the source is a local notation error, and isotropic Gaussian examples make $\psi$ constant. The required strictly increasing profile is $\Psi$.

The theorem concerns $d\ge2$ and derivative estimates at $r>0$. Do not import the separate algorithmic branch's restriction $d\ge3$, impose extra differentiability on $V$, or demand a second-derivative bound at $r=0$.
