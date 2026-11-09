# Reference Proof

## Scope and proof obligations

The two conclusions use their respective settings. The explicit PTQ example uses a Euclidean normal basin and is not asserted to satisfy the bounded-gradient and width assumptions of the recovery statement. Its loss is defined globally, so the loss of any finite-codebook minimizer is meaningful even when that minimizer lies outside the local neighborhood.

The theorem-critical obligations are: identify the example's proxy and exclude all low-normal-distance lattice points uniformly in bitwidth; obtain the loss bound; establish the weighted-distance differential and discrepancy estimates; establish locality and positive drift; prove descent and invariance without circularity; and derive the bound for the actual first deployed entry. All six obligations are discharged below without a specialized external dependency.

## Step 001: Proxy and uniform exclusion of lattice points

Write \(c=\cos\theta\), \(s=\sin\theta\). Then \(c>s>0\), \(\alpha=c-s>0\), and \((\tau,\nu)\) is an orthonormal basis. Also \(s>\alpha\): indeed, \(2s\ge1>c\) on the specified angle range.

At \(\bar w_{\rm ex}=w_0-u\tau\), one has \(t=-u\) and \(z=0\). Since \(r>0\), the normal loss vanishes in a neighborhood of this point, and therefore
\[
\nabla f_\theta(\bar w_{\rm ex})=0,\qquad
\nabla^2 f_\theta(\bar w_{\rm ex})=\tau\tau^\top,\qquad
S_{\rm ex}(q)=\tfrac12(t(q)+u)^2.
\]
This reference choice gives the same proxy as every stationary reference admitted by the source. To check this, the gradient formula shows that stationarity is equivalent to \(t=-u\) and \(|z|\le r\). At \(|z|=r\), the normal second derivative does not exist because its two one-sided values are \(0\) and \(\mu>0\). Every stationary reference with an existing Hessian thus has \(|z|<r\), Hessian \(\tau\tau^\top\), and the displayed proxy.

The nearest-point projection onto \(M_{\rm ex}\) is \(w_0+t(w)\tau\), with residual \(z(w)\nu\). Consequently the example's specified basin is precisely its identity-metric normal basin. In particular, its definition does not involve the general setting's arbitrary matrix \(H\).

Set
\[
\zeta=\frac{R_{\rm ex}+\delta}{2},\qquad
\mathcal N=\{(1,0),(0,0),(2,0),(1,1),(1,-1)\}.
\]
Then \(R_{\rm ex}<\zeta<\delta\). For integer indices, write
\[
q_{ij}(\sigma)=\sigma(i,j),\quad
t_{ij}(\sigma)=c(\sigma i-1)+s\sigma j,\quad
z_{ij}(\sigma)=-s(\sigma i-1)+c\sigma j.
\]
Orthonormality gives
\[
t_{ij}(\sigma)^2+z_{ij}(\sigma)^2=(\sigma i-1)^2+(\sigma j)^2.
\]
Privately introduce the comparison codeword \(q_b(\sigma)=(0,\sigma)\), which is feasible for every integer \(B\ge2\), and put \(a(\sigma)=c-s\sigma\). At \(\sigma=1\), \(a(1)=\alpha>u\).

At scale \(1\), the five absolute proxy residuals for the indices in \(\mathcal N\), in the listed order, are
\[
u,\quad c-u,\quad c+u,\quad s+u,\quad s-u.
\]
Every one is strictly greater than \(\alpha-u\). For the first this follows from \(2u>\alpha\); for the last it follows from \(s>\alpha\); the other comparisons follow directly from \(c>\alpha\), \(s>\alpha\), and \(u>0\).

There is a single open interval \(I_{\rm fail}\subset(0,\infty)\) about \(1\) on which all the following strict inequalities hold:
\[
s|\sigma-1|<r,\qquad s+c\sigma>R_{\rm ex},\qquad a(\sigma)>u,
\]
\[
|t_{ij}(\sigma)+u|>a(\sigma)-u\qquad((i,j)\in\mathcal N),
\]
\[
\sqrt2\,\sigma-|\sigma-1|>
\sqrt{\zeta^2+a(\sigma)^2}.
\]
The first three and the five finite comparisons hold at \(1\) by the hypotheses and the preceding calculations. For the final inequality, at \(1\) its strictness is exactly
\[
\zeta^2+\alpha^2<\delta^2+\alpha^2=2.
\]
All the displayed functions of \(\sigma\) are continuous, so intersecting finitely many sufficiently small neighborhoods proves the interval's existence. This construction does not involve \(B\).

The good codeword satisfies \(|z(q_g(\sigma))|=s|\sigma-1|<r<R_{\rm ex}\), hence belongs to \(\mathcal B_{\rm ex}\). The comparison codeword satisfies
\[
z(q_b(\sigma))=s+c\sigma>R_{\rm ex},\qquad
|t(q_b(\sigma))+u|=a(\sigma)-u>0.
\]

It remains essential to control every index outside \(\mathcal N\), not merely a finite codebook chosen in advance. For such an index,
\[
\|(i-1,j)\|\ge\sqrt2.
\]
Since \(\sigma>0\), the reverse triangle inequality gives the uniform bound
\[
\|(\sigma i-1,\sigma j)\|
=\|\sigma(i-1,j)+(\sigma-1,0)\|
\ge\sqrt2\,\sigma-|\sigma-1|
>\sqrt{\zeta^2+a(\sigma)^2}.
\]
Thus, if \(|z_{ij}(\sigma)|<\zeta\), the orthonormal-coordinate identity implies
\[
|t_{ij}(\sigma)|>a(\sigma),\qquad
|t_{ij}(\sigma)+u|\ge|t_{ij}(\sigma)|-u>a(\sigma)-u.
\]
Together with the finite comparisons, this proves, for every integer pair,
\[
|z(q_{ij}(\sigma))|<\zeta
\quad\Longrightarrow\quad
S_{\rm ex}(q_{ij}(\sigma))>S_{\rm ex}(q_b(\sigma)).
\]
The codebook is finite and nonempty, so minimizers exist. Every minimizer has proxy value no greater than that of the feasible comparison codeword. Hence every minimizer satisfies \(|z(q_*)|\ge\zeta>R_{\rm ex}\), proving the required exclusion simultaneously for all bitwidths.

## Step 002: True-loss lower bound

Because \(|z(q_g(\sigma))|<r\),
\[
f_\theta(q_g(\sigma))=\tfrac12\bigl(u+c(\sigma-1)\bigr)^2.
\]
For every proxy minimizer, \(|z(q_*)|\ge\zeta>r\), and the tangential loss is nonnegative. Therefore
\[
f_\theta(q_*)\ge\tfrac\mu2(\zeta-r)^2.
\]
Moreover,
\[
\zeta-r=\tfrac12(R_{\rm ex}+\delta-2r)>	frac12(\delta-r)>0.
\]
Subtracting the good codeword's loss proves
\[
f_\theta(q_*)-f_\theta(q_g(\sigma))
\ge\frac\mu8(\delta-r)^2-
\frac12\bigl(u+c(\sigma-1)\bigr)^2.
\]
This is the asserted affine-in-\(\mu\) lower bound when the other displayed quantities are fixed. In particular, at \(\sigma=1\), with \(\theta,u,r,\varepsilon\) fixed and \(r<\delta\), the regime \(R_{\rm ex}<\delta\) holds for all sufficiently large \(\mu\), and the lower bound grows linearly. No claim that an arbitrary varying choice of parameters or minimizers produces an exactly linear loss gap is needed.

## Step 003: Weighted-distance calculus and discrepancy estimates

Now use only the general recovery setting. For \(x\in U\), define
\[
n(x)=x-P_M(x),\qquad d(x)=\|n(x)\|_H,\qquad
\Phi(x)=\tfrac12d(x)^2,\qquad L_\Phi=\lambda_1(1+L_P).
\]
The nearest-point first-order condition gives \(n(x)\in N_M(P_M(x))\): differentiate squared distance along any manifold curve through the nearest point. For every vector \(h\), differentiating the manifold-valued curve \(P_M(x+th)\) at \(t=0\) shows that \(DP_M(x)h\) is tangent at \(P_M(x)\). Since \(H\) preserves the normal space, \(DP_M(x)^\top Hn(x)=0\). The chain rule consequently yields
\[
\nabla\Phi(x)=(I-DP_M(x))^\top Hn(x)=Hn(x).
\]
For all \(x,y\in U\),
\[
\|n(x)-n(y)\|\le(1+L_P)\|x-y\|,
\]
so
\[
\|\nabla\Phi(x)-\nabla\Phi(y)\|\le L_\Phi\|x-y\|.
\]
Also, whenever \(x,y\in U\) and \(\|y-x\|\le\rho\),
\[
d(y)\le d(x)+\sqrt{\lambda_1}(1+L_P)\rho.
\]
These estimates involving \(P_M(y)\) will be applied to \(y=\mathsf Q(x)\) only after establishing \(y\in U\).

The lower width inequality gives both
\[
a:=R-\sqrt{\lambda_1}(1+L_P)\rho>0
\]
and
\[
D=c_\perp\sqrt{\lambda_d}R-L_\Phi\rho G>0.
\]
The second assertion follows by using the \((G/c_\perp)\sqrt{\lambda_1/\lambda_d}\) term inside the maximum and multiplying the resulting strict inequality by \(c_\perp\sqrt{\lambda_d}\).

## Step 004: Locality and positive drift

Suppose \(x_k\in\mathcal B\), and put \(y_k=\mathsf Q(x_k)\), \(d_k=d(x_k)\). Quantization is defined because \(x_k\in U\). For every \(t\in[0,1]\),
\[
\operatorname{dist}(x_k+t(y_k-x_k),M)
\le d_k/\sqrt{\lambda_d}+t\rho
\le R/\sqrt{\lambda_d}+\rho<R_U.
\]
Thus \(y_k\) and the entire quantization segment belong to \(U\). In particular \(\nabla f(y_k)\) is defined and has norm at most \(G\). The step-size restriction gives \(\eta G\le\rho\), so the prospective update segment also lies in \(U\):
\[
\operatorname{dist}(x_k-t\eta\nabla f(y_k),M)
\le R/\sqrt{\lambda_d}+t\eta G<R_U.
\]
This establishes locality before any descent or next-iterate invariance is used.

If \(y_k\notin\mathcal B\), it belongs to \(U\setminus\mathcal B\), so the sharp-wall assumption applies. The spectral inequality \(H^2\succeq\lambda_d H\) implies \(\|Hv\|\ge\sqrt{\lambda_d}\|v\|_H\). Decomposing the pairing gives
\[
\begin{aligned}
\langle Hn(x_k),\nabla f(y_k)\rangle
&=\langle Hn(y_k),\nabla f(y_k)\rangle
 +\langle H(n(x_k)-n(y_k)),\nabla f(y_k)\rangle\\
&\ge c_\perp\|Hn(y_k)\|-\lambda_1(1+L_P)\rho G\\
&\ge c_\perp\sqrt{\lambda_d}\,d(y_k)-L_\Phi\rho G\\
&\ge c_\perp\sqrt{\lambda_d}R-L_\Phi\rho G=D.
\end{aligned}
\]
Here \(d(y_k)>R\), the quantizer error is at most \(\rho\), and the projection discrepancy is bounded by \(L_P\rho\). This proves the required drift margin with precisely the constants in the statement.

## Step 005: Descent and invariance

For a segment \(x+th\) contained in \(U\), the fundamental theorem of calculus and the gradient Lipschitz bound give
\[
\begin{aligned}
\Phi(x+h)-\Phi(x)-\langle\nabla\Phi(x),h\rangle
&=\int_0^1\langle\nabla\Phi(x+th)-\nabla\Phi(x),h\rangle\,dt\\
&\le\tfrac12L_\Phi\|h\|^2.
\end{aligned}
\]
Apply this with \(h=-\eta\nabla f(y_k)\). Step 004 already established containment of this segment. While \(y_k\notin\mathcal B\),
\[
\begin{aligned}
\Phi(x_{k+1})
&\le\Phi(x_k)-\eta D+\tfrac12L_\Phi\eta^2G^2\\
&\le\Phi(x_k)-\tfrac12\eta D,
\end{aligned}
\]
where the last inequality uses \(\eta\le D/(L_\Phi G^2)\). Equivalently,
\[
d_{k+1}^2\le d_k^2-\eta D.
\]
Since the update endpoint is already known to belong to \(U\), this inequality implies \(x_{k+1}\in\mathcal B\) whenever \(x_k\in\mathcal B\) and the deployed iterate has not yet entered.

Starting from \(x_0=\bar w\in\mathcal B\), Steps 004 and 005 inductively establish that every needed latent iterate lies in \(\mathcal B\), every needed deployed point lies in \(U\), and every pre-entry update is well defined. If entry has not occurred, the same reasoning constructs the next step. No behavior after the first deployed entry is asserted or used.

## Step 006: Actual first-entry time

For each constructed iterate, Step 003 applies because both \(x_k\) and \(y_k\) are in \(U\). It shows that
\[
d_k\le a\quad\Longrightarrow\quad d(y_k)\le R
\quad\Longrightarrow\quad y_k\in\mathcal B.
\]
This threshold is sufficient for entry; it need not characterize the first entry exactly.

If \(T=\infty\), the induction constructs all iterates and the decrease inequality gives
\[
0\le d_k^2\le d_0^2-k\eta D
\]
for every integer \(k\ge0\), a contradiction for sufficiently large \(k\). Thus \(T<\infty\). The initial-failure assumption gives \(T\ge1\) and \(d_0>a\). At the last pre-entry index,
\[
a^2<d_{T-1}^2\le d_0^2-(T-1)\eta D.
\]
Consequently,
\[
T<1+\frac{d_0^2-a^2}{\eta D}
\le1+\frac{\max\{d_0^2-a^2,0\}}{\eta D}.
\]
Substituting the definitions of \(d_0\) and \(a\) proves the stated non-strict upper bound for the actual first deployed entry. Together with Steps 001 and 002, this proves both conclusions.
