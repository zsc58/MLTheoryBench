# Reference Proof

## Contract and Obligations

The three assertions concern the same null law Q but two different planted laws: the moment-matching law P_k and the point-mass mixture R_alpha. The algorithmic assertion applies to every fixed law D having the stated line mass; it does not require D to have finite moments. The low-degree experiment uses independent product laws and is not the corrupted observation experiment.

The obligations are: the scalar Gaussian mean/variance comparison; variance-normalized anti-concentration on the two-dimensional parameter law; a uniform one-sided estimate and quantitative dilation; finite convex realization and all mixed-moment equalities, including odd-coordinate cases and k=1; the single-sample LDA bound and tensorization; and null soundness, planted completeness, zero-observation handling, and dimension-aware complexity. Each is discharged below. The specialized quantitative random-polytope theorem cited by the source is not invoked; no random-polytope sample-count guarantee is needed for the target.

## 1. Gaussian Mean/Variance Comparison

Let h_i be normalized probabilists' Hermite polynomials. Their Gaussian orthonormality and value formula are given in the source. In particular h_{2r}(0)^2=binom(2r,r)/4^r<=C/sqrt(r+1), while h_{2r+1}(0)=0. Thus sum_{i=0}^d h_i(0)^2<=C sqrt(d+1).

For a polynomial q in two scalar variables with total degree at most d>=1 and q(0,0)=0, write q=sum_{i+j<=d} gamma_ij h_i(lambda)h_j(g). Orthonormality gives Eq=gamma_00 and Var q=sum_{0<i+j<=d}gamma_ij^2. Evaluating at the origin gives gamma_00=-sum_{0<i+j<=d}gamma_ij h_i(0)h_j(0). By Cauchy-Schwarz,

|Eq|^2<=Var q sum_{0<i+j<=d}h_i(0)^2h_j(0)^2<=C d Var q.

This includes the univariate case. The comparison is not being asserted for an arbitrary number of Gaussian coordinates.

## 2. Anti-Concentration and Quantitative Positive Depth

For k>=2 define nu as the law of (lambda,z)=(lambda,lambda g), with lambda,g independent scalar standard Gaussians. Let T contain all pairs of nonnegative even integers (a,b) with 0<a+b<=k, and let Phi(lambda,z)=(lambda^a z^b)_{(a,b) in T}. There is no constant coordinate.

For every unit coefficient vector beta, p=<beta,Phi> is nonconstant. After substitution, q(lambda,g)=p(lambda,lambda g) has degree at most K=2k, has zero monomial constant term, and is nonconstant: distinct pairs (a,b) yield distinct monomials lambda^{a+b}g^b. A nonzero polynomial has zero set of Gaussian measure zero. This follows by induction on the number of variables, conditioning on all but one variable and using that a nonzero univariate polynomial has finitely many roots. Consequently Var_nu p>0 and every affine hyperplane has zero Phi-measure.

The audited standard independent Carbery-Wright statement used here is: for a nonconstant polynomial of degree at most K under a log-concave probability measure with finite positive variance, its probability of lying in any interval of radius t times its standard deviation is at most A K t^{1/K}, for a universal A. Apply it under N(0,I_2), which is log-concave; all polynomial moments are finite. Distributional transfer to nu gives

sup_s P_nu(|p-s|<=t sqrt(Var p))<=eta(t):=A K t^{1/K}.

The comparison in Section 1 also gives |E_nu p|<=M sqrt(k Var_nu p), with universal M>=1, absorbing the degree factor 2 into M. It additionally recovers the source's mean-normalized anti-concentration estimate, but the variance-normalized estimate above is what the one-sided argument needs.

Here is that argument explicitly. For Z=p-Ep and sigma^2=Var p, E Z=0 and E Z_+=E|Z|/2. Cauchy-Schwarz implies P(Z>=0)>=E|Z|^2/(4sigma^2). If eta(t_1)<=1/2, then E|Z|>=t_1 sigma/2. Subtracting P(0<=Z<t sigma)<=eta(t) therefore gives

P(p>=Ep+t sigma)>=t_1^2/16-eta(t).

Increase A to be at least 1 and choose

t_1=(4AK)^(-K),  t_0=(t_1^2/(32AK))^K,  delta=t_0/(M sqrt(k)).

Then eta(t_1)=1/4 and eta(t_0)=t_1^2/32. Also delta Ep<=delta|Ep|<=t_0 sigma. Hence, uniformly in beta,

P(p>=(1+delta)Ep)>=P(p>=Ep+t_0 sigma)>=t_1^2/32>0.

Thus theta'=(1+delta)E_nu Phi has positive Tukey depth, where depth means inf_{||beta||=1}P(<beta,Phi-theta'>=0). Taking logarithms of the displayed parameters shows log(1/delta)<=B k^2 log(k+1) for a universal B. In particular delta>=a_0(k+1)^(-B k^2) after adjustment of universal constants. This calculation accounts for the degree doubling; no exponent 1/k is used for a degree-2k polynomial.

## 3. Finite Convex Realization and Moment Matching

Write D=|T|. For k>=2, D is positive and finite. The law nu assigns probability one to lambda!=0. For each unit vector u in R^D, positive depth gives P(<u,Phi-theta'>=0)>0. Hyperplane non-atomicity gives P(<u,Phi-theta'>=0)=0, so

P(<u,Phi-theta'>>0)>0.

It follows that there is an actual parameter pair (lambda_u,z_u), with lambda_u!=0, such that <u,Phi(lambda_u,z_u)-theta'>>0. Fix one such pair for each direction, and put v_u=Phi(lambda_u,z_u). The set

U_u={w in the unit sphere:<w,v_u-theta'>>0}

is open in the sphere and contains u. These sets cover the sphere. Compactness of the finite-dimensional unit sphere gives a finite subcover U_{u_1},...,U_{u_N}. Put v_j=v_{u_j}; all are actual parameter moment vectors with nonzero lambda coordinates. Consequently the continuous function

F(w)=max_{1<=j<=N}<w,v_j-theta'>

is strictly positive on the sphere. It attains a positive minimum gamma>0.

Let K_* be the convex hull of v_1,...,v_N. This is a compact convex set, since it is the continuous image of the compact simplex of convex weights. We now prove that B(theta',gamma/2) is contained in K_*, without presupposing theta' belongs to K_*.

If y were outside K_*, choose a closest point q in K_*. It exists by compactness, and y!=q. For each v in K_*, the segment q+t(v-q), 0<=t<=1, belongs to K_*. Minimality of q and the one-sided derivative of its squared distance to y at t=0 give <y-q,v-q><=0. Therefore, for w=(y-q)/||y-q||,

max_{v in K_*}<w,v><=<w,q><<w,y>.

In particular <w,y-theta'>>max_j<w,v_j-theta'>=F(w)>=gamma. But if ||y-theta'||<gamma/2, Cauchy-Schwarz gives <w,y-theta'><gamma/2, a contradiction. This proves the ball containment. It proves both actual finite convex representation and an interior neighborhood, rather than only membership in a closed convex hull. The radius depends on the law and target through the chosen witnesses; it is not determined solely by numerical depth.

Set alpha=delta/(1+delta), so 1/(1-alpha)=1+delta. Write c_j=E H^j for a scalar standard Gaussian H, with c_0=1. Under nu,

E(lambda^a z^b)=c_b c_{a+b}.

Choose mu_1 uniform on {-s,s}, for some s>0 to be specified. Define the target coordinates

theta_{a,b}=c_b c_{a+b}/(1-alpha) if a>0,

theta_{0,b}=(c_b^2-alpha s^b)/(1-alpha) if a=0.

For a>0 this equals theta'_{a,b}. For a=0 its difference from theta'_{0,b} is -delta s^b. Because the index set is finite and every such b is positive, choosing s sufficiently small makes ||theta-theta'||<gamma/2. Thus theta belongs to K_*. By the definition of a finite convex hull there are nonnegative weights summing to one such that theta=sum_j w_j v_j. Assign these weights to their parameter pairs to obtain a finitely supported law mu_2 with nonzero lambda and E_mu2 Phi=theta. Independently symmetrize its lambda and z signs; all constrained coordinates are even in each variable, so their expectations are unchanged and lambda remains nonzero. The law mu_1 is already symmetric.

Construct P_k by taking (0,...,0,z), z~mu_1, with probability alpha; otherwise draw (lambda,z)~mu_2, independently draw H~N(0,I_{n-1}), and take X=(lambda H,z). All its moments are finite. Since mu_2 has nonzero lambda, its Gaussian component has zero probability on the distinguished line when n>=2. Thus that line has mass exactly alpha in (0,1).

To verify all monomial constraints, let the first n-1 coordinate exponents be r_1,...,r_{n-1}, let b be the last exponent, and put a=sum r_j. If some r_j is odd, conditional Gaussian symmetry makes the P_k and Q moments zero. If all r_j are even but b is odd, the independent z sign symmetry makes the P_k moment zero, as does Gaussian symmetry for Q. Otherwise all relevant exponents are even. If a>0, the P_k moment is

(1-alpha)(product_j c_{r_j})E_mu2(lambda^a z^b)=(product_j c_{r_j})c_b c_{a+b},

which equals the Q moment. If a=0 and b>0, the mixture equation gives alpha s^b+(1-alpha)E_mu2 z^b=c_b^2, again the Q moment. The degree-zero constraint holds because both laws are probabilities. These cover every monomial of total degree at most k.

Finally alpha>=delta/2, since the chosen delta<=1. This proves alpha>=a_0(k+1)^(-B k^2) after adjusting a_0. For k=1, instead take a mixture with weight 1/2 on the symmetric two-point law supported on +-e_n and weight 1/2 on N(0,I_n). It has zero mean, line mass 1/2, and matches Q through degree 1. Decrease a_0 if necessary to include this case. This completes the quantitative construction in every dimension n>=2. No bound on N is needed: the quantitative planted weight was determined before the finite convex realization.

## 4. Single-Sample LDA and Tensorization

For any degree-at-most-k polynomial f, replace f by f-f(0). This preserves its variance and its expectation gap, and makes f(0)=0. Do not additionally center it under Q. For R_alpha=(1-alpha)Q+alpha delta_0,

E_Ralpha f-E_Q f=-alpha E_Q f.

Let h(lambda)=E_G f(lambda G), where G~N(0,I_n). It is a univariate polynomial of degree at most k with h(0)=0. All expectations are finite, and total variance gives Var_lambda h<=Var_Q f. The scalar specialization of Section 1 therefore yields

|E_Q f|=|E_lambda h|<=C sqrt(k Var_lambda h)<=C sqrt(k Var_Q f).

This includes the case Var h=0, since then h is identically zero. Consequently the single-sample advantage is at most C alpha sqrt(k).

For completeness, choose an orthonormal basis 1,psi_1,...,psi_J for the finite-dimensional one-sample polynomial space of degree at most k under Q. The inner product is nondegenerate because Q has full support and a nonzero polynomial cannot vanish Q-almost surely. Q and R_alpha have all moments finite. Put mu_j=E_Ralpha psi_j. On centered, variance-one polynomials, Cauchy-Schwarz and its equality case show that the squared one-sample supremum is exactly sum_{j=1}^J mu_j^2.

Products of this basis over m independent samples form an orthonormal basis of the tensor-product space. Every polynomial of total degree at most k belongs to that space, although the tensor-product space is larger. The expectation of a basis product under R_alpha^{otimes m} factors into the product of its one-sample expectations. Removing the all-constant basis element, the squared norm of this expectation functional is

(1+sum_j mu_j^2)^m-1.

Thus the supremum restricted to total degree at most k is at most sqrt((1+C^2 alpha^2 k)^m-1). Since (1+x)^m<=exp(mx), it is bounded by an absolute constant when alpha^2 k m is bounded by a fixed absolute constant.

## 5. Relative-Perturbation Pair Test

Write y_i=x_i+z_i for the observations after independent rerandomization. Define a_i=0 when y_i=0, and a_i=y_i/||y_i|| otherwise. Enumerate unordered pairs and accept the planted hypothesis iff some matrix (a_i,a_j) has smallest singular value at most 1/2. Under the sample-size condition, choosing C>=4 gives m>=2. Hence any zero column ensures acceptance.

### Null soundness

Under the null, rerandomization leaves independent samples from Q. They are nonzero almost surely and their directions u_i=x_i/||x_i|| are independent uniform spherical directions. Conditional on one direction, rotational invariance represents the inner product with an independent direction as g_1/sqrt(g_1^2+H), where g_1 is scalar standard Gaussian and H=sum_{j=2}^n g_j^2 is independent. The event that the absolute inner product exceeds 1/2 implies g_1^2>H/3. Gaussian integration and Markov's inequality with t=1/4 give

P(g_1^2>H/3)<=E exp((g_1^2-H/3)/4)=sqrt(2)(7/6)^{-(n-1)/2}.

Thus the per-pair probability is at most A exp(-b n) for universal A,b>0. A union bound, reducing c>0 and making the bound vacuous for finitely many small dimensions if necessary, gives

P(for all i!=j, |<u_i,u_j>|<=1/2)>=1-m^2 exp(-c n).

On this event, expand the perturbed inner product and use ||x_i+z_i||>=(1-epsilon)||x_i|| and ||z_i||<=epsilon||x_i||. Uniformly over every allowed adversary,

|<a_i,a_j>|<=((1/2)+2epsilon+epsilon^2)/(1-epsilon)^2<=161/225

when epsilon<=1/16. The Gram matrix of a pair has diagonal entries 1 and eigenvalues 1+-|<a_i,a_j>|. Its minimum eigenvalue is at least 64/225, so its smallest singular value is at least 8/15>1/2. The test therefore rejects under the null on this event. This proof uses a fixed threshold, not the source's logarithmic-coherence claim with its erroneous exponential confidence.

### Planted completeness

Let S be the fixed line with D(S)>=alpha, and put theta=alpha(1-p). The number N of retained samples from D belonging to S is binomial with parameter q=(1-p)D(S)>=theta and mean mu=mq>=m theta. For m theta>=4, N<2 implies N<mu/2. For s=log 2, independence and Markov's inequality give

P(N<=mu/2)<=exp(s mu/2)(1-q+q exp(-s))^m<=exp(-(1-log 2)mu/2)<=exp(-mu/8).

Consequently P(N<2)<=exp(-m theta/8).

If N>=2 and a relevant observation is zero, the zero-column rule accepts. Otherwise choose two retained nonzero samples on S. Their unperturbed normalized columns form a matrix M with a unit vector beta satisfying M beta=0. For every nonzero x and ||z||<=epsilon||x||, put y=x+z. The triangle inequality gives ||y||>=(1-epsilon)||x|| and | ||x||-||y|| |<=epsilon||x||. Therefore

||y/||y||-x/||x||||<=||z||/||y||+| ||x||/||y||-1 |<=2epsilon/(1-epsilon).

The estimate includes the absolute value of the change in normalization. Thus for the corresponding corrupted pair matrix A, Cauchy-Schwarz applied to the two coefficients of beta gives

sigma_min(A)<=||A beta||<=2sqrt(2)epsilon/(1-epsilon)<=2sqrt(2)/15<1/2.

The test accepts. Its planted error is therefore at most exp(-c m alpha(1-p)), for a universal c>0 and sufficiently large universal C in the sample-size condition. This is not an exponentially small-in-n error when m alpha(1-p) is merely a fixed constant.

### Complexity and conclusion

There are binomial(m,2)=O(m^2) pair checks. Normalization costs O(nm), and each pair's singular value can be obtained from its 2-by-2 Gram matrix in O(n) arithmetic operations. The complete arithmetic runtime is O(nm^2). Both error estimates hold uniformly over all measurable, arbitrarily correlated perturbations satisfying the relative bounds. Taking the common c no larger than the constants in both error estimates, and taking C large enough for both the LDA and sample-size claims, the success probability under either hypothesis is at least 1-m^2 exp(-c n)-exp(-c m alpha(1-p)). Together with Sections 3 and 4, this proves the integrated theorem without identifying the two distinct planted laws or altering the sampling experiments.
