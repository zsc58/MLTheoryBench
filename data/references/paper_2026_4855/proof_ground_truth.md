# Reference Proof

## Contract and boundary conventions

Let v_{mn}=(V^T)_{mn}. All factors are nonnegative, alpha>0 is fixed, and the current pair has finite objective. Thus x^t_{mn}>0 whenever v_{mn}>0. For fixed data v, the boundary extension is d_alpha(0||0)=0 and d_alpha(v||0)=+infinity for v>0. Define r(v,x)=v/x when x>0 and r(0,0)=0. The latter convention applies to the inner data/reconstruction quotients, not to the outer update quotients, whose 0/0 convention is 1.

The source's normalization rescales corresponding factor columns and rows reciprocally and preserves V^T E D. It imposes no simplex constraint on the fixed-factor minimizations considered here. The scalar alpha is the explicitly allowed equal-dispersion specialization of the appendix. The argument is deterministic and needs no probabilistic observation assumptions.

Write

q(v)=v log v-(alpha+v)log(alpha+v),

where 0 log 0=0. Then

F(E,D)=sum_{m,n}[q(v_{mn})-v_{mn}log x_{mn}+(alpha+v_{mn})log(alpha+x_{mn})].

Here -v log x is identically zero for v=0, including x=0, and is +infinity for v>0,x=0.

## Fixed D: construction and tightness

Fix D and a current E^t with finite objective. For entries with v_{mn}>0, define

c^{mn}_{n'k}=(V^T)_{mn'}E^t_{n'k}D_{kn}/x^t_{mn},

and S_{mn}={(n',k):c^{mn}_{n'k}>0}. The weights on S_{mn} sum to one. Define

L_{mn}(E)=-v_{mn} sum_{(n',k) in S_{mn}} c^{mn}_{n'k} log(((V^T)_{mn'}E_{n'k}D_{kn})/c^{mn}_{n'k})

when v_{mn}>0, and define L_{mn}(E)=0 when v_{mn}=0. In the first formula a zero logarithm argument gives +infinity. No weights or logarithms are needed for zero-data entries.

For completeness, the standard Jensen inequality used here says that, for positive weights w_j summing to one and positive y_j,

-log(sum_j w_j y_j) <= -sum_j w_j log y_j.

It extends to zero y_j with the extended-value convention. Since the full reconstruction is at least the sum of the terms indexed by S_{mn}, monotonicity of -log and this inequality give

-v_{mn}log x_{mn} <= L_{mn}(E).

This remains valid if some current factor coordinates are zero: terms outside S_{mn} are merely omitted from the partial reconstruction. At E=E^t those omitted terms vanish and every logarithm argument in the weighted sum equals x^t_{mn}, so equality holds. At v_{mn}=0, both negative-log contributions are zero.

Put b_{mn}=(alpha+v_{mn})/(alpha+x^t_{mn})>0. The standard concavity inequality log u <= log u_0+(u-u_0)/u_0, for u,u_0>0, applies with u=alpha+x_{mn} and u_0=alpha+x^t_{mn}, even if either reconstruction is zero. Define the full auxiliary

G_E(E,E^t)=sum_{m,n}[q(v_{mn})+L_{mn}(E)+(alpha+v_{mn})log(alpha+x^t_{mn})+b_{mn}(x_{mn}-x^t_{mn})].

The two inequalities prove G_E(E,E^t)>=F(E,D) for every nonnegative E, in the extended-value sense. Equality holds at E=E^t, and that common value is finite. This is tightness, the meaning of tangency in the task.

## Fixed D: coefficient calculation and minimization

Let R_{mn}=r(v_{mn},x^t_{mn}). Expanding the auxiliary into coordinate-dependent terms gives

G_E(E,E^t)=constant+sum_{n',k}[-A_{n'k}log E_{n'k}+B_{n'k}E_{n'k}],

where

A_{n'k}=sum_{m,n:v_{mn}>0}v_{mn}c^{mn}_{n'k}=E^t_{n'k}[V R D^T]_{n'k},

B_{n'k}=sum_{m,n}(V^T)_{mn'}D_{kn}b_{mn}=[V b D^T]_{n'k}.

The constant is finite: only positive weights are expanded, and their fixed coefficients and current coordinates are positive. A term -A log z is defined to be zero for all z>=0 if A=0.

All coefficients are finite and nonnegative. Because every b_{mn}>0, B_{n'k}=0 forces every nonnegative coefficient (V^T)_{mn'}D_{kn} to vanish. Consequently [V R D^T]_{n'k}=0 as well. In particular, a positive outer numerator with a zero denominator is impossible.

For g(z)=-A log z+Bz on z>=0:

* If A>0, then B>0. On z>0, g'(z)=-A/z+B and g''(z)=A/z^2>0, so the unique minimizer is A/B.
* If A=0<B, g(z)=Bz has its unique minimum at z=0.
* If B=0, then A=0 and the coordinate is flat; retain its current value.

Thus a simultaneous coordinatewise minimizer is

E^{t+1}=E^t ⊙ [V(V^T/(V^T E^t D))D^T]/[V((alpha+V^T)/(alpha+V^T E^t D))D^T],

with the task's distinct inner and outer quotient conventions. This statement also covers a zero current coordinate with a positive outer numerator: its logarithmic coefficient A is zero and the update remains zero.

The selected minimizer has finite G_E: every positive A has a positive minimizer, and the remaining scalar terms are finite. Since G_E majorizes F, the updated F is finite. Equivalently, no positive data entry acquires a zero reconstruction. More directly, for any v_{mn}>0 there is a positive weight c^{mn}_{n'k}; its coordinate has A_{n'k}>0 and remains positive, so at least one positive term in that reconstruction survives. Reconstructions of zero data entries may become zero, as they are allowed to do.

## Fixed E: construction, coefficients, and minimization

Fix E and a current D^t with finite objective, and put P=V^T E and x^t=P D^t. For each v_{mn}>0 define

c^{mn}_k=P_{mk}D^t_{kn}/x^t_{mn},

with S_{mn}={k:c^{mn}_k>0}. Define

L^D_{mn}(D)=-v_{mn}sum_{k in S_{mn}}c^{mn}_k log(P_{mk}D_{kn}/c^{mn}_k)

for v_{mn}>0, and L^D_{mn}(D)=0 for v_{mn}=0. Put b_{mn}=(alpha+v_{mn})/(alpha+x^t_{mn}), and define

G_D(D,D^t)=sum_{m,n}[q(v_{mn})+L^D_{mn}(D)+(alpha+v_{mn})log(alpha+x^t_{mn})+b_{mn}((PD)_{mn}-x^t_{mn})].

The weights sum to one at positive-data entries. The partial-sum/Jensen argument gives -v_{mn}log((PD)_{mn})<=L^D_{mn}(D), with equality at D^t. The logarithm tangent bound applies at every entry. Therefore G_D(D,D^t)>=F(E,D) for every nonnegative D, and G_D(D^t,D^t)=F(E,D^t)<infinity.

With R_{mn}=r(v_{mn},x^t_{mn}), the coordinate-dependent part is

-C_{kn}log D_{kn}+H_{kn}D_{kn},

where

C_{kn}=sum_{m:v_{mn}>0}v_{mn}c^{mn}_k=D^t_{kn}[P^T R]_{kn},

H_{kn}=sum_m P_{mk}b_{mn}=[P^T b]_{kn}.

If H_{kn}=0, positivity of every b_{mn} forces P_{mk}=0 for every m, so the outer numerator is also zero. The same three scalar minimization cases therefore give

D^{t+1}=D^t ⊙ [(V^T E)^T(V^T/(V^T E D^t))]/[(V^T E)^T((alpha+V^T)/(alpha+V^T E D^t))].

Every positive logarithmic coefficient retains a positive minimizing coordinate, and the auxiliary minimum is finite. Hence the updated objective is finite here too.

## Alternation and descent

The preceding constructions give actual minimizers on the nonnegative extended-value domain, not merely infima on an open domain. Consequently

F(E^{t+1},D)<=G_E(E^{t+1},E^t)<=G_E(E^t,E^t)=F(E^t,D),

and

F(E,D^{t+1})<=G_D(D^{t+1},D^t)<=G_D(D^t,D^t)=F(E,D^t).

Because each update preserves finiteness of F, the other factor can then be updated with the same conventions. This proves the alternating MM claim, including boundary iterates and entirely zero data. It does not assert convexity of the original fixed-factor objective, uniqueness in flat coordinates, or convergence to a global optimum.

## Source-local corrections used

The E-majorization chain at source L000269 and L000276 must have F(E;D,V), rather than F(E^t;D,V), on its left side. The strict-positive argmin notation at L000290 and L000306 must include nonnegative boundary minimizers. Finally, the block-convexity assertion at L000176 is unnecessary and false; it is the displayed separable auxiliary that is convex. These corrections are recorded under theory_006, theory_007, and theory_008 and do not change the update formulas or their proof mechanism.
