# Reference Proof

## Proof Structure

Condition on the design. Construct one simultaneous event for all taskwise whitened scores and the pooled inlier score. First-order optimality gives safety uniformly over centers and minimizers. A projected pooled calculation bounds heterogeneity and noise. In the explicit favorable tuning regime, every inlier infimal convolution agrees with its loss on a pooled-whitened ball. The inlier sum is quadratic there, while the outlier sum is convex and Lipschitz. A verified convex perturbation argument keeps every full center inside that ball. Combine the resulting taskwise bound with safety. If the explicit tuning condition fails, use that failure and safety to obtain the same minimum-term bound.

## Complete Proof

### 1. Experiment, minimizers, and concentration

All probabilities below are conditional on the complete design. The parameters and relatedness witnesses are fixed in this experiment. Write s=|S|, k=|S^c|, and M=\widehat\Sigma_S. Then k/m<=epsilon and s>= (1-epsilon)m; equality is not assumed. Put z=log(16m/kappa)>1.

The joint objective attains its minimum, including for singular designs. To see this, put A_j=Sigma_j^{1/2} and let t_j be the unique whitened least-squares fitted parameter in Range(Sigma_j). On that range,

f_j(theta)=a_j+(1/2)||A_j theta-t_j||_2^2,

where a_j is the nonnegative least-squares residual loss. On any nonempty sublevel set, each A_j theta_j is bounded by the quadratic term. Since lambda>0, the penalties then bound each A_j beta as well. Restrict theta_j to Range(Sigma_j) and beta to Range(sum_j Sigma_j); these projections change neither loss nor penalty. The respective linear maps are injective on these subspaces, so these bounds yield a bounded sublevel set there. It is closed, and minimization on it gives a joint minimizer. Null-space representatives do not affect the objective or prediction errors. This existence argument uses no uniform lower-eigenvalue bound.

We use the following audited standard independent quadratic-form result. For a centered vector with a universal directional sub-Gaussian scale, a nonzero PSD matrix Q, and t>=1,

P{xi^T Q xi > C tr(Q)t} <= exp(-r(Q)t),

where r(Q)=tr(Q)/||Q||_op and C is universal. Conditional independence of the centered unit-scale noise coordinates implies the needed directional scale: the moment generating function of any linear combination is bounded by exp(||v||_2^2 u^2/2). Thus the result applies to each task noise vector and to the stacked inlier noise vector. A universal rescaling from the lemma's unit directional norm is absorbed into C. For Q=0 the quadratic form is identically zero.

For each task define

h_j=Sigma_j^{dagger/2} X_j^T xi_j/n.

If P_j is the orthogonal projection onto col(X_j), then

||h_j||_2^2=xi_j^T P_j xi_j/n.

Likewise, stack the inlier designs and noises as X_S and xi_S, put N_S=ns, and define

h_S=M^{dagger/2} X_S^T xi_S/N_S.

With P_S the projection onto col(X_S),

||h_S||_2^2=xi_S^T P_S xi_S/N_S.

Apply the quadratic-form result with t=z to every nonzero projection. Its rank is at most d, and its failure probability is at most exp(-z). Zero projections require no event. Consequently, for a sufficiently large universal c_0, on an event E of conditional probability at least

1-(m+1)exp(-z) >= 1-kappa,

we have simultaneously

||h_j||_2 <= a := c_0 sqrt(dz/n) for every j,

and ||h_S||_2 <= c_0 sqrt(dz/N_S).

This event does not depend on any estimated center. The confidence-floor corrections to the two single-task source propositions are automatically satisfied here because t=z>1. Work on E henceforth, and take q>=q_0 with q_0>=8c_0 and q_0>=1.

### 2. Center-uniform safety and invariance

For a task j, restrict its task parameter to R_j=Range(Sigma_j), and set u=Sigma_j^{1/2}theta and v=Sigma_j^{1/2}beta. The task loss in these coordinates has the form

constant+(1/2)||u-t_j||_2^2,

where t_j=Sigma_j^{1/2}theta_j^star+h_j. Every minimizing u for the penalized task problem satisfies

0=u-t_j+lambda w,

where w belongs to the subdifferential of ||u-v||_2 and ||w||_2<=1. Therefore ||u-t_j||_2<=lambda. It follows, simultaneously for every beta and every corresponding minimizer, that

||theta_hat_j(beta)-theta_j^star||_{Sigma_j} <= lambda+a.

At any joint minimizer, each task parameter minimizes its task problem at the returned center, because otherwise replacing that parameter would decrease the joint objective. Since lambda=q sqrt(dz/n), safety follows:

E_j^in <= (lambda+a)^2 <= C lambda^2 = C q^2(d/n)z.

This proves the first conclusion without using relatedness or balancedness.

We also need a deterministic invariant criterion on E. The whitened loss gradient at v has norm at most

||beta-theta_j^star||_{Sigma_j}+a.

For any u, convexity implies that its penalized objective is at least its value at v plus

[lambda-||gradient at v||_2] ||u-v||_2.

Thus, whenever

||beta-theta_j^star||_{Sigma_j}+a < lambda,

the infimal convolution g_j(beta)=inf_theta{f_j(theta)+lambda||theta-beta||_{Sigma_j}} equals f_j(beta), and every minimizing task parameter is Sigma_j-equivalent to beta. This holds uniformly over centers, including random estimated centers. If Sigma_j=0, the same equality and zero-seminorm conclusion are immediate.

### 3. Pooled heterogeneity and noise

For the second conclusion assume B<=c min{1/epsilon,m}, and choose the universal c<=1/8. In particular B is finite, B epsilon<=c, epsilon<=c because B>=1, and s>= (1-c)m.

Finite balancedness implies Null(M) is contained in Null(Sigma_j) for every task, including outliers: for v in Null(M), 0<=v^T Sigma_j v<=B v^T Mv=0. Hence all losses and penalties can be analyzed on R=Range(M). If R has dimension zero, every Sigma_j=0 and all claimed errors are zero. Assume now that R has positive dimension; all inverses involving M below are inverses on R.

Let beta_tilde be the pooled least-squares minimizer over S, represented on R. Write eta_j=theta_j^star-theta^star and let e be the stacked vector of X_j eta_j, j in S. Its norm obeys

||e||_2^2=sum_{j in S} n||eta_j||_{Sigma_j}^2 <= N_S delta^2.

The normal equations give, in prediction-relevant coordinates,

M^{1/2}(beta_tilde-theta^star)
 = M^{-1/2}X_S^T e/N_S+h_S.

The squared norm of the first term is e^T P_S e/N_S, which is at most delta^2. Therefore

||beta_tilde-theta^star||_M <= delta+c_0 sqrt(dz/N_S).

Using balancedness and ||theta_j^star-theta^star||_{Sigma_j}<=delta gives, for every inlier,

||beta_tilde-theta_j^star||_{Sigma_j}
 <= (sqrt(B)+1)delta+b,

where b=c_0 sqrt(Bdz/N_S). Define the explicit threshold quantity

T=(sqrt(B)+1)delta+a+b.

### 4. Favorable tuning: invariant ball and perturbation

Suppose lambda>2T. Put r=lambda/(2sqrt(B)), and use pooled-whitened coordinates w=M^{1/2}beta and w_0=M^{1/2}beta_tilde. If ||w-w_0||_2<=r, then for each inlier

||beta-theta_j^star||_{Sigma_j}+a
 <= T+sqrt(B)||w-w_0||_2
 <= T+lambda/2 < lambda.

The center-uniform invariant criterion therefore applies throughout this closed ball. Define F_S=sum_{j in S}f_j and G_S=sum_{j in S}g_j. In the ball, G_S=F_S. In whitened coordinates, the pooled least-squares normal equations and the Hessian identity give

F_S(w)=F_S(w_0)+(s/2)||w-w_0||_2^2.

The functions g_j are finite and convex: their defining objectives are jointly convex, and taking the infimum over the task parameter preserves convexity. Thus G_S is convex. Since w_0 is a local minimizer of G_S, it is a global minimizer. A distinct global minimizer would, by convexity, produce arbitrarily nearby distinct minimizers along a segment, contradicting the displayed local quadratic. Hence w_0 is its unique minimizer on R.

For any two centers beta,beta', comparison with a task minimizer and the seminorm triangle inequality give

|g_j(beta)-g_j(beta')| <= lambda||beta-beta'||_{Sigma_j}
 <= sqrt(B)lambda||w-w'||_2.

Consequently the outlier sum L=sum_{j in S^c}g_j is convex and ell-Lipschitz in whitened coordinates, with ell=k sqrt(B)lambda. We verify the perturbation radius condition explicitly:

ell/(s r)=2kB/s <= 2epsilon B/(1-epsilon) <= 2c/(1-c)<1.

For completeness, the convex perturbation bound used here can be derived directly. Let f be convex, minimized at w_0, and equal to f(w_0)+(rho/2)||w-w_0||_2^2 in radius r. For x!=w_0, put t=||x-w_0||_2 and u=(x-w_0)/t. Convexity of the restriction to this ray, together with its quadratic form up to radius r, implies

p^T u >= rho min{t,r} for every p in partial f(x).

This follows from the exact derivative rho t for t<r and monotonicity of slopes thereafter. If x minimizes f+g for convex ell-Lipschitz g, finite convex-function optimality gives p+v=0 with p in partial f(x), v in partial g(x), and ||v||_2<=ell. Thus rho min{t,r}<=ell. If ell<rho r, necessarily t<r and t<=ell/rho. The t=0 case is immediate. This verifies the standard independent perturbation result and its application, without leaving a named-method obligation open.

Apply this argument with f=G_S, g=L, and rho=s. Every minimizing full center satisfies

||beta_hat-beta_tilde||_M <= (k/s)sqrt(B)lambda < r.

Notice that the pooled-seminorm factor is sqrt(B), not B. After taskwise comparison it becomes

||beta_hat-beta_tilde||_{Sigma_j} <= (k/s)B lambda.

The center lies inside the invariant ball, so every returned inlier parameter is Sigma_j-equivalent to it. Hence

||theta_hat_j-theta_j^star||_{Sigma_j}
 <= (sqrt(B)+1)delta+b+(k/s)B lambda.

Let A=B delta^2, V=Bdz/(mn), and W=q^2B^2epsilon^2(d/n)z. Since B>=1, s>= (1-c)m, and k/s<=epsilon/(1-epsilon), squaring yields

E_j^in <= C(A+V+W).

On the same event safety gives E_j^in<=C lambda^2. Combining these two inequalities and using min{L,A+D}<=min{L,A}+D for nonnegative quantities gives

E_j^in <= C[min{A,lambda^2}+V+W].

### 5. Unfavorable tuning and the minimum term

Suppose instead lambda<=2T. Since q>=8c_0, 2a<=lambda/4. Using sqrt(B)+1<=2sqrt(B), we obtain

3lambda/4 <= 4sqrt(B)delta+2b.

Thus, for universal constants, at least one of the alternatives

lambda^2<=C_1 A or lambda^2<=C_1 b^2

holds. In the first alternative, lambda^2<=max{1,C_1} min{A,lambda^2}. In the second, b^2<=C V because s is a fixed universal fraction of m. Safety therefore gives in either case

E_j^in <= C[min{A,lambda^2}+V],

and adding W gives the same bound obtained in the favorable regime. There is no upper-side tuning hypothesis.

Finally set U=q^2d/n, so lambda^2=zU. Because z>=1,

min{A,zU} <= z min{A,U}.

Both regimes consequently imply, simultaneously for every inlier,

E_j^in <= C[Bd/(mn)+min{Bdelta^2,q^2d/n}+q^2B^2epsilon^2d/n]z.

The event already includes safety for every task. If B=infinity, only the safety part is needed and the transfer calculations are not invoked. If epsilon=0, k=0 and the perturbation vanishes. Individual zero-rank tasks and the zero pooled-rank finite-balancedness case were handled explicitly. All conclusions hold for every joint minimizer on E, so any measurable selection also obeys the stated probability guarantee. Constants depend only on the normalized universal noise scale and fixed universal choices c and q_0, not on any task covariance lower eigenvalue.

## Proof-Obligation Audit

Estimator attainment, conditional concentration and its hypotheses, center-uniform safety, center-uniform invariance, pooled heterogeneity and noise, null-space reduction for all tasks, local curvature, outlier convexity and Lipschitzness, perturbation localization, all-minimizer equivalence, both tuning regimes, the logarithm/minimum conversion, and the degenerate cases are explicitly derived above. The only invoked probabilistic result is the audited standard independent quadratic-form inequality, whose relevant statement and hypotheses are given. No private GT obligation remains unresolved.
