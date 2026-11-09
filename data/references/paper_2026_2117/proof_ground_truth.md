# Reference Proof

## Proof Structure

1. Establish orthogonal/diagonal equality of Gaussian KL and the exact diagonal-family decomposition.
2. Justify convergence of expected spectral losses and of the normalized decomposition using MP convergence and elementary Gaussian moment bounds.
3. Differentiate the limiting objective and classify every interior stationary point.
4. Compare the boundaries, prove existence and uniqueness of the collapse threshold, and establish all three phases.

## 1. Finite-sample loss and diagonal reformulation

Fix alpha in (0,1) and epsilon in (0,1). Write k=N_K, S=X^T X/D, and let lambda_1>=...>=lambda_n be its eigenvalues. All calculations below concern sufficiently large dimensions; n/D→alpha implies D>n+3 eventually.

Direct substitution of Gaussian densities gives

2 D_KL(N(0,Sigma_0)||N(0,Sigma_1)) = tr(Sigma_1^{-1}Sigma_0)-n+log(det Sigma_1/det Sigma_0).

For Sigma_0=I_n this expression is invariant under orthogonal conjugation of Sigma_1. Thus the trained eigenbasis model and the fixed-basis diagonal model with variances lambda_1,...,lambda_k,epsilon,...,epsilon have identical KL for every dataset, and hence identical expected KL.

Set f(x)=x^{-1}+log x and A(x)=f(x)-1. The exact loss is

2 D_KL(P||Q) = sum_{i=1}^k A(lambda_i)+(n-k)A(epsilon).

For completeness, the source's decomposition also applies directly to the diagonal family. Its natural coordinates are theta_i=-1/(2d_i), and the last n-k coordinates are fixed, so its constraints are affine. Minimizing Gaussian KL over this family gives retained variances one and discarded variances epsilon. This is its m-projection Q^0.

Let m_i=E[lambda_i^{-1}] for i<=k. Averaging log Gaussian densities shows that the e-mixture has retained variances h_i=m_i^{-1} and discarded variances epsilon. The three components are therefore

2 ME = (n-k)A(epsilon),

2 DataBias = sum_{i=1}^k (m_i-1-log m_i),

2 Variance = sum_{i=1}^k (log m_i+E log lambda_i).

For the last formula, E[h_i/lambda_i]=1 cancels the trace and dimension terms. Adding these formulas gives exactly the expected loss above. Each component is nonnegative: the first two are Gaussian KL divergences, and the last is the expected Gaussian KL from the e-mixture to the diagonal trained model. Equivalently, the e-mixture identity follows by averaging log densities, and the Pythagorean split holds here because P and Q^0 agree in the free coordinates while Q^0 and every family member agree in the pinned coordinates. Thus no unproved paper-specific decomposition is needed.

## 2. Expected MP limit and normalized component limits

Weak MP convergence alone would not justify averaging the inverse-eigenvalue loss. We supply the necessary tail control from the sampling model.

Elementary Gaussian fourth moments give

E[(1/n)tr S^2] = 1+(n+1)/D.

Indeed, writing the independent observation rows as x_d, the diagonal terms in tr(X^T X)^2 have expectation E||x_d||^4=n(n+2), and the D(D-1) off-diagonal terms have expectation E(x_d^T x_e)^2=n.

We also derive an inverse second-moment bound. Put W=X^T X and partition X=[x,Y], where x is the first column. Let B=Y^T Y, P_Y=YB^{-1}Y^T, t=x^T(I-P_Y)x, and v=B^{-1}Y^T x. Block inversion gives

(W^{-2})_{11}=t^{-2}(1+||v||^2).

Conditionally on Y, the Gaussian projections P_Y x and (I-P_Y)x are independent. The variable t is the sum of squares of D-n+1 independent standard Gaussians, its conditional distribution does not depend on Y, and E[||v||^2|Y]=tr B^{-1}. Integrating the density proportional to t^{nu/2-1}e^{-t/2} gives E[t^{-1}]=1/(nu-2) and E[t^{-2}]=1/[(nu-2)(nu-4)]. Applying the same diagonal Schur-complement identity to B, whose dimension is n-1, gives E tr B^{-1}=(n-1)/(D-n). Consequently, symmetry of the columns yields

E[(1/n)tr S^{-2}] = D^2(D-1)/[(D-n)(D-n-1)(D-n-3)].

Both displayed spectral moment bounds are uniformly bounded along the prescribed limit.

Put a=lambda_- and b=lambda_+, and let q(s), 0<s<1, be the decreasing quantile function of the supplied MP density. Thus integral_{q(s)}^b rho(lambda)d lambda=s, and a<=q(s)<=b. Let q_n(s)=lambda_i for (i-1)/n<s<=i/n.

The supplied MP convergence, with the continuous strictly increasing distribution function on its support, implies convergence in probability of q_n(s) to q(s) for every s in (0,1). On any fixed compact interval bounded away from zero, boundedness and continuity therefore give convergence in expected integrated absolute difference after clipping. The preceding second-moment bounds remove the clipping: for example,

E integral q_n(s)^{-1} 1_{q_n(s)<delta} ds <= delta E integral q_n(s)^{-2} ds,

and

E integral q_n(s) 1_{q_n(s)>R} ds <= R^{-1} E integral q_n(s)^2 ds.

For logarithms, the ratios |log x|/x^{-2} as x→0 and log x/x^2 as x→infinity tend to zero, so the same bounds control both logarithmic tails. It follows that

E integral_0^1 |q_n-q| ds → 0,

E integral_0^1 |q_n^{-1}-q^{-1}| ds → 0,

E integral_0^1 |log q_n-log q| ds → 0.

In particular, E integral_0^1 |A(q_n)-A(q)| ds→0. For any deterministic k/n→r, integration over (0,k/n) now proves convergence of the expected retained sum. If c is the unique cutoff with r=integral_c^b rho, the limiting objective is

2 G_epsilon(r) = (1-r)A(epsilon)+integral_c^b A(lambda)rho(lambda)d lambda.  (1)

This also proves existence and independence of the deterministic rank sequence, including r=0 and r=1. The objective is continuous on [0,1].

To justify the decomposition route as well, define m_n(s)=E[q_n(s)^{-1}]. The preceding L1 convergence implies m_n→q^{-1} in L1(0,1). Jensen's inequality gives

integral m_n^2 <= E integral q_n^{-2},

and, since m_n>=1/E[q_n],

integral m_n^{-2} <= integral (E q_n)^2 <= E integral q_n^2.

Thus the logarithms log m_n are uniformly integrable; convergence in measure and truncation give log m_n→-log q in L1. Applying these facts to the exact component formulas proves

ME/n → (1-r)A(epsilon)/2,

DataBias/n → (1/2)integral_c^b A(lambda)rho(lambda)d lambda,

Variance/n → 0.

Only normalized variance disappearance is required. The proof does not infer disappearance of an unnormalized quantity merely from a deterministic limiting empirical measure.

## 3. Interior stationary points

For c in (a,b), dr/dc=-rho(c)<0. Differentiating (1) gives

d(2G_epsilon)/dr = f(c)-f(epsilon).  (2)

The exact derivative f'(x)=(x-1)/x^2 shows that f decreases strictly on (0,1) and increases strictly on (1,infinity). Its unique minimum is f(1)=1, and it tends to infinity at both ends of the positive half-line. It is not globally convex; no such assertion is needed.

For a<epsilon<1, the equation f(c)=f(epsilon) has exactly two positive solutions: c=epsilon and one value c'>1. The second solution is a stationary cutoff only if it belongs to (a,b). Differentiating again at an interior cutoff gives

d^2(2G_epsilon)/dr^2 = -f'(c)/rho(c).

At c=epsilon this is (1-epsilon)/(epsilon^2 rho(epsilon))>0. At c'>1 it is negative when that root is in the interior of the support. Thus c=epsilon is the unique interior local minimum and its rank ratio is

r_epsilon=integral_epsilon^b rho(lambda)d lambda.

## 4. Endpoint comparison and retain-all

A spectral value being larger than epsilon does not by itself imply that retaining it lowers KL. We therefore prove the required endpoint comparison.

Write x=sqrt(alpha), so a=(1-x)^2 and b=(1+x)^2. Direct calculation gives

h(x):=f(a)-f(b)=4x/(1-x^2)^2-2log((1+x)/(1-x)).

Its continuous extension has h(0)=0, and

h'(x)=4x^2(5-x^2)/(1-x^2)^3>0 for 0<x<1.

Hence f(a)>f(b). Since a<1<b and f decreases before one and increases after one, its maximum on [a,b] is attained at an endpoint, and therefore at a. In fact f(c)<f(a) for every c in (a,b).

If 0<epsilon<=a, monotonicity below one gives f(epsilon)>=f(a). Equation (2) is consequently strictly negative for every r in (0,1). By continuity, r=1 is the unique global minimizer, including epsilon=a.

## 5. Interior versus collapse

Suppose a<epsilon<1. The only possible global minimizers are r=0, r=r_epsilon, and r=1: the only other possible interior stationary point is a strict local maximum. Moreover,

2[G_epsilon(1)-G_epsilon(r_epsilon)] = integral_a^epsilon [f(lambda)-f(epsilon)]rho(lambda)d lambda > 0,

because f is strictly decreasing below one. Thus retain-all cannot be globally optimal in this range.

Subtracting the collapse value from the interior value gives

Delta_alpha(epsilon):=2[G_epsilon(r_epsilon)-G_epsilon(0)]

= integral_epsilon^b [f(lambda)-f(epsilon)]rho(lambda)d lambda.

This expression is continuous for epsilon in [a,1]. Its derivative on (a,1) is

Delta_alpha'(epsilon)=-f'(epsilon)r_epsilon=(1-epsilon)r_epsilon/epsilon^2>0;

the moving-endpoint contribution is zero. At epsilon=a the integrand is strictly negative throughout (a,b), by the endpoint comparison, so Delta_alpha(a)<0. At epsilon=1,

Delta_alpha(1)=integral_1^b [f(lambda)-f(1)]rho(lambda)d lambda>0.

The intermediate value theorem and strict monotonicity give a unique epsilon_*(alpha) in (a,1) with Delta_alpha(epsilon_*)=0. Below it the interior candidate is the unique global minimizer; above it collapse is the unique global minimizer. At equality the interior and collapse choices both minimize, and no other rank ratio does. Combining this comparison with the retain-all case establishes all three stated phases.

The initial orthogonal-invariance identity transfers the entire analysis from the diagonal representation to the specified eigenbasis estimator.

## Audit Closure

The theorem-critical obligations are all closed: finite-sample Gaussian KL and orthogonal equivalence; the exact diagonal decomposition; convergence of expected spectral losses including the endpoints; normalized variance disappearance when using that decomposition; classification of all interior critical points; the support-endpoint inequality; exclusion of retain-all in the interior regime; and existence, uniqueness, and equality behavior of the collapse threshold. The only external spectral input is the supplied MP convergence for the stated independent Gaussian sample covariance.
