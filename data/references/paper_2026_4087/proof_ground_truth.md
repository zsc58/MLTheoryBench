# Reference Proof

## Proof Structure

1. Derive the scalar conjugacy identity and the candidate dual with the prescribed multiplier convention.
2. Establish primal attainment and positive optimal marginals, then obtain dual attainment, strong duality, the KKT relations, and uniqueness.
3. Establish local boundedness and continuity of the dual maximizer and justify differentiation under the specified mass perturbation.
4. Identify the derivative with the negative score and interpret its sign.

## Complete Proof

The segment data, their labels, their empirical label-conditioned distributions, and the representation are fixed. Thus D is a fixed finite nonnegative matrix, including when c=0. Only the outer marginal reference masses vary. Write r=T1_m and s=T^T1_n, and let

P_{a,b}(T)=sum_{p,q}D_{pq}T_{pq}+kappa sum_p a_p h(r_p/a_p)+kappa sum_q b_q h(s_q/b_q),

where h(t)=t log t-t+1 for t>0 and h(0)=1. All entries of a and b are positive and each vector sums to one.

### 1. Scalar conjugacy and weak duality

For a scalar alpha>0 and u in R, minimize kappa alpha h(t/alpha)+ut over t>=0. Its derivative for t>0 is kappa log(t/alpha)+u, so its unique minimum is at t=alpha exp(-u/kappa), with value alpha psi_kappa(u), where psi_kappa(u)=kappa(1-exp(-u/kappa)). Consequently,

kappa alpha h(t/alpha) >= alpha psi_kappa(u)-ut,

with equality exactly when t=alpha exp(-u/kappa).

Introduce independent marginal variables r and s with multiplier terms f·(r-T1_m)+g·(s-T^T1_n). Minimization in r and s gives the scalar values above; minimization over T>=0 is finite exactly when f_p+g_q<=D_{pq}. The candidate dual is therefore

maximize F_{a,b}(f,g)=sum_p a_p psi_kappa(f_p)+sum_q b_q psi_kappa(g_q)
subject to f_p+g_q<=D_{pq} for every p,q.

For any primal and dual feasible pair, the scalar inequalities give

P_{a,b}(T) >= F_{a,b}(f,g)+sum_{p,q}(D_{pq}-f_p-g_q)T_{pq} >= F_{a,b}(f,g).

This proves weak duality directly. No extra factor kappa occurs outside psi_kappa.

### 2. Attainment, strong duality, KKT relations, and uniqueness

Let M=sum_{p,q}T_{pq}. Convexity of h and sum_p a_p=sum_q b_q=1 give

sum_p a_p h(r_p/a_p)>=h(M),

sum_q b_q h(s_q/b_q)>=h(M).

Since D>=0, P_{a,b}(T)>=2 kappa h(M), which tends to infinity as M tends to infinity. Each entry of a nonnegative T is at most M. The objective is continuous on the closed nonnegative orthant, including at zero, and its sublevel sets are bounded. Since T=0 has finite objective, a minimizing sequence has a convergent subsequence yielding a minimizer T*.

Every row and column marginal of T* is strictly positive. Indeed, suppose r_p*=0 and increase one entry T*_{pq} by t>0. The change in its row penalty is kappa[t log(t/a_p)-t]. The transport-cost change is D_{pq}t. If s_q*>0, its column-penalty change is O(t); if s_q*=0, that change is kappa[t log(t/b_q)-t]. In either case the total change is negative for sufficiently small t, because log t tends to minus infinity. This contradicts optimality. The same argument with rows and columns exchanged rules out a zero column marginal.

At T*, the objective is therefore differentiable in a neighborhood as a function of the matrix entries, with coordinate derivatives

G_{pq}=D_{pq}+kappa log(r_p*/a_p)+kappa log(s_q*/b_q).

One-sided feasible variations imply G_{pq}>=0; if T*_{pq}>0, two-sided variations imply G_{pq}=0. Define

f_p*=-kappa log(r_p*/a_p),

g_q*=-kappa log(s_q*/b_q).

These finite potentials satisfy

f_p*+g_q*<=D_{pq},

T*_{pq}(D_{pq}-f_p*-g_q*)=0,

r_p*=a_p exp(-f_p*/kappa),

s_q*=b_q exp(-g_q*/kappa).

The scalar inequalities in Step 1 are equalities for these marginals, and the complementary-slackness sum vanishes. Hence P_{a,b}(T*)=F_{a,b}(f*,g*). Weak duality now proves strong duality and dual attainment without any additional duality theorem.

Because psi_kappa''(u)=-exp(-u/kappa)/kappa<0 and every mass is positive, F_{a,b} is strictly concave in the full pair (f,g). Its feasible set is convex, so its maximizer is unique. This proves uniqueness of dual potentials, not uniqueness of T*. There is no additive gauge freedom in the objective: the transformation (f,g) -> (f+t1_n,g-t1_m) preserves the constraints but generally changes F_{a,b}.

### 3. Local compactness, continuity, and differentiation

Fix i and let a_i(delta)=1/n+delta and a_p(delta)=1/n-delta/(n-1) for p!=i, with b=Delta_m. These are positive probability vectors for -1/n<delta<(n-1)/n. Let z_delta=(f(delta),g(delta)) be their unique dual maximizer, and set z_0=(f*,g*) for the uniform problem.

The feasible pair (0,0) has objective zero because D>=0. Every maximizer therefore belongs to the superlevel set F_{a,b}>=0. On this set,

sum_p a_p exp(-f_p/kappa)+sum_q b_q exp(-g_q/kappa)<=2.

Choose a neighborhood of delta=0 and eta>0 such that all a_p(delta) and b_q are at least eta there. The preceding inequality gives f_p,g_q>=-kappa log(2/eta). Let D_max=max_{p,q}D_{pq}. Feasibility then gives f_p,g_q<=D_max+kappa log(2/eta). Thus all local maximizers lie in one compact box. These bounds depend only on the fixed finite matrix, kappa, and the chosen local positive lower bound on the masses.

To prove z_delta -> z_0, take any sequence delta_l -> 0. Every convergent subsequence of its maximizers has a feasible limit z_bar. For any fixed feasible z, optimality gives F_{a(delta_l),b}(z_delta_l)>=F_{a(delta_l),b}(z). Passing to the limit along that subsequence yields F_{Delta_n,b}(z_bar)>=F_{Delta_n,b}(z). Hence z_bar is the unique maximizer z_0. Compactness then implies convergence of the full family at zero.

Define

H(f,g)=psi_kappa(f_i)-(1/(n-1))sum_{p!=i}psi_kappa(f_p).

The dependence on delta is exactly affine:

F_{a(delta),b}(z)=F_{Delta_n,b}(z)+delta H(z).

Applying optimality at delta and at zero gives

delta H(z_0) <= W(a(delta),b)-W(Delta_n,b) <= delta H(z_delta).

For either sign of delta, these inequalities imply

|W(a(delta),b)-W(Delta_n,b)-delta H(z_0)| <= |delta| |H(z_delta)-H(z_0)|.

Continuity of H and convergence z_delta -> z_0 make the right side o(|delta|). Therefore the two-sided derivative exists and equals

(d/d delta)W(a(delta),Delta_m)|_{delta=0}
=psi_kappa(f_i*)-(1/(n-1))sum_{p!=i}psi_kappa(f_p*).

This establishes the envelope conclusion directly, without assuming differentiability of the optimizer.

### 4. Score and sign

By the prescribed definition, the displayed derivative equals -v(x_i). Equivalently,

W(a(delta),Delta_m)=W(Delta_n,Delta_m)-delta v(x_i)+o(|delta|).

If v(x_i)>0, the first-order change for positive delta is strictly negative, and the discrepancy is smaller for all sufficiently small positive delta. If v(x_i)<0, the first-order change is positive. If v(x_i)=0, the first-order term vanishes and no strict-change conclusion follows from this derivative alone.

The proof covers zero costs, c=0, repeated segments, tied scores, and nonunique primal plans. It uses neither statistical independence nor entropy regularization.
