# Reference Proof

Let \(\Delta_n=\hat\theta_{\mathrm{fe}}-\hat\theta_{\mathrm{or}}\), \(\Sigma_n=(n\omega V_0)^{-1}\), and \(N_j=\mathcal N(\hat\theta_j,\Sigma_n)\) for \(j\in\{\mathrm{or},\mathrm{fe}\}\). Assumption (A1) gives \(d_{\mathrm{TV}}(q_{n,j},N_j)=o_P(1)\) for each \(j\). Assumption (A3) directly gives \(\|\Delta_n\|=O_P(r_n^2)\); no derivation of that assumed bound from orthogonality is needed.

The normals have equal covariance, so
\[
\mathrm{KL}(N_{\mathrm{fe}}\|N_{\mathrm{or}})
=\tfrac12\Delta_n^\top\Sigma_n^{-1}\Delta_n
=\tfrac{n\omega}{2}\Delta_n^\top V_0\Delta_n.
\]
Since \(\omega\) and \(V_0\) are fixed, Pinsker's inequality yields
\[
d_{\mathrm{TV}}(N_{\mathrm{fe}},N_{\mathrm{or}})
\leq \tfrac12\sqrt{n\omega\lambda_{\max}(V_0)}\,\|\Delta_n\|
=O_P(\sqrt n\,r_n^2).
\]
The triangle inequality and (A1) therefore give
\[
d_{\mathrm{TV}}(q_{n,\mathrm{fe}},q_{n,\mathrm{or}})
\leq d_{\mathrm{TV}}(q_{n,\mathrm{fe}},N_{\mathrm{fe}})
+d_{\mathrm{TV}}(N_{\mathrm{fe}},N_{\mathrm{or}})
+d_{\mathrm{TV}}(N_{\mathrm{or}},q_{n,\mathrm{or}})
=O_P(\sqrt n\,r_n^2)+o_P(1).
\]
If \(r_n=o_P(n^{-1/4})\), then \(\sqrt n\,r_n^2=o_P(1)\), proving posterior convergence in total variation. The Gaussian-center comparison also gives \(d_{\mathrm{TV}}(N_{\mathrm{fe}},N_{\mathrm{or}})=o_P(1)\), so the oracle BvM approximation transfers to the feasible posterior with feasible center. Equivalently, that feasible-centered approximation is already an explicit part of (A1).
