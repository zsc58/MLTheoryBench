# Reference Proof

## Contract and Proof Status

The activation and noise strength are fixed as p varies. The proportional limit is taken with p fixed, and the width limit is taken afterward. The public AMP convention permits a finite iteration count depending on the nonzero initialization strength, then removes that strength. It does not remove the seed before permitting amplification.

The analytic gain calculation below is reconstructed and locally repaired. Section 9 now derives the threshold and specialization events for the precise public overlap recursion; it does not assume that a cited attainability result for some AMP scheme applies to that recursion.

One private source-correspondence obligation remains: the supplied paper does not provide the precise finite-dimensional AMP construction or a proof that it realizes the stipulated fixed-iteration profile with the stated initialization. The public task specifies that profile explicitly, so its deterministic threshold claim is proved below. This does not constitute an independent proof of the specialized finite-dimensional state-evolution theorem.

## 1. Limiting Experiment and Normalizations

At finite d, conditional on U*, the vector U*X is Gaussian with covariance U*U*^T; it is not exactly a vector of independent standard Gaussians. For fixed p, U*U*^T converges in probability to I_p. The limiting channel used below is therefore

Y=p^{-1/2} sum_{k=1}^p phi(Z_k)+sqrt(delta) xi,

where Z_1,...,Z_p,xi are independent standard Gaussians. Passing from the finite-dimensional algorithm to this limiting channel belongs to the external AMP realization obligation, not to an assertion of exact finite-d independence.

Let m=E[phi(G)], A=phi(G)-m, H=G^2-1, b=beta_*, and s^2=E[A^2]. All mixed moments used below are finite by polynomial boundedness. Also s^2>0: if phi(G) were almost surely constant, every mu_j would vanish.

Centering labels subtracts the known constant sqrt(p)m. It does not alter the observation information or the thresholds. Centering the activation does not alter the NSE: E[H]=0 and the binomial identity gives E[H(phi(G)-m)^j]=0 for j<b and E[H(phi(G)-m)^b]=mu_b. Unit variance is unnecessary; retain s^2 explicitly. Label translation also leaves the public output potential unchanged after changing the integration variable.

## 2. Conditional Symmetry

In the limiting experiment, changing the sign of any Z_k leaves the likelihood unchanged. Thus E[Z_k|Y]=0 and E[Z_k Z_h|Y]=0 for k!=h. Permuting coordinates leaves the joint law unchanged, so all diagonal conditional second moments agree. Therefore

G_p(Y):=E[ZZ^T-I_p|Y]=a_p(Y) I_p,

a_p(Y)=E[Z_1^2-1|Y].

Define K_p=E[a_p(Y)^2]. Conditional Jensen gives K_p<=E[(Z_1^2-1)^2]=2.

K_p is strictly positive. Indeed, for the centered label, expansion of Y^b and independence show

E[(Z_1^2-1)Y^b]=p^{-b/2}mu_b !=0.

Every term with fewer than b powers of the first activation vanishes. Hence a_p cannot vanish almost surely.

## 3. External Source Statements and Their Role

The source invokes the following nonstandard results.

1. Matched Gaussian multi-index AMP has, for each fixed p, initialization strength, and iteration, limiting Gram and planted cross-overlap equal to q^t, with the Gaussian-prior update stated in the public limiting-performance convention.
2. If E[Z|Y]=0, its weak-recovery threshold is

alpha_WR^Alg = [sup_{M>=0, ||M||_F=1} ||E[G_p(Y) M G_p(Y)]||_F]^{-1}.

3. Above this threshold an appropriate AMP scheme recovers the easy subspace. When G_p(Y)=a_p(Y)I_p and a_p is not almost surely zero, that subspace is the full planted span.

The supplied paper states and cites these assertions, but does not prove them. No assertion here is closed merely by its citation. Neither the Bayes-optimal global-potential theorem nor the non-rigorous generic-activation committee ansatz is needed.

For source context, assertions 2 and 3 would conditionally give the threshold 1/K_p and full-subspace recovery. That conditional argument is not the proof of the specific public recursion. Section 9 supplies the missing profile argument directly and therefore does not need assertions 2 or 3. Assertion 1 remains an unresolved private obligation concerning finite-dimensional realization of the public limiting convention.

## 4. Exact Signed-Density Expansion

Let e=p^{-1/2}, let A_1,...,A_p be independent copies of the centered activation, and put S_p=e sum_{k=2}^p A_k. Let rho_delta be the centered Gaussian density of variance delta. The centered label density and signed density are

D_p(y)=E[rho_delta(y-S_p-eA_1)],

n_p(y)=E[(Z_1^2-1)rho_delta(y-S_p-eA_1)].

Then a_p(y)=n_p(y)/D_p(y) and K_p=integral n_p(y)^2/D_p(y) dy.

Taylor-expand only the small first-coordinate shift. The constant term and orders 1,...,b-1 vanish after multiplication by Z_1^2-1 and expectation. Therefore

n_p(y)=L_p(y)+r_p(y),

L_p(y)=(-e)^b mu_b E[rho_delta^{(b)}(y-S_p)]/b!.

This is an exact expansion with remainder. It is not an assertion that S_p is Gaussian at fixed p.

## 5. Repaired Single-Index Remainder Estimate

First consider D_e(x)=E[rho_delta(x-eA)] and n_e(x)=E[H rho_delta(x-eA)]. Set

r_e(x)=n_e(x)-(-e)^b mu_b rho_delta^{(b)}(x)/b!.

Choose M with P(|A|<=M)>0. For eM<=sqrt(delta), a bounded-shift comparison gives

D_e(x)>=c rho_delta(x)exp(-|x|/sqrt(delta)),

where c>0 is independent of sufficiently small e.

Split at T_e={|A|>e^{-1/2}}. On its complement, |eA|<=sqrt(e). Taylor's formula with the Lagrange remainder, the Gaussian derivative identity, and the denominator bound give

integral r_in(x)^2/D_e(x) dx <= C e^{2b+2} E[H^2 |A|^{2b+2}].

Here Gaussian derivatives at shifts of magnitude at most sqrt(e) are bounded by a Gaussian times a fixed polynomial; after division by the displayed denominator lower bound the resulting function of x is integrable uniformly for small e.

For the signed tail density, weighted Cauchy-Schwarz gives

integral (E[H rho_delta(x-eA)1_{T_e}])^2/D_e(x) dx <= E[H^2 1_{T_e}].

The right side is smaller than any prescribed power of e by Markov and Cauchy-Schwarz, since A and H have all mixed moments. Each Taylor coefficient removed by truncation has the same arbitrarily small order. The weighted norms of the finitely many Gaussian derivatives are uniformly bounded by the denominator comparison. Consequently

integral r_e(x)^2/D_e(x) dx=o(e^{2b}).

This signed-density bound replaces the invalid denominator cancellation in the source's tail calculation.

## 6. Transfer of the Remainder Through the Nuisance Mixture

For each value s of S_p, the remainder is r_e(y-s) and its corresponding single-index density is D_e(y-s). Weighted mixture Cauchy-Schwarz yields

[ E_{S_p} r_e(y-S_p) ]^2 / E_{S_p} D_e(y-S_p)
<= E_{S_p}[r_e(y-S_p)^2/D_e(y-S_p)].

Integration and translation invariance therefore give

integral r_p(y)^2/D_p(y) dy <= integral r_e(x)^2/D_e(x) dx=o(e^{2b}).

This establishes the required remainder order before comparing squared norms.

## 7. Gaussian-Smoothed CLT and Leading Integral

Define

J_p=integral [E rho_delta^{(b)}(y-S_p)]^2/D_p(y) dy.

The CLT gives S_p converging in distribution to N(0,s^2), and S_p+eA_1 has the same limit. Gaussian densities and their fixed-order derivatives are bounded continuous functions. Thus the numerator and denominator converge pointwise to rho_v^{(b)}(y) and rho_v(y), respectively, where v=s^2+delta>0.

To justify integration, the bounded-A event gives

D_p(y)>=c E[rho_delta(y-S_p)exp(-|y-S_p|/sqrt(delta))].

Weighted Cauchy-Schwarz and

rho_delta^{(b)}(u)=(-1)^b delta^{-b/2}He_b(u/sqrt(delta))rho_delta(u)

bound the integrand of J_p by

G_p(y)=C E[rho_delta(y-S_p)exp(|y-S_p|/sqrt(delta))He_b((y-S_p)/sqrt(delta))^2],

with C including delta^{-b}. The function inside this convolution is continuous, bounded, and integrable. Hence G_p converges pointwise to its convolution with N(0,s^2), while integral G_p is finite and independent of p and equals the integral of that limiting convolution. These facts verify the moving-domination hypotheses needed for Pratt's lemma, rather than relying only on bounded integrals. Equivalently, the nonnegative envelopes converge in L1 by their pointwise convergence and convergence of their integrals; truncation then justifies passage under the integral for the dominated integrands. Therefore

J_p -> integral [rho_v^{(b)}(y)]^2/rho_v(y) dy=b!/v^b.

The variance power is v^{-b}, not v^{-1/2}.

## 8. Include the Cross Term

Use the weighted norm ||f||_p^2=integral f^2/D_p. Sections 6 and 7 give

||r_p||_p=o(e^b),

||L_p||_p^2=e^{2b}mu_b^2 J_p/(b!)^2=O(e^{2b}).

The correct comparison is

| ||L_p+r_p||_p^2-||L_p||_p^2 |
<=2||L_p||_p||r_p||_p+||r_p||_p^2=o(e^{2b}).

It follows that

p^b K_p -> mu_b^2/[b! (s^2+delta)^b],

which is finite and strictly positive. In particular K_p=Theta(p^{-b}), with constants depending on the fixed activation and noise strength but not on p.

## 9. Direct Bridge to the Public Recursion

All arguments in this section are at fixed p. They concern exactly the noisy output potential and isotropic initialization specified in the public task.

### 9.1 Scalar Invariance and Normalized Overlap

Let S be any signed permutation matrix. Evenness and permutation invariance of the committee channel, together with Gaussian invariance, imply

Psi(SQS^T)=Psi(Q).

At Q=qI_p, its symmetric-matrix gradient must commute with every diagonal sign matrix and every permutation matrix. Commutation with the sign matrices makes the gradient diagonal; commutation with permutations makes all its diagonal entries equal. Thus

grad Psi(qI_p)=c_p(q)I_p.

Writing psi_p(q)=Psi(qI_p), differentiation along I_p gives psi_p'(q)=p c_p(q).

The public recursion consequently preserves Q_eta^t=q_eta^t I_p. Its scalar update is

F_alpha(q)=2alpha c_p(q)/(1+2alpha c_p(q)).

For a scalar nonnegative profile,

R(qI_p)=sqrt(q)I_p.

Every deterministic unit witness therefore has the same normalized score sqrt(q). In particular the weak-recovery and specialization events are identical when p>=2: one may use v=(e_1-e_2)/sqrt(2) for specialization. This is a conclusion about the actual specified profile, not an appeal to an external full-subspace attainability theorem.

### 9.2 Gaussian-Kernel Representation

Let P(y|z) be the noisy committee likelihood and D(y)=E_Z[P(y|Z)] its marginal density. D(y)>0 for every y. Denote the conditional law of Z given Y=y by nu_y.

For q in (0,1), the density of V conditional on Z=z in the joint Gaussian experiment V=sqrt(q)Z+sqrt(1-q)N, relative to standard Gaussian measure in v, is

k_q(z,v)=(1-q)^(-p/2) exp(-q(||z||^2+||v||^2)/(2(1-q))+sqrt(q)z^T v/(1-q)).

Bayes' formula gives

h_q(y,v):=J_{qI_p}(y,v)/D(y)=E_{nu_y}[k_q(Z,v)].

The conditional law nu_y is invariant under changing any coordinate sign. Hence the same conditional expectation can be taken with the sign-averaged kernel

bar k_q(z,v)=(1-q)^(-p/2) exp(-q(||z||^2+||v||^2)/(2(1-q))) product_{i=1}^p cosh(sqrt(q)z_i v_i/(1-q)).

Consequently

psi_p(q)-psi_p(0)=integral D(y) E_V[h_q(y,V)log h_q(y,V)] dy.

Both potentials are finite. The label has finite second moment, and conditional labels are mixtures with fixed additive Gaussian noise. Their entropies are bounded below by the noise entropy and have an integrable upper bound from their second moments. Equivalently the displayed difference is the mutual information of Y and V, bounded by that of Z and V.

### 9.3 Differentiate the Entropy Explicitly

Let L_V=Delta_V-V^T grad_V be the Gaussian integration-by-parts operator. Direct differentiation of the Gaussian kernel gives

partial_q h_q=-(2q)^(-1)L_V h_q.

Differentiate the entropy expression and integrate by parts against standard Gaussian measure in V. Since E_V[h_q(y,V)]=1, the result is

psi_p'(q)=(2q)^(-1) integral D(y) E_V[||grad_V h_q(y,V)||^2/h_q(y,V)] dy.

This identity also proves nonnegativity of c_p(q). Its finiteness for each q<1 follows without differentiating phi. Weighted conditional Cauchy-Schwarz bounds the integrand by the conditional expectation of ||grad_V k_q||^2/k_q. Integrating over Y and V reduces this bound to a Gaussian calculation:

integral D(y)E_V[||grad_V h_q||^2/h_q]dy
<=E_{Z,V independent standard Gaussian}[||grad_V k_q(Z,V)||^2/k_q(Z,V)]
=pq/(1-q).

Thus 0<=psi_p'(q)<=p/[2(1-q)]. The same estimate on compact q intervals, or conditional versions bounded by a constant times E[||Z||^2|Y] plus a deterministic constant, justifies differentiation after integrating over Y. Gaussian cutoffs justify integration by parts. For each fixed y the likelihood relative to the Gaussian latent prior is bounded by (2pi delta)^(-1/2)/D(y); smoothing by k_q supplies the needed V derivatives. The integrated bounds above permit removal of the cutoffs. The same Gaussian-kernel differentiation in a neighborhood of any interior qI_p justifies the matrix gradient used in Section 9.1.

In particular the scalar update is defined and maps [0,1) into [0,1), with its value at zero obtained by the limit below.

### 9.4 Identify the Linear Gain With Its Required Integrability

For every fixed z,v,

bar k_q(z,v)->1,

q^(-1) partial_{v_i} bar k_q(z,v)->(z_i^2-1)v_i.

Indeed,

partial_{v_i} log bar k_q
=-q v_i/(1-q)+sqrt(q)z_i tanh(sqrt(q)z_i v_i/(1-q))/(1-q).

The inequality |tanh(u)|<=|u| gives, for sufficiently small q,

|q^(-1) partial_{v_i} bar k_q|<=C |v_i|(1+z_i^2)bar k_q.

These convergences also hold in every fixed finite L^a norm under independent Gaussian z,v, after restricting q to a sufficiently small interval depending on a and fixed p. To verify domination, bound each cosh by exp(|u|) and use 2|z_i v_i|<=z_i^2+v_i^2. The resulting bounds are a polynomial times exp(C sqrt(q)(||z||^2+||v||^2)), which has all the specified Gaussian integrals for sufficiently small q. Also cosh>=1 gives Gaussian exponential bounds for each fixed power of bar k_q^{-1}.

Conditional Jensen transfers these bounds and convergences to h_q under the fixed reference measure D(y)dy times standard Gaussian measure in v. Integrating over y restores the standard Gaussian marginal of Z. Consequently

h_q->1,

q^(-1)grad_V h_q -> (E[Z_i^2-1|Y]V_i)_{i=1}^p=a_p(Y)V

in every fixed finite L^a norm for sufficiently small q. Moreover, for any fixed a,

h_q^{-a} <= E_{nu_Y}[bar k_q(Z,V)^{-a}],

so the needed inverse moments are uniformly bounded. From h_q->1 and |h_q^{-1}-1|=|h_q-1|/h_q, Holder's inequality also gives h_q^{-1}->1 in fixed finite norms.

These estimates justify, rather than assume, passage through the Fisher-information denominator. Using the L4 convergence of grad h_q/q and the inverse-moment bounds yields

q^(-2) integral D(y) E_V[||grad_V h_q||^2/h_q] dy -> E[a_p(Y)^2||V||^2]=pK_p.

Combining this with Section 9.3 proves

psi_p'(q)=pK_p q/2+o(q),

c_p(q)=K_p q/2+o(q).

In particular c_p(0)=0 and

F_alpha(q)=alpha K_p q+o(q).

No specialized threshold theorem has been used to establish this multiplier.

### 9.5 Match the Exact Seed and Iteration Quantifiers

Suppose alpha K_p<1. Choose lambda in (alpha K_p,1). There is r_0>0 such that

0<=F_alpha(q)<=lambda q for 0<=q<=r_0.

Every initialization eta<=r_0 then stays in that neighborhood and satisfies q_eta^t<=lambda^t eta. Thus sup_{t>=1}sqrt(q_eta^t)<=sqrt(eta), which tends to zero. Neither public event holds.

Suppose alpha K_p>1. Choose lambda in (1,alpha K_p). There is r_0>0 such that

F_alpha(q)>=lambda q for 0<q<r_0.

Every sufficiently small nonzero initialization must leave (0,r_0) after finitely many iterations: otherwise q_eta^t>=lambda^t eta for every t, contradicting q_eta^t<r_0. At the first exit, q_eta^t>=r_0. Hence

liminf_{eta->0+}sup_{t>=1}sqrt(q_eta^t)>=sqrt(r_0)>0.

The exiting iteration is finite for each eta and is independent of d, precisely as required by the public convention. By Section 9.1, the same lower bound holds for every deterministic unit witness, including the fixed orthogonal witness.

Every alpha<1/K_p therefore fails and every alpha>1/K_p succeeds for both events. Whatever happens at the equality point cannot affect their infima. Consequently

alpha_WR^Alg(p)=alpha_spec^Alg(p)=1/K_p

for the prescribed public profile at each p>=2.

## 10. Conclusion

Sections 8 and 9 give

alpha_WR^Alg(p)=alpha_spec^Alg(p)=Theta(p^{beta_*}).

The positive limiting gain constant in Section 8 supplies constants independent of p. The proof uses no overlap bound uniform in p and no generic-activation committee-symmetry ansatz. It also does not interchange the dimension limit with a dimension-dependent iteration count.

## Remaining Private Obligation

The signed-density expansion, weighted remainder estimate, smoothed CLT integration, corrected variance constant, scalar profile invariance, gain identification, finite-time amplification criterion, specialization equivalence, and threshold inversion are closed above for the explicit public profile.

The source-to-algorithm correspondence remains unproved in the supplied material: derive the finite-dimensional Bayes-matched noisy-channel AMP construction and verify that it realizes the stipulated fixed-iteration overlaps under admissible isotropic side-information initialization. The source refers this specialized construction and its state-evolution proof to external works. This is retained as the private GT warning.

The external threshold and easy-subspace attainability assertions remain unproved as source statements, but they are not dependencies of the direct public-profile proof. A citation or named method is not recorded as closing the remaining realization obligation.
