# Reference Proof

## Proof Structure

We prove validity conditional on every positive-probability configuration of all labels. The conditional density ratio includes a constant class-prevalence factor, which cancels from normalized permutation weights. A finite assignment representation and a multiplicity-correct weighted-rank argument establish validity of the randomized p-values. Retaining full-label conditioning then justifies the last-all-negative-prefix argument for the nested rule.

## Complete Proof

### 1. Well-definedness and conditional laws

Write a=P(Y=0) and b=Q(Y=0). Since dQ/dP(x,y)=w(x), the generated marginal satisfies Q_X(dx)=w(x)P_X(dx). In particular, w(G_j)>0 almost surely. All weights are finite, and the identity term W(id;z^(k)) is strictly positive almost surely. Therefore the denominator defining r_k is finite and positive, and 0<r_k<=1 almost surely.

If b=0, every H_k has probability zero. All fixed-prefix joint inequalities hold trivially, and the nested error event is contained in {C_1=0}, which also has probability zero. Hence suppose b>0. Absolute continuity implies a>0.

Define P_0=P_{X|Y=0}, Q_0=Q_{X|Y=0}, and c=a/b. For every measurable set D,
\[
Q_0(D)=\frac{Q(X\in D,Y=0)}b
=\frac1b\int_{D\times\{0\}}w(x)\,dP(x,y)
=c\int_Dw(x)\,dP_0(x).
\]
Thus
\[
\frac{dQ_0}{dP_0}=cw,
\qquad \int w\,dP_0=c^{-1}.
\]
The factor c need not equal one.

Let L=(B_1,...,B_n,C_1,...,C_N) be the full label vector. Fix any value ell of L having positive probability and satisfying H_k. Conditioning independent pairs on their individual labels preserves independence: this follows directly by factoring joint probabilities of coordinatewise measurable events together with the label events. Consequently, if m is the number of zero calibration labels in ell, the vector z^(k), with retained calibration indices in increasing order, has conditional law
\[
P_0^{\otimes m}\otimes Q_0^{\otimes k}.
\]
Its density relative to R=P_0^{\otimes(m+k)} is
\[
c^k W(\mathrm{id};x).
\]
Conditioning on labels after k does not change this law, by independence of the generated pairs. The score s_{m,k} remains fixed, and the auxiliary permutations retain their specified uniform laws.

### 2. A finite weighted assignment representation

This construction avoids any requirement that covariates be distinct or that the covariate space support a particular pointwise conditional distribution given an unordered multiset.

Put M=m+k, let F=S_M, and write D=|F|=M!. For x in X^M and tau in F, set x_tau=(x_{tau(1)},...,x_{tau(M)}), and define
\[
S(x)=\sum_{\tau\in F}W(\tau;x).
\]
Because R is invariant under coordinate permutations,
\[
\int W(\tau;x)\,dR(x)=c^{-k}
\]
for every tau. It follows that
\[
d\mu(x)=\frac{c^kS(x)}D\,dR(x)
\]
defines a probability measure. It assigns probability zero to {S=0}.

Draw X* from mu and, given X*=x, draw an indexed assignment T_0 in F with probabilities
\[
\Pr(T_0=\tau\mid X^*=x)=\frac{W(\tau;x)}{S(x)}.
\]
For any bounded measurable f, coordinate-permutation invariance gives
\[
\begin{aligned}
\mathbb E[f(X^*_{T_0})]
&=\frac{c^k}D\sum_{\tau\in F}\int W(\tau;x)f(x_\tau)\,dR(x)\\
&=c^k\int W(\mathrm{id};x)f(x)\,dR(x).
\end{aligned}
\]
Thus X*_{T_0} has exactly the conditional law of z^(k). Assignments are permutations of indexed occurrences, so repeated covariate values cause no difficulty. If several assignments produce the same ordered vector, their probabilities are added automatically.

### 3. The randomized assignment law and weighted ranks

In this representation, generate the auxiliary permutations sigma_1,...,sigma_B independently and uniformly from F, and put T_b=T_0 composed with sigma_b for b>=1. Given X*=x and T_0, the assignments T_1,...,T_B are independent uniform elements of F. Therefore
\[
\Pr(T_0=\tau_0,...,T_B=\tau_B\mid X^*=x)
=\frac{W(\tau_0;x)}{S(x)D^B}.
\]
Moreover, applying sigma_b to the observed vector x_{T_0} yields x_{T_b}, and its joint weight is W(T_b;x). Hence this representation reproduces the public randomized p-value exactly.

Condition on x and the multiset of the B+1 assignments. Let h(tau) be the number of occurrences of tau in that multiset. For any tau with h(tau)>0, the number of ordered lists having T_0=tau and these multiplicities is
\[
\frac{B!}{(h(\tau)-1)!\prod_{\eta\ne\tau}h(\eta)!}.
\]
Combining this count with the preceding joint mass yields
\[
\Pr(T_0=\tau\mid x,h)
=\frac{h(\tau)W(\tau;x)}{A},
\qquad A=\sum_{\eta\in F}h(\eta)W(\eta;x)>0.
\]
This is a law on permutation values with their multiplicities included, not a separate disjoint event for every repeated occurrence.

Set v_tau=s_{m,k}(x_tau). When T_0=tau, the p-value equals
\[
R_\tau=\frac{\sum_{\eta\in F}h(\eta)W(\eta;x)\mathbf1\{v_\eta\ge v_\tau\}}A.
\]
To bound its lower tail, group equal scores and order the groups in decreasing score order. If the normalized masses of the groups are a_1,...,a_J, their upper-tail ranks are the cumulative sums q_j=a_1+...+a_j. The groups with q_j<=t form an initial segment, whose total mass is its final cumulative sum and is at most t. Empty segments and zero-mass groups do not change the conclusion. Therefore
\[
\sum_{\tau\in F}\frac{h(\tau)W(\tau;x)}A\mathbf1\{R_\tau\le t\}\le t.
\]
Averaging over the assignment multiset and the latent vector proves, for every positive-probability label configuration ell satisfying H_k,
\[
\Pr(r_k\le t\mid L=\ell)\le t.
\tag{*}
\]
No continuity, distinctness, or positive inactive-calibration count was used. In particular, m=0 is covered by the same finite product and permutation argument.

### 4. Fixed-prefix and batch certification guarantees

Sum (*) over label configurations satisfying H_k:
\[
\Pr(r_k\le t,H_k)
=\sum_{\ell:H_k}\Pr(L=\ell)\Pr(r_k\le t\mid L=\ell)
\le t\Pr(H_k).
\]
Zero-probability configurations contribute nothing. Dividing by Pr(H_k) proves the conditional formulation whenever that probability is positive.

Since p_N=r_N, the certification rule satisfies
\[
\Pr(\psi=1,H_N)=\Pr(r_N\le\alpha,H_N)
\le\alpha\Pr(H_N).
\]
Also, p_k>=r_k gives both the joint bound
\[
\Pr(p_k\le t,H_k)\le t\Pr(H_k)
\]
and, importantly, the stronger bound conditional on each full label configuration satisfying H_k:
\[
\Pr(p_k\le t\mid L=\ell)\le\Pr(r_k\le t\mid L=\ell)\le t.
\tag{**}
\]
The latter follows from the directly proved (*) and event inclusion, not by conditioning the joint inequality further. It remains true although p_k includes later raw p-values.

### 5. Nested selection

Let K_0 be the length of the initial all-zero generated-label prefix, with K_0=0 when C_1=1. It is determined by L. Write
\[
E=\{\hat K>0,\ C_1=\cdots=C_{\hat K}=0\}.
\]
For any fixed label configuration with K_0>0,
\[
E=\{0<\hat K\le K_0\}=\{p_{K_0}\le\alpha\}.
\]
Indeed, a crossing by K_0 implies p_{K_0}<=alpha by monotonicity; conversely, a crossing at K_0 guarantees that the first crossing exists and is at most K_0. Applying (**) at this now deterministic index gives Pr(E|L)<=alpha. If K_0=0, E is impossible. Averaging yields
\[
\Pr(E)\le\alpha.
\]
The argument includes t and alpha equal to zero or one. All proof obligations for the integrated target are closed.

## Source-Audit Notes

The normalized conditional derivative, multiplicity corrections, and label-conditioning inference are substantive details of the proof and are deliberately kept out of the public problem. The standalone inference from validity conditional only on H_k to validity conditional on all labels is not used. No external specialized theorem is needed.
