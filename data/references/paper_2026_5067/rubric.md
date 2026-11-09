# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly sets up the linear path, sampled baseline, and integrated-gradient expressions, including the relation between the intermediate-baseline path and the original path.
- **3 points:** Performs the reparameterization and change of variables correctly to show that each sampled-baseline IG coordinate is the tail integral from s to 1 along the original path. Handles s=1 directly or notes that this endpoint is irrelevant to integration against a density.
- **4 points:** Correctly justifies interchanging the sampling and path integrals from the explicit path-integrability assumption and the fact that p is a probability density, then evaluates the inner integral as G(alpha), preserving all factors and limits. A sufficient justification is that the absolute double integral is at most integral_0^1 |partial_i F(gamma(alpha))| d alpha. An equivalent valid justification is accepted.
- **1 point:** Matches the resulting expression to PWIG with weight G and states the coordinate-wise equality for all i. Recognizes, explicitly or through the integrability argument, that G is an admissible weight.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its auxiliary notation. Routine measurability and integrability observations may be concise; the tail-integral representation and its uniform absolute bound establish that the sampled attribution is measurable and integrable. Treat an unjustified exchange of signed integrals, an incorrect Jacobian, or a wrong integration region as a substantive gap; propagate its failure to the final identification only when that conclusion is unsupported. Do not require p to be bounded or continuous, F to be continuously differentiable, or any coordinate displacement to be nonzero. The case x=x' is included. A harmless omitted endpoint discussion is a readily repairable omission, not a failure of the central argument.
