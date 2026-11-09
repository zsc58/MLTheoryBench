# Problem

## Setup

Let N and n be positive integers. Fix training inputs x_1,...,x_N in a measurable input space X, a probability measure μ on X, and a measurable deterministic target function y:X→R. The training labels are y_a=y(x_a), and y=(y_1,...,y_N)^T denotes their vector. The training data, μ, and target function are held fixed in every expectation below; expectation is only over the law of the frozen random parameter Θ.

Let h(x;Θ)∈R^n be jointly measurable random features. Define Φ_{ai}=h_i(x_a;Θ), K=n^(-1)ΦΦ^T, and k(x)=n^(-1)Φh(x;Θ). For λ>0, the ridge readout minimizes N^(-1)||Φw-y||_2^2+λ||w||_2^2 over w∈R^n. Set γ=Nλ/n and G=(K+γI_N)^(-1).

Assume
\[
\mathbb E\|K\|_2<\infty,\qquad
\mathbb E\int_X\|k(x)\|_2^2\,d\mu(x)<\infty,\qquad
c:=\int_X y(x)^2\,d\mu(x)<\infty.
\]
Define
\[
C=\int_X k(x)k(x)^T\,d\mu(x),\qquad
b=\int_X y(x)k(x)\,d\mu(x).
\]
The training, test, and generalization errors are
\[
E_{\rm tr}=\frac{\gamma^2}{N}y^TG^2y,\qquad
E_{\rm te}=y^TGCGy-2b^TGy+c,\qquad
E_{\rm gen}=E_{\rm te}-E_{\rm tr}.
\]

Write
\[
\bar K=\mathbb EK,\quad \bar C=\mathbb EC,\quad \bar b=\mathbb Eb,
\qquad
\Delta K=K-\bar K,\quad\Delta C=C-\bar C,\quad\Delta b=b-\bar b,
\]
so all three fluctuations are centered, and set G_0=(\bar K+γI_N)^(-1). Assume ||G_0ΔK||_2<1 almost surely. All three fluctuations arise from the same Θ; no independence between them is assumed.

Let V be a deterministic tensor such that, for every deterministic A∈R^{N×N},
\[
\mathbb E[\Delta K A\Delta K]=n^{-1}(V\star A),\qquad
(V\star A)_{\alpha\delta}
=\sum_{\beta,\eta=1}^N V_{(\alpha\beta)(\eta\delta)}A_{\beta\eta}.
\]
For precision, use the following finite-order moment formulation of finite-width power counting. Put
\[
\delta_K=\|\Delta K\|_2,\qquad
\delta_C=\|\Delta C\|_2,\qquad
\delta_b=\|\Delta b\|_2.
\]
The moments below are finite. For a width-indexed family, with N, the training data, μ, and the target fixed, assume
\[
\mathbb E\delta_K^p=O(n^{-p/2})\quad(1\le p\le4),
\]
\[
\mathbb E[\delta_K^q\delta_C]=O(n^{-(q+1)/2}),\qquad
\mathbb E[\delta_K^q\delta_b]=O(n^{-(q+1)/2})\quad(0\le q\le2),
\]
where δ_K^0=1 and the constants in these moment bounds are independent of n.

The remainder notation in the conclusions refers to fluctuation-insertion order. A deterministic matrix remainder O(ΔK^4) has operator norm at most a deterministic constant times Eδ_K^4. A scalar remainder O(Δ^3) has absolute value at most a deterministic constant times
\[
\mathbb E\big[\delta_K^3+\delta_K^2\delta_C+\delta_K^2\delta_b\big].
\]
Here Δ denotes the tuple (ΔK,ΔC,Δb), not an additional random matrix. Remainder constants may depend on N, γ, ||y||_2, ||\bar K||_2, ||\bar C||_2, and ||\bar b||_2, but not on the realized Θ or other features of its law. No uniformity in these deterministic quantities is asserted.

## Task

Prove that
\[
\mathbb E E_{\rm tr}=\frac{\gamma^2}{N}y^T(G_0^2+L_1+L_2+O(\Delta K^4))y,
\]
where
\[
\begin{aligned}
L_1={}&\mathbb E[G_0\Delta K G_0\Delta K G_0^2+G_0^2\Delta K G_0\Delta K G_0+G_0\Delta K G_0^2\Delta K G_0],\\
L_2={}&-\mathbb E[G_0\Delta K G_0\Delta K G_0\Delta K G_0^2+G_0^2\Delta K G_0\Delta K G_0\Delta K G_0\\
&\qquad+G_0\Delta K G_0\Delta K G_0^2\Delta K G_0+G_0\Delta K G_0^2\Delta K G_0\Delta K G_0].
\end{aligned}
\]
Moreover,
\[
\mathbb E E_{\rm te}=E_{\rm te}^{(0)}+E_{\rm te}^{(1)}+O(\Delta^3),
\]
with
\[
E_{\rm te}^{(0)}=y^T G_0\bar C G_0y-2\bar b^T G_0y+c,
\]
\[
\begin{aligned}
E_{\rm te}^{(1)}=\mathbb E\{&y^T[G_0\Delta K G_0\Delta K G_0\bar C G_0+G_0\bar C G_0\Delta K G_0\Delta K G_0\\
&+G_0\Delta K G_0\bar C G_0\Delta K G_0-G_0\Delta K G_0\Delta C G_0-G_0\Delta C G_0\Delta K G_0]y\\
&-2[\bar b^T G_0\Delta K G_0\Delta K G_0y-\Delta b^T G_0\Delta K G_0y]\}.
\end{aligned}
\]
Finally,
\[
\mathbb E E_{\rm gen}=E_{\rm gen}^{(0)}+E_{\rm gen}^{(1)}+O(\Delta^3),
\]
where
\[
E_{\rm gen}^{(0)}=E_{\rm te}^{(0)}-\frac{\gamma^2}{N}y^T G_0^2y,
\qquad
E_{\rm gen}^{(1)}=E_{\rm te}^{(1)}-\frac{\gamma^2}{N}y^T L_1y.
\]
Thus the quadratic gap correction retains the mixed ΔK–ΔC and Δb–ΔK contractions in addition to the pure training-kernel contractions.
