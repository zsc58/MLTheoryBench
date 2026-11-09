# Reference Proof

## Proof Structure

The normalized outputs have bounded norm, so their means and covariances exist. The LayerNorm normalized vector is always orthogonal to the all-ones vector. Its centered covariance therefore has that vector in its kernel; diagonal rescaling transports the kernel to the coordinatewise inverse scale, while the bias has no effect on covariance. For zero scale coordinates, the corresponding LayerNorm outputs are constant. For RMSNorm, an isotropic Gaussian input yields a normalized vector with identity covariance, so diagonal scaling produces a positive-definite covariance and rules out any universal parameter-only null direction.

## Complete Proof

Both normalized vectors \(\sqrt d\,PX/\|PX\|\) and \(\sqrt d\,Y/\|Y\|\) have norm \(\sqrt d\) almost surely on their respective admissible domains. Their coordinates, and the coordinates obtained after deterministic diagonal scaling and addition of a fixed bias, are bounded. Thus all output means and covariances used below are finite. In particular, no moment assumption on the LayerNorm input \(X\) itself is necessary.

Let \(D_\gamma=\operatorname{diag}(\gamma)\), and first suppose every \(\gamma_i\ne0\). Define
\[
Z=\frac{\sqrt d\,PX}{\|PX\|},\qquad P=I-\frac1d\mathbf 1\mathbf 1^\top.
\]
Since \(\mathbf 1^\top P=0\), we have \(\mathbf 1^\top Z=0\) almost surely. Taking expectations gives \(\mathbf 1^\top\mathbb EZ=0\), and hence
\[
\operatorname{Cov}(Z)\mathbf 1
=\mathbb E[(Z-\mathbb EZ)(Z-\mathbb EZ)^\top]\mathbf 1=0.
\]
LayerNorm satisfies \(\operatorname{LN}_{\gamma,\beta}(X)=D_\gamma Z+\beta\). Subtracting its expectation gives \(D_\gamma(Z-\mathbb EZ)\), so
\[
C_{\mathrm{LN}}=D_\gamma\operatorname{Cov}(Z)D_\gamma.
\]
Therefore
\[
C_{\mathrm{LN}}\gamma^{-1}
=D_\gamma\operatorname{Cov}(Z)D_\gamma\gamma^{-1}
=D_\gamma\operatorname{Cov}(Z)\mathbf 1=0.
\]
The vector \(\gamma^{-1}\) is nonzero, so \(v_*=\gamma^{-1}/\|\gamma^{-1}\|\) is a well-defined unit kernel direction, independent of the distribution of \(X\). This does not assert that the kernel is one-dimensional.

Now allow arbitrary LayerNorm scale coordinates. If \(\gamma_i=0\), the \(i\)-th output coordinate equals the constant \(\beta_i\). Its centered value is zero almost surely, so its covariance row and column vanish and \(C_{\mathrm{LN}}e_i=0\). This applies to every zero scale coordinate, including the case \(\gamma=0\), when the entire output is constant.

For RMSNorm, fix \(\gamma\) with every coordinate nonzero. Let \(Y\sim N(0,I_d)\). This distribution has a density, is nonzero almost surely, and has finite positive-definite covariance \(I_d\), so it is admissible. Put \(U=\sqrt d\,Y/\|Y\|\).

The Gaussian density depends only on \(\|Y\|\), so the law of \(Y\), and therefore that of \(U\), is invariant under coordinate sign changes and coordinate permutations. A sign change of coordinate \(i\) shows \(\mathbb E U_i=0\). For \(i\ne j\), the same sign change shows \(\mathbb E[U_iU_j]=0\). Coordinate permutations show that all \(\mathbb E U_i^2\) are equal. Since
\[
\sum_{i=1}^d\mathbb E U_i^2=\mathbb E\|U\|^2=d,
\]
each diagonal second moment equals \(1\). Thus \(\mathbb EU=0\) and \(\operatorname{Cov}(U)=I_d\). Consequently,
\[
C_{\mathrm{RMS}}(Y)
=D_\gamma\operatorname{Cov}(U)D_\gamma=D_\gamma^2.
\]
For every nonzero \(v\in\mathbb R^d\),
\[
v^\top C_{\mathrm{RMS}}(Y)v
=\sum_{i=1}^d\gamma_i^2v_i^2>0,
\]
because every \(\gamma_i\ne0\).

For each fixed all-nonzero \(\gamma\), this single admissible input law therefore rules out every unit vector simultaneously. In particular, no unit direction chosen using only \(\gamma\) can have zero quadratic form for every admissible input distribution. The conclusion is nonexistence of a universal direction, not positive definiteness of the RMSNorm output covariance for every admissible input. This proves all parts of the integrated theorem.
