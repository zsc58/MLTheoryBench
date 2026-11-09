# Reference Proof

## Proof Structure and Obligations

1. Establish the scalar mass-ratio inequality, retaining the singular component.
2. Derive the quantitative relative-error estimate and verify the scalar sublevel properties used in the directional conclusions. The quantitative estimate is supporting material, not an additional public target.
3. Under the strict q||p condition, obtain uniform two-sided small-ball comparability and transfer both gauge classes.
4. Under the finite p||q condition, obtain uniform one-sided comparison and transfer the appropriate gauge classes, including empty and unbounded cases.

## Complete Proof

Fix 0<alpha<1 and write k=alpha/(1-alpha). The generator is continuous on [0,infinity), and for u>0,

f'_alpha(u)=k(1-u^(alpha-1)),   f''_alpha(u)=alpha u^(alpha-2)>0.

It is convex on [0,infinity), has minimum f_alpha(1)=0, and satisfies

0<=f_alpha(u)=1+ku-u^alpha/(1-alpha)<=1+ku.

Thus all local divergence integrals are finite for probability measures. Lebesgue decomposition and Radon–Nikodym derivatives apply because the measures are finite.

### 1. Scalar control of the full mass ratio

Fix a measurable E with p(E)>0. Write q=q_ac+q_s relative to p and set

R=dq_ac/dp,   x=(1/p(E)) integral_E R dp,   h=q_s(E)/p(E).

These are finite nonnegative quantities and q(E)/p(E)=x+h. Under the probability measure p restricted to E and divided by p(E), convexity gives

f_alpha(x)<= (1/p(E)) integral_E f_alpha(R) dp.

For completeness, when x>0, integrate the supporting-line inequality f_alpha(u)>=f_alpha(x)+f'_alpha(x)(u-x). When x=0, nonnegativity implies R=0 almost everywhere on E, so equality holds.

For every x,h>=0, the explicit formula gives

f_alpha(x+h)-f_alpha(x)=kh-((x+h)^alpha-x^alpha)/(1-alpha)<=kh.

This also covers x=0 without differentiating there. Hence

f_alpha(q(E)/p(E))<=D_alpha^E(q||p)/p(E)=Dbar_alpha^E(q||p).  (1)

Exactly the same reasoning applies with p and q interchanged whenever q(E)>0.

### 2. Quantitative relative-error bound and sublevel properties

For 0<y<=1, the integral Taylor formula gives

f_alpha(y)=alpha integral_y^1 (u-y)u^(alpha-2) du >= (alpha/2)(1-y)^2.

The bound extends to y=0 by continuity. It therefore implies

f_alpha(y)>=alpha|y-1|^2/[2(1+|y-1|)]

on [0,1]. For y=1+s with s>=0,

f_alpha(1+s)=alpha integral_0^s (s-u)(1+u)^(alpha-2) du
>=alpha integral_0^s (s-u)/(1+u)^2 du
=alpha(s-log(1+s)).

The function H(s)=s-log(1+s)-s^2/[2(1+s)] satisfies H(0)=0 and H'(s)=s^2/[2(1+s)^2]>=0. Consequently the same scalar lower bound holds for all y>=0.

Set z=Dbar_alpha^E(q||p) and s=|1-q(E)/p(E)|. Equation (1) yields alpha s^2<=2z(1+s), whence

s<=z/alpha+sqrt((z/alpha)^2+2z/alpha)
=(z+sqrt(z^2+2alpha z))/alpha
<=2sqrt(z(z+2))/alpha.

The last inequality follows from alpha<1, z<=sqrt(z(z+2)), and sqrt(z^2+2alpha z)<=sqrt(z(z+2)). This includes z=0. Thus

|1-q(E)/p(E)|<=(2/alpha)sqrt(Dbar_alpha^E(q||p))sqrt(Dbar_alpha^E(q||p)+2).  (2)

We also need the following properties, directly from the generator formula:

f_alpha(0)=1,   f_alpha(1)=0,   lim_{y->infinity} f_alpha(y)/y=k>0.

Continuity and divergence to infinity imply that every finite sublevel set is bounded above. If 0<=lambda<1, continuity at zero excludes a neighborhood of zero from {y>=0:f_alpha(y)<=lambda}; hence this sublevel set is contained in [c,C] for some 0<c<C<infinity. These constants depend on alpha and lambda, not on E or r.

### 3. Strict q||p control

Write m_p(r)=p(B_r(theta)) and m_q(r)=q(B_r(theta)). Suppose limsup_{r->0} Dbar_alpha^{B_r(theta)}(q||p)<1. Choose lambda strictly between that limsup and 1. Nonnegativity permits lambda>=0. For all sufficiently small r, equation (1) gives

f_alpha(m_q(r)/m_p(r))<=lambda.

The sublevel property supplies fixed 0<c<C<infinity such that

c m_p(r)<=m_q(r)<=C m_p(r).

For every positive gauge g(r), this comparison implies that m_p=O(g) if and only if m_q=O(g), and m_p=Omega(g) if and only if m_q=Omega(g). Applying this to every power gauge shows equality of the two upper gauge sets and equality of the two lower gauge sets. Their infima and suprema agree, including empty and unbounded cases. By existence of the power indices, MI_pow(q,theta)=MI_pow(p,theta), also when the common index is zero or infinity.

If MI_log(p,theta) exists, its definition requires that the power index be finite and strictly positive. Equality of the power indices therefore gives a common well-defined exponent a=d/MI_pow(p,theta)=d/MI_pow(q,theta). Apply the same comparison to g(r)=r^a(-log r)^eta for every real eta. Both logarithmic gauge sets coincide. Their thresholds coincide under the stated conventions, so MI_log(q,theta) exists and equals MI_log(p,theta).

### 4. Finite p||q control

Suppose limsup_{r->0} Dbar_alpha^{B_r(theta)}(p||q)<infinity. Choose a finite nonnegative M larger than this limsup. For all sufficiently small r, the swapped version of (1) gives

f_alpha(m_p(r)/m_q(r))<=M.

The finite sublevel set is bounded above. Choose a fixed C>=1 bounding it. Then

m_q(r)>=C^(-1)m_p(r).

Equation (2) with the measures swapped gives the same bounded-ratio conclusion as an alternative.

Every lower power gauge of p is a lower power gauge of q, so L_pow(p) is contained in L_pow(q). These sets contain only positive real numbers. Their suprema are therefore ordered even when the first set is empty, because its assigned supremum is zero. Unbounded sets have supremum infinity. Existence of both power indices gives

MI_pow(q,theta)=d sup L_pow(q)>=d sup L_pow(p)=MI_pow(p,theta).

Finally suppose the power indices are equal and both logarithmic indices exist. Their common power index is then finite and positive, so both logarithmic gauge definitions use the same exponent a. The one-sided mass comparison gives both L_log(p) subset L_log(q) and U_log(q) subset U_log(p). Use the latter inclusion: with inf(empty set)=infinity, infima are monotone under reverse inclusion, including unbounded sets. Therefore

MI_log(p,theta)=inf U_log(p)<=inf U_log(q)=MI_log(q,theta).

Using upper gauges here avoids applying unrestricted supremum monotonicity to real-valued logarithmic gauge sets under the source's convention sup(empty set)=0. This proves all public claims without any additional finiteness assumption on the logarithmic index.

## Closure

All four obligations are explicitly established. The only measure-decomposition background is the standard finite-measure Lebesgue decomposition and its Radon–Nikodym representation. No paper-specific result is invoked without its needed derivation.
