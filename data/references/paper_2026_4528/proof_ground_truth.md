# Reference Proof

## Proof Structure

Use the conditional Gaussian observation kernel to obtain a fixed-center decision problem. Translate by the historical center, apply the standard positive-part James--Stein comparison, and establish the minimax lower bound by Gaussian priors. The lower bound must cover randomized as well as deterministic rules. Finally transfer the pointwise conclusions to the conditional risks.

## Complete Proof

### 1. Conditional experiment and translation

Work with the conditional Gaussian kernel specified in the problem, which holds almost surely. Write q=q_t and m=m_{t-1} for the values of the mean and historical center. For the decision problem, m is fixed and available, whereas q is an unknown parameter ranging over R^p. A decision rule cannot use q as an input. The fact that the actual random vector q_t is past-measurable is used to identify the conditional observation law, not to grant an oracle to a rule.

Set Y=g_t-m and mu=q-m. In the fixed-center experiment, Y has distribution N(mu,sigma^2 I_p). Translating both the observation and the action by m gives a bijection between the original decision rules and the rules for estimating mu from Y, preserving squared-error risks. This holds for probability kernels as well as deterministic functions.

The unrestricted rule is Y in translated coordinates. Its risk is

E_mu||Y-mu||^2 = E||epsilon_t||^2 = p sigma^2.

### 2. Positive-part risk comparison

The standard independent positive-part James--Stein result used here is the following: if Y~N(mu,sigma^2 I_p), p>=3, and sigma^2>0 is fixed, then

delta_+(Y)=[1-(p-2)sigma^2/||Y||^2]_+Y

(with value zero at Y=0) has squared-error risk at most p sigma^2 for every mu, with strict inequality for every nonzero mu. This is the classical result recorded in theory_008 and quoted in the source's dominance proof. Its dimension, covariance, loss, and fixed-center hypotheses are all satisfied after translation.

For completeness, the zero translated-mean case is also strict. Put a=(p-2)sigma^2>0. For every y!=0, the multiplier [1-a/||y||^2]_+ belongs to [0,1), so

||delta_+(y)||^2 < ||y||^2.

Under mu=0, Y!=0 almost surely and E||Y||^2=p sigma^2<infinity. Taking expectations proves E_0||delta_+(Y)||^2<p sigma^2.

Translating the action back gives exactly

m+[1-(p-2)sigma^2/||g_t-m||^2]_+(g_t-m).

Its risk is therefore at most p sigma^2 for every q, with strict inequality in particular whenever q!=m. The argument also establishes strictness at q=m. The definition at zero is measurable, and the Gaussian observation assigns that point probability zero.

### 3. Minimax lower bound, including randomized rules

Fix tau^2>0 and put the prior mu~N(0,tau^2 I_p) on the translated mean. Completing the square in the product of the Gaussian prior density and the likelihood gives

mu | Y ~ N(cY,v I_p),

where c=tau^2/(tau^2+sigma^2) and v=tau^2 sigma^2/(tau^2+sigma^2).

Let A be the action of any admissible decision rule. For a randomized rule, its conditional distribution given Y is the specified parameter-independent probability kernel. Consequently A and mu are conditionally independent given Y. The posterior squared-error decomposition gives

E[||A-mu||^2 | Y,A] = ||A-cY||^2 + pv.

Integrating this nonnegative identity shows that every rule has integrated risk at least pv, including rules with infinite risk. The deterministic posterior mean A=cY attains this value. Thus the Bayes risk is

B_tau = p tau^2 sigma^2/(tau^2+sigma^2).

For every rule K, its supremum risk is at least its prior-averaged risk and hence at least B_tau. Therefore

inf_K sup_mu E_mu||A-mu||^2 >= B_tau

for every tau^2>0. Letting tau^2 tend to infinity yields the lower bound p sigma^2. The unrestricted rule has constant risk p sigma^2, so the minimax value is exactly p sigma^2. Translation preserves this value for every fixed historical center m.

### 4. Minimaxity, inadmissibility, and conditional conclusions

The positive-part rule has supremum risk at most p sigma^2. The minimax lower bound forces its supremum risk to equal p sigma^2, so it is minimax. The unrestricted rule is also minimax because its risk is constant at that value. There is no conflict between strict pointwise improvement and equal supremum risk: strictness is not a uniform positive gap.

The positive-part rule has no greater risk at any parameter and strictly smaller risk at nonzero translated parameters (indeed, at every parameter). Hence it dominates the unrestricted rule in the fixed-center experiment, proving that the unrestricted rule is inadmissible. These conclusions already establish the minimax and dominance consequences for which the source additionally cites Baranchik; no further specialized result is needed.

Finally, the pointwise risk statements hold for every finite pair (q,m). Substituting the past-measurable pair (q_t,m_{t-1}) into the conditional Gaussian kernel proves

R_t(g_t)=p sigma^2,

R_t(qhat_t^+)<=p sigma^2,

with strict inequality almost surely on {q_t!=m_{t-1}}. Thus the conditional-risk inequality is strict almost surely on every positive-probability event contained in that set. If such an event belongs to F_{t-1}, integrating the conditional risks over the event also gives a strict comparison of the event-conditional expected losses. The pointwise bounds require no unconditional moment assumption on q_t or m_{t-1}.

## Obligation Audit

- Conditional experiment, information restrictions, and translation: closed directly from the observation kernel and the decision-rule definition.
- Unrestricted risk: closed by the Gaussian covariance calculation.
- Positive-part risk comparison: closed by the explicitly stated standard_independent result in theory_008 with all hypotheses checked.
- Zero translated mean and the zero-observation convention: closed by the direct norm comparison and Gaussian non-atomicity.
- Posterior calculation and minimax lower bound for the full randomized class: closed by completing the square and posterior loss decomposition.
- Minimaxity, inadmissibility, and transfer to conditional risks: closed by the preceding pointwise bounds.

There are no unresolved theorem-critical proof obligations.
