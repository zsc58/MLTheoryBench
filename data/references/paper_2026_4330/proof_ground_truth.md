# Reference Proof

## Contract and obligations

All norms below are under the full probability density p unless an empirical norm is indicated. Kernels and functions of inclusive-parent coordinates are lifted to R^d. Proper parents are pa(i), whereas Pa(i)=pa(i)∪{i}. Every node uses the same iid sample. The positive regularization parameters are deterministic. The estimator is the explicit formula in the task; neither its score estimate nor the estimator itself is assumed to belong to H_i.

The theorem-critical obligations are: extend the weak identity to the antiderivatives; identify the population Tikhonov equation; control population-score, training-score, and covariance deviations; prove the deterministic perturbation bounds for the explicit estimator; propagate errors through every possible directed path; convert the resulting tail statement to expected norm, including zero approximation errors; construct admissible vanishing schedules; and verify the polynomial specialization, including roots. Each obligation is discharged below.

Constants denoted C may change and depend on the fixed graph, dimension, and the uniform drift, diffusivity, and antiderivative bounds, but not on n, the confidence level, or the admissible regularization values. Additional constants in the rate specialization may depend on its approximation constants, exponents, and ε.

## 1. Population identity

For fixed i,y, K_{i,y} belongs to W^{2,∞}(R^d). There are K_m∈C_c^∞(R^d) converging to it in W^{2,2}(p). Here is the approximation argument needed for this application. Mollify K_{i,y}, choosing the scale so that the unweighted W^{2,2} error on the ball of radius m tends to zero, and multiply by a smooth cutoff equal to one on that ball and zero outside the ball of radius m+1/4. Such cutoffs have derivatives through order two uniformly bounded: use γ(||x||−m) for a fixed smooth transition γ and m≥1. The mollified and cut-off functions have uniformly bounded derivatives through order two. On the inner ball, bounded p controls the weighted error by the unweighted error; on the complement, it is bounded by a constant times the p-mass of the complement. Thus the weighted error tends to zero. This argument is applied in the full space: boundedness of p does not imply boundedness of its marginals.

Apply the weak identity to K_m. Cauchy–Schwarz, boundedness of b* and D, and weighted Sobolev convergence justify the limit. Derivatives of the limiting K_{i,y} outside Pa(i) vanish. Separating its i-th drift term gives

ζ_i(y):=−∫k_i(x,y)b_i^*(x)dp(x)=E[z_i(X,y)],

where

z_i(x,y)=Σ_{j∈pa(i)}b_j^*(x)∂_{x_j}K_{i,y}(x)−(1/2)〈D_{Pa(i),Pa(i)}(x),∇^2_{Pa(i)}K_{i,y}(x)〉_F.

Since k_i is bounded, J_i is bounded and ζ_i=−J_i^*b_i^*∈H_i. The strictly convex Tikhonov objective has the unique normal equation

(L_i+λI)b_{i,λ}=J_i^*b_i^*=−ζ_i.

Comparison with h=0 also gives T_i(λ)≤||b_i^*||_2 uniformly in λ>0.

## 2. Score and covariance deviations

Write ||f||_{E_n}²=n^{-1}Σ_a|f(X_a)|², e_i=||b̂_i−b_i^*||_2, ē_i=||b̂_i−b_i^*||_{E_n}, and A_i=||b_{i,λ_i}−b_i^*||_{E_n}. These empirical quantities use the training sample, not an independent sample. Let κ bound K and its derivatives through order two. The true scores z_i and their centered versions g_i(x,y)=z_i(x,y)−ζ_i(y) are uniformly bounded by a fixed constant M.

We use the following standard, distribution-independent concentration statement: for independent centered random elements Y_a of a separable Hilbert space satisfying ||Y_a||≤M, their mean has norm at most C M sqrt(log(2/δ)/n) with probability at least 1−δ. Its scalar version applies also under conditioning that leaves the summands independent and centered. These applications have the required measurability: the kernels and their specified derivatives are continuous in their arguments, b* and D are measurable, L²(p) is separable, and a continuous kernel on a Euclidean space has separable RKHS, as follows by taking feature maps on a countable dense subset.

The plug-in part of ζ̂_i−ζ_i satisfies, both in L²(p) and at every evaluation point,

|n^{-1}Σ_aΣ_{j∈pa(i)}(b̂_j(X_a)−b_j^*(X_a))∂_{x_j}K_{i,y}(X_a)|≤κΣ_{j∈pa(i)}ē_j.

This is a deterministic Cauchy–Schwarz bound and makes no independence assertion about fitted parent errors.

For the remaining population-norm term, apply Hilbert concentration to g_i(X_a,·)∈L²(p). Hence, with probability at least 1−δ,

ε_{2,i}:=||ζ̂_i−ζ_i||_2≤C sqrt(log(2/δ)/n)+κΣ_{j∈pa(i)}ē_j.

For the training norm, condition on X_a. The variables g_i(X_b,X_a), b≠a, are conditionally independent and centered, each bounded by M. Scalar Hoeffding, a union bound over a, and the bound M/n on the omitted diagonal yield

max_a|n^{-1}Σ_b g_i(X_b,X_a)|≤C sqrt(log(2n/δ)/n)+M/n

with probability at least 1−δ. Consequently,

ε_{1,i}:=||ζ̂_i−ζ_i||_{E_n}≤C[1+sqrt(log n)+sqrt(log(2/δ))]/sqrt(n)+κΣ_{j∈pa(i)}ē_j.

This closes the same-sample empirical-score obligation directly. Equivalently, the source's canonical kernel is h_y(u,v)=g_i(u,y)g_i(v,y). For independent observations, its off-diagonal sum equals (Σ_b g_i(X_b,y))²−Σ_b g_i(X_b,y)². Scalar Hoeffding and the diagonal bound give the exact order needed in that U-statistic application; a specialized citation is not being used as an unexpanded obligation.

Finally,

L̂_i=n^{-1}Σ_a k_i(X_a,·)⊗k_i(X_a,·).

Each summand has Hilbert–Schmidt norm k_i(X_a,X_a)≤κ, its mean is L_i, and centered summands have norm at most 2κ. Hilbert concentration in the separable Hilbert–Schmidt space, followed by the operator-norm bound by the Hilbert–Schmidt norm, gives

ε_{3,i}:=||L̂_i−L_i||op≤C sqrt(log(2/δ)/n)

with probability at least 1−δ.

## 3. Deterministic perturbation for the explicit estimator

Fix i and omit its index. Let S:H→E_n be sample evaluation, so L̂=S*S and SS*=G/n with the empirical normalization. Put U=(SS*+λI_{E_n})^{-1} and R=(L̂+λI_H)^{-1}. The explicit estimator can be written

b̂=λ^{-1}S*U ζ̂^{vec}−λ^{-1}ζ̂,

where the first term is an RKHS function and the second is an ordinary bounded function. For f∈H, direct multiplication verifies

Rf=λ^{-1}f−λ^{-1}S*USf.

Apply this identity only to the genuine RKHS element ζ. Decompose

b*−b̂=(b*−b_λ)+(b_λ−R(−ζ))+(R(−ζ)−b̂).

The inverse-difference identity and −ζ=J*b* show that the second summand is, up to sign,

R(L̂−L)(L+λI)^{-1}J*b*.

Spectral calculus gives

||SR||≤λ^{-1/2},  ||(L+λI)^{-1}J*||≤λ^{-1/2},  ||SS*U||≤1.

These inequalities follow respectively from sqrt(u)/(u+λ)≤λ^{-1/2} and u/(u+λ)≤1 for u≥0. If q=||L̂−L||op, then

(JR)*(JR)=RL̂R+R(L−L̂)R,

so ||JR||≤λ^{-1/2}+sqrt(q)/λ. Likewise,

(JS*U)*(JS*U)=USS*SS*U+US(L−L̂)S*U,

which gives ||JS*U||≤1+sqrt(q/λ). All inverses here act on the displayed Hilbert spaces; in particular U is an E_n operator.

Taking empirical norms in the decomposition now yields

ē_i≤A_i+ε_{3,i}||b_i^*||_2/λ_i+2ε_{1,i}/λ_i.

Taking population norms yields

e_i≤T_i+(ε_{3,i}/λ_i+ε_{3,i}^{3/2}/λ_i^{3/2})||b_i^*||_2+(ε_{1,i}+ε_{2,i})/λ_i+ε_{1,i}sqrt(ε_{3,i})/λ_i^{3/2}.

Thus the proof never applies an H_i inverse to ζ̂_i.

## 4. Simultaneous component bounds

Use confidence δ/(3d) in the deviations and take a union bound. Put t=log(2/δ). Since n≥3, constants absorb shifts in logarithms. The regularization condition implies λ_i sqrt(n)≥1, because r_i≥6 and λ_i≥n^{-2/r_i}. Substitution into the perturbation inequalities gives, simultaneously for every vertex, on an event of probability at least 1−δ,

ē_i≤A_i+C(log n)t/(λ_i sqrt(n))+(C/λ_i)Σ_{j∈pa(i)}ē_j,

e_i≤T_i+C(log n)t/(λ_i sqrt(n))+(Ct/λ_i)Σ_{j∈pa(i)}ē_j.

The population inequality uses t, not an unjustified sqrt(t): the covariance-mismatch terms include higher fractional powers of the deviation. Crucially, the parent multiplier in the training inequality has no t factor.

## 5. DAG propagation and expectation

Expand the training recursion inside the population inequality. The DAG is fixed and finite, so the number of directed paths and all products of fixed constants can be absorbed into a graph-dependent constant. There are two kinds of terms.

A sampling contribution associated with a path v_0→⋯→v_l=i has coefficient bounded by

C(log n)t² n^{-1/2}∏_{q=0}^l λ_{v_q}^{−1}.

This includes the length-zero path, after increasing C. Depths increase strictly along every edge, so the depths occurring on this path are distinct members of {0,…,d_i}. Hence

Σ_{q=0}^l 2/r_{v_q}≤Σ_{h=0}^{d_i}2/(6·3^h)=1/2−1/r_i.

The sampling contribution is therefore at most C(log n)t² n^{-1/r_i}.

A bias contribution associated with a proper path m=v_0→⋯→v_l=i is bounded by

Ct A_m∏_{q=1}^l λ_{v_q}^{−1}.

Write u=T_m(λ_m). For u>0 let Q_m=A_m²/u²; for u=0 set Q_m=0. Because b_{m,λ_m} is deterministic and the observations are iid, E[A_m²]=u². Thus A_m=u sqrt(Q_m) almost surely and E[Q_m]≤1, including u=0.

Set s_q=d_{m,v_q}. Concatenating a longest path ending at v_q with the next edge shows s_{q+1}≥s_q+1; also s_1≥1 and s_l=d_{mi}. Therefore

Σ_{q=1}^l 2/3^{s_q}≤Σ_{h=1}^{d_{mi}}2/3^h=1−3^{-d_{mi}}.

The ancestor regularization inequalities imply

u∏_{q=1}^l λ_{v_q}^{−1}≤u^{1−Σ_q2/3^{s_q}}≤w_{mi},

where w_{mi}=max{u^{3^{-d_{mi}}},u}. The last step treats u≤1 and u>1 separately; when u=0 the bias term vanishes and no division is used. This also handles graphs with a direct edge and a longer alternative path between the same vertices.

Using t sqrt(Q_m)≤(t²+Q_m)/2 and summing paths gives

e_i≤T_i+CΣ_{m∈an(i)}w_{mi}Q_m+C[(log n)n^{-1/r_i}+Σ_{m∈an(i)}w_{mi}]t²

with probability at least 1−δ for every δ∈(0,1).

For completeness, if nonnegative random variables V,W satisfy P(V≤W+βlog²(2/δ))≥1−δ for every δ, then the positive part Z=(V−W)_+ has that same tail bound. Integrating the bound above βlog²2 gives EZ≤Cβ; below that threshold use the trivial probability bound one. Thus EV≤EW+Cβ, with no independence requirement between V and W. The case β=0 follows by letting δ tend to zero.

Apply this with W=T_i+CΣ_m w_{mi}Q_m and use E[Q_m]≤1. It follows that

E e_i≤C_i[(log n)n^{-1/r_i}+T_i+Σ_{m∈an(i)}w_{mi}].

Finally u=T_m(λ_m)≤||b_m^*||_2≤B for a fixed B. For 0<a≤1,

max{u^a,u}≤max{1,B}u^a.

Absorbing this fixed factor proves exactly the requested expected-norm bound. Roots have empty ancestor sums and depth zero, and all zero-bias cases have already been covered.

## 6. Consistency

For any fixed h∈H_i, optimality gives

T_i(λ)²≤||h−b_i^*||_2²+λ||h||_{H_i}².

If H_i is dense in the inclusive-parent marginal L² space, first choose h with arbitrarily small approximation error and then let λ decrease to zero. This proves T_i(λ)→0.

Construct schedules topologically by setting each λ_i(n) equal to the maximum in the regularization lower bounds. At a root this is n^{-1/3}. If all ancestor schedules tend to zero, their T_j values tend to zero, so the maximum for i also tends to zero. This proves existence of admissible vanishing schedules. More generally, any deterministic admissible schedules tending to zero give E e_i→0 by the established bound. If monotone decrease is desired, T_i is nondecreasing in λ, as follows either from the spectral representation of Tikhonov regularization or by comparing the two minimization inequalities, so this recursive construction can be taken nonincreasing in n.

## 7. Polynomial specialization

Let ε∈(0,1/(2d)), ε_i=d_iε, and λ_i(n)=n^{-2(1−ε_i)/r_i}. Since d_i≤d−1, 0≤ε_i<1/2, so λ_i→0 and λ_i≥n^{-2/r_i}.

For j∈an(i), concatenating longest paths gives d_i≥d_j+d_{ji}, hence r_j3^{d_{ji}}≤r_i. Also ε_j<ε_i. The approximation assumption gives

T_j(λ_j)^{2/3^{d_{ji}}}=O(n^{-2(1−ε_j)/(r_j3^{d_{ji}})}(log n)^{2α_j/3^{d_{ji}}}).

The exponent (1−ε_j)/(r_j3^{d_{ji}}) is strictly larger than (1−ε_i)/r_i. Therefore the displayed quantity is o(λ_i), proving every ancestor lower bound for sufficiently large n. The same comparison with half these exponents bounds each ancestor contribution in the risk by O(n^{-(1−ε_i)/r_i}). The own-component term is

T_i(λ_i)=O(n^{-(1−ε_i)/r_i}(log n)^{α_i}).

Together with the sampling term, this proves the requested O(n^{-(1−2ε_i)/r_i}) rate up to logarithmic factors. In fact, for d_i>0 the positive slack ε_i absorbs all these logarithms and gives the displayed rate without them. At a root ε_i=0, the proved bound is O(n^{-1/6}(log n)^{max{1,α_i}}), which is exactly within the frozen logarithmic-factor formulation. No log-free root conclusion is used or claimed.

## Audit closure

All obligations for the frozen public task are closed. The source-local corrections are full-space approximation in the score identity, the component index and empirical-space inverse in the perturbation argument, and the indices, zero case, and explicit path algebra in the recursive argument. The stronger log-free root statement in the original source is not part of the frozen target and is not certified by this reference.
