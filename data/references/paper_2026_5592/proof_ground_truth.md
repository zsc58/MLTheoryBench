# Reference Proof

## Proof structure and normalization

Use a conditional log-MGF relaxation separately on each epoch. Its exponential potential uses predictable, not realized, learner loss. Paired conditional rollouts and ordinary agnostic ERM implement the prediction rule with controlled mean-square error. The KL chain rule combines epochs, and a directly proved multi-rate weights procedure removes knowledge of the divergence. A threshold-tree block construction, with an explicit simulator normalization, gives the converse.

Throughout this proof, `ln` is the natural logarithm, `exp` is its inverse, and KL is measured in bits as in the public task. Write kappa=KL(Q||R). Thus natural relative entropy equals (ln 2)kappa.

## Standard independent background

We use the following standard results, in the stated forms.

1. For bounded measurable Z, eta>0, and Q absolutely continuous with respect to R,
   E_Q Z <= eta^{-1} ln E_R exp(eta Z)+(ln 2)KL(Q||R)/eta.
2. If a function F of independent coordinates has coordinate oscillations c_i, then
   ln E exp(lambda(F-EF)) <= lambda^2 sum_i c_i^2/8.
3. There is a universal A such that, for every deterministic m-point sequence and nonempty binary class of VC dimension d>=1,
   E_epsilon sup_h sum_{i=1}^m epsilon_i(2h(x_i)-1)/2 <= A sqrt(dm),
   where the signs are independent and fair.
4. For consecutive blocks B_j and preceding indices H_j, finite total divergence satisfies
   KL(Q||R)=sum_j E_Q KL(Q_{B_j}(.|X_{H_j})||R_{B_j}(.|X_{H_j})).

All entropy applications below concern bounded finite-horizon regret. All concentration applications condition on the entire covariate sequence and use independent auxiliary signs, not independence of the covariates. The class in every VC application is the given class. Finite total KL ensures the required absolute continuity and conditional absolute continuity almost surely under Q.

## 1. Boundary cases

If d=0, any two hypotheses agree at every point: disagreement at one point would shatter that singleton. Obtain a hypothesis by an ERM call on the empty sample and follow it. Its regret is identically zero, for any Q and R.

For d>=1, infinite KL gives a vacuous upper bound. Also Reg_T<=T for every prediction strategy. Consequently d>=T is trivial. For the remaining algorithm assume 1<=d<T. In verifying its bound, kappa>=T is likewise covered by Reg_T<=T; the algorithm need not know whether this case occurs.

## 2. One epoch: ideal prediction and exponential admissibility

Fix an epoch [a,b] of length L=b-a+1 and a covariate prefix through a-1. Define the epoch comparator loss

L_t(h)=sum_{s=a}^t 1{h(X_s)!=Y_s},  with L_{a-1}(h)=0.

All simulator continuations below are conditional on the full observed covariate prefix X_{1:t} and truncated at b. Put

Rel_t=eta^{-1} ln E exp(eta sup_h[sum_{s=t+1}^b epsilon_s(2h(X_s)-1)/2-L_t(h)]).

The expectation is over that conditional simulator continuation and independent fair signs. At t=a-1 this definition uses the entire epoch continuation and zero historical loss. Every supremum is over a bounded finite-sample criterion, whose minimum can be obtained by ERM, so the assumed measurable oracle model makes these quantities measurable.

After observing X_t, let

G_y=sup_h[sum_{s=t+1}^b epsilon_s(2h(X_s)-1)/2-L_{t-1}(h)-1{h(X_t)!=y}],

M_y=E exp(eta G_y),  and r_y=eta^{-1} ln M_y.

Write ell(q,y)=q when y=0 and ell(q,y)=1-q when y=1. The two label objectives are q+r_0 and 1-q+r_1. They are equal at

q_t=1/2+(ln M_1-ln M_0)/(2eta).

Pointwise |G_1-G_0|<=1, whence exp(-eta)<=M_1/M_0<=exp(eta), and q_t belongs to [0,1]. Thus the equalizing probability minimizes the maximum label objective, whose value is

V_t=1/2+(r_0+r_1)/2.

For a fresh fair sign epsilon_t and y=(1+epsilon_t)/2,

1{h(X_t)!=y}-1/2=-epsilon_t(2h(X_t)-1)/2.

Therefore exp(eta(r_y+1/2)) is the conditional exponential moment of the same supremum with the signed sum extended to s=t. The geometric-mean/arithmetic-mean inequality gives

exp(eta V_t)
<= (1/2) sum_{y=0}^1 exp(eta(r_y+1/2)).

Integrate over X_t under R(.|X_{1:t-1}) and use the conditional-kernel tower rule. The right-hand side becomes exp(eta Rel_{t-1}). Hence

E_{R}[exp(eta sup_y[ell(q_t,y)+Rel_t(y)]) | X_{1:t-1},Y_{a:t-1}]
<= exp(eta Rel_{t-1}).

For the actual fixed labeling function, define predictable epoch loss

bar L_t=sum_{s=a}^t ell(q_s,Y_s).

Then Phi_t=exp(eta bar L_t+eta Rel_t) is a supermartingale under R, conditional on the epoch's starting prefix. At its terminal time,

Phi_b=exp(eta[bar L_b-min_h L_b(h)]).

This statement is about predictable loss. It does not assert that replacing bar L_t by the realized randomized loss preserves the supermartingale.

## 3. Initial MGF and change of measure

For any deterministic epoch sequence z, let

U(z,epsilon)=sup_h sum_{s=a}^b epsilon_s(2h(z_s)-1)/2.

Changing one sign changes U by at most one. Conditional bounded differences and the VC bound therefore give

E_epsilon exp(eta U) <= exp(eta A sqrt(dL)+eta^2 L/8),

uniformly in z. Averaging over the possibly dependent simulator covariates preserves this bound, so

Rel_{a-1}<=A sqrt(dL)+eta L/8.

For the given starting prefix let

kappa_a=KL(Q_{a:b}(.|X_{1:a-1})||R_{a:b}(.|X_{1:a-1})).

Apply the entropy inequality to Z=bar L_b-min_h L_b(h), a bounded measurable function of the epoch trajectory with the prefix fixed. The supermartingale estimate yields

E_Q Z <= A sqrt(dL)+eta L/8+(ln 2)kappa_a/eta.

Because g is fixed and each prediction is drawn after observing X_t but before receiving its label, expected realized learner loss equals expected predictable loss. The same display therefore bounds the ideal learner's conditional expected epoch regret. If a conditional divergence is infinite, its bound is interpreted as vacuous.

## 4. ERM implementation and paired moment estimation

For each t draw N independent conditional continuations, each truncated at b, and independent sign vectors. Use the same continuation and signs to evaluate G_0 and G_1 in each pair. If m=b-t and the future artificial labels are (1+epsilon_s)/2, then

G_y=m/2-min_h[sum_{s=a}^{t-1}1{h(X_s)!=Y_s}+1{h(X_t)!=y}+sum_{s=t+1}^b1{h(X_s)!=(1+epsilon_s)/2}].

Thus one ordinary, unweighted agnostic ERM call and evaluations on a sample of length L compute each G_y. No access to g on simulated points is used.

Let A_i=exp(eta G_1^{(i)}), B_i=exp(eta G_0^{(i)}), and let bars denote their empirical means. Define

qhat_t=1/2+(ln bar A-ln bar B)/(2eta).

Every A_i/B_i belongs to [exp(-eta),exp(eta)], so their ratio of sums, the population ratio, and both prediction probabilities have the same required bounds.

Assume 0<eta<=1 and write

r=EA/EB,  v=max_y E exp(2eta G_y)/(E exp(eta G_y))^2,

E_good={bar B>=EB/2}.

Chebyshev gives P(E_good^c)<=4v/N. Put C_i=A_i-rB_i. These variables are independent and centered, and paired sampling gives

|C_i|<=B_i(exp(eta)-exp(-eta))<=C eta B_i.

On E_good, the natural logarithm is exp(eta)-Lipschitz on the ratio interval, so

(qhat_t-q_t)^2 1_{E_good}
<= C eta^{-2} (bar C)^2/(EB)^2.

Taking expectations and using independence and centering gives at most Cv/N: the eta^2 from the preceding bound cancels eta^{-2}. On the complementary event, both probabilities lie in [0,1], giving another 4v/N. Thus

E(qhat_t-q_t)^2<=Cv/N.

To bound v uniformly in the history, set L*=min_h L_{t-1}(h) and

U'=sup_h sum_{s=t+1}^b epsilon_s(2h(X_s)-1)/2.

Then G_y+L*<=U'. Choosing a historical empirical minimizer in the supremum and averaging over the signs also gives E G_y+L*>=-1. Therefore

E exp(2eta G_y)<=exp(-2eta L*) E exp(2eta U'),

E exp(eta G_y)>=exp(-eta L*-eta).

The common historical factor cancels, and

v<=exp(2eta) E exp(2eta U')
<=exp(2eta+2eta A sqrt(dL)+eta^2 L/2).

The last step again conditions on covariates and applies the same independent-sign concentration and VC bounds. Choose eta=1/sqrt(dL), making v universally bounded, and choose N=L. Then

E|qhat_t-q_t|<=C/sqrt L.

The loss ell(q,y) is 1-Lipschitz in q. Moreover, the ideal and implemented rules can be compared on exactly the same observed covariates and labels: these are unaffected by either learner's prediction randomization. Summing over the epoch adds at most C sqrt L to expected regret. Consequently

E_Q Reg_epoch <= C sqrt(dL)(1+kappa_a).

All rollouts use the permitted oracle, and their labels are artificial independent signs. The computation uses polynomially many samples, ERM calls, and evaluations. If numerical evaluation of exponentials and logarithms is charged, their arguments have polynomial magnitude in the nontrivial regime d<T. Polynomial precision suffices to perturb each prediction by at most T^{-2}, adding at most one to total regret.

## 5. Epoching and adaptation without knowing KL

For each K in {1,2,4,...,2^{floor(log_2 T)}}, partition the horizon into K consecutive blocks with lengths L_j in {floor(T/K),ceil(T/K)}. Run the preceding implementation independently within each block, retaining the full covariate prefix for simulator conditioning.

Pathwise, global regret is at most the sum of block regrets because the sum of the blockwise comparator minima is no larger than the minimum of the summed comparator losses. Let kappa_j denote the conditional block divergence. The KL chain rule, Cauchy-Schwarz, and L_j<=2T/K yield

E_Q Reg^{(K)}
<=C sum_j sqrt(dL_j)+C sum_j sqrt(dL_j) E_Q kappa_j
<=C[sqrt(dTK)+sqrt(dT/K) kappa].

We now supply the aggregation argument rather than assume a specialized cited algorithm. Regard each K-predictor's probability as an expert advice value. After Y_t is observed, its probability loss ell_{t,K} is known and belongs to [0,1]. Initialize weights w_{1,K}=pi_K proportional to 2^{-K}, and set

alpha_K=min(1/2,sqrt(K/T)).

Predict with the mixture of expert probabilities having weights proportional to alpha_K w_{t,K}. Its probability loss is the same weighted average of ell_{t,K}; call it ell_t. Update

w_{t+1,K}=w_{t,K}[1+alpha_K(ell_t-ell_{t,K})].

All weights remain positive. Their sum stays one because the sum of their increments is zero by the mixture definition. Hence w_{T+1,K}<=1. Since |alpha_K(ell_t-ell_{t,K})|<=1/2, the elementary inequality ln(1+u)>=u-u^2 gives

sum_t(ell_t-ell_{t,K})
<=ln(1/pi_K)/alpha_K+alpha_K T.

The normalization of pi gives ln(1/pi_K)<=K ln 2. For K<=T, the last bound is O(sqrt(TK)), including the capped-rate case. This comparison is pathwise for the realized expert advice and applies to randomized, data-dependent base predictors. Taking expectations and using d>=1 absorbs the overhead into the epoch bound.

If 1+kappa<T, choose an available dyadic K with (1+kappa)/2<K<=1+kappa, allowing equality at a dyadic endpoint. Both terms are O(sqrt(dT(1+kappa))). If 1+kappa>=T, the deterministic regret cap suffices. Thus the single aggregated learner satisfies the claimed upper bound without being given kappa, Q, or g. There are O(1+log T) base predictors, each doing polynomial work, so the total runtime is polynomial in the stated oracle model.

## 6. Threshold converse with exact binary KL

Fix T, D in {1,...,T}, and an arbitrary randomized learner in the public information model. Partition T into D positive block sizes n_j differing by at most one.

Here is an explicit finite threshold-tree realization. Start with a nonempty open interval of possible thresholds inside (1/4,3/4). At a node of depth j, choose n_j distinct covariate points inside the middle third of its threshold interval. The child associated with label 0 retains an open threshold interval below all these points; the child associated with label 1 retains one above all these points. Repeat to depth D. All selected points are distinct. Every sequence of D branch labels has a threshold in its final retained interval that assigns the selected branch label constantly to every point of its corresponding node block.

Independently assign a fair binary label to every point in this finite tree construction. Extend the labeling to a function g on [0,1], for example by assigning zero off that finite set. This assignment is auxiliary randomness used only to prove existence.

Let R_0 output the root block and then choose independent fair branches between consecutive blocks. It has D-1 observable branch choices, so every distinct D-block trajectory has probability 2^{-(D-1)}. Define the simulator

R=(1/2)R_0+(1/2)delta_{(0,...,0)}.

The added trajectory is outside the tree support. Both R and specified versions of all its conditional kernels are independent of the auxiliary labeling.

For each fixed g, define Q_g as the point mass on the trajectory that starts at the root and chooses the next block using the majority label of the current block, with a fixed deterministic rule for ties. Only the first D-1 majorities determine the observed trajectory. The last majority determines the final comparator branch, not an additional observation. For every g,

R({the Q_g trajectory})=(1/2)2^{-(D-1)}=2^{-D},

so KL(Q_g||R)=D exactly, with binary logarithms.

Before each prediction, the point's label is a fresh fair bit conditional on all preceding observed labels and covariates. Selection of its node depends only on earlier blocks; the within-block order does not depend on its labels. Simulator responses do not alter this fact: the simulator, including its off-support kernel versions, is independent of the entire labeling, and adaptive queries only apply that fixed oracle to the learner's existing information. The ERM oracle for the fixed threshold class likewise need not reveal any ground-truth labels. Thus the learner's expected total loss, averaged over the auxiliary labeling and all its randomization, is T/2.

Choose the comparator threshold realizing all visited block majorities, including the last one. If S_j is the sum of the n_j independent label signs in the visited block, the comparator makes (n_j-|S_j|)/2 mistakes there. Conditional on the preceding blocks, these signs are independent and fair. For a sum S of n such signs,

E S^2=n,  E S^4=3n^2-2n<=3n^2.

Hölder applied to |S|^{2/3}|S|^{4/3} gives

n<= (E|S|)^{2/3}(E|S|^4)^{1/3},

hence E|S|>=sqrt(n/3). Each n_j>=T/(2D), so the expected regret is at least

(1/2)sum_j E|S_j| >= (1/(2sqrt 3))sum_j sqrt(n_j)
>=sqrt(DT)/(2sqrt 6).

Averaging now fixes one deterministic g for which the fixed learner's expected regret has this lower bound. For that g, both Q_g and R are fixed before the trajectory draw, and KL(Q_g||R)=D. This proves the required learner-first quantifier order and covers D=1, D=T, and T=1.

## Closure of proof obligations

The minimax rule, probability range, predictable-loss supermartingale, entropy transfer, initial MGF, ordinary-ERM reduction, paired-estimator concentration, normalized variance, conditional epoch summation, divergence-free aggregation, exact-KL converse, and fixed-label extraction are all established above. The only external inputs are the explicitly stated standard independent inequalities and uniform VC Rademacher bound. No unresolved private proof obligation remains.
