# Reference Proof

## Proof Structure

1. Characterize every epsilon-LDP mechanism by a common feasible set Q_m.
2. Establish projection existence and pointwise, hence uniform, Wasserstein dominance.
3. Verify that every WPM is epsilon-LDP.
4. Reduce worst-case projection utility to Dirac inputs without assuming measurable projection choices.
5. Solve the finite Dirac problems, prove the displayed formula and convexity, and verify continuity.
6. Obtain a minimizing base measure and prove the minimax equality.

## Complete Proof

Write alpha=exp(-epsilon/2), beta=exp(epsilon/2), and Q_m=Q_{m,epsilon}. All measures below are Borel measures. Measures on V are extended by zero to Z.

### Standard Background and Its Hypotheses

We use the following standard independent compact-space facts: probability measures on a compact metric space form a weakly compact space; finite Borel measures on a compact metric space are regular; and inequalities between integrals of all nonnegative continuous functions characterize domination of such finite measures. Weak convergence preserves integrals of continuous functions. These facts apply to Z and Z x Z because Z is compact metric, and to the finite base measures and probability measures used below. The cost (x,y) -> d(x,y)^p is bounded and continuous because p is finite and Z is compact. The Radon-Nikodym theorem applies to each output dominated by the finite reference probability measure.

### Step 1: Common-Set Characterization

If every output M[mu] belongs to Q_m, then for any inputs mu,mu' and Borel A subseteq V,

M[mu](A) <= beta m(A) <= (beta/alpha) M[mu'](A) = exp(epsilon) M[mu'](A).

Thus M is epsilon-LDP.

Conversely, let M be epsilon-LDP. Since X is nonempty, choose a reference input mu_0 and set lambda=M[mu_0]. For every input mu, LDP in both directions gives

exp(-epsilon) lambda <= M[mu] <= exp(epsilon) lambda

as measure inequalities. Therefore f_mu=dM[mu]/dlambda exists, and exp(-epsilon)<=f_mu<=exp(epsilon) lambda-almost everywhere for each mu. Likewise, for each pair of inputs,

f_mu <= exp(epsilon) f_mu'

lambda-almost everywhere. The exceptional set can depend on the pair, so an uncountable union of exceptional sets is not justified.

Here is the countable-envelope argument. For any nonempty finite set F of inputs, let h_F=max_{mu in F} f_mu, and set L=sup_F integral h_F dlambda. This supremum is finite because h_F<=exp(epsilon) almost everywhere. Choose finite sets F_n whose integrals tend to L, and let C_+ be their countable union. The function h=sup_{mu in C_+} f_mu is measurable and has integral L: its increasing finite maxima have integrals at most L, while h dominates every chosen h_{F_n}. For any input mu, finite maxima with f_mu still have integral at most L. Monotone convergence gives integral max(h,f_mu) dlambda<=L=integral h dlambda. Hence f_mu<=h almost everywhere. Thus h is the essential upper envelope f^+.

Similarly, take the infimum of integrals of finite minima, choose finite sets approaching that infimum, and form their countable union C_-. Their pointwise infimum l has that limiting integral by bounded convergence. For any input mu, integral min(l,f_mu) is at least the defining infimum, which equals integral l. Therefore f_mu>=l almost everywhere, and l is the essential lower envelope f^-.

Take C=C_+ union C_- union {mu_0}. Its supremum and infimum represent both essential envelopes almost everywhere. All density-ratio inequalities between pairs in C hold outside a single null set, since C is countable. Taking the supremum and infimum on that set gives f^+<=exp(epsilon)f^-. Define g=sqrt(f^+f^-) and m=g lambda. The envelopes are bounded between exp(-epsilon) and exp(epsilon), so g is nonnegative, measurable, and bounded, and m is finite. For every input mu separately,

alpha g <= f_mu <= beta g

almost everywhere. Integrating over each Borel A subseteq V gives alpha m(A)<=M[mu](A)<=beta m(A). Thus every output belongs to Q_m. In particular Q_m is nonempty, and applying its inequalities to V gives 1/beta<=m(V)<=1/alpha. No simultaneous choice of density versions for all inputs is required.

### Step 2: Projection Existence and Dominance

Fix any finite nonnegative m on V with Q_m nonempty. Regard Q_m as a subset of P(Z). It consists exactly of probabilities nu satisfying alpha m<=nu<=beta m as measures on Z. The upper bound implies nu(Z outside V)=0, so these probabilities are precisely the required laws on V.

For each nonnegative continuous h on Z, the inequalities alpha integral h dm<=integral h dnu<=beta integral h dm define a weakly closed condition. By regularity these conditions are equivalent to the measure inequalities. Thus Q_m is weakly closed in the weakly compact P(Z), hence compact. It is convex by its defining measure inequalities. This argument does not require V to be closed or compact.

For a fixed input mu, consider all probabilities pi on Z x Z whose first marginal is mu and whose second marginal belongs to Q_m. This set is nonempty, since mu tensor nu is feasible for any nu in Q_m. It is weakly closed and compact: marginals vary continuously under weak convergence, the first marginal is fixed, and Q_m is closed. The integral of the bounded continuous cost d(x,y)^p is continuous on this set, so it attains its minimum at some pi*. Its second marginal nu* minimizes the Wasserstein cost over Q_m. This proves that the WPM is defined for every input; any choice of minimizer may be used.

For M and m from Step 1, the output M[mu] is feasible for this projection. Consequently

W_p(M_{m,epsilon}[mu],mu) <= W_p(M[mu],mu)

for every input mu. Taking suprema gives U[M_{m,epsilon}]<=U[M].

### Step 3: WPM Privacy

Every WPM output lies in Q_m. Therefore, for any two inputs and Borel A subseteq V,

M_{m,epsilon}[mu](A) <= beta m(A) <= exp(epsilon) M_{m,epsilon}[mu'](A).

Thus every WPM used below is epsilon-LDP, regardless of the choices among minimizers.

### Step 4: Dirac Reduction

For any fixed feasible m, put

R=sup_{x in X} min_{nu in Q_m} integral_V d(x,y)^p nu(dy).

A coupling with one marginal delta_x is uniquely determined by its other marginal. Hence R=sup_{x in X} W_p(M_{m,epsilon}[delta_x],delta_x)^p. All these quantities are finite by compactness of Z.

To avoid any unsupported measurability assertion about x -> M_{m,epsilon}[delta_x], fix eta>0 and choose a finite Borel partition A_1,...,A_N of X into nonempty cells of diameter at most eta. Such partitions exist by compactness of X, using a finite cover by sufficiently small metric balls and disjointizing it. Choose x_l in A_l and an optimal Dirac projection q_l in Q_m. For any input mu, set rho=sum_l mu(A_l)q_l. The common measure bounds imply rho in Q_m.

Define a coupling by using q_l as the conditional output law on A_l; explicitly its integrals are sum_l integral_{A_l} integral_V h(x,y)q_l(dy)mu(dx). This is a well-defined finite mixture with marginals mu and rho. Let omega(eta) be the supremum of |d(x,y)^p-d(x',y)^p| over x,x' in X with d(x,x')<=eta and y in Z. Uniform continuity gives omega(eta)->0 as eta->0. The coupling cost is at most

sum_l mu(A_l) integral_V d(x_l,y)^p q_l(dy) + omega(eta) <= R+omega(eta).

Projection optimality gives W_p(M_{m,epsilon}[mu],mu)^p<=R+omega(eta). Letting eta tend to zero proves the upper inequality. The reverse inequality follows by taking Dirac inputs. Therefore U[M_{m,epsilon}]^p=R.

In the finite specialization, an exact version suffices: choose a Dirac optimizer q^(i) for each i, form rho=sum_i mu_i q^(i), and use the coupling pi_ij=mu_i q_j^(i). This gives the same result directly, with no limiting argument.

### Step 5: Finite Feasibility, Formula, Convexity, and Continuity

On V={1,...,k_v}, the set Q_m is exactly the probability vectors satisfying alpha m_j<=q_j<=beta m_j for every j. Singleton sets give the necessity, and summing coordinate inequalities gives the converse.

Necessity of m in D follows by summing these bounds. Conversely, for m in D, set s=1-alpha sum_j m_j and b_j=(beta-alpha)m_j. The mass constraints imply 0<=s<=sum_j b_j. Therefore residual masses r_j with 0<=r_j<=b_j and sum_j r_j=s exist, and q_j=alpha m_j+r_j is feasible. Thus feasibility is exactly m in D.

For input delta_i, the only coupling with an output q has cost sum_j c_ij q_j. Fix the displayed nondecreasing ordering, write a_t=c_{i,sigma_i(t)}, B_t=sum_{r<=t}b_{sigma_i(r)}, and set B_0=0. The greedy residual allocation is

r_{sigma_i(t)}=min{b_{sigma_i(t)},(s-B_{t-1})_+}.

It satisfies the capacity bounds, and its first t coordinates have total residual mass min{s,B_t}. In particular its total is s. For any feasible residual allocation, let R_t be its first t coordinates' total mass. Then R_t<=min{s,B_t}. The elementary summation identity

sum_{t=1}^{k_v} a_t r_{sigma_i(t)} = a_{k_v}s - sum_{t=1}^{k_v-1}(a_{t+1}-a_t)R_t

shows that the greedy allocation minimizes cost, since each difference a_{t+1}-a_t is nonnegative and every prefix total is maximal. For k_v=1 the last sum is empty. Equal costs give zero differences, so ties cause no issue; zero capacities and s=0 or s=sum_j b_j are also included. Adding the baseline cost alpha sum_j m_j c_ij gives exactly phi_i(m) as defined in the task. Hence phi_i(m)=W_p(M_{m,epsilon}[delta_i],delta_i)^p, and Step 4 gives U[M_{m,epsilon}]=f(m)^(1/p).

For convexity, take m,m' in D and optimal vectors q,q' for a fixed Dirac problem. For theta in [0,1], the vector q_theta=theta q+(1-theta)q' is feasible at m_theta=theta m+(1-theta)m', because all coordinate bounds and the probability normalization are affine. Thus

phi_i(m_theta) <= sum_j c_ij q_theta,j = theta phi_i(m)+(1-theta)phi_i(m').

Each phi_i is convex, and their finite maximum f is convex. For continuity, keep the sorted order fixed independently of m. The displayed greedy expression is a finite sum of affine functions and compositions of continuous minimum and positive-part functions. Thus every phi_i and f are continuous on all of D, including its boundary.

### Step 6: Attainment and Minimax Equality

The domain D is nonempty: any probability vector m has total mass 1 in [1/beta,1/alpha]. It is closed and bounded, with 0<=m_j<=1/alpha, so it is compact. Continuity of f therefore yields m* in argmin_D f.

For any epsilon-LDP mechanism M', Step 1 supplies a common base measure m. In the finite setting its coordinates belong to D. Steps 2, 4, and 5 give

U[M'] >= U[M_{m,epsilon}] = f(m)^(1/p) >= f(m*)^(1/p).

The WPM at m* is itself epsilon-LDP by Step 3 and has utility f(m*)^(1/p). Taking the infimum over all epsilon-LDP mechanisms proves

U[M_{m*,epsilon}] = inf_{M' epsilon-LDP} U[M'] = min_{m in D} f(m)^(1/p).

## Private Source-Repair Notes

The source's threshold minimum over unrestricted real t is undefined at alpha sum_j m_j=1: its qualifying set is all real numbers. Restricting that minimum to the finite row-cost set repairs the threshold and gives the same greedy cost. The public task retains its already well-defined greedy formula rather than exposing this source correction.

The general Dirac-reduction derivation above replaces the source's unjustified integral of arbitrary projection choices by finite mixtures and uniform continuity. The attainment derivation explicitly supplies continuity, which the source's final compactness inference omitted. These are local repairs preserving the original theorem and proof route.

All theorem-critical obligations are closed; there is no unresolved private GT obligation.
