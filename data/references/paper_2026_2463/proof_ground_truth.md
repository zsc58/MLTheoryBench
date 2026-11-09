# Reference Proof

## Obligations and Conventions

Use full total variation. Put b=beta^K and C=||c_K||_infinity. We establish: the conditional-law representation; continuity needed for both discounted Bellman operators; their identification with unrestricted admissible-policy values; the predictor-to-block-law comparison; value-error propagation under a stationary true policy; policy loss; and expected predictor contraction.

The direct augmented-state weak-Feller assumption is used as a hypothesis. We neither prove nor invoke the invalid general-observation sufficient-condition claim previously indexed by theory_015. The specialized external regularity and stationary-optimality results indexed by theory_010 and theory_011 are not needed below.

## 1. Conditional-Law Representation

A block prescription is chosen from common information before the block's private observations arrive. Conditional on the hidden state at that boundary and this prescription, observations, realized actions, transitions, and costs have the iterated law in the setup. Measurable decentralized block rules can be represented as measurable prescription choices: integration against the fixed reference observation measures makes the coordinates defining their Young measures measurable.

The old prior and stored joint observation/realized-action blocks determine every intermediate predictor. The next old prior is the update through the oldest stored block. The next window shifts and appends the generated block. Therefore the true augmented process is a controlled Markov process, with block reward r(z,a)=c_K(phi(z),a), where phi reconstructs the current predictor. Conditional expectation gives equality of its discounted reward and the team objective. A full-common-history team policy may induce a history-dependent prescription policy; no stationary restriction is imposed at this representation step.

The substitute process reconstructs phi(nu,I), generates the next block with that prior, shifts the window, and resets its old-prior coordinate to nu. Its reward is r*(I,a)=c_K(phi(nu,I),a). A substitute policy is transferred to the true process only through (nu,I).

## 2. Reward and Transition Regularity

### Deterministic Young convergence

For a fixed private action history and finite action alphabet, let deterministic maps f_n converge to f in the specified Young topology. Then their graph measures have a fixed observation marginal m and converge weakly. For each action u, weak convergence implies convergence of integrals v(y)1_{f_n(y)=u} for bounded continuous v. It also implies this for any bounded measurable v: approximate v in L1(m) by bounded continuous functions, with an error bound independent of n because the marginal is fixed. The approximation fact follows from regularity of finite Borel probabilities on separable metric spaces, by approximating indicators between closed and open sets and then simple functions.

Taking v=1_{f(y)=u}, and summing over the finite action alphabet, gives m{f_n!=f}->0. Apply this to every agent, stage, and preceding private action string; there are only finitely many such strings in one block. Changes on reference-null sets do not affect the induced laws, since the actual observation records have densities relative to the corresponding product reference measures.

### Continuity of the block reward

Write g_a(x) for the expected internally discounted block cost starting from x under a. Fix x. For each open-loop joint action string of length K, the joint observation record has an integrable density relative to the product reference probability. There are finitely many such strings. The union of the prescription-disagreement sets just described has reference measure tending to zero, so its probability tends to zero under each of these finitely many laws.

The event that a_n and a first disagree can be bounded by summing over those open-loop strings. Equivalently, generate both processes together until the first prescription disagreement. Their observations, actions, and states agree up to that event. Bounded block costs therefore give g_{a_n}(x)->g_a(x).

For x_n->x, each individual observation channel converges in total variation: its densities converge pointwise by state continuity, and all have integral one, so the elementary density convergence lemma gives L1 convergence. Finite products preserve this conclusion for Q. The given plant kernels also converge in total variation, uniformly over the finitely many joint actions. Compare the first observation and subsequent transition under the same prescription. After matching them, the remainder of the path has the same conditional law. Together with uniform continuity of c on compact X times finite U, this yields an equicontinuity bound for g_a(x), uniform over a. Compactness of X upgrades the preceding pointwise convergence in a to uniform convergence in x by a finite-net argument.

Thus, if p_n converges weakly to p and a_n converges to a,

|c_K(p_n,a_n)-c_K(p,a)| <= ||g_{a_n}-g_a||_infinity + |integral g_a d(p_n-p)| -> 0.

The block reward is jointly continuous and bounded.

### Continuity of reconstruction and substitute dynamics

The first coordinate of the true next augmented state is deterministically G(p,B_old), independently of the current prescription. For any continuous f on compact X, the next-state test function that integrates f against this first coordinate is bounded and continuous. The assumed true weak-Feller property therefore makes integral f dG(p,B_old) continuous in the current state. Hold the other stored blocks and the current prescription fixed. Since these tests generate the weak topology on P(X), the oldest-block update G is continuous in p and B_old. Its M successive applications make phi(z) continuous.

Consequently r(z,a) and r*(I,a) are jointly continuous. Let s(z)=(nu,I) be the continuous projection that replaces the old-prior coordinate. The substitute transition is exactly the pushforward by s of the true transition evaluated at (nu,I), because their generated next-block laws then coincide. Hence it is weak-Feller as well.

## 3. Discounted Bellman Characterization

The prescription space is a nonempty compact metric space: its Young topology is inherited from a finite product of metrizable probability-measure spaces. The state and window spaces are standard Borel metric spaces. For either model, the Bellman operator

V -> inf_a [r(.,a)+b P_a V]

maps bounded continuous functions to bounded continuous functions, by joint continuity and compactness of actions, and is a contraction of factor b in the supremum norm. Iteration from zero gives a bounded continuous fixed point, with absolute value at most C/(1-b).

Here is the measurable-policy justification, without a specialized stationary-optimality citation. Choose a countable dense sequence of actions. Continuity in the action makes the infimum over this sequence equal the minimum over the full action space. For any eta>0, choose the first action in the sequence whose Bellman expression is within eta of the infimum. This is a Borel stationary selector.

The fixed-point Bellman inequality, conditional on each history and iterated for n steps, bounds the fixed point below the cost of every admissible history-dependent policy. The stationary eta-selector gives an upper cost bound of eta/(1-b) above the fixed point. The terminal terms vanish because costs and the fixed point are bounded. Sending eta to zero identifies the fixed point with the unrestricted optimum. This proves the needed characterization for both models and the equivalence to the team optimum from Section 1.

Write v(z)=J(z), w(I)=J_M*(nu,I), and E(z)=|v(z)-w(I)|. Both v and w, and therefore E, are bounded and continuous. Exact existence of a measurable minimizing selector is not needed for the value bounds. The policy-loss claim applies to any optimal stationary substitute policy, as stated in the task.

## 4. Mixture and Reward Comparisons

At a common retained window and prescription a, let p=phi(z) and p*=phi(nu,I). Conditional on the current hidden state, the next joint observation/realized-action block has the same kernel H_a in both experiments. Thus

||pH_a-p*H_a||_TV <= ||p-p*||_TV.

Indeed, integrating any block test function bounded by one against H_a gives a state test function bounded by one. Shifting the window cannot increase total variation.

Since C takes a supremum over every prior, including point masses, |g_a(x)|<=C. Therefore

|r(z,a)-r*(I,a)| <= C e(z),

where e(z)=||phi(z)-phi(nu,I)||_TV. The substitute continuation value is bounded by C/(1-b), so its next-law discrepancy contributes at most bC e(z)/(1-b). Their sum is A e(z), where A=C/(1-b).

## 5. Value Error Under a Stationary True Policy

No true optimal policy is transferred to the substitute experiment. Instead compare the two Bellman minima at their respective current states. Define

R(z,a)=|r(z,a)-r*(I,a)| + b|P_a(w composed with s)(z)-P_a* w(I)| + bP_a E(z).

The Bellman equations and the triangle inequality give E(z)<=max_a R(z,a). Every term defining R is jointly continuous, by Sections 2 and 3. Using a countable dense action sequence, choose a Borel stationary true policy sigma_eta with

max_a R(z,a) <= R(z,sigma_eta(z))+eta.

The comparison estimates then give

E(z) <= A e(z)+bP_{sigma_eta}E(z)+eta.

The standing domination requirement covers this policy; it cannot be excluded from the stability supremum. Iterate under this single stationary policy for n blocks. The terminal term is at most 2C b^n/(1-b), so

E(z) <= A sum_{q>=0} b^q E_z^{sigma_eta} e(hat Z_q)+eta/(1-b)

<= A sum_{q>=0} b^q L_q^M(z)+eta/(1-b).

Send eta to zero. Since b=beta^K<=beta, A<=C/(1-beta), proving the deterministic value bound.

For generated initialization, integrate the same recursion before bounding its expectations. The selector sigma_eta is a single stationary policy on the true state space. Its expectations under any allowed Lambda are bounded by bar L_q^M. Hence

E_Lambda E(hat Z_0) <= A sum_{q>=0} b^q bar L_q^M.

The absolute difference of the two expected optimal values is no larger than this quantity. This does not interchange initialization expectation with a statewise policy supremum.

## 6. Transferred Substitute Policy

Let gamma_M* be an optimal stationary substitute policy and sigma(z)=gamma_M*(nu,I). This is an admissible stationary true policy. Substitute optimality gives the policy Bellman identity for w. Consequently

d(z)=r(z,sigma(z))+bP_sigma(w composed with s)(z)-w(I)

has |d(z)|<=A e(z). Telescope this identity along the true sigma process. The terminal discounted w term tends to zero, yielding

|J^{gamma_M*}(z)-w(I)| <= A sum_{q>=0} b^q E_z^sigma e(hat Z_q)

<= A sum_{q>=0} b^q L_q^M(z).

Adding the value bound from Section 5 proves the factor-two loss bound. The same telescoping calculation integrated over Lambda gives the generated-initialization policy bound with bar L_q^M.

If the applicable stability sequence tends to zero for every fixed q as M increases, its discounted sum tends to zero by dominated convergence: full-TV distances are at most two and sum_q 2b^q is finite. This proves the stated conditional or generated-initialization near-optimality conclusions. The arguments also cover C=0.

The previously recorded source coefficient repairs remain valid: with D=||c||_infinity, the immediate block estimate is D(1-b)/(1-beta), not merely D/(1-beta). Adding bD/(1-beta) for the continuation discrepancy gives exactly D/(1-beta).

## 7. Dobrushin Predictor Stability

Let k_y(x)=product_i h_i(x,y_i) and Psi=product_i psi_i. For priors mu<<nu define p_mu(y)=integral k_y dmu and p_nu(y)=integral k_y dnu. On the positive-true-density region S={p_mu>0}, absolute continuity gives p_nu>0. The posterior before prediction is B_y(mu)=k_y mu/p_mu(y).

Insert k_y nu/p_mu(y) between the two posteriors. Their full-TV difference is at most A_y+B_y, where

A_y=||k_y(mu-nu)||_TV/p_mu(y),

B_y=|p_mu(y)-p_nu(y)|/p_mu(y).

Averaging under the true observation law and using variation measures and Tonelli gives

E_mu A_y <= integral Psi(dy) integral k_y(x)|mu-nu|(dx)=||mu-nu||_TV.

For the normalization term,

E_mu B_y=integral_S |p_mu-p_nu| dPsi <= ||mu Q-nu Q||_TV.

The restriction to S matters in the general model. Under the additional uniform positivity assumptions all observation symbols belong to S.

For completeness, the overlap definition gives the usual contraction. If d=||mu-nu||_TV/2>0, write mu-nu=d(alpha-alpha') using the normalized positive and negative variation measures. Then

||alpha H-alpha' H||_TV <= integral alpha(dx)alpha'(dx') ||H(.|x)-H(.|x')||_TV <= 2(1-delta(H)).

Multiplication by d proves ||mu H-nu H||_TV<=(1-delta(H))||mu-nu||_TV. The zero-distance case is immediate.

It follows that the expected posterior error is at most (2-delta(Q))||mu-nu||_TV. Both posterior predictions use the same realized joint action u. The transition contraction is at most 1-underlinedelta_T, independently of this action. Thus, conditional on the joint history preceding the observation,

E_true ||F(mu,u,y)-F(nu,u,y)||_TV <= rho ||mu-nu||_TV,

where rho=(1-underlinedelta_T)(2-delta(Q)). Admissible actions may depend on their allowed observations and histories; the bound is uniform over their realized values.

The tower property iterates this inequality. If rho<1, the expected error after n updates is at most rho^n||mu-nu||_TV. If rho=0, it vanishes after one update. K analytical updates give the K-period factor rho^K, without revealing intermediate joint records to agents.

For a generated M-block window, condition first on the joint history preceding that window. Start its two recursions at the true old prior and nu, whose distance is at most two. Iterating MK updates and then averaging gives

bar L_q^M <= 2 rho^(MK)

uniformly in q, policies, and allowed generated initializations. Consequently the generated-initialization value and policy bounds vanish geometrically with M. No such uniform conditional assertion is made for every fixed retained record. The additional finite-alphabet, positivity, and two-sided domination hypotheses are explicitly retained in the task; no Hilbert-metric result is invoked.

All theorem-critical obligations used in this reference are now derived. The unreproduced specialized external results remain outside this proof's dependency chain.
