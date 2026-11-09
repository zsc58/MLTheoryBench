# Reference Proof

## Proof Structure

Verify that the Gaussian convolution is finite and differentiable using the nominal square-integrability assumption. Represent the gradient by the Gaussian score, establish feasibility and its affine equality case, and solve the fixed-perturbation optimization by decomposing the likelihood ratio into a linear score component and an orthogonal residual. Cauchy-Schwarz proves global sharpness and attainment. Finally maximize over directions and radii and treat the certified-radius endpoint, including the constant case.

## Complete Proof

Let P be the law of X=z+e, where e~N(0,sigma^2 I_d), and put v=X-z. All functions and equalities involving P are understood up to P-null sets when appropriate. Write E for expectation under P.

### 1. Gaussian Moments, Finiteness, and Differentiation

Completing the square in the Gaussian density gives, for every t in R^d,

E[exp(t^T v)]=exp(sigma^2||t||^2/2).

The same completion of the square identifies the tilted law as N(sigma^2 t,sigma^2 I_d), and therefore

E[v exp(t^T v)]=sigma^2 t exp(sigma^2||t||^2/2).

For a shift a in R^d, define

L_a(X)=exp(a^T v/sigma^2-||a||^2/(2sigma^2)).

This is the density ratio of N(z+a,sigma^2 I_d) to P. The preceding Gaussian calculation gives

E[L_a]=1,    E[L_a^2]=exp(||a||^2/sigma^2).

Consequently E[|f(X)|L_a(X)] is finite by Cauchy-Schwarz whenever E[f(X)^2]<infinity. Thus g(z+a)=E[f(X)L_a(X)] exists as a finite expectation for every a. No square-integrability assumption at shifted inputs is required.

We also justify differentiation rather than inferring it from single-point integrability. For any fixed b>0 and ||a||<=b,

|partial L_a/partial a_i| <= H_b(v):=sigma^{-2}(||v||+b)exp(b||v||/sigma^2).

The function H_b belongs to L^2(P). Indeed, its squared exponential factor grows only exponentially in ||v||, while the Gaussian density decays quadratically; completing the square, or using 2b||v||<=||v||^2/4+4b^2, bounds the resulting integral by a finite polynomial Gaussian integral. Hence E[|f|H_b]<infinity by Cauchy-Schwarz. The mean value theorem bounds the coordinate difference quotients by this integrable envelope. Dominated convergence permits differentiation of E[fL_a] locally. In particular, with B=v/sigma^2,

grad g(z)=E[f(X)B].

Also E[B]=0 and E[BB^T]=I_d/sigma^2. Thus, for m=E[f(X)] and h=f-m, the exact gradient constraint is E[hB]=G.

### 2. Feasibility and the Affine Equality Case

Put Y=G^T v and S=C-sigma^2||G||^2. We have

E[Y]=0,    E[YB]=G,    E[Y^2]=sigma^2||G||^2.

For any function with the prescribed gradient, set u=h-Y. Then E[u]=0 and E[uB]=0, so E[uY]=sigma^2 G^T E[uB]=0. Therefore

Var(f(X))=E[h^2]=sigma^2||G||^2+E[u^2].

The variance constraint requires C>=sigma^2||G||^2. Conversely, f(x)=m+G^T(x-z) has the prescribed gradient and variance sigma^2||G||^2, so this condition is sufficient for nonemptiness.

Equality Var(f(X))=sigma^2||G||^2 holds exactly when u=0 almost surely, namely when f(X)=m+G^T(X-z) almost surely. This includes G=0: equality then means f is constant almost surely. For every admissible function, E[u^2]<=S.

Adding any real constant to f preserves square integrability, variance, gradient, and the difference between shifted and nominal expectations. This explains why the mean m is unrestricted.

### 3. Fixed-Perturbation Optimization

Fix delta and write r=||delta||. Define A_delta=L_delta-1. Change of measure gives

g(z+delta)-g(z)=E[f(X)A_delta(X)]=E[hA_delta],

where all expectations are finite by Step 1.

The Gaussian calculations in Step 1 yield

E[A_delta]=0,
E[A_delta B]=delta/sigma^2,
E[A_delta^2]=exp(r^2/sigma^2)-1,
E[(delta^T B)^2]=r^2/sigma^2.

For example, E[L_delta v]=delta follows by Gaussian tilting, and E[(L_delta-1)^2]=E[L_delta^2]-2E[L_delta]+1.

Let q_delta=A_delta-delta^T B. Then

E[q_delta]=0,    E[q_delta B]=0,

and, using E[A_delta delta^T B]=r^2/sigma^2,

E[q_delta^2]=D(r):=exp(r^2/sigma^2)-1-r^2/sigma^2.

For r>0, D(r)>0: the function exp(t)-1-t is zero at t=0 and has positive derivative exp(t)-1 for t>0.

Using h=Y+u and the orthogonality relations,

E[hA_delta]=G^Tdelta+E[uq_delta].

Cauchy-Schwarz gives

-sqrt(S D(r)) <= E[uq_delta] <= sqrt(S D(r)).

Both endpoints are attained for r>0 by

u=+/-sqrt(S/D(r))q_delta.

These residuals have mean zero, zero score moment, and squared norm S. Thus the signed maximum and minimum are respectively

G^Tdelta+sqrt(S D(r)),    G^Tdelta-sqrt(S D(r)).

The positive endpoint is attained by

f_delta^*(x)=m+G^T(x-z)+k_delta[exp(delta^T(x-z)/sigma^2-r^2/(2sigma^2))-1-delta^T(x-z)/sigma^2],

where k_delta=sqrt(S/D(r)). The function is measurable and nominally square-integrable, has mean m, gradient G, and variance C. When S=0, k_delta=0 and it is simply affine; no division by k_delta is needed.

Taking the larger absolute value of the two endpoints gives the exact fixed-delta absolute optimum

|G^Tdelta|+sqrt(S D(r)).

This does not use f->-f, which would generally change the prescribed gradient. Only the residual sign is changed.

If delta=0, then L_delta=1 and the shift is zero for every admissible function. Thus the value formula also holds at r=0, without defining k_delta there.

### 4. Directional and Ball Maximization

For ||delta||=r,

|G^Tdelta|<=r||G||.

When G is nonzero, delta=rG/||G|| attains equality and may be used with the positive signed extremizer. The negative aligned direction also attains the absolute sphere optimum. When G=0, every point on the sphere has the same optimized value. At r=0 the only perturbation is zero.

For r>=0,

D'(r)=(2r/sigma^2)(exp(r^2/sigma^2)-1)>=0.

Hence sqrt(S D(r))+r||G|| is nondecreasing in r. The maximum over the radius-R ball is therefore attained at radius R, with value

Phi(R)=sqrt(C-sigma^2||G||^2)sqrt(exp(R^2/sigma^2)-1-R^2/sigma^2)+R||G||.

This proves the nested supremum identity for every finite R>=0, including R=0, G=0, and S=0. For positive R, the constructions above attain it; for R=0 every admissible function attains the zero value.

### 5. Certification and the Radius Endpoint

Fix a finite epsilon>=0. The exact worst-case identity shows that the prediction shift is at most epsilon for every admissible f and every ||delta||<=R if and only if Phi(R)<=epsilon. Thus the supremum of uniformly certified finite radii is

R_cert=sup{R>=0:Phi(R)<=epsilon},

with value +infinity if the set is unbounded. This is a certificate uniform over the specified class, not a claim that an individual function cannot have a larger robust radius.

The set is nonempty because Phi(0)=0. If C>0, either ||G||>0 or S>0. In the former case the linear term is strictly increasing and unbounded. In the latter case D(r) is strictly increasing for r>0 and tends to infinity. Consequently Phi is continuous, strictly increasing on [0,infinity), and unbounded. The intermediate value theorem gives a unique finite R_cert with Phi(R_cert)=epsilon. The feasible-radius set is [0,R_cert], so this endpoint is attained; when epsilon=0 it equals zero.

If C=0, feasibility forces G=0. Every admissible function is constant almost surely under P, and the equivalent shifted Gaussian measures give the same smoothed constant. Accordingly Phi(R)=0 for every finite R, all such radii are certified, and R_cert=+infinity.

All theorem-critical obligations are explicitly closed. The score identity, Gaussian moments, feasibility, global sharpness, attainment, absolute-value treatment, directional maximization, ball maximization, and certified-radius endpoints require no unresolved specialized dependency.
