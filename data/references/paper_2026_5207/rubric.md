# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly relates the defining destination integrals to Z and Phi. The reference route differentiates the Gaussian convolutions, rewrites the two destination integrals, and cancels the equal Zx terms to obtain V=Z grad Phi. Award equivalent credit for another correct calculation establishing the relation needed for the claimed obstruction. Analytic operations must be justified under the stated probability-measure assumptions; a concise correct Gaussian domination or equivalent regularity argument suffices.
- **3 points:** Correctly derives the alignment condition for every x and every pair i,j from the existence of a global C2 scalar potential. The reference route uses symmetry of the Jacobian and equality of the mixed partials of Phi. The argument must remain valid when either gradient vanishes.
- **3 points:** Correctly evaluates the atomic configuration and the quantities needed to test the condition at (0,1). The reference values are Phi(x)=1+2x_1, Z(x)=exp(2/tau)sqrt(k(x,b)k(x,a)), grad Phi(0,1)=(2,0), and grad Z(0,1)=(0,-2Z(0,1)/tau), with Z(0,1)=1. Equivalent direct derivative calculations receive full credit; the exact additive constant in Phi need not be computed if only its derivatives are used.
- **1 point:** Exhibits a nonzero violation at (0,1) for tau>0 and correctly concludes that no global C2 scalar-potential representation exists, hence the field fails the necessary spatial-gradient condition for a smooth pointwise Wasserstein-gradient-flow velocity.

# Evaluator Notes

Accept every complete valid alternative proof of the public claims. Do not require the reference proof's notation, intermediate representation, named identities, or order of calculation. In particular, an explicit display of V=Z grad Phi is not mandatory if a direct componentwise or equivalent argument proves the required implication.

A bare assertion that the field has nonzero curl, or merely naming an integrability criterion, does not establish the requested calculations. Conversely, a correctly computed curl tied to the defined field and to the displayed alignment condition is valid evidence.

Do not impose finite total mass of the weighted measures, positive densities, compact support, or finite moments as additional task assumptions. The Gaussian-weighted quantities used here are globally finite and smooth for the stated probability measures. A proof restricted to a smaller class does not establish the general implication.

The task uses only a necessary spatial condition for a smooth pointwise Wasserstein-gradient-flow representation. Do not require construction of a distributional energy, and do not treat spatial conservatism alone as sufficient for such an energy or flow. The atomic obstruction concerns equality with a gradient on all of R^d, not merely equality of velocity representatives q-almost everywhere.
