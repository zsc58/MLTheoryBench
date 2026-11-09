# Reference Proof

## Proof Structure

1. Derive the protected-group fraction represented by each column of the partition matrix, together with its diagonally scaled form.
2. Use the first identity to prove the equivalence for proportional-representation fairness in both directions.
3. Use the scaled identity and positivity of the scaling factors to prove the equivalence for tau-ratio fairness in both directions.

## Complete Proof

Let $j\in[n]$ and let $k(j)$ be the unique index with $j\in C_{k(j)}$. By the definition of $Z$, for every $i$ in the same cluster as $j$, $Z_{ij}=1/|C_{k(j)}|$, and otherwise $Z_{ij}=0$. Therefore
\[
\sum_{i=1}^n Z_{ij}e_i^g
 =\frac{|C_{k(j)}\cap P_g|}{|C_{k(j)}|}.
\]
Also $Z_{jj}=1/|C_{k(j)}|$, and $|P_g|>0$, so
\[
\frac{\sum_i Z_{ij}e_i^g}{Z_{jj}|P_g|}
 =\frac{|C_{k(j)}\cap P_g|}{|P_g|}.
\]

For proportional representation, suppose first that every cluster satisfies
$\beta_g\le |C_k\cap P_g|/|C_k|\le\alpha_g$ for every $g$. Applying the first identity to the cluster containing each $j$ gives
$\beta_g\le\sum_i Z_{ij}e_i^g\le\alpha_g$ for every $g,j$. Conversely, assume these column inequalities hold for every $g,j$. For any cluster $C_k$, choose (using nonemptiness) some $j\in C_k$; the first identity then yields
$\beta_g\le |C_k\cap P_g|/|C_k|\le\alpha_g$. Thus the two proportional-representation conditions are equivalent.

For tau-ratio fairness, suppose first that
$|C_k\cap P_g|/|P_g|\ge\tau_g$ for every $g,k$. The scaled identity, together with $Z_{jj}|P_g|>0$, gives
\[
\sum_i Z_{ij}e_i^g\ge\tau_g|P_g|Z_{jj}
\]
for every $g,j$. Conversely, assume these inequalities for every $g,j$. Divide by the positive quantity $Z_{jj}|P_g|$ and use the scaled identity to obtain the tau-ratio lower bound for the cluster containing each $j$; choosing a member of each nonempty cluster proves the bound for every $g,k$. Hence the tau-ratio condition and its stated linear inequalities are equivalent. Both systems are linear inequalities in the entries of $Z$.
