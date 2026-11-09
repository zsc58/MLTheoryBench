# Reference Proof

## Contract and proof obligations

The procedure sees only the observable filtration
\[
\mathcal F_t=\sigma((p_s,\lambda_s,\delta_s):1\le s\le t),
\qquad \delta_t=\mathbf 1\{p_t\le\lambda_t\}.
\]
The states are not revealed to it. For analysis only, define
\[
\mathcal G_t=\mathcal F_t\vee\sigma(Y_1,\ldots,Y_t).
\]
The threshold is measurable with respect to both \(\mathcal F_{t-1}\) and \(\mathcal G_{t-1}\). In the stationary experiment, fresh sampling makes the pairs \((Y_t,p_t)\) iid. In the deterministic-state experiment the p-values are independent with their specified state-dependent distributions.

The obligations are: the conditional error identities; the expected and almost-sure threshold-floor bounds; the finite-horizon no-rejection product bound; a horizon-independent eventual linear coefficient; and the unrestricted impossibility with an actual \(\Omega(T)\) expected-regret bound. All are proved below. The only external result used is the standard bounded martingale-difference strong law, stated with its hypotheses below.

## 1. Stationary conditional identities

Fix \(\pi\in(0,1)\) and take iid states with null probability \(\pi\). Fresh sampling and predictability give
\[
\mathbb E[\mathbf 1\{Y_t=0,p_t\le\lambda_t\}\mid\mathcal G_{t-1}]
=\pi\lambda_t,
\]
and
\[
\mathbb E[\mathbf 1\{Y_t=1,p_t\le\lambda_t\}\mid\mathcal G_{t-1}]
=(1-\pi)G(\lambda_t).
\]
Taking conditional expectations again also gives the corresponding identities conditioned on \(\mathcal F_{t-1}\). Using \(\mathcal G_t\), rather than claiming adaptation to the observable filtration, is essential when forming martingale differences involving the latent states.

## 2. Positive threshold floor

Continuity, strict increase, and the endpoint values of \(G\) imply that \(\lambda_\beta=G^{-1}(\beta)\in(0,1)\). If \(\lambda_t\ge\lambda_\beta\) almost surely for every \(t\), then
\[
\mathbb E V_T=\pi\sum_{t=1}^T\mathbb E\lambda_t
\ge\pi\lambda_\beta T.
\]
Since \(a,b>0\) and \(M_T\ge0\),
\[
\mathbb E\operatorname{Regret}_T\ge a\pi\lambda_\beta T.
\]

For the almost-sure assertion set
\[
X_t=\mathbf 1\{Y_t=0,p_t\le\lambda_t\}-\pi\lambda_t.
\]
These variables are \(\mathcal G_t\)-adapted, satisfy \(\mathbb E[X_t\mid\mathcal G_{t-1}]=0\), and have \(|X_t|\le1\).

The bounded martingale-difference strong law states that if \(X_t\) is adapted to a filtration \(\mathcal H_t\), has conditional mean zero given \(\mathcal H_{t-1}\), and is bounded in absolute value by a fixed finite constant for every \(t\), then \(T^{-1}\sum_{t=1}^T X_t\to0\) almost surely. All its hypotheses have just been checked. Therefore
\[
\frac{V_T}{T}-\frac{\pi}{T}\sum_{t=1}^T\lambda_t\longrightarrow0
\quad\text{almost surely}.
\]
The threshold-floor conditions hold simultaneously on a probability-one event, since there are countably many rounds. Hence
\[
\liminf_{T\to\infty}\frac{\operatorname{Regret}_T}{T}
\ge a\liminf_{T\to\infty}\frac{V_T}{T}
\ge a\pi\lambda_\beta
\quad\text{almost surely}.
\]

## 3. The two-phase experiment

Fix the procedure and its deterministic no-rejection envelope \((\widetilde\lambda_t)_{t\ge1}\), and suppose
\[
\sum_{t\ge1}\widetilde\lambda_t\le C<1.
\]
Because the envelope is nonnegative, necessarily \(C\ge0\). For each integer \(n\ge1\), consider the experiment with nulls through round \(n\) and alternatives in rounds \(n+1,\ldots,2n\).

Let \(A_0\) be the whole sample space and
\[
A_t=\{\delta_1=\cdots=\delta_t=0\}.
\]
On \(A_{t-1}\), the definition of the supremum gives \(\lambda_t\le\widetilde\lambda_t\). Actual thresholds need not equal this envelope and may still vary with the observed p-values.

In the null phase, conditional uniformity yields
\[
\mathbb P(A_t)
=\mathbb E[\mathbf 1_{A_{t-1}}(1-\lambda_t)]
\ge(1-\widetilde\lambda_t)\mathbb P(A_{t-1}).
\]
Iteration and the elementary inequality \(\prod_{j=1}^m(1-u_j)\ge1-\sum_{j=1}^m u_j\) for \(u_j\in[0,1]\) give
\[
\mathbb P(A_n)\ge\prod_{t=1}^n(1-\widetilde\lambda_t)
\ge1-\sum_{t=1}^n\widetilde\lambda_t
\ge1-C.
\]
The product inequality follows by induction from \((1-u)(1-v)=1-u-v+uv\ge1-u-v\).

Since \(G(0)=0\) and \(G\) is \(L\)-Lipschitz, \(G(x)\le Lx\). In the alternative phase,
\[
\begin{aligned}
\mathbb P(A_t)
&=\mathbb E[\mathbf 1_{A_{t-1}}(1-G(\lambda_t))]\\
&\ge(1-L\widetilde\lambda_t)_+\mathbb P(A_{t-1}).
\end{aligned}
\]
Consequently
\[
\mathbb P(A_{2n})\ge(1-C)
\prod_{t=n+1}^{2n}(1-L\widetilde\lambda_t)_+.
\]
These recursions remain valid when an event has probability zero or a product factor vanishes; no conditioning on a zero-probability event is needed.

On \(A_{2n}\), every alternative is missed, so \(M_{2n}=n\). It follows that
\[
\mathbb E\operatorname{Regret}_{2n}
\ge b n\mathbb P(A_{2n})
\ge b n(1-C)\prod_{t=n+1}^{2n}(1-L\widetilde\lambda_t)_+.
\]
This proves the finite-horizon bound for every \(n\ge1\).

## 4. Uniform eventual linear growth

Summability permits choosing an integer \(N\) such that
\[
L\sum_{t>N}\widetilde\lambda_t\le\tfrac12.
\]
For every \(n\ge N\), each factor in the relevant tail has \(L\widetilde\lambda_t\le1/2\), and the same elementary product inequality gives
\[
\prod_{t=n+1}^{2n}(1-L\widetilde\lambda_t)_+
\ge1-L\sum_{t=n+1}^{2n}\widetilde\lambda_t
\ge\tfrac12.
\]
Thus
\[
\mathbb E\operatorname{Regret}_{2n}\ge\frac{b(1-C)}2 n
\quad(n\ge N).
\]
The coefficient is strictly positive. The cutoff may depend on the fixed envelope and \(L\), not on the horizon being evaluated. This includes \(C=0\). The displayed right-hand side in the task is also at most \(b(1-C)n\), so it has linear order. The expected regret itself is at most \(2\max(a,b)n\).

For comparison with the source's infinite-product display, the same bound holds for every finite tail ending at \(m\ge n+1\); taking its decreasing limit as \(m\to\infty\) bounds the infinite tail product below by \(1/2\). Thus the frozen finite-product formulation and the source's infinite-product lower bound are both justified.

## 5. General impossibility and quantitative linear regret

The first two mechanisms are not an exhaustive dichotomy for arbitrary deterministic rules. To prove the unrestricted claim, use a fixed stationary mixed environment without imposing either a threshold floor or envelope summability.

Write \(q=1-\pi\), let
\[
S_T=\sum_{t=1}^T\mathbf 1\{Y_t=1,p_t\le\lambda_t\},
\qquad A_T=\sum_{t=1}^T\mathbb E\lambda_t.
\]
The conditional identities and the Lipschitz bound give
\[
\mathbb E V_T=\pi A_T,
\qquad
\mathbb E S_T=q\sum_{t=1}^T\mathbb E G(\lambda_t)\le q L A_T.
\]
Also \(S_T+M_T=\sum_{t=1}^T\mathbf 1\{Y_t=1\}\), so
\[
\mathbb E M_T=qT-\mathbb E S_T.
\]
In particular, \(\mathbb E V_T=o(T)\) would imply \(\mathbb E M_T=qT-o(T)\), whereas \(\mathbb E M_T=o(T)\) would force \(\mathbb E V_T=\Omega(T)\).

For the claimed linear weighted-regret bound at all horizons, combine the same identities directly:
\[
\mathbb E M_T+\frac{qL}{\pi}\mathbb E V_T\ge qT.
\]
Set \(d=\min\{b,a\pi/(qL)\}>0\). Nonnegativity of both error counts gives
\[
\begin{aligned}
\mathbb E\operatorname{Regret}_T
&\ge d\left(\mathbb E M_T+\frac{qL}{\pi}\mathbb E V_T\right)\\
&\ge\min\{b(1-\pi),a\pi/L\}\,T.
\end{aligned}
\]
The coefficient is independent of the procedure and of \(T\) for fixed \(a,b,\pi,L\). A single stationary environment, for example with \(\pi=1/2\), therefore witnesses linear expected regret for every such procedure. In particular, simultaneous sublinear expected errors cannot be guaranteed uniformly over environments.

## Source-local repair and closure

The equality at source L000251-L000252 is replaced by the successive-conditioning lower bound in Section 3. No assumption or conclusion changes. The finite-product target is explicitly supported by source L000255. The stronger quantitative conclusion in Section 5 is elementary algebra from the source's coupling, not an additional public target. All listed proof obligations are closed; there are no unresolved specialized dependencies.
