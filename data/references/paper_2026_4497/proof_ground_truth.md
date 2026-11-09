# Reference Proof

## Proof Structure

1. Fix a supported state and any admissible pair of coarsenings of the two separate proxies.
2. Derive the action and proxy conditional-matrix factorizations through the latent variable.
3. Use square invertibility and marginalization to eliminate the latent matrices.
4. Derive the interventional adjustment identity from consistency, positivity, and latent exchangeability, and identify the maximizing actions.

## Complete Proof

Fix any s in the support of S_t and any admissible pair Z'_t=phi_Z(S_{t-1}) and W'_{t-1}=phi_W(W_{t-1}) for this s. Write U=U_{t-1}, A=A_t, S=S_t, Z'=Z'_t, and W'=W'_{t-1}. Throughout this proof the chosen maps are held fixed. In particular, P_{W'} is the unconditional marginal distribution of the chosen coarsening, not its conditional distribution given S=s.

Use column probability vectors and define
\[
B_s[a,u]=P(A=a\mid U=u,S=s),\qquad
R_s[u,j]=P(U=u\mid Z'=j,S=s),
\]
\[
C[i,u]=P(W'=i\mid U=u).
\]
Their dimensions are respectively |mathcal A| by m, m by m, and m by m. Each latent category has positive marginal probability, and positivity gives P(U=u,S=s)>0. Admissibility gives P(Z'=j,S=s)>0 for every j. Thus all these conditional probabilities are defined.

### 1. Action factorization

The assumption S_{t-1} independent of A conditional on (S,U) is preserved when S_{t-1} is replaced by its deterministic function Z'. Thus A is independent of Z' conditional on (S,U). For every a and j, conditioning on U gives
\[
\begin{aligned}
P(A=a\mid Z'=j,S=s)
&=\sum_u P(A=a\mid U=u,Z'=j,S=s)P(U=u\mid Z'=j,S=s)\\
&=\sum_u B_s[a,u]R_s[u,j].
\end{aligned}
\]
Terms whose latent conditional weight is zero contribute zero and need no conditional law on a null event. Consequently,
\[
P_{A\mid Z',s}=B_sR_s.
\]

### 2. Proxy factorization

The assumption (S_{t-1},S) independent of W_{t-1} conditional on U implies that (Z',S) is independent of W' conditional on U: applying deterministic functions separately to the variables on the two sides preserves their conditional product law. Therefore,
\[
\begin{aligned}
P(W'=i\mid Z'=j,S=s)
&=\sum_u P(W'=i\mid U=u,Z'=j,S=s)P(U=u\mid Z'=j,S=s)\\
&=\sum_u C[i,u]R_s[u,j],
\end{aligned}
\]
again ignoring zero-weight terms. Hence
\[
P_{W'\mid Z',s}=CR_s.
\]
This uses the fact that Z' is a coarsening of S_{t-1}, not a coarsening of a pair containing W_{t-1}.

### 3. Elimination and marginalization

By hypothesis CR_s is an invertible m by m matrix. Both factors are square, and
\[
0\ne\det(CR_s)=\det(C)\det(R_s),
\]
so both are invertible. The law of total probability also gives, coordinate by coordinate,
\[
P(W'=i)=\sum_u P(W'=i\mid U=u)P(U=u),
\qquad P_{W'}=CP_U.
\]
It follows that
\[
\begin{aligned}
P_{A\mid Z',s}(P_{W'\mid Z',s})^{-1}P_{W'}
&=B_sR_s(CR_s)^{-1}CP_U\\
&=B_sR_sR_s^{-1}C^{-1}CP_U\\
&=B_sP_U.
\end{aligned}
\]

### 4. Causal adjustment and policy identification

For each latent category u, positivity ensures P(S=s\mid U=u)>0. Latent exchangeability and consistency therefore imply
\[
\begin{aligned}
P(A_t^{(s)}=a\mid U=u)
&=P(A_t^{(s)}=a\mid U=u,S=s)\\
&=P(A=a\mid U=u,S=s)\\
&=B_s[a,u].
\end{aligned}
\]
Marginalizing over U yields
\[
P(A_t^{(s)})=B_sP_U
=P_{A\mid Z',s}(P_{W'\mid Z',s})^{-1}P_{W'}.
\]
The argument applies to every supported s and every admissible pair chosen for that s. It does not require a single pair to work at all states. All quantities in the final expression are determined by the observed joint distribution of (S_{t-1},S_t,W_{t-1},A_t). Since the action space is finite and nonempty, the resulting probability vector has a nonempty set of maximizing actions. This set, and therefore a policy obtained by any fixed tie-breaking rule, is identified.

All theorem-critical obligations have been derived directly. The argument also covers m=1 and allows zero individual conditional-probability entries wherever the conditioning event itself has positive probability. No external identification result is invoked.
