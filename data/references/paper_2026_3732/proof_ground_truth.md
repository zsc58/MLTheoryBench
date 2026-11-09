# Reference Proof

## Obligations and proof

The source contract is a deterministic mean recursion with a finite, nonempty MDP, a full-support probability distribution $d$, full-column-rank features, and the stated strict step-size range. No existence of a projected Bellman fixed point is assumed in the spectral endpoint cases.

Put $C=I-\alpha G$. Positivity of $D$ and full column rank give $G\succ0$. Its eigenvalues show that the step-size range implies $\|C\|_2<1$. Thus $I-C^m$ is invertible for each $m\ge1$.

First close the two elementary switching obligations. For parameters $u,v$, at a state let $a_j=Q_u(s,j)$ and $b_j=Q_v(s,j)$. If $j_a$ maximizes $a_j$ and $j_b$ maximizes $b_j$, then
\[
a_{j_b}-b_{j_b}\le \max_j a_j-\max_j b_j\le a_{j_a}-b_{j_a}.
\]
Consequently the difference of the maxima is a convex combination of action differences. Choosing those weights state by state gives a stochastic selector $\mu_{u,v}$ with $V_u-V_v=\Pi^{\mu_{u,v}}\Phi(u-v)$. Its matrix lies in the convex hull of deterministic-selector matrices: the coefficient of a deterministic policy $\pi$ can be taken as the product, over states $s$, of its statewise selection probabilities.

For completeness, the cited JSR-norm construction also has an elementary proof here. If a finite family $\mathcal H$ has $r=\rho(\mathcal H)<1$, choose $r<q<\beta<1$. Submultiplicativity of the maximal length-$j$ product norm and the JSR limit give a constant $K$ such that every length-$j$ product has norm at most $Kq^j$. With the empty product equal to $I$, define
\[
W(x)=\sum_{j\ge0}\beta^{-2j}\max_{H_1,\ldots,H_j\in\mathcal H}\|H_j\cdots H_1x\|_2^2,
\qquad p(x)=\sqrt{W(x)}.
\]
The geometric majorant makes $W$ finite and gives $\|x\|_2^2\le W(x)\le K'\|x\|_2^2$. Each maximal-product expression is a seminorm; the triangle inequality in the weighted sequence space shows that $p$ is a norm. Shifting a word by a first matrix $H$ yields $W(Hx)\le\beta^2(W(x)-\|x\|_2^2)\le\beta^2W(x)$. Norm convexity extends $p(Hx)\le\beta p(x)$ to $H\in\operatorname{co}(\mathcal H)$. The construction applies for every $\beta\in(\rho(\mathcal H),1)$, including when the JSR is zero.

To establish the fixed point rather than presuppose it, define the boundary-to-boundary map $T_m$ by performing $m$ frozen-target updates starting at and targeting $u$. If $L(u)=G^{-1}\Phi^\top D(R+\gamma PV_u)$, summing the geometric matrix series gives
\[
T_m(u)=C^m u+(I-C^m)L(u).
\]
The statewise interpolation, applied to two boundary inputs, gives $T_m(u)-T_m(v)=A_{\mu_{u,v},m}(u-v)$. Because the period mode depends affinely on the selector, $A_{\mu_{u,v},m}\in\operatorname{co}(\mathcal A_m)$. If $\rho(\mathcal A_m)<1$, the norm construction makes $T_m$ a strict contraction on $\mathbb R^p$. Iterating it gives a Cauchy sequence: successive differences are bounded by a geometric sequence. Its limit is a fixed point, and contraction makes that point unique. Since $I-C^m$ is invertible,
\[
T_m(u)=u\quad\Longleftrightarrow\quad L(u)=u,
\]
so this fixed point is precisely the unique solution $\theta^*$ of the projected Bellman equation.

Subtracting its projected equation from one frozen-target update, with $e=\theta-\theta^*$ and frozen-target error $\bar e$, gives
\[
e^+=Ce+\alpha\gamma\Phi^\top DP(V_{\bar\theta}-V_{\theta^*}).
\]
The selector $\mu_{\bar\theta,\theta^*}$ is fixed over the block because the target is fixed. Iterating from $\bar e=e_{km}$ gives the exact boundary recursion
\[
e_{(k+1)m}=A_{\mu_{km},m}e_{km},\qquad A_{\mu_{km},m}\in\operatorname{co}(\mathcal A_m).
\]
The same norm therefore bounds boundary errors by $\beta^k p(e_0)$. Each of the finitely many within-block update matrices, over all stochastic selectors, is uniformly bounded for fixed $m$. Thus all online errors converge, with an upper exponential factor $\beta^{1/m}$ per online step. Letting $\beta$ decrease to $\rho(\mathcal A_m)$ establishes the asserted JSR upper rate; it does not assert that each realized trajectory attains that rate. Greedy tie breaking does not affect the frozen greedy value vector.

For endpoints, the finite-sum identity $\sum_{i=0}^{m-1}C^i\alpha G=I-C^m$ yields, for each deterministic policy,
\[
A_{\pi,m}=A_\pi^{\rm PQVI}+C^m(I-A_\pi^{\rm PQVI}).
\]
At $m=1$ this is $I-\alpha G+\alpha\gamma B_\pi$, the period-one family. As $m\to\infty$, $C^m\to0$ uniformly across the finite policy set, so the corresponding tuples of matrices converge entrywise to the PQVI tuple. The standard independent fact that JSR is continuous for finite, correspondingly indexed tuples of fixed-size matrices then gives $\rho(\mathcal A_m)\to\rho_{\rm P}$. Its hypotheses hold because the MDP has finitely many deterministic policies and every matrix has size $p\times p$. Strict inequalities give the asserted sufficiently-large-period signs, and the period-one identity gives the other endpoint; combining them gives all four cases without asserting anything about intermediate periods.

Finally, if a finite family has JSR $r>1$, choose $1<\lambda<r$. By the JSR definition, for every sufficiently large length $k$ the maximum norm of its length-$k$ products exceeds $\lambda^k$. This rules out uniform convergence of arbitrary products of that matrix family. The arbitrary deterministic-policy words used in this conclusion are an abstract worst-case switching family; they need not be generated by greedy choices along any actual hard-target trajectory. There is therefore no claimed divergence of realized iterates in an unstable endpoint case.

All theorem-critical obligations are closed: selector interpolation and convex-hull membership, the finite-family contraction norm, existence and uniqueness under the stable-family condition, the boundary and within-period bounds, the endpoint identities and limit, and the precise worst-case interpretation of JSR above one.
