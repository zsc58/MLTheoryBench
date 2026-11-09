# Problem

## Setup

Let \(A\) and \(B\) be finite nonempty action sets, with cardinalities also denoted by \(A\) and \(B\). Write \(\Delta_A\) and \(\Delta_B\) for their probability simplices. A two-player zero-sum matrix game has a loss matrix \(L:A\times B\to[0,1]\). For mixed policies \(\mu\in\Delta_A\) and \(\nu\in\Delta_B\), define
\[
L(\mu,\nu)=\sum_{a\in A,b\in B}\mu(a)\nu(b)L(a,b),
\qquad
\operatorname{Gap}(\mu,\nu)
=-\min_{\mu'\in\Delta_A}L(\mu',\nu)
+\max_{\nu'\in\Delta_B}L(\mu,\nu').
\]

For each action pair \((a,b)\), the game also specifies a fixed probability law \(\rho_{ab}\) on \([0,1]\) with mean \(L(a,b)\). A learning rule consists of randomized decision maps fixed before the matrix and these laws are selected. The maps receive neither the matrix nor the laws nor a parameter indexing them as inputs. They may depend on the action sets, time, and the specified norm exponent. Initial internal randomness \(U\) has a law independent of the game and is separate from the random draws used to sample game actions.

At round \(t\), the policies \((\mu_t,\nu_t)\) are predictable from the permitted past information. Conditional on the full past and these policies, the game actions are sampled independently with laws \(\mu_t\) and \(\nu_t\). A single loss \(X_t\in[0,1]\) is observed, with
\[
\mathcal L(X_t\mid U,a_1,b_1,X_1,\ldots,a_{t-1},b_{t-1},X_{t-1},a_t,b_t)
=\rho_{a_tb_t}.
\]

An uncoupled implementation uses two decision maps without communication: each player uses initial internal randomness, its own past actions, and the observed losses, rather than observing the opponent's sampled actions. Shared initial randomness is allowed. The full history containing both actions is an analysis filtration, not an additional observation available to either player.

For the lower-bound experiment, allow both policy maps access to the entire reduced history
\[
\widetilde{\mathcal H}_t=(U,a_1,X_1,\ldots,a_t,X_t),
\]
but do not reveal any sampled second-player action \(b_s\) to either map. Both policies at time \(t\) must be measurable functions of \(\widetilde{\mathcal H}_{t-1}\). The same decision maps and the same law of \(U\) must be used for every game being compared.

For a random gap and \(p>0\), write
\[
\|\operatorname{Gap}(\mu_t,\nu_t)\|_p
=\bigl(\mathbb E[\operatorname{Gap}(\mu_t,\nu_t)^p]\bigr)^{1/p},
\]
where the expectation includes the rule's randomness and the game observations. A subscript \(\varepsilon,p\) denotes this quantity in the game indexed by \(\varepsilon\).

Consider the two-action Bernoulli game family
\[
G_\varepsilon=
\begin{pmatrix}
2/3-\varepsilon&1/3+\varepsilon\\
1/3&2/3
\end{pmatrix},
\qquad \varepsilon\in[-1/12,1/12],
\]
where each entry is the parameter of the corresponding fixed Bernoulli observation law.

## Task

Prove the following integrated minimax characterization for every \(p\in(0,2]\), with \(\alpha=1/(2+p)\). All logarithms are natural.

1. For every single learning rule satisfying the lower-bound experiment's reduced-history restriction,
\[
\limsup_{t\to\infty}t^\alpha
\sup_{\varepsilon\in[-1/12,1/12]}
\|\operatorname{Gap}(\mu_t,\nu_t)\|_{\varepsilon,p}
\geq\frac{4^{-1/p}}{118}.
\]
This assertion allows both decision maps access to the entire reduced history, whether or not they admit an uncoupled implementation.

2. For every pair of finite nonempty action sets, there exists one uncoupled learning rule, depending on \(p\) and the action sets but not on the game, that works for every loss matrix and every collection of fixed observation laws described above. The rule can also be chosen to satisfy the reduced-history restriction in part 1. For every such game and every integer \(t\geq1\), it satisfies
\[
\|\operatorname{Gap}(\mu_t,\nu_t)\|_p
\leq17\sqrt{A+B}\,2^{1/p}t^{-\alpha}
\log\!\left(\frac{4(A+B)t^2}{p}\right).
\]

Conclude that, in this common reduced-history experiment, the polynomial last-iterate rate \(t^{-1/(2+p)}\) is minimax-optimal up to logarithmic factors.
