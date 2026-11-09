# Reference Proof

## Proof Structure

First convert the pointwise attention-to-normal-space assumption into a squared bound by applying the elementary quadratic inequality and Cauchy-Schwarz across the attention layers. Taking expectation identifies the resulting sum with the consistency loss. Then use the loss guarantee and the almost-sure lower bound on the update magnitude to control the normalized normal-energy fraction in the definition of a proximal anchor.

## Complete Proof

Let
\[
x_\ell=\|H_\ell(z_t,t,u)-H_\ell(z_t,t,a_\star)\|_F\ge 0.
\]
The architectural assumption gives, almost surely,
\[
\|P_ND_{a_\star}\|\le C\sum_{\ell=1}^L x_\ell+\eta.
\]
Therefore, using \((r+s)^2\le 2r^2+2s^2\),
\[
\|P_ND_{a_\star}\|^2
\le 2C^2\left(\sum_{\ell=1}^Lx_\ell\right)^2+2\eta^2.
\]
Cauchy-Schwarz across the \(L\) layers yields
\[
\left(\sum_{\ell=1}^Lx_\ell\right)^2
\le L\sum_{\ell=1}^Lx_\ell^2.
\]
Combining these inequalities and taking expectation under the distribution specified in the setup gives
\[
\mathbb E\|P_ND_{a_\star}\|^2
\le 2C^2L\,\mathbb E\left[\sum_{\ell=1}^L
\|H_\ell(z_t,t,u)-H_\ell(z_t,t,a_\star)\|_F^2\right]+2\eta^2
=2C^2LJ(a_\star)+2\eta^2.
\]
Since \(J(a_\star)\le\gamma\), this also implies
\[
\mathbb E\|P_ND_{a_\star}\|^2
\le 2C^2L\gamma+2\eta^2.
\]

For the normalized energy fraction, \(\delta>0\) and the almost-sure bound \(\|D_{a_\star}\|^2\ge c_{\min}>0\) imply
\[
\frac{\|P_ND_{a_\star}\|^2}
{\|D_{a_\star}\|^2+\delta}
\le
\frac{\|P_ND_{a_\star}\|^2}{c_{\min}}
\quad\text{almost surely}.
\]
Taking expectations and applying the preceding normal-energy estimate gives
\[
\mathbb E\left[
\frac{\|P_ND_{a_\star}\|^2}
{\|D_{a_\star}\|^2+\delta}
\right]
\le
\frac{2C^2L\gamma+2\eta^2}{c_{\min}}
=\rho^2.
\]
Because the assumed parameter regime has \(\rho\in[0,1)\), this is exactly the defining inequality for \(a_\star\) to be a \(\rho\)-proximal anchor.
