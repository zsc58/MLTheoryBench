# Reference Proof

## Proof Structure and Critical Obligations

1. Verify that the scalar recursion defines finite nonnegative weights and a positive normalizer on its entire domain, including diagonal and singleton cases.
2. Derive the learned-versus-ideal KL decomposition with prediction error evaluated under the data law, not generated states.
3. Verify privately that the public revealed-batch prediction error agrees with the source's all-masked-coordinate normalization for this schedule.
4. Derive the ideal fixed-schedule KL recursion, with residual contexts averaged under the true first-batch law.
5. Explicitly expand and telescope the subset entropies, including both endpoint coefficients.
6. Explicitly prove the harmonic coefficient bound, including K=2 and K=L'.
7. Apply convexity to the schedule mixture and handle zero probabilities and infinite learned KL.

Every obligation is derived below. No paper-specific result is assumed without proof.

## 1. Scalar Identities and Schedule Well-Definedness

Abbreviate f_tc by f. For a fixed pair (k,n), where 2<=k<=n, write

m=n-k+1,

t_ell=f(k-1,n-ell),

w_ell=w_ell^tc(k,n),

Psi=Psi_tc(k,n),

A=1+(n-2)t_1.

We induct on k to establish 0<=f(k,n)<1 for k>=2, f(k,k)=0, and well-defined schedule probabilities. At level 1, all coefficients are nonnegative, and f(1,1)=0. Assume the preceding level is well-defined and nonnegative, with f(k-1,k-1)=0. Every denominator occurring in a weight product has the form 1+(n-i-2)f(k-1,n-i-1), with n-i>=k>=2. It is therefore at least 1. The weights are finite and nonnegative; w_1=1 ensures Psi>=1. Moreover t_m=0 and A>=1.

For 1<=ell<m, the weight recurrence gives

w_ell(n-ell)t_ell = w_{ell+1}[1+(n-ell-2)t_{ell+1}].

Set D_ell=w_ell(n-ell-1)t_ell. The preceding identity implies

w_ell t_ell = w_{ell+1}+D_{ell+1}-D_ell.

Since t_m=0, summation yields

sum_{ell=1}^m w_ell t_ell = Psi-1-(n-2)t_1 = Psi-A.                 (1)

This also holds when m=1: both sides are zero. Thus the defining update can be written

f(k,n)=(Psi-A)/Psi=(sum_ell w_ell t_ell)/Psi>=0.

Because A>0, f(k,n)<1. On the diagonal n=k, m=1 and t_1=0, so Psi=A=1 and f(k,k)=0. This completes the induction and proves that every prescribed batch-size probability is well-defined. The batch-size restriction leaves at least k-1 indices, so recursion terminates with exactly k nonempty batches.

We will also need a second scalar identity. Define

F_ell=w_ell(n-ell)[1+(n-ell-1)t_ell].

For ell<m, the same weight recurrence gives

F_ell-F_{ell+1}=w_ell(n-ell).

Since F_m=w_m(n-m), summing, including the final term, gives

sum_{ell=1}^m w_ell(n-ell)=F_1=(n-1)A.

Equivalently,

sum_{ell=1}^m w_ell ell=n Psi-(n-1)A.                            (2)

Again this includes m=1.

## 2. Learned-versus-Ideal Decomposition

Fix a schedule S=(B_1,...,B_K), and let U_{k-1}=union_{j<k}B_j. Write Q_S for the learned output law and Q_S^star for the ideal output law. Their probability masses factor as

Q_S(x)=product_k product_{i in B_k} hat p_i(x_i|x_{U_{k-1}}),

Q_S^star(x)=product_k product_{i in B_k} p(X_i=x_i|X_{U_{k-1}}=x_{U_{k-1}}).

For every x with p_data(x)>0, every true conditional factor in Q_S^star(x) is positive. Hence KL(p_data||Q_S^star) is finite on the finite alphabet. Arbitrary choices of true conditional kernels on zero-probability contexts do not affect this KL calculation.

Expanding the expected log ratio, and then conditioning on X_{U_{k-1}}, gives

KL(p_data||Q_S)
=KL(p_data||Q_S^star)
 +sum_k sum_{i in B_k} E_{X~p_data} KL(p(X_i|X_{U_{k-1}})||hat p_i(.|X_{U_{k-1}})).                 (3)

If a learned factor vanishes on a positive-data-probability event, the learned KL and the corresponding prediction term are infinite, and (3) remains valid as an additive extended-real identity. No subtraction of infinite quantities is used.

Averaging (3) over the schedule gives

E_S KL(p_data||Q_S)=E_S KL(p_data||Q_S^star)+epsilon_pred(pi_tc). (4)

### Agreement with the Source Prediction-Error Normalization

The source definition uses all currently masked coordinates. Writing I_k=[L]\U_{k-1} and using its time probabilities |B_k|/L, that definition becomes

E_S sum_k (|B_k|/|I_k|) sum_{i in I_k} E_X KL(p(X_i|X_{U_{k-1}})||hat p_i(.|X_{U_{k-1}})).

Conditional on the preceding index sets and |B_k|=ell, B_k is uniform among the ell-subsets of I_k. Each i in I_k is included with probability ell/|I_k|. The coordinate prediction-error terms depend on the preceding context, but not on the next batch selection. Therefore the conditional expectation of their sum over B_k equals ell/|I_k| times their sum over I_k. Applying this at every step proves that the source definition equals the public revealed-batch definition for the selected schedule.

This equality is an averaged uniform-subset identity, not a fixed-schedule identity and not a general assertion for arbitrary state-dependent schedules.

## 3. Correct Ideal KL Recursion

For a positive-probability context X_{I^c}=x_{I^c}, define

G_k(I,x_{I^c})=E_{S~pi_tc(k,I)} KL(p_{X_I|x_{I^c}}||Q_{I,x_{I^c},S}^star),

where Q_{I,x_{I^c},S}^star is the ideal output law obtained by starting from that context and following the fixed residual schedule S. The expectation here is over schedules only. Token randomness has already been integrated into the output law.

With one remaining step,

G_1(I,x_{I^c})=sum_{i in I}H(X_i|x_{I^c})-H(X_I|x_{I^c})
=TC(p_{X_I|x_{I^c}}).

This equals f(1,|I|)TC, also when |I|=1 because singleton TC is zero.

For k>=2, fix the first batch B and the residual schedule. Factor the true conditional law into its joint first-batch marginal and its residual conditional law. Factor the ideal law into the product of first-batch conditional marginals and the residual ideal law. Expanding the KL log ratio yields

G_k(I,x_{I^c})
=E_B[TC(p_{X_B|x_{I^c}})
 +E_{X_B~p_{X_B|x_{I^c}}}G_{k-1}(I\B,(x_{I^c},X_B))].          (5)

The inner expectation is under the true data law, not the ideal product-marginal first-batch law. The residual schedule depends only on the remaining indices, so its prescribed distribution is unchanged by conditioning on token values.

## 4. Explicit Subset-Entropy Telescoping

Induct on k to prove

G_k(I,x_{I^c})=f(k,|I|)TC(p_{X_I|x_{I^c}}).                    (6)

The base case was proved above. For the inductive step, fix a context and suppress it in the entropy notation. Put n=|I| and use the scalar notation from Section 1. Define the average subset entropy

h_r=(1/binom(n,r)) sum_{T subseteq I, |T|=r} H(X_T),

so h_1=(1/n)sum_{i in I}H(X_i) and h_n=H(X_I).

For a uniform first batch B of size ell, let a_ell be the average of

TC(X_B)+t_ell TC(X_{I\B}|X_B).

By the induction hypothesis and (5), G_k=(1/Psi)sum_ell w_ell a_ell. Expanding both TC terms and using H(X_j|X_B)=H(X_{B union {j}})-H(X_B) gives

a_ell=ell h_1-t_ell h_n-[1+(n-ell-1)t_ell]h_ell+(n-ell)t_ell h_{ell+1}.                    (7)

Here each coordinate belongs to a uniform ell-subset with probability ell/n. Also, each (ell+1)-subset T is obtained from exactly ell+1 pairs (B,j), where |B|=ell and j is outside B. Consequently the average of sum_{j outside B}H(X_{B union {j}}) is (n-ell)h_{ell+1}. In the unnormalized version of this calculation, the entropy in the sum indexed by T is H(X_T), retaining the previously recorded local source correction.

The recurrence

w_ell(n-ell)t_ell=w_{ell+1}[1+(n-ell-2)t_{ell+1}]

cancels every intermediate h_{ell+1} term in the weighted sum of (7). The upper endpoint vanishes because t_m=0; the lower endpoint contributes -A h_1. Therefore

sum_ell w_ell a_ell
=(sum_ell w_ell ell-A)h_1-(sum_ell w_ell t_ell)h_n.

Substitute the explicitly proved scalar identities (1) and (2):

sum_ell w_ell a_ell
=n(Psi-A)h_1-(Psi-A)h_n
=(Psi-A)[sum_{i in I}H(X_i)-H(X_I)].

Division by Psi proves (6). It covers the diagonal m=1 as well: Psi-A=0. All conditional expectations in this induction concern positive-probability data contexts.

Taking I=[L] gives

E_S KL(p_data||Q_S^star)=f(K,L)TC(p_data).                      (8)

## 5. Complete Harmonic Coefficient Bound

We prove, for all 2<=k<=n,

R(k,n):=Psi_tc(k,n)/[1+(n-2)f(k-1,n-1)]
 <=[k+H_{n-k+1}-2]/(k-1).                                    (9)

Since f(k,n)=1-1/R(k,n), this implies

f(k,n)<=[H_{n-k+1}-1]/[k+H_{n-k+1}-2].                       (10)

Every denominator in (9) and (10) is positive.

For k=2 and n>=3, the base coefficients give

w_ell^tc(2,n)=(n-1)/(n-ell), 1<=ell<=n-1,

and A=n-1. Thus R(2,n)=H_{n-1}, which is exactly the right side of (9). For n=2, Psi=A=1 and R(2,2)=1=H_1. This separately checks the singleton coefficient appearing at that boundary.

For n=k, Section 1 gives Psi=A=1 and R(k,k)=1, again exactly the right side of (9).

Now use strong induction on k+n, with n>k>2. Put m=n-k+1>=2 and t=f(k-1,n-1). Extracting the first factor from each nonempty weight product and reindexing the remaining products gives

Psi_tc(k,n)
=1+[(n-1)t/(1+(n-3)f(k-1,n-2))]Psi_tc(k,n-1).                 (11)

The induction hypothesis for (k,n-1) yields

Psi_tc(k,n)<=1+(n-1)t[k+H_{m-1}-2]/(k-1).                     (12)

To obtain (9), it suffices to show that the right side of (12) is at most

[1+(n-2)t][k+H_m-2]/(k-1).

After multiplying by k-1 and collecting terms, the required inequality is

t[(n-1)(k+H_{m-1}-2)-(n-2)(k+H_m-2)]<=H_m-1.

Using H_m=H_{m-1}+1/m and n=m+k-1, the bracket equals

k-3+H_m-(k-2)/m.

Since t>=0, its product with t is at most (k-3+H_m)t. The induction hypothesis for (k-1,n-1), whose harmonic index is also m, gives

t<=(H_m-1)/(k-3+H_m).

The last denominator is positive. Hence the required product is at most H_m-1. This proves (9), and consequently (10), on the full domain.

In particular, when K=L, the numerator is H_1-1=0 and the denominator is K-1>0. No undefined endpoint quotient occurs.

## 6. Final Bound and Mixture

Combine (4), (8), and (10):

E_S KL(p_data||p_{Y_out^S})
<=[(H_{L-K+1}-1)/(K+H_{L-K+1}-2)]TC(p_data)+epsilon_pred(pi_tc(K,[L])).

This remains valid when epsilon_pred is infinite. When TC is zero, (8) gives zero ideal intrinsic KL directly.

The output law is the finite schedule mixture p_{Y_out}(x)=E_S p_{Y_out^S}(x). For every x with p_data(x)>0, convexity of -log gives

-log(E_S p_{Y_out^S}(x))<=E_S[-log p_{Y_out^S}(x)],

with the usual extended-real interpretation at zero. Multiply by p_data(x), sum over x, and add sum_x p_data(x)log p_data(x). This yields

KL(p_data||p_{Y_out})<=E_S KL(p_data||p_{Y_out^S}).

Together these are the two requested inequalities for every 2<=K<=L.
