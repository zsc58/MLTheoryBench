# Reference Proof

## Proof Structure

1. Derive the mean completion time for reset interval \(\tau\) as \(G(\tau)/F(\tau)\).
2. Compare consecutive intervals by expanding the ratio difference.
3. Express the numerator as a negative covariance under a \(u_\tau\)-weighted law; prove the associated kernel is decreasing, so the covariance is nonpositive.
4. Conclude monotonicity and optimality of \(\tau=1\).

## Complete Proof

Write \(q=1-p\), and let
\[
u_\tau(p)=\sum_{j=0}^{\tau-1}q^j,\qquad
F(\tau)=\mathbb E[1-q^\tau],\qquad
G(\tau)=\mathbb E[u_\tau(p)].
\]
The assumption \(\mathbb P(p>0)>0\) implies \(F(\tau)>0\) for every finite \(\tau\ge1\).

Under interval \(\tau\), a question is attempted until it succeeds or has accumulated \(\tau\) failures; after \(\tau\) failures a fresh independent question is drawn. For \(k=n\tau+r\), with \(n\ge0\) and \(0\le r<\tau\), survival through \(k\) attempts has probability
\[
\mathbb E[q^\tau]^n\,\mathbb E[q^r].
\]
Therefore the tail-sum formula gives
\[
\mathbb E[T_\tau]
 =\sum_{n\ge0}\sum_{r=0}^{\tau-1}\mathbb E[q^\tau]^n\mathbb E[q^r]
 =\frac{\sum_{r=0}^{\tau-1}\mathbb E[q^r]}{1-\mathbb E[q^\tau]}
 =\frac{G(\tau)}{F(\tau)}.
\]

Let \(A_\tau=F(\tau)\) and \(B_\tau=G(\tau)\). Since \(u_{\tau+1}=u_\tau+q^\tau\),
\[
A_\tau=\mathbb E[p u_\tau],\quad B_\tau=\mathbb E[u_\tau],\quad
A_{\tau+1}=\mathbb E[p u_\tau+p q^\tau],\quad
B_{\tau+1}=\mathbb E[u_\tau+q^\tau].
\]
Define the probability law \(\mu_\tau\) by
\[
d\mu_\tau=\frac{u_\tau(p)}{G(\tau)}\,dP(p),
\]
and define \(h_\tau(p)=q^\tau/u_\tau(p)\). Then
\[
B_{\tau+1}A_\tau-B_\tau A_{\tau+1}
 =G(\tau)^2\big(\mathbb E_{\mu_\tau}[p]\,\mathbb E_{\mu_\tau}[h_\tau]
       -\mathbb E_{\mu_\tau}[p h_\tau]\big)
 =-G(\tau)^2\operatorname{Cov}_{\mu_\tau}(p,h_\tau).
\]
The function \(h_\tau\) is nonnegative and nonincreasing in \(p\). Indeed, for \(0<p\le1\), \(h_\tau=p(1-p)^\tau/[1-(1-p)^\tau]\), and direct differentiation (with the continuous value \(h_\tau(0)=1/\tau\)) yields
\[
h_\tau'(p)= -\frac{q^{\tau-1}\left(\tau+\sum_{j=1}^{\tau-1}(\tau-j)q^j\right)}{u_\tau(p)^2}\le0.
\]
For any one-dimensional law, an increasing function and a decreasing function have nonpositive covariance (e.g. by the independent-copy identity \(2\operatorname{Cov}(X,Y)=\mathbb E[(X-X')(Y-Y')]\)). Hence \(\operatorname{Cov}_{\mu_\tau}(p,h_\tau)\le0\), so
\[
B_{\tau+1}A_\tau-B_\tau A_{\tau+1}\ge0.
\]
Because \(A_\tau,A_{\tau+1}>0\),
\[
\mathbb E[T_{\tau+1}]-\mathbb E[T_\tau]
=\frac{B_{\tau+1}A_\tau-B_\tau A_{\tau+1}}{A_{\tau+1}A_\tau}\ge0.
\]
Thus \(\mathbb E[T_\tau]\) is nondecreasing over integer \(\tau\ge1\). Consequently \(\tau=1\) minimizes the expected attempts per solved question among all deterministic reset intervals, proving the claim.
