# Reference Proof

## Contract and proof obligations

The target error is `E_n=E[||Q_n^(0)-Q*||_infinity]`. Quasi-optimality concerns the explicitly defined certificate-feasible comparison classes, not all schedules achieving the actual stochastic error. We prove: the inner mean-square estimate; the expected-norm outer estimate; feasibility and frequency floors; costs including integer rounding; and lower bounds over both comparison classes. The specialized external optimization theorem is not needed.

Write `d=|S||A|`, `delta=1-gamma`, and `mu=(1+gamma)/2`. The exploration assumption implies `0<xi<=1/d<=1`, so `s=2/xi>=2` and every step size belongs to `(0,1]`. Bounded rewards and a fixed finite initialization ensure integrability of all quantities at every finite iteration. In fact, the updates are convex combinations and all iterates have sup norm at most `max{||Q_0^(0)||_infinity,B/(1-gamma)}`.

If `E_0=0`, the prescribed empty schedule has zero error and zero cost. Its cost equals the infimum in both comparison classes. Henceforth assume `E_0>0` and take epsilon sufficiently small that `epsilon<E_0`.

## 1. Conditional inner estimate

Fix an outer index n. Let `Z_n=||Q_n^(0)-Q*||_infinity`, `Delta_k=Q_n^(k)-T*Q_n^(0)`, and

`e_n^(k)=E[||Delta_k||_2^2 | F_{n,0}]`.

Crucially, this conditions on the cycle-start history, not the history at step k. Put

`C_n=2sigma^2+4gamma^2(Z_n^2+||Q*||_infinity^2)`.

For a sampled coordinate x, the Bellman sample `Y=R+gamma max_a Q_n^(0)(S',a)` has conditional mean `(T*Q_n^(0))(x)` given the current history and x. Its conditional variance is bounded by

`2sigma^2+2gamma^2||Q_n^(0)||_infinity^2 <= C_n`.

The first inequality uses `Var(U+V)<=2Var(U)+2Var(V)` and `Var(V)<=E[V^2]`; it does not assume reward and next state are independent. The second uses `||Q_n^(0)||_infinity^2<=2Z_n^2+2||Q*||_infinity^2`.

Writing `alpha=alpha_n^(k)` and `pi(x)=P(X_{n,k}=x | F_{n,k})`, expansion of the coordinate update and cancellation of the centered cross term give

`E[Delta_{k+1}(x)^2 | F_{n,k}] <= [1-(2alpha-alpha^2)pi(x)]Delta_k(x)^2+alpha^2 pi(x)C_n`.

Sum over x. Since `sum_x pi(x)=1`, `pi(x)>=xi`, and `2alpha-alpha^2>=alpha`, this yields

`E[||Delta_{k+1}||_2^2 | F_{n,k}] <= (1-xi alpha)||Delta_k||_2^2+alpha^2 C_n`.

The tower property, with `C_n` measurable at the cycle start, gives

`e_n^(k+1) <= (1-2/(k+s))e_n^(k)+4C_n/[xi^2(k+s)^2]`.

Set

`Gamma_n=(s+1)max{e_n^(0),2C_n/xi}`.

Then `Gamma_n>=s e_n^(0)` and `Gamma_n>=4C_n/xi^2`. Thus the induction starts with `e_n^(0)<=Gamma_n/s`. If `t=k+s`, the induction step is

`e_n^(k+1) <= (1-2/t)Gamma_n/t+4C_n/(xi^2t^2) <= Gamma_n(t-1)/t^2 <= Gamma_n/(t+1)`.

The last inequality follows from `(t-1)(t+1)<=t^2`. Therefore `e_n^(k)<=Gamma_n/(k+s)` for every k.

The Bellman contraction follows directly from `|max_a u_a-max_a v_a|<=max_a|u_a-v_a|` and taking expectations. Consequently,

`e_n^(0)=||Q_n^(0)-T*Q_n^(0)||_2^2 <= d(||Q_n^(0)-Q*||_infinity+||T*Q_n^(0)-T*Q*||_infinity)^2 <= d(1+gamma)^2 Z_n^2`.

The square is taken after adding the two norms; no cross term is discarded. Using `max{u,v}<=u+v` in `Gamma_n` and collecting coefficients gives exactly

`e_n^(k) <= (c1 Z_n^2+c2)/(k+s)`.

This unshifted induction conclusion justifies evaluation at the terminal inner iterate.

## 2. Expected-norm outer estimate

Conditional Cauchy-Schwarz and `||v||_infinity<=||v||_2` give

`E[||Q_n^(K_n)-T*Q_n^(0)||_infinity | F_{n,0}] <= sqrt((c1 Z_n^2+c2)/(K_n+s)) <= (sqrt(c1)Z_n+sqrt(c2))/sqrt(K_n)`.

The triangle inequality and Bellman contraction therefore imply

`E[Z_{n+1} | F_{n,0}] <= (gamma+sqrt(c1/K_n))Z_n+sqrt(c2/K_n)`.

For deterministic frequencies satisfying `K_n>=K_min=c1/(mu-gamma)^2`, taking expectations yields

`E_{n+1} <= mu E_n+sqrt(c2/K_n)`.

Induction on the number of outer cycles gives

`E_m <= mu^m E_0+sum_{j=0}^{m-1}mu^(m-1-j)sqrt(c2/K_j)=B_m(K)`.

This proves that the public certificate implies the desired actual-error guarantee for implemented schedules. It does not turn that certificate into a necessary condition for actual accuracy.

## 3. Fixed schedule

Let

`N=ceil(log(epsilon/(2E_0))/log(mu))`,

`T_m=sum_{r=0}^{m-1}mu^r=(1-mu^m)/(1-mu)`,

and let the unrounded frequency be `k*=4c2 T_N^2/epsilon^2`.

The ceiling defining N gives `mu^N E_0<=epsilon/2`. Also `sqrt(c2/k*)T_N=epsilon/2`. Upward rounding to `K=ceil(k*)` only decreases the certificate. Since `sigma^2>0`, we have `c2>0`, and `k*>=4c2/epsilon^2` tends to infinity. Hence `K>=K_min` for sufficiently small epsilon. For example, `epsilon<=delta sqrt(c2/c1)` suffices once `N>=1`. Thus the outer estimate proves `E_N<=epsilon`.

For quasi-optimality, consider any certificate-feasible fixed comparator `(m,k)` at accuracy epsilon. Nonnegativity of the two certificate terms implies

`m>=M:=ceil(log(epsilon/E_0)/log(mu))`,

`sqrt(c2/k)T_m<=epsilon`.

Therefore

`mk>=c2 m T_m^2/epsilon^2>=c2 M T_M^2/epsilon^2`.

This is a lower bound for the infimum over the entire fixed comparison class, including its real-valued frequencies and any asymmetric error allocation. Since N and M differ by a bounded amount as epsilon tends to zero, `N/M->1`. Also `T_N/T_M->1`. Eventually `k*>=1`, so the constructed cost is at most `2Nk*=8c2 N T_N^2/epsilon^2`. Its ratio to the comparison infimum is bounded. This proves fixed-class quasi-optimality without making any claim of instance-wise sample-complexity optimality.

## 4. Variable schedule and its comparison bound

For fixed N, put `a_j=sqrt(c2)mu^(N-1-j)`. For arbitrary positive real frequencies, Holder's inequality with exponents `3/2` and `3` gives

`sum_j a_j^(2/3)=sum_j(a_j/sqrt(k_j))^(2/3)k_j^(1/3) <= (sum_j a_j/sqrt(k_j))^(2/3)(sum_j k_j)^(1/3)`.

All sums are finite and all frequencies are positive, so its hypotheses hold. Cubing yields

`(sum_j a_j^(2/3))^3 <= (sum_j a_j/sqrt(k_j))^2 sum_j k_j`.

Define `S_m=sum_{r=0}^{m-1}mu^(2r/3)=(1-mu^(2m/3))/(1-mu^(2/3))`. Equality in the displayed inequality is attained by frequencies proportional to `a_j^(2/3)`. Imposing approximation budget `epsilon/2` gives

`k_j*=C_epsilon mu^(2(N-1-j)/3)`,

`C_epsilon=4c2 S_N^2/epsilon^2`.

Direct substitution verifies `sum_j a_j/sqrt(k_j*)=epsilon/2` and `sum_j k_j*=4c2 S_N^3/epsilon^2`. Thus the rounded frequencies satisfy the certificate constraint.

The smallest unrounded frequency occurs at j=0. The ceiling definition gives

`mu^N<=epsilon/(2E_0)<mu^(N-1)`.

Using `S_N>=1`, we obtain

`k_0*>=4c2 epsilon^(-2)(epsilon/(2E_0))^(2/3)`.

This tends to infinity as epsilon tends to zero, so every frequency eventually exceeds the correct floor `K_min=4c1/delta^2`. Hence the rounded schedule is admissible and `E_N<=epsilon`. This corrects the source's accidental use of c2 in place of c1 when checking the floor. Once every `k_j*>=1`, rounding increases total cost by at most a factor of two.

Now consider any variable comparator with certificate at most epsilon. As before, its outer count m is at least M and its approximation term is at most epsilon. Applying the same Holder inequality to that comparator gives

`sum_{j=0}^{m-1}k_j >= c2 S_m^3/epsilon^2 >= c2 S_M^3/epsilon^2`.

The constructed cost is at most `8c2 S_N^3/epsilon^2`. Because `S_N/S_M->1`, the ratio to the infimum comparison cost stays bounded. This proves quasi-optimality over the entire variable class. The argument explicitly derives the optimization result, so no obligation is delegated to the specialized cited theorem.

## 5. Parameter dependence of the costs

Bounded rewards give `||Q*||_infinity<=B/delta`. Since `xi<=1`,

`c2<=(12/xi^2)(sigma^2+2B^2/delta^2)<=12(sigma^2+2B^2)xi^(-2)delta^(-2)`.

This uses the specified variance-bound parameter; a possibly loose bound sigma^2 is not incorrectly inferred to be at most B^2.

For the fixed schedule, `T_N<=1/(1-mu)=2/delta`. Also

`N<=1+log(2E_0/epsilon)/log(1/mu)`.

For each fixed finite initialization, sufficiently small epsilon gives `log(2E_0/epsilon)<=2log(delta^(-1)epsilon^(-1))`. Absorbing the additive one then proves

`cost=O(log(delta^(-1)epsilon^(-1))/(delta^4 xi^2 log(2/(1+gamma))epsilon^2))`.

The multiplicative constant can depend only on B and sigma; the small-epsilon threshold may additionally depend on the fixed initialization and model parameters. No false bound on the arbitrary initial error is needed.

For the variable schedule, concavity of `x^(2/3)` gives `1-mu^(2/3)>=(2/3)(1-mu)=delta/3`. Thus `S_N<=3/delta`, and the rounded total cost is bounded by `8c2 S_N^3/epsilon^2`. Therefore

`cost=O(xi^(-2)delta^(-5)epsilon^(-2))`,

with no logarithmic factor in epsilon. All theorem-critical obligations are closed.
