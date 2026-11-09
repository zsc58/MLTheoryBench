# Problem

## Setup

Let d>=2 and n>=1 be integers. Write

\[
\Delta_d=\{p\in\mathbb R^d:p_i\ge0,\ \sum_i p_i=1\},
\]

and let e_1,...,e_d be the standard basis vectors of R^d. Outcomes satisfy y_t in {e_1,...,e_d}.

The adversary may fix the outcome sequence in advance, or may be non-anticipating: at round t it may use past outcomes, past predictions, and its own randomness to select y_t, but it has no access to the learner's fresh round-t randomization. All strategies and losses are measurable. The learner observes y_t only after issuing its round-t prediction.

A bounded loss is a Borel measurable function

\[
\ell:\Delta_d\times\{e_1,\ldots,e_d\}\longrightarrow[-1,1].
\]

It is proper if, for every p in Delta_d,

\[
p\in\operatorname*{argmin}_{q\in\Delta_d}
\mathbb E_{Y\sim p}[\ell(q,Y)].
\]

Define L(q,p)=sum_i p_i ell(q,e_i), and let mathcal L be the class of these bounded proper losses.

For beta>0, let mathcal S_beta consist of losses in mathcal L that are differentiable in their prediction argument and satisfy, for every p,q in Delta_d and every y in {e_1,...,e_d},

\[
\ell(q,y)-\ell(p,y)
\le \langle\nabla_p\ell(p,y),q-p\rangle
+\frac\beta2\|q-p\|_2^2.
\]

Differentiability is understood on the closed simplex: the gradient is a vector in the tangent space {v:sum_i v_i=0} representing the first-order expansion

\[
\ell(p+h,y)=\ell(p,y)+\langle\nabla_p\ell(p,y),h\rangle
+o(\|h\|_2)
\]

as h tends to zero through vectors with p+h in Delta_d. This convention includes boundary points.

Set rho=d^{3/4}/sqrt(n), and assume rho<=1/2. Let B_2^d={u in R^d:||u||_2<=1}, let H(p)={u in R^d:<u,p>=0}, and let diag(p) denote the diagonal matrix with diagonal p.

Initialize hat p_0=(1/d,...,1/d). At each round t=1,...,n:

1. Use hat p_{t-1}=(t-1)^{-1}sum_{s<t}y_s when t>1, and the initialization when t=1.
2. Using fresh randomness, sample U_t uniformly from rho B_2^d intersect H(hat p_{t-1}), with uniformity defined by normalized (d-1)-dimensional Euclidean volume on that subspace. Conditional on the past history and the adversary's chosen y_t, this is the sampling law of U_t.
3. Set xi_t=diag(hat p_{t-1})U_t and predict q_t=hat p_{t-1}+xi_t.
4. Observe y_t and update hat p_t=t^{-1}sum_{s<=t}y_s.

For a fixed loss ell, define expected regret by

\[
\operatorname{Reg}_\ell(n)=
\mathbb E\left[
\sum_{t=1}^n\ell(q_t,y_t)
-\sum_{t=1}^n\ell(\hat p_n,y_t)
\right],
\]

where the expectation includes the learner's randomness and any adversary randomness.

## Task

Prove that this single algorithm simultaneously satisfies the following expected-regret upper bounds, uniformly over the allowed adversaries:

1. For every ell in mathcal L,
   \[
   \operatorname{Reg}_\ell(n)=\widetilde O(d^{5/4}\sqrt n).
   \]
2. For every beta>0 and every ell in mathcal S_beta,
   \[
   \operatorname{Reg}_\ell(n)=O(\beta\log n+\beta\sqrt d\,\log d).
   \]

The implied constants are universal. The notation tilde O may hide logarithmic factors in d and n. Both claims concern each fixed loss in expectation, with the same algorithm and parameter choice.
