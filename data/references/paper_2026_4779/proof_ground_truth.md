# Reference Proof

## Proof structure

Use the unlabeled sound certifier to control learning on a random empirical marginal. Compare its distribution-fixed optimum with OIG's transductive error by conditioning on omission of an occurrence index. Finally apply leave-one-out exchangeability and bound the probability of an index collision.

All randomization below is independent of the sampled instances unless explicitly conditioned otherwise. Repeated instance values are allowed throughout.

## 1. Certifiability and the empirical comparison

If H is empty, the stipulated error is zero and the claim is immediate. Assume H is nonempty. Fix a certifiable rate epsilon, a marginal D, m>=1, and eta in (0,1). Choose the learner A and unlabeled certifier C witnessing certifiability at D. This is a single pair valid for every sample size, and C is sound for A at every marginal Q. In particular,

E_{T~D^m} C(T) <= epsilon(D,m),

and

 epsilon_A(Q,m) <= E_{T~Q^m} C(T)

for every Q.

Set M=ceil(e m^2/eta) and n=M-1. Since e m^2/eta>m+1 for m>=1, we have M-1>=m and M>=3. For U=(x_1,...,x_M), let Q_U=M^{-1} sum_i delta_{x_i}, with multiplicities retained, and define

 R_C(U)=E_{T~Q_U^m} C(T)
       =M^{-m} sum_{j_1,...,j_m in [M]} C(x_{j_1},...,x_{j_m}).

This is a measurable function of U because it is a finite average of measurable certificate evaluations.

For a fixed finite marginal Q, define

 epsilon*(Q,k)=inf_B sup_{h in H} E_{T~Q_h^k,B}[L(B(T),Q_h)],

where B ranges over the learners allowed in the setup and may be chosen with knowledge of Q. This is a pointwise infimum; no attainment is assumed. Ignoring additional training examples proves that epsilon*(Q,k) is nonincreasing in k. Consequently, for every U,

 epsilon*(Q_U,M-1) <= epsilon*(Q_U,m)
                  <= epsilon_A(Q_U,m)
                  <= R_C(U).                                      (1)

The last inequality uses global soundness for the original fixed learner A, not a certificate newly selected after seeing U.

## 2. The collision mixture

Draw U~D^M and, independently, J_1,...,J_m iid uniform on [M]. Let E be the event that the indices J_1,...,J_m are all distinct, and let

 Gamma=Pr(E)=(M)_m/M^m.

Conditional on any distinct index tuple, the selected entries of U are independent with common law D. Thus

 E[C(x_{J_1},...,x_{J_m}) 1_E]
 =Gamma E_{T~D^m} C(T).

Since 0<=C<=1, the contribution of E's complement is at most 1-Gamma. Therefore

 E_{U~D^M} R_C(U)
 <= Gamma epsilon(D,m)+1-Gamma.                    (2)

This argument conditions on distinct indices, not distinct instance values. In particular, it remains valid for atomic D and for repeated values in U. It also applies when m=1: then Gamma=1 and the complementary contribution is zero, so conditioning on a null event is unnecessary.

## 3. Why the randomized orientation gives transductive optimality

Fix U of size M. Its set of realizable label vectors is finite. For any withheld coordinate i and any realizable visible labeling, there is either one possible full label vector or two. In the first case a rule can predict the forced label with zero error. In the second case the two possible vectors differ exactly at i and form an edge of the one-inclusion graph.

A randomized prediction in this second case is exactly a choice of probabilities for orienting that edge toward its two endpoints. Conversely, any fractional orientation specifies these prediction probabilities. Dependence between random decisions at different edges does not affect their expected errors. Any transductive rule can therefore be represented by a fractional orientation after correcting predictions at forced labels, which cannot increase its error for any h. This proves that the orientation minimizing OIG's worst-case error is optimal among all randomized transductive rules for U.

This also explains why replacing fractional orientations by integral ones is not justified for the stated constant. The finite optimization has a minimizer: its variables lie in a finite product of closed intervals, and its objective is the maximum of finitely many continuous affine functions. Averaging a minimizing rule over permutations of the occurrences preserves optimality and gives permutation-equivariant multiset semantics.

## 4. Indexed omission comparison

Continue with fixed U, and put k=M-1. For delta>0 choose a learner B, fixed for Q_U, with

 epsilon_B(Q_U,k) <= epsilon*(Q_U,k)+delta.

Such a learner exists by the definition of infimum. Construct a transductive comparison rule for this U as follows. When occurrence i is withheld, draw k labeled examples independently and uniformly from the other M-1 occurrences, run B on that sequence, and predict at x_i. This rule knows U, but it never uses the withheld label.

To analyze it, draw independent uniform indices K_1,...,K_k from [M]. Let E_i be the event that none equals i. Its probability is

 p=(1-1/M)^(M-1)
  =(1+1/(M-1))^{-(M-1)} >= e^{-1},

where the last inequality follows from log(1+t)<=t. Conditional on E_i, these indices are iid uniform on [M] excluding i. This statement concerns omission of an occurrence, so it remains correct even if another occurrence has the same instance value as x_i.

For fixed h, let a_i be the conditional probability, over B's randomness, that B trained on ((x_{K_j},h(x_{K_j})))_{j=1}^k predicts x_i incorrectly. Nonnegativity gives

 E[a_i | E_i]=E[a_i 1_{E_i}]/p <= E[a_i]/p.

Averaging over i shows that the comparison rule's transductive error against h is at most

 (1/p) E_{T~(Q_U)_h^k,B}[L(B(T),(Q_U)_h)].

Taking the worst case over h, using p>=1/e, and then using OIG's optimality proves

 epsilon_OIG^Trans(U)
 <= e(epsilon*(Q_U,M-1)+delta).

Let delta decrease to zero. Since this is a pointwise statement for fixed U, no measurable selection of B as a function of U is required. Together with (1), it yields

 epsilon_OIG^Trans(U) <= e epsilon*(Q_U,M-1) <= e R_C(U).       (3)

## 5. Leave-one-out conversion with the correct quantifier order

Fix h in H. For U~D^M, let b_h(U) be the average, over its M withheld occurrences, of OIG's prediction-error probability when the other occurrences are labeled by h. Each summand is measurable by the public measurability assumptions. Permutation-equivariant prediction and iid sampling imply

 E_{U~D^M} b_h(U)
 =E_{S~D_h^{M-1},OIG}[L(OIG(S),D_h)].

Indeed, each term in the average has the law of an iid training sample of size M-1 and an independent test point. Pointwise, (3) gives b_h(U)<=e R_C(U). Hence

 E_{S~D_h^{M-1},OIG}[L(OIG(S),D_h)]
 <= e E_{U~D^M} R_C(U).

The right side does not depend on h. Taking the supremum over h only now gives

 epsilon_OIG(D,M-1)
 <= e E_{U~D^M} R_C(U)
 <= e Gamma epsilon(D,m)+e(1-Gamma).                    (4)

This proof integrates only fixed-hypothesis losses and the measurable certificate average. It does not exchange a supremum and expectation, and it does not require measurability of an empirical optimizer or an uncountable supremum. In the usual formulation where the empirical optimum is measurable, the intermediate comparison epsilon_OIG(D,M-1)<=e E_U epsilon*(Q_U,M-1) follows from the same pointwise argument.

## 6. Constants, small samples, and the exact budget

An index collision requires J_a=J_b for some a<b. A union bound therefore gives

 1-Gamma <= binom(m,2)/M.

Since M>=e m^2/eta,

 e(1-Gamma) <= e m(m-1)/(2M) <= eta/2 <= eta.

Also Gamma<=1 and epsilon(D,m)>=0. Applying these facts to (4) proves

 epsilon_OIG(D,ceil(e m^2/eta)-1)
 <= e epsilon(D,m)+eta.

Every step applies to m=1 and m=2 as well as to larger sample sizes. We have proved the claim at exactly the requested training budget; no monotonicity of OIG's population error is used. The same argument works for any integer M>=e m^2/eta with M-1>=m, so the source's alternative ceiling-budget convention can also be obtained directly, not by asserting monotonicity.

All choices and bounds respect the required quantifiers: epsilon, D, m, and eta were arbitrary, and OIG is fixed independently of epsilon and D. This establishes relative (e,sigma)-smartness for sigma(m,eta)=ceil(e m^2/eta)-1.

## Proof-obligation audit

Closed obligations: the globally sound unlabeled witness; the collision mixture including its additive slack; monotonicity only of the distribution-fixed optimum; fractional-orientation optimality; admissible simulation without the withheld label; the indexed omission probability and conditional-loss inequality; the infimum limit; measurable leave-one-out integration with the supremum in the correct position; and the exact integer budget for every m>=1. No specialized external reduction is left as an unexplained invocation.
