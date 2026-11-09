# Problem

## Setup

Let n,m,N be positive integers and S>0. Fix a list G^1,...,G^N in {0,1}^{n by m}, each with no zero row and no zero column. Sample an index I uniformly from {1,...,N} and set G=G^I. Repetitions in the list are allowed and retain their multiplicities. The state space is R^{n by m}, with Frobenius norm ||X||_F^2=sum_{v,e}X_{ve}^2.

For any matrix g in this list, let 1_k denote the k-dimensional all-ones vector and define

\[
D_V(g)=\operatorname{diag}(g\mathbf 1_m),\qquad
D_E(g)=\operatorname{diag}(g^\top\mathbf 1_n),
\]
\[
L_V(g)=I_n-D_V(g)^{-1/2}gD_E(g)^{-1}g^\top D_V(g)^{-1/2},
\]
\[
A_E(g)=\operatorname{offdiag}\!\left(D_E(g)^{-1/2}g^\top gD_E(g)^{-1/2}\right),\qquad
D_{\mathrm{ov}}(g)=\operatorname{diag}(A_E(g)\mathbf 1_m),
\]
\[
L_E(g)=I_m-D_{\mathrm{ov}}(g)^{-1/2}A_E(g)D_{\mathrm{ov}}(g)^{-1/2},\qquad
\mathcal A_g(X)=L_V(g)X+XL_E(g).
\]

Here diag forms a diagonal matrix from a vector, offdiag sets a matrix's diagonal entries to zero, and every inverse diagonal power is evaluated on positive entries and assigned zero on zero entries. Zero overlap degrees are permitted.

Fix tau,gamma>0 and a deterministic matrix bar M in R^{n by m}, common to every sampled G. Let alpha,beta:[0,S]->[0,1] be deterministic continuous functions, with alpha nonincreasing and beta nondecreasing, satisfying

\[
\alpha(s)+\beta(s)=1,\qquad \alpha(0)=1,\qquad \beta(0)=0,\qquad \beta(s)>0\quad(0<s\leq S).
\]

Let W be an n-by-m matrix Brownian motion with independent standard Brownian entries, independent of I. Conditional on G, define

\[
dX_s=-\alpha(s)\mathcal A_G(X_s)\,ds-\beta(s)\gamma(X_s-\bar M)\,ds+\sqrt{2\tau\beta(s)}\,dW_s,\qquad X_0=G.
\]

For 0<s<=S, let p_s(·|g) be the conditional density of X_s given G=g, with respect to Lebesgue measure on the state space, and put

\[
\widehat p_s(X)=\frac1N\sum_{i=1}^N p_s(X\mid G^i),\qquad
r_{s\mid g}(X)=\nabla_X\log p_s(X\mid g),\qquad
\widehat r_s(X)=\nabla_X\log\widehat p_s(X).
\]

Gradients are taken with respect to the matrix entries. Define the conditional target

\[
\nu^*_{s\mid g}(X)=\alpha(s)\mathcal A_g(X)+\beta(s)\gamma(X-\bar M)+2\tau\beta(s)r_{s\mid g}(X).
\]

For fixed s, minimize

\[
J_s(u)=\mathbb E\left\|u(X_s)-\nu^*_{s\mid G}(X_s)\right\|_F^2
\]

over Borel state-only fields u:R^{n by m}->R^{n by m} satisfying E||u(X_s)||_F^2<infinity. Such a field may depend on the fixed data list and the fixed time s, but not separately on the sampled G. All expectations and conditional expectations use the joint experiment specified above.

## Task

Prove that for every s in (0,S], the minimizers of J_s are exactly the fields equal, up to widehat p_s-null sets, to the conditional-expectation predictor

\[
\nu_s^\dagger(X)=\mathbb E\!\left[\nu^*_{s\mid G}(X_s)\mid X_s=X\right],
\]

and that its canonical posterior version satisfies

\[
\nu_s^\dagger(X)=\alpha(s)\mathbb E\!\left[\mathcal A_G(X)\mid X_s=X\right]
+\beta(s)\gamma(X-\bar M)+2\tau\beta(s)\widehat r_s(X).
\]

Use this canonical version in the following reverse SDE. Suppose it has a nonexplosive solution unique in law on [0,S), with the stated initial distribution, and is solved exactly:

\[
dY_t=\nu_{S-t}^\dagger(Y_t)\,dt+\sqrt{2\tau\beta(S-t)}\,d\overline W_t,\qquad
Y_0\sim\widehat p_S.
\]

Here overline W is an n-by-m matrix Brownian motion with independent standard Brownian entries, and the initial draw is independent of its increments. Prove that

\[
\operatorname{Law}(Y_t)=\widehat p_{S-t}\quad(0\leq t<S),
\]

and that these laws converge weakly to the empirical measure N^{-1}sum_{i=1}^N delta_{G^i} as t increases to S.
