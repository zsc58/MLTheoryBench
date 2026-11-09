# Reference Proof

## Contract and proof obligations

The target is the source's lower-bound rate with N and B fixed; its constant is not asserted to be uniform in these dimensions. We work in the permitted one-customer-type, K=1 experiment. Unit rewards are used throughout. The source construction uses gamma=1+u; after the private choice u=1 below, its rewards and regrets are exactly twice ours.

The obligations are: construct admissible environments and identify their optimum; derive the omission-to-regret inequality; bound the KL divergence of the complete observed history, including seller feedback; apply Pinsker with the correct history law; aggregate over the source's deletion neighbors; and select an admissible perturbation and a horizon-independent positive constant. Every obligation is derived below. The only standard result used without a proof is Pinsker's inequality, whose relevant statement and applicability are specified explicitly. No logarithmic exploration requirement or efficiency assumption is used.

## 1. Adversarial family and optimality

Fix N, B, T, and any admissible policy pi. Put

  C_B = (B+1)(2B+9)/4,
  d = (N-2B+1)/(N-B+1),
  epsilon = d / [2 sqrt(2 C_B T)].

Because 1 <= B <= N/2, we have 0<d<=1. Since C_B>=11/2 and T>=1, we have 0<epsilon<1.

For every set J of size B or B-1, define an environment theta_J by

  u_i=1 for every seller,
  a_i=v_i=(1/2)(1+epsilon) if i belongs to J,
  a_i=v_i=1/2 otherwise.

All parameters belong to (0,1]. Write P_J and E_J for the law and expectation induced by this environment and the same policy pi.

For any feasible assortment A, put W_J(A)=sum_{i in A} a_i. Conditional on a proposal, the seller accepts with probability 1/2, so its unit-reward expectation is

  r_J(A) = (1/2) W_J(A)/(1+W_J(A)).

For a target index H of size B, adding a seller to an assortment of size less than B increases W_H(A), and hence strictly increases reward. Among assortments of size B, H uniquely maximizes W_H(A), since its sellers have strictly larger customer parameters. Thus H is the unique optimal assortment under theta_H.

There is no state carried between periods, and the conditional expected reward is r_H(A_t) regardless of earlier observations. Therefore offering H every period also attains the clairvoyant optimum. The fixed-assortment benchmark in the task agrees with the source's clairvoyant benchmark on these environments. No optimality assertion is needed for the auxiliary indices J of size B-1.

## 2. Regret decomposition, including underfilled assortments

Let H have size B and A have size at most B. Direct subtraction gives

  r_H(H)-r_H(A)
    = [W_H(H)-W_H(A)] / [2(1+W_H(H))(1+W_H(A))].

Moreover,

  W_H(H)-W_H(A)
    = (1/2)[B-|A| + epsilon(B-|A intersect H|)]
    >= (epsilon/2)(B-|A intersect H|).

Every customer parameter is at most one, so both denominator factors 1+W are at most 1+B. Hence

  r_H(H)-r_H(A)
    >= epsilon [B-|A intersect H|] / [4(B+1)^2].                 (1)

For each seller i define the actual offer count

  N_i(T)=sum_{t=1}^T 1{i belongs to A_t}.

Taking conditional expectations of the match indicators and then summing (1) yields

  Reg_H(T)
    >= epsilon/[4(B+1)^2]
        [BT - sum_{i in H} E_H N_i(T)].                         (2)

This applies directly to the actual policy actions, including the empty assortment. We do not replace them by fictitious padded actions or assign feedback from such actions to the policy.

## 3. Conditional observation KL and complete-history KL

Let G have size B-1, let i not belong to G, and put H=G union {i}. These environments differ in exactly one customer-side parameter, not in two exchanged coordinates.

For a common preceding history and common current action A, let p and q be the categorical proposal laws under G and H, respectively. If i is absent from A, the laws coincide. Suppose i belongs to A. With v=1/2, the changed utility is v epsilon. Denote the two MNL denominators by D and D+v epsilon, where D is the denominator under G. Both lie in [1,B+1].

The outside-option probability difference is at most v epsilon. For seller i, splitting the numerator change and denominator change bounds its probability difference by v epsilon+v^2 epsilon <=2v epsilon. For every other offered seller j, the utility is unchanged and is at most v(1+epsilon)<=2v, so its probability difference is at most 2v^2 epsilon. Under H, the outside-option probability is at least 1/(B+1), and every offered seller's probability is at least v/(B+1). This last bound does not assume that an unperturbed seller has enhanced utility.

For categorical laws with positive q on their common support,

  D(p||q) <= sum_j (p_j-q_j)^2/q_j.

Indeed, applying log(x)<=x-1 to sum_j p_j log(p_j/q_j), and using sum_j(p_j-q_j)=0, gives this inequality. All support probabilities here are positive; unoffered sellers are excluded from the categorical support.

The displayed probability bounds consequently give

  D(p||q)
    <= (B+1)[v^2+4v+4Bv^3] epsilon^2
    <= C_B epsilon^2.

The seller acceptance kernel, conditional on the proposal, is identical in the two environments: acceptance has probability 1/2 for a proposal, and no match is possible without one. Thus adjoining the observed seller decision contributes zero additional conditional KL.

Let P_J^T be the joint law of all actions, proposals, and match indicators through time T. The admissibility contract supplies identical policy action kernels in all environments, with no parameter-dependent initial information. In the likelihood ratio of the two sequential experiments, these action kernels cancel. Taking the logarithm and expectation under G gives the chain rule

  D(P_G^T||P_H^T)
    = sum_{t=1}^T E_G[D(law_G(Y_t,X_t | past,A_t)
                           || law_H(Y_t,X_t | past,A_t))]
    <= C_B epsilon^2 E_G N_i(T)
    <= T C_B epsilon^2.                                        (3)

Common policy kernels and strictly positive outcome probabilities on each available support ensure absolute continuity. The bound concerns the full history, not a single epoch after discarding the information that selected its action.

## 4. Offer-count comparison and exact neighbor averaging

Pinsker's inequality states that, for probability laws P,Q with finite D(P||Q),

  ||P-Q||_1 <= sqrt(2D(P||Q)).

For a statistic F taking values in [0,T], it follows directly that

  |E_P F-E_Q F| <= T ||P-Q||_1 <= T sqrt(2D(P||Q)).

Apply this to the complete-history laws in (3) and the measurable statistic N_i(T). We obtain

  E_H N_i(T) <= E_G N_i(T) + T epsilon sqrt(2 C_B T).             (4)

Let H_B be the collection of B-element subsets and H_{B-1} the collection of (B-1)-element subsets. The map (H,i), with i in H, to (G=H minus {i},i) is a bijection onto pairs with G in H_{B-1} and i outside G. Thus, averaging (4),

  [1/binom(N,B)] sum_{H in H_B} sum_{i in H} E_H N_i(T)
    <= [1/binom(N,B)] sum_{G in H_{B-1}}
            sum_{i outside G} E_G N_i(T)
       + B T epsilon sqrt(2 C_B T).

The error coefficient is exactly B because there are B binom(N,B) such pairs. For every environment and every sample path, sum_i N_i(T)=sum_t |A_t|<=BT. Also binom(N,B-1)/binom(N,B)=B/(N-B+1). Consequently,

  [1/binom(N,B)] sum_{H in H_B} sum_{i in H} E_H N_i(T)
    <= B^2 T/(N-B+1) + B T epsilon sqrt(2 C_B T).

Subtracting from BT gives

  [1/binom(N,B)] sum_{H in H_B}
       [BT-sum_{i in H} E_H N_i(T)]
    >= BT [d-epsilon sqrt(2 C_B T)]
    = BTd/2.                                                   (5)

This argument holds for every admissible policy without a low-regret hypothesis or a complementary-case argument.

## 5. Quantitative lower bound

The supremum over the task's parameter class is at least the maximum over the environments theta_H, which is at least their average regret. Combining (2) and (5),

  sup_{u,v} Reg_{pi,(u,v)}(T)
    >= epsilon BTd/[8(B+1)^2]
    = D_{N,B} sqrt(T),

where

  D_{N,B}= B d^2/[16(B+1)^2 sqrt(2 C_B)] > 0.                   (6)

The perturbation may depend on T because the supremum over parameters is taken separately at each horizon. In contrast, D_{N,B} depends on neither T nor the policy. This uses exactly the quantifier order in the task.

## 6. Conversion to the requested rate and boundary checks

For T>=1, let x=T^(1/4)>=1. The elementary inequality log(x)<=x implies

  log(T)=4log(x)<=4x,
  log(N)<=x log(N).

Therefore

  [log(NT)]^2 <= [log(N)+4]^2 sqrt(T).

Together with (6), this proves the task with

  c_{N,B}=D_{N,B}/[log(N)+4]^2 > 0.

The constant is independent of T, pi, u, and v. No uniform lower bound for this constant over N and B is asserted. The proof covers T=1, B=1 (where the auxiliary set G is empty), N=2B (where d=1/(B+1)>0), randomized policies, and underfilled or empty offers. Every parameter in the constructed environments remains strictly positive and at most one.

The source's fixed-perturbation linear-in-T intermediate bound, its history-free use of epoch KL, and the previous GT's logarithmic required-offer assertion are not used or certified. The corrected proof closes the source-level log-squared converse by routine sequential-KL accounting and perturbation tuning within the same construction.
