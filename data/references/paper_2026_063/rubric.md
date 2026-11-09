# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Convex energy and Legendre dual (2 points):** Correctly construct or use the separable energy with \(\nabla E(q)=y\), establish strict convexity/positive Hessian, and derive \(q=\nabla E^*(y)\) together with \(\nabla^2E^*=(\nabla^2E)^{-1}\).
2. **Gradient-coordinate derivation (3 points):** Starting from the network equation, correctly compute the gradient of \(\Phi\), match \(\dot q=-\nabla_y\Phi\), differentiate the dual relation, and obtain \(\nabla^2E^*(y)\dot y=-\nabla_y\Phi\) (including the output relation \(\nabla_u\Phi=-y\)).
3. **Dissipation calculation (3 points):** Apply the chain rule along time-dependent inputs, substitute the gradient equation and output relation, and derive the exact identity \(\dot\Phi=-\dot y^T\nabla^2E^*(y)\dot y-y^T\dot u\) with correct signs.
4. **Inequality and completeness (2 points):** Use positive definiteness of the metric to conclude \(\dot\Phi\le -y^T\dot u\), while maintaining the stated domains and trajectory assumptions and proving all parts of the integrated target.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Do not award credit for merely naming Legendre duality, gradient systems, or passivity without carrying out the required identities and sign-sensitive calculations.
