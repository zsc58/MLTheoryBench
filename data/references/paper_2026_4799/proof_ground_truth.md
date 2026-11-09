# Reference Proof

## Proof Structure and Obligations

1. Establish the two optimal continuation values directly from the communicating controlled Markov experiment, without conditioning on successful completion.
2. Bound actual policy value by the mixture of these optimal values and deduce the margin-regret inequality.
3. Compare the soft threshold count with a tie-broken binomial median; control the small-margin thresholds, degenerate cases, clipping, and uniform averaging.
4. Transfer the estimate to the interventional kernel by the assumed pointwise mismatch bound.
5. Construct two complete structural Markov models satisfying the environment assumptions, with identical interventional kernels and different cross-action coupling.

All five obligations are closed below. The only standard independent results invoked are the explicitly stated Cantelli inequalities and binomial-median bound. The specialized branch-optimum citation is replaced by a direct derivation.

## 1. The experiment and its branch optima

Fix a test and write p=P_{ss'}(a). All probabilities are for the same fixed initial state s0. The marker is chosen at time zero. Failure to obtain n subsequent occurrences of (s,a) is failure of the goal; it is not a conditioning event.

After the marker transition, realize future transitions by assigning to each state-action row an independent infinite sequence of outcomes with distribution P(\cdot\mid s,a). At each visit to a row, consume its next unused outcome. These sequences are independent of the past and of the policy's private randomization. At every finite history the next unused outcome has the prescribed row distribution, so this construction realizes the controlled Markov law for any admissible nonanticipating policy.

For the tested row, let X be the number of s' outcomes in its first n entries. Then X has distribution Bin(n,p), independently of the marker and the state reached by that marker. Write F(k)=Pr(X<=k). On the event T_n<infinity, the actual n tested outcomes are exactly these first n entries. Consequently, conditional on marker L the success event is a subset of {X<=k}; conditional on marker R it is a subset of {X>k}. Thus any continuation policy has success probability at most F(k) or 1-F(k), respectively. This argument does not assert that the outcome sequence remains iid after conditioning on T_n<infinity.

Both upper bounds are attained. After either marker, use independent uniform random actions. Communication supplies, from each current state, a finite positive-probability route to s, after which choosing a produces an attempt. Since the state and action sets are finite, there are an integer M and rho>0 such that, conditional on any current history, this exploration policy obtains an attempt within the next M steps with probability at least rho. By repeated conditioning, the probability of no attempt during r such blocks is at most (1-rho)^r, which tends to zero. Repeating after each attempt shows that the first n attempts all occur almost surely. Their outcomes are the first n entries of the tested row sequence. Hence the branch optima are F(k) and 1-F(k), and

V_k^*=max{F(k),1-F(k)}>=1/2.

The denominator defining regret is therefore positive, and actual normalized regret lies in [0,1].

## 2. Regret controls branch-choice errors

Let q_k be the evaluated policy's probability of choosing L. Its continuation need not be optimal, so the correct relation is

V_k <= q_k F(k)+(1-q_k)(1-F(k)).

Set m_k=|F(k)-1/2| and define w_k=1-q_k when F(k)>=1/2, and w_k=q_k otherwise. This definition chooses L as the reference at a tie; at a tie it is a reference-disagreement probability, not necessarily mass on a strictly inferior action. The mixture on the right equals

(1-w_k)(1/2+m_k)+w_k(1/2-m_k).

Dividing by V_k^*=1/2+m_k yields

\[
\delta_k\ge w_k\frac{4m_k}{1+2m_k}.
\]

The coefficient is increasing in m_k, so m_k>=gamma implies w_k<=delta_k/c(gamma). Equality in the displayed regret relation is not required and need not hold when the evaluated policy fails to complete the attempts.

## 3. Threshold count and concentration

Let

\[
j=\min\{k\in\{0,\ldots,n\}:F(k)\ge1/2\},\qquad H=\sum_{k=0}^n(1-q_k).
\]

The reference decision selects R exactly for k<j; therefore its R-count is exactly j. For every threshold,

\[
\left|(1-q_k)-\mathbf1\{k<j\}\right|=w_k.
\]

This identity remains true at ties with the convention just specified. Hence, with K_gamma={k:|F(k)-1/2|<gamma},

\[
|H-j|\le\sum_k w_k\le |K_\gamma|+\frac1{c(\gamma)}\sum_{k=0}^n\delta_k.
\]

For completeness, the standard independent concentration fact used here is: for a random variable Y with finite mean mu and positive finite variance sigma^2, and t>0,

\[
\Pr(Y-\mu\ge t\sigma)\le\frac1{1+t^2},\qquad
\Pr(Y-\mu\le-t\sigma)\le\frac1{1+t^2}.
\]

Apply it to the bounded binomial variable X, whose mean is mu=np and variance is sigma^2=np(1-p). First suppose 0<p<1, so sigma>0. If k>=mu+t_gamma sigma, event inclusion gives

\[
\Pr(X\ge k)\le\Pr(X-\mu\ge t_\gamma\sigma)\le\frac1{1+t_\gamma^2}=\frac12-\gamma.
\]

It follows that F(k)>=1/2+gamma. If k<=mu-t_gamma sigma, the lower-tail inequality gives F(k)<=1/2-gamma. Thus

\[
K_\gamma\subset(\mu-t_\gamma\sigma,\mu+t_\gamma\sigma),\qquad
|K_\gamma|\le2t_\gamma\sigma+2.
\]

If p=0 or p=1, X is deterministic and F(k) is either zero or one at every integer threshold. Thus K_gamma is empty, and the same bound holds without applying a standardized tail inequality.

The other standard independent fact used is the binomial-median bound: for n>=1 and p in [0,1], the lower median j of Bin(n,p) satisfies |j-np|<=1. Its hypotheses hold here, including the deterministic endpoints. Since projection onto [0,1] cannot increase distance to p,

\[
\begin{aligned}
|\widehat P_{ss'}(a)-p|
&\le\frac{|H-j|+|j-np|+1/2}{n}\\
&\le2t_\gamma\sqrt{\frac{p(1-p)}n}
 +\frac1{n c(\gamma)}\sum_{k=0}^n\delta_k+\frac7{2n}.
\end{aligned}
\]

These estimates hold for every n>=1.

Let d be the actual uniform average regret over all quadruples. Then 0<=d<=1 and d<=bar delta. The exact threshold normalization is

\[
\mathbb E_{s,a,s'}\left[\frac1n\sum_{k=0}^n\delta_k\right]
=\frac{n+1}{n}d
\le\bar\delta+\frac1n.
\]

Averaging the pointwise estimate consequently gives

\[
\mathbb E_{s,a,s'}|\widehat P_{ss'}(a)-P_{ss'}(a)|
\le2t_\gamma\mathbb E_{s,a,s'}\sqrt{\frac{P_{ss'}(a)(1-P_{ss'}(a))}{n}}
+\frac{\bar\delta}{c(\gamma)}
+\frac{7/2+1/c(\gamma)}n.
\]

The remainder depends only on gamma, not on the environment, policy, initial state, regret upper bound, or n. Since sqrt(p(1-p))<=1/2, the second requested inequality follows.

## 4. Interventional transfer

The optional assumption gives, pointwise,

\[
|\widehat P_{ss'}(a)-P^{\rm do}_{ss'}(a)|
\le |\widehat P_{ss'}(a)-P_{ss'}(a)|+\varepsilon_{\rm cMP}.
\]

Uniform averaging and the preceding bound prove both requested interventional bounds. The variance term continues to involve P, exactly as in the claim.

## 5. Complete structural counterexample

Take S=A={0,1}, fix any common initial distribution, and use independent exogenous variables U_t uniform on [0,1]. Let Z_t=1{U_t<1/2}. Define two structural transition models as follows.

At current state S_t=0:

- Model I: S_{t+1}=Z_t.
- Model II: S_{t+1}=A_t xor Z_t.

At current state S_t=1, in both models set

\[
S_{t+1}=\mathbf1\{U_t<1/4+A_t/2\}.
\]

The full interventional kernels agree. At state 0, either action produces next state 1 with probability 1/2. At state 1, actions 0 and 1 produce next state 1 with probabilities 1/4 and 3/4, respectively. The complementary next-state probabilities agree as well. Both environments are finite, stationary, fully observed, communicating, and action-dependent: every transition probability is positive, and the action changes the row at state 1.

At state 0, counterfactuals under the two actions use the same U_t. In model I the pair (S_{t+1}^0,S_{t+1}^1) is (Z_t,Z_t), whereas in model II it is (Z_t,1-Z_t). Therefore

\[
\Pr(S_{t+1}^0=S_{t+1}^1\mid S_t=0)=1
\quad\text{in model I},\qquad
\Pr(S_{t+1}^0=S_{t+1}^1\mid S_t=0)=0
\quad\text{in model II}.
\]

Thus even the complete interventional kernel does not identify the joint cross-action law.

## Source-local corrections

The source's tail display at L000323 uses equality where event inclusion gives an inequality; the proof above uses the corrected inequality. Its claim at L000316 about optimal decisions is read with the explicit L-favoring tie convention already used by its definition of w_k and lower median. Neither correction changes the theorem. No unresolved specialized dependency remains.
