# Reference Proof

## Proof Structure

Verify the local hypotheses of the standard diffusion time-reversal theorem and use its reversed martingale-problem conclusion. Disintegrate at the conditioning state, then use the task's conditional envelope to justify the unbounded-coordinate increment calculation. For the squared-Bessel specialization, factor the bridge density, evaluate its first moment using the correct modified-Bessel product integral, average its exact quadratic expression under the posterior initial-state law, and substitute into the general identity.

## Audited Standard Dependencies

### Local Diffusion Time Reversal

The standard-independent result indexed by theory_002 is used in its local martingale-problem form. The relevant statement is as follows.

Let a continuous, nonexplosive Markov diffusion have locally Lipschitz spatial coefficients b and sigma, with locally bounded continuous spatial derivatives through order two on positive-time interior cylinders. Write a=sigma sigma^T and

L_r f = b(r,.) dot grad f + (1/2) sum_(i,j) a_ij(r,.) partial_ij f.

Suppose its positive density p is C^{1,2}, satisfies the local weak Fokker-Planck equation partial_r p=L_r^*p, and satisfies, for every compact time interval J inside (0,T) and every relatively compact spatial set K inside the state-space interior,

integral_J integral_K [p^2 + ||grad p||^2 + p(||b||+tr a)

+ sum_(i,j) |partial_j(a_ij p)|] dx dr < infinity.

Then on interior time intervals the actual reversed path solves the local martingale problem with covariance a and drift

-b + div(pa)/p,

with the original time argument read backwards. In particular, for compactly supported C^2 tests, subtracting the integrated reverse generator gives a local martingale in the reversed natural filtration. The corresponding quadratic variation is determined by a. This statement concerns the reversed path law, not merely one-time marginals. It does not assume uniform ellipticity or an unconditional first moment of the coordinate process.

The local formulation is important: all integrability and differentiation conditions are checked on compact cylinders, and the martingale statement is localized with compactly supported tests and exit stopping times. It is not a theorem requiring the task's per-state conditional envelope to be integrable after averaging over the conditioning state. Nor does localization require replacing the original density by the density of a killed process.

The generator in this standard statement is the density-weighted adjoint generator

L_r^rev f = [L_r^*(p(r,.)f) - f L_r^*p(r,.)]/p(r,.).

Expanding the numerator on compactly supported tests gives covariance a and drift -b+div(pa)/p. This also identifies the precise local density derivatives used in the theorem.

### Squared-Bessel Transition Kernel

For nu>0, the standard transition result indexed by theory_013 gives, for r>0 and u,v>0,

q_r(u,v) = (1/(2r))(v/u)^(nu/2) exp(-(u+v)/(2r)) I_nu(sqrt(uv)/r).

At u=0,

q_r(0,v) = v^nu exp(-v/(2r))/((2r)^(nu+1) Gamma(nu+1)).

These are positive probability densities on v>0; at positive times there is no atom at zero. The parameter nu>0 in the task verifies the relevant transition-result hypotheses.

### Markov Bridge and Modified-Bessel Identities

The Markov bridge result indexed by theory_014 gives the conditional density

q_(t-epsilon)(z,y) q_epsilon(y,x)/q_t(z,x),

for 0<epsilon<t, whenever q_t(z,x)>0.

The standard-independent identities indexed by theory_015 are, for A,B,C>0 and nu>0,

F(A,B,C;nu) = integral_0^infinity exp(-Cu) I_nu(A sqrt(u)) I_nu(B sqrt(u)) du

= C^(-1) exp((A^2+B^2)/(4C)) I_nu(AB/(2C)),

and

I'_nu(r) = nu I_nu(r)/r + I_(nu+1)(r), r>0.

The transformed integral is 2 integral_0^infinity v exp(-Cv^2) I_nu(Av) I_nu(Bv) dv. Its weight is not v^nu. The exponential quadratic decay permits differentiation in C, yielding -partial_C F as the integral with one extra factor u.

## 1. General Identity

### 1.1 Verify the Local Reversal Hypotheses

Fix a compact time interval J inside (0,T) and a compact spatial set K inside D. The task's coefficient assumptions imply local spatial Lipschitz continuity of b and sigma and boundedness of their derivatives through order two on a slightly larger compact cylinder. The functions p and grad p are bounded there. In addition,

partial_j(a_ij p) = p partial_j a_ij + a_ij partial_j p

is continuous and bounded on that cylinder. Since the cylinder has finite volume, every integral in the local reversal criterion is finite. Positivity and continuity of p also bound 1/p on each such compact cylinder.

It remains to check the local weak Fokker-Planck equation. For f in C_c^2(D), apply Ito's formula between two times in J. The drift integrand L_r f is bounded: derivatives of f vanish outside a compact set, and the coefficients are bounded on that set. The stochastic integrand grad f sigma is likewise bounded, so its integral is a true square-integrable martingale and has mean zero. Taking expectations gives

integral_D p(v,x) f(x) dx - integral_D p(u,x) f(x) dx

= integral_u^v integral_D p(r,x) L_r f(x) dx dr.

This is partial_r p=L_r^*p in the local weak sense. The supplied C^{1,2} regularity makes the density derivatives in the reversal criterion ordinary continuous derivatives. Thus all hypotheses of the stated local reversal theorem are verified.

This argument uses compactly supported tests and compact-cylinder integrability. It never infers an unconditional integrability statement from the conditional envelope.

### 1.2 Condition and Use the Coordinate Martingale

Fix 0<t<T. Choose alpha and H with 0<alpha<t<H<T and consider Y_u=X_(H-u) on the corresponding reversed interval. The local reversal theorem gives drift

beta(u,x) = -b(H-u,x) + div_x(p(H-u,x)a(H-u,x))/p(H-u,x).

The row-divergence convention and symmetry of a give

div(pa)/p = div a + a grad log p.

Consequently,

beta(u,x) = -b(H-u,x) + div a(H-u,x) + a(H-u,x)s(H-u,x).

Let u_0=H-t. Disintegrate the reversed path law given Y_(u_0)=x. For this fixed t, compactly stopped martingale identities pass to the conditional laws for p(t,.)-almost every x. One can use a countable compact exhaustion, rational times, and compactly supported coordinate cutoffs to choose a common full-measure set for these identities; continuity then supplies the full time intervals. No single exceptional set uniform in all t is claimed or needed.

Under such a conditional law, the coordinate decomposition is

Y_(u_0+h)-x = integral_0^h beta(u_0+v,Y_(u_0+v)) dv + M_h,

where M is a continuous local martingale starting at zero and its quadratic-covariation matrix is

integral_0^h a(t-v,X_(t-v)) dv.

Choose a shorter interval inside [alpha,t] on which the task's conditional envelope is finite. This is possible by reducing its state-dependent delta. On that interval the conditional expectation of the total quadratic variation is finite, because it is at most the interval length times the conditional supremum of tr a. Therefore M is a square-integrable martingale under this conditional law and E[M_h | X_t=x]=0. The same envelope bounds the total drift variation and the coordinates themselves.

It follows that, for sufficiently small epsilon depending on t and x,

E[X_(t-epsilon)-X_t | X_t=x]

= integral_0^epsilon E[-b(t-h,X_(t-h)) + div a(t-h,X_(t-h))

+ a(t-h,X_(t-h))s(t-h,X_(t-h)) | X_t=x] dh.

Here the reverse path is the actual forward path read backwards, so no identification based only on one-time marginals is being used.

The paths and displayed drift fields are continuous. The integrand therefore tends, under the conditional law, to

-b(t,x)+div a(t,x)+a(t,x)s(t,x).

Its magnitude is bounded by the conditional integrable supremum in the task. Conditional dominated convergence and then averaging over [0,epsilon] give

lim_(epsilon down to 0) epsilon^(-1) E[X_(t-epsilon)-X_t | X_t=x]

= -b(t,x)+div a(t,x)+a(t,x)s(t,x).

Rearrange to obtain the first identity. At points where a(t,x) is invertible, multiply by its inverse to obtain the equivalent inverse formula.

## 2. Exact Squared-Bessel Bridge Mean

Fix t>0, x>0, z>0 and 0<epsilon<t. Put h=t-epsilon. Multiplying the two transition kernels cancels their powers of the intermediate state. The bridge density is therefore proportional to

exp(-Cy) I_nu(A sqrt(y)) I_nu(B sqrt(y)),

where

A=sqrt(z)/h, B=sqrt(x)/epsilon, C=t/(2h epsilon).

All three parameters are positive, so the stated product-integral identity applies. The bridge first moment is

m_epsilon(z,x) = -partial_C log F(A,B,C;nu),

where differentiation holds A and B fixed. Write rho=AB/(2C). The derivative recurrence gives

m_epsilon = (1+nu)/C + (A^2+B^2)/(4C^2) + (rho/C) I_(nu+1)(rho)/I_nu(rho).

For the bridge parameters, rho=sqrt(xz)/t is independent of epsilon. Substituting the parameters yields the exact expression

m_epsilon(z,x) = x h^2/t^2 + z epsilon^2/t^2

+ (2h epsilon/t)(1+nu+rho I_(nu+1)(rho)/I_nu(rho)).

Define K(z)=rho I_(nu+1)(rho)/I_nu(rho). Expanding the polynomial gives exactly

m_epsilon(z,x) = x + 2epsilon(1+nu-x/t+K(z))

+ epsilon^2((x+z)/t^2 - 2(1+nu+K(z))/t).

This explicitly derives, rather than assumes, the source's bridge asymptotic.

## 3. Boundary and Posterior Integrability

The defining positive series is

I_nu(r) = sum_(k>=0) (r/2)^(2k+nu)/(k! Gamma(k+nu+1)).

It shows that I_nu(r) is positive for r>0 and that I_(nu+1)(r)/I_nu(r) tends to zero as r tends to zero. In particular, the score integrand sqrt(z) I_(nu+1)(sqrt(xz)/t)/I_nu(sqrt(xz)/t) has continuous value zero at z=0.

The same series gives two useful elementary bounds. Since Gamma(k+nu+1)>=Gamma(nu+1)k! for nu>0, and (2k)!<=4^k(k!)^2,

I_nu(r) <= (r/2)^nu exp(r)/Gamma(nu+1).

Termwise comparison of the series for I_(nu+1) and I_nu also gives

0 <= I_(nu+1)(r)/I_nu(r) <= r/(2(nu+1)).

Thus, for fixed t,x>0, the transition kernel satisfies

q_t(z,x) <= C_(nu,t,x) exp(-z/(2t)+sqrt(xz)/t),

for z>=0, with its continuous interpretation at zero. For every nonnegative integer k, z^k times the right side is bounded on [0,infinity).

Let mu be the initial probability law. The marginal density and posterior initial-state law are

p(t,x) = integral_[0,infinity) q_t(z,x) mu(dz),

pi_(t,x)(dz) = q_t(z,x) mu(dz)/p(t,x).

The denominator is positive and finite. The preceding bound shows that every posterior polynomial moment is finite, even if the corresponding unconditional prior moment is infinite. In particular, E[X_0 | X_t=x]<infinity and E[K(X_0) | X_t=x]<infinity, since K(z)<=xz/(2(nu+1)t^2).

At z=0, the bridge-density limit follows from the kernel limit. More explicitly, its density is proportional to

y^(nu/2) exp(-Cy) I_nu(B sqrt(y)).

The integral of this unnormalized density, computed from the positive series, is

(B/2)^nu C^(-(nu+1)) exp(B^2/(4C)).

Its negative logarithmic derivative in C is (1+nu)/C+B^2/(4C^2). This is the preceding exact bridge mean at z=0 with K(0)=0. Thus the exact bridge mean applies throughout [0,infinity).

## 4. Averaging and the Score

Use the tower property to average the exact bridge formula under pi_(t,x). The posterior bounds just proved justify all terms. One obtains

E[X_(t-epsilon) | X_t=x] = x

+ 2epsilon(1+nu-x/t+E[K(X_0) | X_t=x])

+ epsilon^2((x+E[X_0 | X_t=x])/t^2

- 2(1+nu+E[K(X_0) | X_t=x])/t).

The coefficient of epsilon^2 is finite. Divide by epsilon and take epsilon down to zero. This supplies the conditional backward-increment limit without interchanging a merely pointwise asymptotic and an expectation.

For this diffusion, a(t,x)=4x, b(t,x)=2(nu+1), and div a=4. Substitution into the general identity gives

4x s(t,x)+4 = 2(nu+1)

+2(1+nu-x/t+E[K(X_0) | X_t=x]).

Since K(X_0)=(sqrt(x)/t) sqrt(X_0) I_(nu+1)(sqrt(xX_0)/t)/I_nu(sqrt(xX_0)/t), simplification gives

s(t,x) = nu/x - 1/(2t)

+ (1/(2t sqrt(x))) E[sqrt(X_0) I_(nu+1)(sqrt(xX_0)/t)/I_nu(sqrt(xX_0)/t) | X_t=x].

This proves the second frozen target, including the zero-initial-state convention.

## Private Contextual Source Repairs

In the source's general-identity proof, the reversed drift integral must use p(T-s,Y_s), not p(s,Y_s); this is determined by the preceding time-reversal formula.

The selected source record also contains a constant-coefficient extension, which is not a public target. If dX=mu dt+sigma sqrt(X)dW, then Z=(4/sigma^2)X is the normalized BESQ process. Therefore p_X(t,x)=(4/sigma^2)p_Z(t,4x/sigma^2) and s_X(t,x)=(4/sigma^2)s_Z(t,4x/sigma^2), with initial law Z_0=(4/sigma^2)X_0. The source display uses the reciprocal factor and argument; both are corrected in the material record.

## Obligation Closure

1. The relevant local time-reversal theorem is stated as a standard-independent reversed martingale-problem result. Its coefficient, density, compact-cylinder integrability, and weak Fokker-Planck hypotheses are verified explicitly.
2. The conditional coordinate calculation is separate from theorem applicability. Disintegration of compactly stopped martingale identities and the per-state envelope justify zero conditional martingale mean and the short-time drift limit. No unsupported passage from conditional finiteness to unconditional integrability is used.
3. The transition kernel and Markov bridge factorization are stated standard-independent results with verified parameter and positivity hypotheses.
4. The correctly defined product integral and derivative recurrence evaluate the bridge mean explicitly.
5. The zero-initial-state extension, posterior integrability, averaging limit, and final score algebra are derived above.

No specialized paper-specific dependency or unresolved theorem-critical obligation remains.
