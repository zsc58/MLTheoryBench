# Reference Proof

## Proof Structure

Fix a channel, expand the coordinatewise products in the mixer, and isolate the factors depending only on the output position and input position. The displacement kernel supplies the middle Toeplitz factor. Entrywise matrix multiplication then gives the required diagonal-Toeplitz-diagonal representation.

## Complete Proof

Fix a channel \(h\in\{1,\ldots,p\}\). Since all products in the mixer are coordinatewise,
\[
y_i^{(h)}
=\phi(Sx_i)^{(h)}\sum_{j=1}^n
 \kappa^{(h)}\!\left(\frac{i-j}{n}\right)
 (Qx_j)^{(h)}\phi(Rx_j)^{(h)}.
\]
With
\[
a_j^{(h)}=(Qx_j)^{(h)}\phi(Rx_j)^{(h)},
\qquad
b_i^{(h)}=\phi(Sx_i)^{(h)},
\]
this becomes
\[
y_i^{(h)}=\sum_{j=1}^n
 b_i^{(h)}\kappa^{(h)}\!\left(\frac{i-j}{n}\right)a_j^{(h)}.
\]
Thus the channelwise summand matrix has entries
\[
M_{ij}^{(h)}=b_i^{(h)}\kappa^{(h)}\!\left(\frac{i-j}{n}\right)a_j^{(h)}.
\]

Define
\[
T_{ij}^{(h)}=\kappa^{(h)}\!\left(\frac{i-j}{n}\right),
\quad
D_{\mathrm{out}}^{(h)}=\operatorname{diag}(b_1^{(h)},\ldots,b_n^{(h)}),
\quad
D_{\mathrm{in}}^{(h)}=\operatorname{diag}(a_1^{(h)},\ldots,a_n^{(h)}).
\]
For fixed \(n\), the entry \(T_{ij}^{(h)}\) depends on \(i,j\) only through \(i-j\). Hence \(T^{(h)}\) is Toeplitz. Moreover,
\[
\bigl(D_{\mathrm{out}}^{(h)}T^{(h)}D_{\mathrm{in}}^{(h)}\bigr)_{ij}
=b_i^{(h)}T_{ij}^{(h)}a_j^{(h)}
=M_{ij}^{(h)}.
\]
Therefore
\[
M^{(h)}=D_{\mathrm{out}}^{(h)}T^{(h)}D_{\mathrm{in}}^{(h)},
\]
so \(M^{(h)}\) is separable and its row sums give \(y_i^{(h)}\). The argument applies independently to every channel \(h\), completing the proof.
