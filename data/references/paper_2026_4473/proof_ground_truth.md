# Reference Proof

## Contract and obligations

The grammar is drawn once and remains fixed during training and testing. The root is uniform, all node productions are conditionally independent, and a stage observes only fresh input-label pairs. Conditional-label vectors refer to the first patch. The proof must establish: (i) the random grammar's signal bound; (ii) uniform feature control on the actually reachable representations; (iii) finite-sample ridge prediction control without factoring empirical conditional expectations; (iv) optimization and nonzero normalization; (v) the depth recursion and stated resource bounds; and (vi) exact final classification.

All constants below are universal and may be enlarged. Statements involving the random regime hold for sufficiently large members of the parameter sequence in the task. Put J=Vm.

## 1. Random grammar and conditional labels

Let A_l be the first-token transition matrix from depth l-1 to depth l. Its entry is N_(nu,mu)/m, where Vm balls, m of each color, are uniformly allocated to V bins with m slots each. Every row and column sums to one, and matrices from different levels are independent. Consequently, starting from the uniform root, the first token at every depth is uniform. There are J distinct possible patches at each level, and each first patch has probability 1/J. Thus the non-degeneracy requirement holds with kappa=1 and hence with every kappa>=1.

For a possible patch mu let nu(mu) be its unique parent. Its production probability from that parent is 1/m. Bayes' rule therefore gives

q_mu^(l)=A_1...A_(l-1)e_(nu(mu)).

The empty product for l=1 is the identity. This identity uses both the uniform root and the first-token marginal law; it is not valid for an unspecified root distribution.

### Fixed-vector transition estimate

We give the transition estimate rather than assume a lower singular-value bound. Fix a zero-sum vector z independent of a matrix A. The case z=0 is immediate; by homogeneity suppose ||z||=1. Give each color-mu ball value z_mu. If tau=Az, tau_nu is the mean of the m values in bin nu.

We use the following standard independent sampling comparison, stated in the source: for a finite real multiset, n no larger than its size, and convex g, E g(sum of n draws without replacement) is at most E g(sum of n independent draws with replacement). Here the populations are finite multisets of ball values or indicator values, all sample sizes are feasible, and the test functions used below are exponentials or fourth powers, which are convex.

Expose bins sequentially and let F_(nu-1) record the preceding bins. Let H_(nu,mu) be the number of color-mu balls remaining. Fix alpha in (0,1/2), and put t=log(CV^2/alpha). Applying sampling comparison to indicator exponentials, followed by the ordinary exponential Markov argument, gives, simultaneously in the middle third of bins and all colors, with probability at least 1-alpha,

|H_(nu,mu)-m(1-(nu-1)/V)| <= C sqrt(mt).

For completeness, this is a hypergeometric count: the m positions occupied by a fixed color are a uniform sample of m slots, and membership in the first nu-1 bins is a zero-one population with mean (nu-1)/V. Comparison bounds its centered moment generating function by that of a binomial count. The estimate E exp(lambda(B-E B)) <= exp(Cm lambda^2) for |lambda|<=1, obtained by expanding the Bernoulli exponential, yields the displayed deviation with failure at most 2 exp(-ct). A union bound proves the simultaneous statement.

On this event, write b_nu and v_nu for the conditional mean and variance of one remaining ball value. Since sum z_mu=0 and ||z||=1,

|b_nu| <= C sqrt(t/(mV)),

E[Z^2|F_(nu-1)] = (1+O(sqrt(t/m)))/V.

Indeed, divide the remaining weighted sums by m(V-nu+1); their error is bounded using ||z||_1<=sqrt(V) and sum z_mu^2=1. Therefore v_nu >= (1-O(sqrt(t/m))-O(t/m))/V.

The exact variance formula for sampling m values without replacement from M_nu=m(V-nu+1) remaining values gives

E[tau_nu^2|F_(nu-1)] = b_nu^2 + (v_nu/m)(1-(m-1)/(M_nu-1)).

It follows, for sufficiently large m/t and V, that throughout the middle third

1/(2mV) <= E[tau_nu^2|F_(nu-1)] <= Ct/(mV).

The fourth moment is bounded without any signed negative-association factorization. Conditional on the exposed bins, apply sampling comparison to the fourth power of the centered sum. For independent centered draws U_i from the remaining population,

E[(sum_(i=1)^m U_i)^4] = m E U_1^4 + 3m(m-1)(E U_1^2)^2.

Here E U_1^4<=C/V and E U_1^2<=C/V: the remaining proportion of each color is at most C/V, ||z||_infinity<=1, and the mean is bounded as above. Using (a+b)^4<=8(a^4+b^4), we obtain

E[tau_nu^4|F_(nu-1)] <= C(1/(m^3 V)+t^2/(m^2 V^2))=:v_*.

Set xi_*=Ct/(mV). Predictably set tau_nu^2 to zero whenever its conditional second or fourth moment exceeds these deterministic bounds. Denote the resulting variable by U_nu. Then W_nu=E[U_nu|F_(nu-1)]-U_nu has conditional mean zero, is bounded above by xi_*, and has conditional second moment at most v_*.

For any mean-zero W bounded above by b, and 0<=lambda<=1/b,

E exp(lambda W) <= exp(lambda^2 E W^2).

This follows from e^x<=1+x+x^2 for x<=1. Applying it conditionally and iterating gives

Pr(sum W_nu >= u) <= exp(-c min(u^2/(Vv_*),u/xi_*)).

There are at least V/4 middle bins for sufficiently large V. On the simultaneous count event, truncation does nothing and the sum of conditional means is at least 1/(8m), hence at least 1/(10m). Take u=1/(20m). The preceding bound shows

Pr(||Az||^2 < 1/(20m)) <= alpha + exp(-c min(m,V/t^2)).

In particular, if min(m,V)/t^3 tends to infinity, this is at most a constant multiple of alpha for sufficiently large parameters.

### Products and simultaneous separation

For A_1...A_k(e_a-e_b), apply the estimate from right to left. The vector to which A_j is applied is determined by A_(j+1),...,A_k, and is independent of A_j. It remains zero-sum because the matrices are column stochastic. Thus conditioning validates every application; no simultaneous assertion about all zero-sum vectors is needed.

Allocate alpha=delta/(C L^2 V^2). The relevant logarithm is O(log(VL/delta)). Because m,V=Theta(log d), L=O(log d/log log d), and log^3(2/delta)=o(min(m,V)), the cube of this enlarged logarithm is still o(min(m,V)). Union bounding over the at most L^2 V^2 applications gives, with probability at least 1-delta/3,

||A_1...A_(l-1)(e_a-e_b)|| >= (20m)^(-(l-1)/2)

for every required level and distinct parents. At level one the norm is sqrt(2). The Bayes identity proves the public signal bound. Defining K_rho=sqrt(m)20^(-(L-1)/2), we also have

(20m)^(-(l-1)/2) >= K_rho m^(-l/2).

Moreover log(K_rho^(-1))_+ <= (L/2)log 20, so this signal constant has the source's required inverse-subpolynomial dependence on input length.

## 2. Uniform random-feature control

The feature map has exactly unit norm. Suppose token representations have diameter at most b within each token class and separation at least r between different token classes. Concatenations for a common patch have diameter at most sqrt(s)b; distinct patches have distance at least r.

For the RBF kernel, distinct-patch kernel values are at most exp(-r^2/(2 sigma^2)). If random-feature inner products approximate this kernel to error u, same-patch squared feature distances are at most sb^2/sigma^2+2u. Consequently it suffices to choose

sigma^2=r^2/(2 log(2/epsilon_O)),

b <= epsilon_S sigma/sqrt(2s),

u := u <= min(epsilon_O/2,epsilon_S^2/4).

These conditions give cross-patch inner products of magnitude at most epsilon_O and within-patch feature diameter at most epsilon_S.

The standard independent feature theorem quoted in the source says that in dimension h, the probability of kernel approximation error exceeding u on the unit ball is at most

256 h/(sigma^2 u^2) exp(-M u^2/(4(h+2))).

For a ball of radius B, rescale inputs by B and bandwidth by B. The bound becomes

256 h B^2/(sigma^2 u^2) exp(-M u^2/(4(h+2))).

In our induction h=sV and B=2sqrt(s): leaves have norm one, and every successful learned token representation is within less than one of a probability vector. Therefore this theorem applies to the entire reachable region, not merely the training points. Choose M to make its failure probability at most delta/(CL). This establishes uniform control for all later inputs, including every possible descendant realization.

## 3. Finite-sample ridge regression

Fix a stage and condition on the grammar and successful preceding stages. Its training sample is fresh. Let p_mu be the probability of its first patch and n_mu its count. Put lambda=1/J. A binomial exponential bound and a union bound imply

n_mu >= N/(2 kappa J)

simultaneously with failure at most alpha whenever N>=C kappa J log(CJ/alpha).

### The empirical cross-moment correction

Condition also on the stage's patch identities and feature vectors x_i. Conditional independence of the descendant subtree and root label given the patch implies that the labels Y_i remain independent, with conditional means q_(mu_i). This conditional statement is justified by fresh sampling and by the fact that the representation uses only the patch's descendants and previously fixed layers.

For every observed patch define

D_mu=(1/n_mu) sum_(i:mu_i=mu) (Y_i-q_mu)x_i^T.

Conditional on the features, its summands are independent, centered matrices of Frobenius norm at most two. Thus, simultaneously over patches,

||D_mu||_F <= C sqrt(log(CJ/alpha)/n_mu)

with failure at most alpha. Here is a dimension-free derivation. For an average of n independent centered Hilbert-space variables of norm at most two, independence gives expected squared norm at most 4/n, hence expected norm at most 2/sqrt(n). Replacing one variable changes that norm by at most 4/n. The bounded-difference exponential argument then gives a deviation at most C sqrt(log(1/alpha)/n): expose variables, use the centered bounded-interval exponential inequality on the Doob differences, and optimize exponential Markov. This applies to the finite-dimensional Frobenius space regardless of feature width. The same argument also bounds conditional empirical label means with denominator n_mu, not N.

Let X have columns x_i, and let Q have columns q_(mu_i). The actual empirical cross-moment differs from QX^T/N by

sum_mu (n_mu/N)D_mu,

whose operator norm is at most C sqrt(log(CJ/alpha)/n_min). Since the ridge inverse has operator norm at most J, the actual ridge solution and the surrogate-label ridge solution differ, on every unit input, by at most

C J sqrt(log(CJ/alpha)/n_min).

This term replaces the source's invalid exact empirical factorization.

### Near-orthogonality and the scalar coefficient

Write G=X^TX, and let G_0 retain only within-patch blocks. Then ||G-G_0||<=N epsilon_O. Both G+lambda N I and G_0+lambda N I have inverse norm at most 1/(lambda N). The resolvent identity and ||Q||,||X||<=sqrt(N) show that replacing G by G_0 in the dual ridge formula changes predictions by at most epsilon_O/lambda^2.

For a test representation x of patch mu, all other blocks contribute at most J epsilon_O/lambda, because every cross-patch inner product has magnitude at most epsilon_O. Thus the surrogate prediction is

b_mu(x)q_mu + error,

with error norm at most 2J^2 epsilon_O, where

b_mu(x)=p_hat_mu xbar_mu^T(p_hat_mu C_mu+lambda I)^(-1)x,

xbar_mu and C_mu being the conditional empirical first and second feature moments.

If epsilon_S<=lambda/4, write C_mu=xbar_mu xbar_mu^T+S_mu, with ||S_mu||<=epsilon_S^2. The resolvent identity bounds the inverse perturbation by p_hat_mu epsilon_S^2/lambda^2. Also xbar_mu^T x>=1-epsilon_S^2/2 and ||xbar_mu||<=1. The rank-one inverse formula therefore gives

xbar_mu^T(p_hat_mu C_mu+lambda I)^(-1)x >= 1/[4(p_hat_mu+lambda)].

Indeed the rank-one term is at least 1/[2(p_hat_mu+lambda)], and the perturbation is at most epsilon_S^2/lambda^2<=1/16, no larger than 1/[4(p_hat_mu+lambda)] since p_hat_mu+lambda<=2. On the count event,

b_mu(x) >= 1/[4(1+2 kappa)] >= 1/(12 kappa).

### Optimization and normalization

The Hessian spectrum of the ridge objective lies in [lambda,1+lambda]. Choose eta=1/(1+lambda). Gradient descent from zero therefore satisfies

||W_T-W_*||_F <= exp(-T/(J+1))||W_*||_F <= J exp(-T/(J+1)).

The last bound follows from the ridge formula and ||Ehat[Yx^T]||_F<=1.

Combining the estimates, uniformly for all representations of all patches,

W_T x=b_mu(x)q_mu+e_mu(x),

||e_mu(x)|| <= 2J^2 epsilon_O + C J sqrt(log(CJ/alpha)/n_min) + J exp(-T/(J+1)).

If the right side is at most a/(100 kappa sqrt(V)), with 0<a<1/10, then the coordinate sum is positive: its distance from b_mu(x) is at most sqrt(V)||e_mu(x)||. Since ||q_mu||<=1, subtracting q_mu from the normalized output gives error at most

2(1+sqrt(V))||e_mu(x)||/b_mu(x) <= 48 kappa sqrt(V)||e_mu(x)|| < a.

Sufficient resource conditions are consequently

N >= C kappa^3 J^3 V a^(-2) log(CJ/alpha),

epsilon_S=1/(4J),

epsilon_O=a/(C kappa sqrt(V)J^2),

T >= C J log(C kappa sqrt(V)J/a).

These conditions include the count requirement. They prove the desired uniform single-layer conclusion without assuming exact empirical independence.

## 4. Chaining and resources

Let rho_l=K_rho m^(-l/2), and set

H=1+L log(20m)+log(C kappa J V s L/delta),

D=C J sqrt(sH),

a_l=rho_l/D.

For the specified K_rho, rho_l<=1. Increasing C ensures all a_l<1/10 and the final coordinate error is strictly below 1/2.

The bottom inputs are one-hot, with diameter zero and separation sqrt(2). At any subsequent stage l, successful outputs of stage l+1 are within a_(l+1) of their conditional-label centers. Synonymous child patches have the same conditional-label vector, by the unique-parent production law and conditional independence. Hence each token class has diameter at most 2a_(l+1), and distinct token classes have separation at least rho_(l+1)-2a_(l+1)>=rho_(l+1)/2.

Use r=rho_(l+1)/2 in the feature construction, epsilon_S=1/(4J), and epsilon_O=a_l/(C kappa sqrt(V)J^2). The feature condition is satisfied if

D >= C J sqrt(s log(C kappa sqrt(V)J^2/a_l)).

Our choice of H and D ensures this at every level: log(1/rho_l)<=C L log(20m), and the remaining terms, including log D, are bounded by a universal multiple of H. Thus the recursion closes from leaves to root. Each stage uses failure budget delta/(CL), conditionally on previous success. A union bound, together with the grammar event, gives overall failure at most delta.

Summing the stage sample requirements gives

N <= C kappa^3 J^3 V log(CJL/delta) D^2 K_rho^(-2) sum_(l=1)^L m^l

<= poly(kappa,m,V,s,L,log(1/delta)) K_rho^(-2)m^L.

The last step uses m>=2, J=Vm, and the polynomial bound on H. Integer rounding is absorbed into the same bound.

The rescaled feature theorem gives polynomial widths: inverse bandwidths and inverse feature tolerances are polynomial in K_rho^(-1), kappa,V,s,L,m^L and the displayed logarithmic failure parameter. The iteration requirements are polynomial in the same quantities. Hyperparameters depend only on these parameters, not on hidden productions or latent tokens.

Finally, the first patch at depth one has a unique root parent R, so q_mu^(1)=e_R. Uniform accuracy strictly below 1/2 in every coordinate gives a strictly larger R coordinate than every other coordinate. On the successful training event the classifier is therefore correct for every leaf sentence in the grammar's support, and in particular for an independent fresh example. All normalization denominators encountered on this event are nonzero.

## Audit closure

The transition estimate, its conditional iteration, feature uniformity, conditional sampling and cross-moment concentration, ridge leakage, normalization, optimization, recursion, and final classification have all been derived above. The two quoted independent tools have their relevant statements and verified hypotheses supplied: convex sampling comparison and uniform RBF feature approximation. No paper-specific unproved lemma is treated as a completed obligation.
