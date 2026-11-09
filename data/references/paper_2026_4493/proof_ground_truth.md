# Reference Proof

## Proof Structure

Derive the scalar relaxation identity and its bounds, apply it to both moment equations, and normalize on the actual positivity region. Obtain the nonlinear remainder by integrating the second derivative along a line segment, with an explicit denominator lower bound. Finally identify the prescribed coefficient and characterize its vanishing.

## Complete Proof

Fix a coordinate and write g, m, v and delta for its scalar quantities. Since g is continuous and nonzero on I, its sign is constant and |g| has a positive minimum. No sign condition on the initial moments is assumed. All assertions about the normalized update below are restricted to P={t in I: v_i(t)>0 for every i}.

### 1. Exact scalar relaxation formula

For tau x'=-x+y with y in C^2(I), multiplying by exp((t-t0)/tau) and integrating gives

x(t)=exp(-(t-t0)/tau)x(t0)+integral_{t0}^t K_tau(t,s)y(s) ds,

where K_tau(t,s)=tau^(-1)exp(-(t-s)/tau). Since partial_s K_tau=K_tau/tau, integration by parts gives

integral K_tau y = y(t)-exp(-(t-t0)/tau)y(t0)-tau integral K_tau y'.

Applying the same identity to y' yields

x(t)=y(t)-tau y'(t)+T_x(t)+C_x(t),

T_x(t)=[x(t0)-y(t0)+tau y'(t0)]exp(-(t-t0)/tau),

C_x(t)=tau^2 integral_{t0}^t K_tau(t,s)y''(s) ds.

The kernel is nonnegative and its integral is 1-exp(-(t-t0)/tau)<=1. Thus

|T_x(t)|=|x(t0)-y(t0)+tau y'(t0)|exp(-(t-t0)/tau),

|C_x(t)|<=tau^2 sup_I |y''|.

### 2. Moment decompositions

Apply the identity with (x,y,tau)=(m,g,tau_1) and (v,g^2,tau_2). Explicitly,

T_m(t)=[m(t0)-g(t0)+tau_1 g'(t0)]exp(-(t-t0)/tau_1),

C_m(t)=tau_1^2 integral_{t0}^t K_{tau_1}(t,s)g''(s) ds,

T_v(t)=[v(t0)-g(t0)^2+tau_2 (g^2)'(t0)]exp(-(t-t0)/tau_2),

C_v(t)=tau_2^2 integral_{t0}^t K_{tau_2}(t,s)(g^2)''(s) ds.

Because delta=g'/g,

g'=g delta,  g''=g(delta^2+delta'),

(g^2)'=2g^2 delta,  (g^2)''=2g^2(2delta^2+delta').

Consequently,

m=g(1-tau_1 delta)+T_m+C_m,

v=g^2(1-2tau_2 delta)+T_v+C_v.

For completeness, with Lambda=sup_I |delta|, Lambda'=sup_I |delta'| and G=sup_I |g|, these formulas imply the source curvature bounds

|C_m|<=tau_1^2 G(Lambda^2+Lambda'),

|C_v|<=4tau_2^2 G^2(Lambda^2+Lambda').

All these constants are finite. The sharper derivative-supremum bounds from Step 1 will suffice below.

### 3. Exact nonlinear remainder

Define

q_m=(T_m+C_m)/g,  q_v=(T_v+C_v)/g^2,

X=-tau_1 delta+q_m,  Y=-2tau_2 delta+q_v.

Where v>0, 1+Y=v/g^2>0 and

R=sign(g)F(X,Y),  F(X,Y)=(1+X)/sqrt(1+Y).

For fixed X,Y with 1+Y>0, every point (uX,uY), 0<=u<=1, lies in the domain of F, since

1+uY=(1-u)+u(1+Y)>0.

Let h(u)=F(uX,uY). Twice integrating h'' gives

h(1)=h(0)+h'(0)+integral_0^1 (1-u)h''(u) du.

Here h(0)=1, h'(0)=X-Y/2, and direct differentiation gives

h''(u)=-XY(1+uY)^(-3/2)+(3/4)(1+uX)Y^2(1+uY)^(-5/2).

Accordingly define the explicit function

Q(X,Y)=integral_0^1 (1-u)[-XY(1+uY)^(-3/2)+(3/4)(1+uX)Y^2(1+uY)^(-5/2)] du.

Then F(X,Y)=1+X-Y/2+Q(X,Y). Substituting X and Y proves

R=sign(g)[1+(tau_2-tau_1)delta]+E,

E=sign(g)[q_m-q_v/2+Q(X,Y)].

This is a formula in the initial data, g and its derivatives, and the relaxation times, not merely a definition by subtracting the asserted leading term from R. It contains the transition and curvature contributions and a nonlinear ratio remainder.

### 4. Quantitative compact-subinterval bound

Let K be any nonempty compact subinterval of P, and set a=min K. For the fixed coordinate define

b=min_K |g|>0,  D=sup_K |delta|,

A_m=|m(t0)-g(t0)+tau_1 g'(t0)|,

A_v=|v(t0)-g(t0)^2+tau_2 (g^2)'(t0)|,

M_m=sup_I |g''|,  M_v=sup_I |(g^2)''|.

Choose a normalization lower bound nu>0 such that v(t)/g(t)^2>=nu for t in K. Such a bound exists by continuity and compactness. Put

B_m=[A_m exp(-(a-t0)/tau_1)+tau_1^2 M_m]/b,

B_v=[A_v exp(-(a-t0)/tau_2)+tau_2^2 M_v]/b^2,

U=tau_1 D+B_m,  V=2tau_2 D+B_v,  ell=min(1,nu).

Then |q_m|<=B_m, |q_v|<=B_v, |X|<=U and |Y|<=V on K. Moreover, along every integration segment, 1+uY>=ell and |1+uX|<=1+U. The integral formula therefore gives

|Q(X,Y)|<= (1/2)ell^(-3/2)|XY|+(3/8)(1+U)ell^(-5/2)Y^2

<= C_K(|X|+|Y|)^2,

where one explicit permissible constant is

C_K=(1/2)ell^(-3/2)+(3/8)(1+U)ell^(-5/2).

It follows that, throughout K,

|E|<=B_m+B_v/2+C_K(U+V)^2.

This is finite and uses neither R nor E. Its dependencies are only the stated data, the compact subinterval, and permitted positive normalization lower bounds. The more informative pointwise estimate also holds:

|E(t)|<=|q_m(t)|+|q_v(t)|/2+9C_K(tau_*|delta(t)|+|q_m(t)|+|q_v(t)|)^2,

where tau_*=max(tau_1,tau_2), because |X|+|Y|<=3tau_*|delta|+|q_m|+|q_v|.

The argument remains valid at t0 if all second moments are positive there. If a second moment is zero at an endpoint, that endpoint is excluded from P; no bound uniform up to that excluded endpoint is claimed. Negative initial second moments cause no difficulty on compact subsets of P. If P is empty, there is no interval on which the invariance characterization is asserted.

### 5. Coefficient characterization

In the prescribed decomposition the coefficient of delta_i is

a_i(t)=sign(g_i(t))(tau_2-tau_1).

On every nonempty interval contained in P, these coefficients all vanish if tau_1=tau_2. Conversely, since d>=1 and every sign(g_i(t)) is either 1 or -1, their vanishing on such an interval forces tau_1=tau_2. This concerns the coefficients, not the realized products a_i delta_i, so it also covers constant gradient trajectories.

Finally, for the common Delta t>0, equality exp(-Delta t/tau_1)=exp(-Delta t/tau_2) implies equality of their exponents, and hence tau_1=tau_2. The converse is immediate. Thus the prescribed first-order gradient-scale invariance holds on each nonempty interval of definition exactly when tau_1=tau_2, equivalently beta_1=beta_2.

All obligations are derived above; no unresolved external dependency remains.
