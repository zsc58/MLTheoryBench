# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Derives cancellation of the cubic Taylor term from symmetry and the induced-metric normalization, and obtains a local fourth-order estimate along geodesics.
- **2 points:** Uses normal neighborhoods, compactness, and a finite-cover argument to make the fourth-order comparison uniform for all pairs on the compact manifold.
- **3 points:** Carries out the normal-coordinate kernel expansion with the quadratic divergence approximation, radial moment/odd-term cancellations, and obtains the bias formula with the Laplace-Beltrami term (including the stated remainder regularity). The normalized integral operator must include its factor \(\varepsilon^{-m/2}\).
- **2 points:** Establishes normalized almost-sure empirical concentration via Hoeffding and Borel-Cantelli under the bandwidth rate, uses \(\mathbb EZ_1=\varepsilon_N^{m/2}[f(x)G_{\varepsilon_N}P(x)-G_{\varepsilon_N}(fP)(x)]\), and combines this with the bias expansion and product rule to derive both the general weighted limit and the uniform-density specialization.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat omission of the cubic-cancellation mechanism, the uniform fourth-order bound, the correctly normalized kernel bias calculation, or the almost-sure concentration as a theorem-critical gap.
