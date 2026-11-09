# Reference Proof

## Proof Structure

First derive the finite-grid expectation inequality for nonincreasing functions. Construct a positive strictly decreasing function satisfying the required normalization by expressing its values on the grid augmented by alpha through positive successive decrements. Prove and apply the elementary positive orthogonal-vector lemma, then interpolate. Next analyze the logistic family: its finite-grid mean is continuous in the positive scale parameter and crosses one. Finally verify positivity, smooth strict decrease, invertibility onto the image, exactness, set preservation, and domination of the all-or-nothing map.

All parameters are fixed when their associated maps are constructed. In particular, the logistic scale may depend on n, alpha, and the fixed s, but not on a realized p-value. Exactness is required for the uniform null variable P_n; the guarantee for other grid p-variables is an expectation at most one. No claim of validity for arbitrary nongrid p-variables is used.

## Complete Proof

### 1. Finite-grid validity

Put N=n+1 and G_N={k/N:1<=k<=N}. The setup supplies the uniform null law of P_n on G_N. All probabilities and expectations below refer to the relevant null law.

Let P be any grid p-variable, and let g be a finite-valued, nonnegative, nonincreasing function on G_N. Write a_k=g(k/N) and H_k=Pr(P<=k/N). Pointwise,

g(P)=a_N+sum_{k=1}^{N-1}(a_k-a_{k+1}) 1{P<=k/N}.

Taking expectations, using a_k-a_{k+1}>=0 and H_k<=k/N, and telescoping gives

E[g(P)]
= a_N+sum_{k=1}^{N-1}(a_k-a_{k+1})H_k
<= a_N+sum_{k=1}^{N-1}(a_k-a_{k+1})k/N
= (1/N)sum_{k=1}^N a_k.

Equality holds when P=P_n because then H_k=k/N. Consequently, a finite nonnegative nonincreasing map with grid average one is a grid p-to-e calibrator and is exact for P_n.

### 2. General existence

Let j=floor(alpha N). The hypotheses imply 1<=j<=N-1 and

j/N<alpha<(j+1)/N.

Use exactly the ordered augmented grid G_N union {alpha}, without adding 0 yet. It has M=N+1 points z_1<...<z_M, where

z_i=i/N for 1<=i<=j,
z_{j+1}=alpha,
z_i=(i-1)/N for j+2<=i<=N+1.

Write q=j+1, so z_q=alpha and z_M=1. For positive decrements d_1,...,d_{M-1} and a positive endpoint value b, set

u_i=b+sum_{r=i}^{M-1}d_r,  1<=i<=M,

where an empty sum is zero. Then u_1>...>u_M=b>0.

For 1<=r<=M-1 let m_r be the number of points of G_N not exceeding z_r. Substituting f(z_i)=u_i into the required normalization equation gives the homogeneous equation

(1-alpha)b+sum_{r=1}^{M-1}[m_r/N-alpha 1{r>=q}]d_r=0.

Indeed, every grid value contains b, and d_r contributes to precisely the m_r grid values whose nodes do not exceed z_r. The value at alpha contains d_r precisely when r>=q.

For r<q, m_r=r and the coefficient of d_r is r/N>0. At r=q, the coefficient is j/N-alpha<0. For r>q, m_r=r-1 and the coefficient is (r-1)/N-alpha>0. The coefficient of b is 1-alpha>0. Thus the coefficient vector has both a positive and a negative coordinate. This remains true when j=N-1, in which case the range r>q is empty.

We now prove the elementary fact needed to solve this equation with all coordinates positive. Let a real vector v have at least one positive and one negative coordinate. Choose any vector x^(0) with every coordinate positive and put h=v dot x^(0). If h=0, use x=x^(0). If h>0, choose an index i with v_i<0 and increase x_i^(0) by h/(-v_i). This increase is positive and changes the dot product by -h. If h<0, choose an index i with v_i>0 and increase x_i^(0) by (-h)/v_i. Again every coordinate remains positive and the new dot product is zero. This proves the positive orthogonal-vector lemma rather than assuming it as an internal dependency.

Apply this fact to the coefficient vector of (b,d_1,...,d_{M-1}). It supplies strictly positive b and d_r satisfying the normalization equation. Choose any u_0>u_1 at z_0=0, and define f by linear interpolation through (z_i,u_i), 0<=i<=M. Each segment has strictly negative slope and positive endpoint values. Hence f is finite, continuous, positive, and strictly decreasing on [0,1]. Its values at G_N and alpha satisfy

(1/N)sum_{k=1}^N f(k/N)=alpha f(alpha).

Since alpha f(alpha)>0, the map

F_f(p)=f(p)/(alpha f(alpha))

is finite, positive, and strictly decreasing, and its grid average equals one. Section 1 therefore proves its grid-calibrator validity and exactness for P_n.

Furthermore, F_f(alpha)=1/alpha. Strict decrease gives, for every p in [0,1],

p>alpha if and only if F_f(p)<1/alpha.

Applying this pointwise identity to any conformal p-value proves set preservation.

### 3. Logistic normalization

Fix an arbitrary s satisfying

alpha<s<ceil(alpha N)/N=(j+1)/N.

For C>0 define

L_C(p)=alpha^{-1}[1+exp(C(alpha-s))]/[1+exp(C(p-s))],  p in [0,1],

and set

Sigma(C)=(1/N)sum_{k=1}^N L_C(k/N).

Every denominator is positive, so Sigma is a finite continuous function on (0,infinity). As C tends to zero from above, every term L_C(k/N) tends to 1/alpha. Therefore

lim_{C->0+} Sigma(C)=1/alpha>1.

Since alpha-s<0, the numerator factor 1+exp(C(alpha-s)) tends to one as C tends to infinity. Exactly j grid points lie below s and no grid point equals s. The reciprocal denominator tends to one at those j points and to zero at the remaining points. Thus

lim_{C->infinity} Sigma(C)=j/(alpha N)<1.

Choose finite numbers 0<C_-<C_+ with Sigma(C_-)>1 and Sigma(C_+)<1, which is possible by these strict limits. The standard intermediate value theorem states that a continuous real function on a closed interval takes every value between its endpoint values. Sigma is continuous on [C_-,C_+], and one lies strictly between its endpoint values. Hence there is C in (C_-,C_+) with Sigma(C)=1.

Denote one such choice by C_{n,alpha,s} and set F_{n,alpha,s}=L_{C_{n,alpha,s}}. This proves existence for every fixed admissible s; neither uniqueness nor a choice independent of s is asserted.

### 4. Calibrator properties and set preservation

For the chosen positive scale C=C_{n,alpha,s}, the formula for L_C extends smoothly to every real p and is strictly positive. Differentiation gives

L_C'(p)=-alpha^{-1}[1+exp(C(alpha-s))] C exp(C(p-s))/[1+exp(C(p-s))]^2<0.

Thus F_{n,alpha,s} is smooth, finite, positive, and strictly decreasing on [0,1]. Its grid average is one by construction. Section 1 proves that it is a grid p-to-e calibrator and is exact for P_n.

At p=alpha its value is 1/alpha. Strict decrease therefore gives the pointwise equivalence

p>alpha if and only if F_{n,alpha,s}(p)<1/alpha,

including the correct exclusion at equality p=alpha. This proves set preservation for every conformal construction in the setup.

To verify invertibility with its domain specified, put A=1+exp(C(alpha-s)). The image is the interval [L_C(1),L_C(0)], and for y in this interval the inverse is

p=s+C^{-1}log(A/(alpha y)-1).

The logarithm is defined throughout the image: its argument ranges between exp(-Cs) and exp(C(1-s)), both strictly positive. Substitution verifies the inverse, including the two endpoints. This is invertibility onto the image, not surjectivity onto all nonnegative real numbers.

The logistic construction can also serve as a complete alternative proof of general existence. Namely, take f=L_C after Sigma(C)=1 has been established. Then f is positive and strictly decreasing, its grid average is one, and alpha f(alpha)=1. It therefore satisfies the first target's normalization equation, and its normalized map equals L_C. A separate augmented-grid construction is not logically necessary for an answer that proves these facts through the logistic family.

### 5. Domination

If p<=alpha, then exp(C(p-s))<=exp(C(alpha-s)), so

F_{n,alpha,s}(p)>=1/alpha=F_AoN(p).

If p>alpha, then F_AoN(p)=0 while F_{n,alpha,s}(p)>0. Thus domination holds for every p in [0,1], including p=0, p=alpha, and p=1.

## Obligation Closure

The uniform null law is an explicit setup premise. The finite-grid validity inequality is derived directly; the positive orthogonal-vector lemma is proved; the interpolation and coefficient signs are verified, including empty index ranges; and logistic normalization follows from the explicitly stated intermediate value theorem with its hypotheses checked. Positivity, smooth strict decrease, exactness, the inverse's domain, threshold preservation, and pointwise domination are all established explicitly. No unresolved paper-specific or external proof dependency remains.
