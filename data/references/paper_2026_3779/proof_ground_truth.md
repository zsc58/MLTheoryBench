# Reference Proof

## Source Contract and Proof Obligations

The source uses real-valued outcomes, a convex standard-Borel class of probability measures with its weak-convergence Borel structure, a measurable functional, and a conditional outcome law belonging to that class. Its identification condition consists of the two fixed-distribution epsilon-sided endpoint inequalities, not an exact-zero-set requirement. The prediction-error/expectation-form restriction is part of the selected source contract and remains in the task. The explicit signed-integral conditions merely exclude undefined expectations; absolute integrability of the outcome or forecast endpoints is not additionally assumed.

The theorem-critical obligations are:

1. Obtain the conditional forecast kernel and justify integration of jointly measurable functions against conditional kernels.
2. Construct the conditional forecast barycenter and identify it with the conditional outcome law on one probability-one event under distribution calibration.
3. Establish concentration of the conditional forecast kernel on its functional level set and apply mixture-level-set closure.
4. Starting from conditional calibration alone, derive both unconditional endpoint inequalities for every positive epsilon.

The standard-Borel disintegration fact below is the standard_independent result indexed by theory_028. The specialized external result indexed by theory_030 is not invoked as proof of obligation 4.

## Step 1: Conditional Kernels and Their Integration Rule

We use the following standard-Borel disintegration theorem: if U and Z are jointly distributed random elements of standard-Borel spaces E and S, respectively, there is a measurable probability kernel K_z on E such that, for all measurable A in E and C in S,
\[
\mathbb P(U\in A,Z\in C)=\int_C K_z(A)\,\mathbb P_Z(dz).
\]
In particular, \(K_Z(A)\) is a version of \(\mathbb E[\mathbf1_{\{U\in A\}}\mid Z]\).

Here \(E=\mathcal P\) is standard Borel by assumption, and \(S=\mathscr I\) is standard Borel because its endpoint representation is a Borel subset of \(\mathbb R^2\). Both Q and X are measurable. Thus the theorem gives a conditional forecast kernel \(\Lambda_x\) for Q given X. Write \(\nu=\mathbb P_X\).

We will use the conditional-kernel integration rule. For a nonnegative jointly measurable function h on S times E,
\[
\mathbb E[h(Z,U)]=\int_S\int_E h(z,u)\,K_z(du)\,\mathbb P_Z(dz),
\]
and
\[
\mathbb E[h(Z,U)\mid Z]=\int_E h(Z,u)\,K_Z(du)\quad\text{almost surely}.
\]
To justify the rule, first take h to be the indicator of a measurable rectangle. The identities are precisely the defining identity of the kernel, with testing against measurable events determined by Z for the conditional version. Finite sums, the monotone-class extension from rectangles, and increasing nonnegative simple-function approximations give the stated identities. Applying the nonnegative rule separately to positive and negative parts gives the signed rule whenever at least one unconditional part has finite integral. In that case its conditional integral is finite almost surely, so the subtraction is defined almost surely, and integration gives the corresponding extended-real tower identity.

This rule applies both to \(\Lambda_x\) and to the assumed conditional outcome kernel \(G_x\). The endpoint maps, V, and the probability-measure evaluation maps are measurable under the public measurable structures.

## Step 2: The Conditional Barycenter Under Distribution Calibration

Define
\[
M_x(B)=\int_{\mathcal P}R(B)\,\Lambda_x(dR),\qquad B\in\mathcal B(\mathbb R).
\]
For each x this is a probability measure: normalization is immediate, and countable additivity follows by applying monotone convergence to sums over disjoint Borel sets. For each fixed B it is measurable in x, since \(R\mapsto R(B)\) is measurable. The conditional-kernel rule gives
\[
M_X(B)=\mathbb E[Q(B)\mid X]\quad\text{almost surely}.
\]

Assume distribution calibration. For each Borel B,
\[
M_X(B)=G_X(B)\quad\text{almost surely}.
\]
To conclude equality of the random probability measures, use the countable collection \(B=(-\infty,q]\), \(q\in\mathbb Q\), and intersect the associated probability-one events. On the resulting event the two distribution functions agree at every rational q. Continuity from above of probability measures extends that equality to every real threshold; distribution functions determine Borel probability measures. Consequently,
\[
M_X=G_X\quad\text{almost surely}.
\]
This argument does not intersect an uncountable collection of exceptional sets.

## Step 3: Level-Set Concentration and Conditional Calibration

The set \(\{(x,R):T(R)=x\}\) is measurable: T is measurable and the diagonal of the standard-Borel interval space is measurable. Apply the nonnegative conditional-kernel integration rule to its complement. Since \(X=T(Q)\),
\[
\int_{\mathscr I}\Lambda_x(\{R:T(R)\ne x\})\,\nu(dx)
=\mathbb P(T(Q)\ne X)=0.
\]
The integrand is nonnegative, so
\[
\Lambda_x(\{R:T(R)=x\})=1
\quad\text{for }\nu\text{-almost every }x.
\]
Mixture-level-set closure therefore gives \(M_x\in\mathcal P\) and \(T(M_x)=x\) for \(\nu\)-almost every x. Combining this with Step 2 and the assumed almost-sure membership \(G_X\in\mathcal P\), we obtain
\[
T(G_X)=T(M_X)=X=T(Q)\quad\text{almost surely}.
\]
Thus distribution calibration implies conditional T-calibration.

## Step 4: Conditional Calibration Implies Both Unconditional Inequalities

For this step assume conditional T-calibration; distribution calibration is not needed. Fix an arbitrary \(\varepsilon>0\). For \(\nu\)-almost every \(x=[a,b]\), we have \(G_x\in\mathcal P\) and
\[
T(G_x)=x=[a,b].
\]
Apply the fixed-distribution identification assumptions to the particular probability measure \(R=G_x\). They yield
\[
\int V(a+\varepsilon,y)\,G_x(dy)\ge0,
\qquad
\int V(b-\varepsilon,y)\,G_x(dy)\le0.
\]
These are applications of the defining assumptions, not assertions that V has zero conditional expectation at an endpoint.

The functions \((x,y)\mapsto V(a+\varepsilon,y)\) and \((x,y)\mapsto V(b-\varepsilon,y)\), where x has endpoints a and b, are jointly measurable. Their evaluations at \((X,Y)\) are exactly \(V(T^-(Q)+\varepsilon,Y)\) and \(V(T^+(Q)-\varepsilon,Y)\). The public signed-expectation assumptions ensure that each has at least one integrable part. The conditional-kernel rule therefore identifies the two integrals above with
\[
\mathbb E[V(T^-(Q)+\varepsilon,Y)\mid X]\ge0,
\qquad
\mathbb E[V(T^+(Q)-\varepsilon,Y)\mid X]\le0
\quad\text{almost surely}.
\]
Taking expectations using the signed version of the rule gives
\[
\mathbb E[V(T^-(Q)+\varepsilon,Y)]\ge0,
\qquad
\mathbb E[V(T^+(Q)-\varepsilon,Y)]\le0.
\]
There is no undefined subtraction: the assumed finite positive or negative part remains finite after conditioning and integration. For example, if a nonnegative conditional integral has a globally finite positive part, its negative part is bounded in integral by that positive part; otherwise its already finite negative part directly justifies the extended-real subtraction. The nonpositive case is analogous.

Since epsilon was arbitrary, both inequalities hold for every positive epsilon. No limit as epsilon decreases to zero, endpoint zero identity, or strict separation of the two endpoints is required. Singleton intervals are included.

Combining Steps 3 and 4 proves all three claimed implications.

## Closure Audit

All four obligations are closed. Standard-Borel disintegration is stated with its hypotheses verified; the kernel integration, common-null-set, concentration, and identification-to-unconditional arguments are supplied explicitly. The source citation at L001032-L001034 is retained in the material index but is not used as a substitute for the last derivation. No private proof obligation remains unresolved.
