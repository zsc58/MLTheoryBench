# Reference Proof

## Proof Structure

1. Derive the Gaussian OU lag-pair law and diagonalize its deterministic two-by-two coefficient matrix to obtain an exact difference of independent Gaussian Wisharts.
2. Apply the specialized almost-sure Marchenko-Pastur and Gaussian Wishart asymptotic-freeness results, checking their hypotheses, and compute the R-transform.
3. Derive the Stieltjes cubic, identify its physical analytic branch, recover the absolutely continuous density, and characterize continuous-support boundaries by the discriminant, including degree loss at zero.
4. Determine all atoms, handle zero lag separately, and prove the infinite-lag law and upper-edge limits with the closed-form expression.

## Standard Results Used

The audited standard-independent results in theory_020 are used in the following forms.

- If Y is a d-by-N matrix with independent standard real Gaussian entries and d/N tends to gamma in (0,infinity), the ESD of YY^T/N converges weakly almost surely to the mean-one MP_gamma law. Writing a=(1-sqrt(gamma))^2 and b=(1+sqrt(gamma))^2, its density is sqrt((b-x)(x-a))/(2*pi*gamma*x) on (a,b), and its only atom has mass max(0,1-1/gamma) at zero.
- Two independent Gaussian Wisharts of this type are asymptotically free almost surely. Their fixed real linear combinations have limiting laws given by the corresponding scaled free additive convolution. A free convolution of these compactly supported laws can be realized as the law of the corresponding linear combination of bounded free self-adjoint variables in a faithful tracial probability space.
- R-transforms add under free convolution, satisfy R_{r nu}(w)=rR_nu(rw), and obey R_MP_gamma(w)=1/(1-gamma*w). Near infinity, z=1/G(z)+R(G(z)).
- Stieltjes inversion gives the density almost everywhere by -Im G(x+i0)/pi. An atom at x is the limit of i*eta*G(x+i*eta) as eta decreases to zero.
- The atoms of a free convolution are exactly the sums of input atoms whose masses add to more than one; the resulting mass is the sum minus one.

These are external background results, not paper-specific obligations left unproved.

## Complete Proof

### 1. Exact Gaussian Representation

Fix sigma>0 and tau>0, and put alpha=exp(-tau/2) and beta=sqrt(1-alpha^2). Solving the stationary OU equation gives

X_tau=alpha X_0+sigma*beta*E,

where X_0=sigma*Z and Z,E are independent standard Gaussian vectors. Across the independent pairs and coordinates, the corresponding d-by-N matrices Z,E have jointly independent standard Gaussian entries.

The estimator is therefore

C_hat_tau=(sigma^2/N)[alpha*ZZ^T+(beta/2)(ZE^T+EZ^T)].

The deterministic coefficient matrix acting on the pair (Z,E) is

M=[[alpha,beta/2],[beta/2,0]].

Its characteristic polynomial is r^2-alpha*r-beta^2/4. Since alpha^2+beta^2=1, its eigenvalues are (alpha+1)/2 and (alpha-1)/2. Choose a deterministic orthogonal matrix diagonalizing M and apply it to every pair of entries of Z,E. The resulting matrices U,V still have jointly independent standard Gaussian entries, because their joint covariance remains the identity. On this probability space,

C_hat_tau=c_+*UU^T/N-c_-*VV^T/N,

where c_+=sigma^2(1+alpha)/2 and c_-=sigma^2(1-alpha)/2. This is an exact equality after the rotation, not merely a marginal distributional substitution in an almost-sure argument.

### 2. Almost-Sure Limit and R-Transform

Both coefficients are strictly positive for tau>0. Each matrix UU^T/N and VV^T/N is a Gaussian Wishart, the two are independent, and each is orthogonally invariant: left multiplication of its Gaussian data matrix by any deterministic orthogonal matrix preserves its distribution. Their dimensions satisfy d,N->infinity and d/N->gamma in (0,infinity). Thus all hypotheses of the specialized MP and asymptotic-freeness results above hold. They give almost-sure weak convergence of the estimator's ESD to

mu_tau=(c_+ MP_gamma) boxplus (-c_- MP_gamma).

Scaling and additivity give

R(w)=c_+/(1-c_+*gamma*w)-c_-/(1+c_-*gamma*w).

The free realization also shows that mu_tau is compactly supported: if S,T have laws MP_gamma, then their norms are bounded by (1+sqrt(gamma))^2, and c_+S-c_-T is bounded.

### 3. Cubic and Physical Branch

Write p=c_+c_- and D=c_+-c_-. For the probability-measure Stieltjes transform G,

K(G)=1/G+c_+/(1-c_+*gamma*G)-c_-/(1+c_-*gamma*G)=z.

Multiplication by G(1-c_+*gamma*G)(1+c_-*gamma*G) gives

z*p*gamma^2*G^3+[p*gamma*(2-gamma)+z*D*gamma]*G^2+[D*(1-gamma)-z]*G+1=0.

This is the displayed public cubic. The identity initially holds near infinity and extends throughout the upper half-plane by analyticity. The selected branch is analytic there, has Im G<0, and satisfies zG(z)->1. These properties specify the continuation of the root near infinity; arbitrary pointwise choices of cubic roots are not allowed. The cleared equation does not acquire roots at G=0 or at either denominator pole: substitution into the cleared equation leaves a nonzero term at each of these values.

### 4. Density and Continuous-Support Boundaries

Let

A_3(x)=p*gamma^2*x,
A_2(x)=p*gamma*(2-gamma)+D*gamma*x,
A_1(x)=D*(1-gamma)-x,
A_0=1.

The discriminant is

Delta(x)=18*A_3*A_2*A_1-4*A_2^3+A_2^2*A_1^2-4*A_3*A_1^3-27*A_3^2.

Its degree is exactly four. Indeed, its leading coefficient is

gamma^2*D^2+4*p*gamma^2=gamma^2*(c_++c_-)^2=gamma^2*sigma^4>0.

Away from zero and the finitely many roots of Delta, the cubic has three distinct finite roots. The implicit-function theorem continues each root analytically across a neighborhood of a real point. The physical branch consequently has either a real analytic boundary value or a nonreal analytic boundary value on each such interval. Stieltjes inversion gives

rho_tau(x)=-(1/pi)*Im G(x+i0)

almost everywhere, with positive density on the intervals where the selected boundary value has negative imaginary part. There is no singular continuous component: away from the finite exceptional set, inversion gives an absolutely continuous measure; any remaining measure supported on a finite set consists only of atoms.

At a nonzero endpoint of continuous support, G cannot diverge, because K(g)->0 as g tends to infinity. A simple finite real root would continue as a real analytic branch on both sides and could not bound an interval of nonzero density. Therefore an endpoint must be a multiple root and must satisfy Delta(x)=0.

Zero requires attention because A_3(0)=0. If gamma=2, then A_2(0)=0 as well and Delta(0)=0, so a continuous boundary there is already a discriminant root. If gamma is not 2 and the physical branch stays finite at zero, Delta(0) nonzero would make its finite root simple, ruling out a boundary by the same analytic-continuation argument. Finally, for a divergent branch, expansion at infinity gives

K(g)=(1-2/gamma)/g+D/(p*gamma^2*g^2)+O(g^(-3)).

For gamma<2 such divergence would force a negative atom residue, which a probability measure cannot have. For gamma>2, set m=1-2/gamma>0 and h=1/g. The equation z=m*h+O(h^2) has an analytic inverse near zero. Hence G(z)=m/z plus a real-coefficient analytic remainder. Its boundary values are real on a punctured neighborhood of zero, so zero is an isolated atom rather than a boundary of continuous support.

Thus every continuous-support boundary is a real root of Delta. Conversely, a discriminant root is retained as a boundary only when the physical branch identifies a neighboring interval of density and a neighboring interval without continuous support; roots on other branches or interior degeneracies need not be boundaries. This characterizes the continuous support without presuming that it always has one interval. The upper edge lambda_+(tau) is its largest boundary root. The atom at zero, when present, is not included in this discriminant boundary assertion.

### 5. Atoms and Density Mass

The two scaled MP factors have no atoms except possibly at zero, each of mass q=max(0,1-1/gamma). Positive nonzero scaling and reflection preserve these masses. The exact free-convolution atom rule therefore gives no atoms except possibly at zero, whose mass is

max(0,2*q-1)=max(0,1-2/gamma).

Together with the absence of singular continuous mass proved above, this shows that rho_tau is the density of the unnormalized absolutely continuous part and has total mass min(1,2/gamma). Its almost-everywhere inversion formula does not assign the zero atom to the density.

### 6. Zero Lag

At tau=0 the two observations in each pair coincide. The estimator becomes sigma^2*ZZ^T/N, so its ESD converges weakly almost surely to sigma^2 MP_gamma. Its zero atom has mass max(0,1-1/gamma), and its upper continuous edge is sigma^2(1+sqrt(gamma))^2. Substituting c_-=0 into the cubic yields the MP quadratic

gamma*sigma^2*z*G^2+[sigma^2*(1-gamma)-z]*G+1=0.

No positive-lag atom formula is applied at this degenerate endpoint.

### 7. Infinite-Lag Law and Edge Convergence

The proportional limit has already been taken, with sigma and gamma fixed. In a common faithful tracial realization let S,T be bounded free positive self-adjoint variables with laws MP_gamma. Set

A_tau=c_+(tau)*S-c_-(tau)*T,
A_infinity=c*(S-T), where c=sigma^2/2.

As tau->infinity, both coefficients tend to c and

||A_tau-A_infinity|| <= |c_+(tau)-c|*||S||+|c_-(tau)-c|*||T|| -> 0.

Polynomial moments and then continuous test functions on the common compact spectral bound converge, proving

mu_tau => (c MP_gamma) boxplus (-c MP_gamma).

The limiting law is symmetric, since exchanging the identically distributed free variables S,T reflects A_infinity. Its zero atom remains max(0,1-2/gamma).

In a faithful tracial realization, the support of a self-adjoint variable's law equals its spectrum: a nonzero nonnegative continuous function of the variable has strictly positive trace. For bounded self-adjoint operators, the maximum spectral value changes by at most the operator-norm perturbation. Therefore the upper support edges also converge. The upper edge is positive because the limiting variables have positive variance, and, for finite lag, the mean is sigma^2*alpha>0. It is not the isolated zero atom.

### 8. Closed-Form Infinite-Lag Upper Edge

For the symmetric limiting law,

K(g)=1/g+2*c^2*gamma*g/(1-c^2*gamma^2*g^2).

The real outer branch begins at g=0+ when z is large positive and continues on 0<g<1/(c*gamma). Its first critical point gives the upper edge. Put u=c*gamma*g and t=u^2. Then

K(g)=c*[gamma/u+2*u/(1-u^2)],

and the critical equation is

2*t*(1+t)=gamma*(1-t)^2.

The function 2*t*(1+t)/(1-t)^2 increases strictly from zero to infinity on (0,1), with derivative 2*(1+3*t)/(1-t)^3. Thus the outer critical point is unique and belongs to (0,1), for every gamma>0, including gamma=2.

Writing s=sqrt(1+4*gamma), its solution is

t=(s-1)/(s+3).

For gamma not 2 this is equivalent to [sqrt(1+4*gamma)-(1+gamma)]/(2-gamma); the nonsingular expression above gives t=1/3 at gamma=2. Substitution yields

lambda_+(infinity)=c*[gamma/sqrt(t)+2*sqrt(t)/(1-t)]
                 =(sigma^2/8)*(s+3)^(3/2)*sqrt(s-1).

The uniqueness of the critical point shows that it is the endpoint reached by the outer physical branch, not an unselected discriminant root. Combined with the preceding norm-continuity argument, this proves both the infinite-lag law and upper-edge limits.

## Obligation Closure

The exact coefficients and independence are derived in Section 1. Almost-sure proportional convergence is supplied by the audited Gaussian results with hypotheses checked in Section 2. Sections 3-4 establish the physical cubic, density, quartic degree, and continuous-boundary interpretation, including zero. Section 5 closes the atomic and continuous-mass assertions. Section 6 handles zero lag. Sections 7-8 prove infinite-lag law and edge convergence and derive the closed form. No theorem-critical obligation remains unresolved.
