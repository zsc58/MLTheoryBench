# Problem

## Setup

Consider one time step with finite categorical variables: the observed states S_{t-1} and S_t, the latent delayed context U_{t-1}, the observed noisy proxy W_{t-1}, and the expert action A_t. Let \(\mathcal S=\operatorname{supp}(S_t)\) and let \(\mathcal A\) be the finite nonempty action space. All state and latent values quantified below belong to their supports. Suppose \(U_{t-1}\) has exactly \(m\geq1\) support values.

The expert mechanism is: conditional on \((S_t,U_{t-1})\), the action is sampled according to a law \(\pi_E(\cdot\mid S_t,U_{t-1})\) independently of the proxy variables \((S_{t-1},W_{t-1})\). Let
\[
Z_t=S_{t-1}.
\]
Assume the proxy independences
\[
S_{t-1}\perp A_t\mid(S_t,U_{t-1}),
\qquad
(S_{t-1},S_t)\perp W_{t-1}\mid U_{t-1}.
\]

For each \(s\in\mathcal S\), let \(A_t^{(s)}\) be the action, taking values in \(\mathcal A\), under the intervention \(\mathrm{do}(S_t=s)\). Assume consistency \(A_t=A_t^{(S_t)}\) almost surely, positivity
\[
P(S_t=s\mid U_{t-1}=u)>0
\]
for every \(s\in\mathcal S\) and \(u\in\operatorname{supp}(U_{t-1})\), and latent exchangeability
\[
A_t^{(s)}\perp S_t\mid U_{t-1}
\qquad(s\in\mathcal S).
\]

For each \(s\in\mathcal S\), suppose there exists a pair of deterministic categorical coarsenings
\[
Z'_t=\phi_Z(Z_t),\qquad W'_{t-1}=\phi_W(W_{t-1}),
\]
each with category set \(\{1,\ldots,m\}\), such that \(P(Z'_t=j,S_t=s)>0\) for every \(j\in\{1,\ldots,m\}\) and the \(m\times m\) matrix
\[
P_{W'\mid Z',s}[i,j]
:=P(W'_{t-1}=i\mid Z'_t=j,S_t=s)
\]
is invertible. Call such a pair admissible at s. The coarsening maps may be chosen separately for different s.

For a fixed s and an admissible pair, define the \(|\mathcal A|\times m\) matrix
\[
P_{A\mid Z',s}[a,j]
:=P(A_t=a\mid Z'_t=j,S_t=s).
\]
Let \(P_{W'}\) and \(P_U\) be the column vectors of the marginal probabilities of \(W'_{t-1}\) and \(U_{t-1}\), respectively. In \(P_{W'}\), the chosen map \(\phi_W\) is held fixed and the marginal is not conditioned on \(S_t=s\). Write \(P(A_t^{(s)})\) for the column vector with entries \(P(A_t^{(s)}=a)\), indexed by \(a\in\mathcal A\).

## Task

Prove that, for every \(s\in\mathcal S\) and every pair of coarsenings admissible at s,
\[
P(A_t^{(s)})
=P_{A\mid Z',s}\bigl(P_{W'\mid Z',s}\bigr)^{-1}P_{W'}.
\]
Consequently, the causal-optimal imitation policy
\[
\pi_{\mathrm{opt}}(s)\in\arg\max_{a\in\mathcal A}P(A_t^{(s)}=a)
\]
is identified from the observed joint distribution of \((S_{t-1},S_t,W_{t-1},A_t)\), up to ties among maximizing actions.
