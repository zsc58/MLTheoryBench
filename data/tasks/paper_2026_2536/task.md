# Problem

## Setup

Let \(X_t=(X_t^1,\ldots,X_t^d)\) be a discrete-time Markov system on \(\prod_{i=1}^d\mathcal X_i\), where each \(\mathcal X_i\) is a nonempty finite set, with transition kernel \(p(x_{t+1}\mid x_t)\) on this state space. Let the source-component index set be \(S=\{1,\ldots,d\}\) and the target-component index set be \(T=S\). Impose the product-uniform maximum-entropy intervention
\[
q^\star(x_t)=\prod_{i\in S}\frac{1}{|\mathcal X_i|},
\qquad
q(x_t,x_{t+1})=q^\star(x_t)p(x_{t+1}\mid x_t).
\]
All information quantities below are computed under \(q\). For \(A\subseteq S\) and \(B\subseteq T\), define
\[
\operatorname{EI}(A\to B):=I_q(X_t^A;X_{t+1}^B).
\]
If \(P=\{M_1,\ldots,M_m\}\) is a partition of \(A\), define partition synergy by
\[
\operatorname{Syn}_{P}(A\to B):=\operatorname{EI}(A\to B)-\sum_{i=1}^m\operatorname{EI}(M_i\to B).
\]
Let \(P_{\mathrm{fin}}(A)=\{\{i\}:i\in A\}\) denote the singleton partition. If \(M_\star\in P\) and \(R=\{R_1,\ldots,R_k\}\) is a partition of \(M_\star\), write \(P'=(P\setminus\{M_\star\})\cup R\).

## Task

Prove the following integrated theorem. For every \(A\subseteq S\), \(B\subseteq T\), and partition \(P\) of \(A\),
\[
0\le \operatorname{Syn}_{P}(A\to B)\le \operatorname{EI}(A\to B).
\]
Moreover, every one-block refinement as above satisfies
\[
\operatorname{Syn}_{P'}(A\to B)=\operatorname{Syn}_{P}(A\to B)+\operatorname{Syn}_{R}(M_\star\to B),
\]
and consequently
\[
\operatorname{Syn}_{P}(A\to B)\le \operatorname{Syn}_{P_{\mathrm{fin}}(A)}(A\to B).
\]
