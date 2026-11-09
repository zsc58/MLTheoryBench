# Reference Proof

## Contract and obligations

The quantized expert is deterministic, but the raw expert may be stochastic. Write its deterministic representative-action map as \(v_h^*(x)\), so \((q\#\pi^*)_h(\cdot\mid x)=\delta_{v_h^*(x)}\). The learned policy executes representative actions directly in the original dynamics.

We close four obligations: a trajectory-level finite-class statistical bound; the correctly typed observation/auxiliary-law comparison; a causal shared-noise RTVC/stability estimate; and the reward comparison. The general decomposition and its whole-trajectory gluing argument are not assumed.

## 1. Finite-class statistical control

Let \(P_*\) denote the raw expert trajectory law. For a fixed candidate \(\pi\in\Pi\), define
\[
Z_\pi(\tau)=\prod_{h=0}^{H-1}\pi_h(v_h^*(X_h)\mid X_h),
\qquad
\beta_\pi=1-\mathbb E_{P_*}Z_\pi.
\]
Every factor is in \([0,1]\). Realizability supplies a candidate assigning probability one to every observed expert label, so the maximal empirical log-likelihood is zero. Every empirical maximizer therefore satisfies \(Z_\pi(\tau^i)=1\) for all training trajectories.

For each fixed candidate, independence of the trajectories gives
\[
\Pr\{Z_\pi(\tau^i)=1\text{ for all }i\}
=\Pr_{P_*}\{Z_\pi=1\}^{n}
\le (\mathbb E_{P_*}Z_\pi)^n
=(1-\beta_\pi)^n
\le e^{-n\beta_\pi}.
\]
A union bound over the finite class shows that, with probability at least \(1-\delta\), every empirical maximizer satisfies
\[
\beta_{\widehat\pi}\le t,
\qquad t=\frac{\log(|\Pi|/\delta)}{n}. \tag{1}
\]
This also covers \(|\Pi|=1\); if \(t\ge1\), the conclusion is automatic. No strict positivity assumption on candidate probabilities is used.

## 2. Observation and auxiliary-law comparison

This section verifies the trajectory-distance interpretation without identifying auxiliary dequantization with deployment.

For each representative \(v\), choose a reference probability measure supported on the nonempty fibre \(q^{-1}(v)\). Define \(\eta_h(du\mid v,x)\) to be the expert conditional law on that fibre when it has positive expert probability, and the reference measure otherwise. Thus \(\eta\) is the source's expert-induced dequantization kernel. Define
\[
K_h(dx'\mid x,v)=\int T_h(dx'\mid x,u)\eta_h(du\mid v,x).
\]
The observed expert state/label trajectory law is \(P=P^{v^*,K}\). For a candidate, let \(Q_\pi=P^{\pi,K}\). These are auxiliary statistical laws, not deployment laws.

Let \(E\) be the event that all labels equal \(v_h^*(X_h)\). Then \(P(E)=1\). Restricting \(Q_\pi\) to this event and multiplying its stagewise action probabilities gives
\[
Q_\pi|_E=w_\pi P,
\qquad
w_\pi=\prod_h\pi_h(v_h^*(X_h)\mid X_h).
\]
This equality is valid when some factors vanish. Since \(0\le w_\pi\le1\), the common mass of \(P,Q_\pi\) is \(\mathbb E_P w_\pi\), and hence
\[
\operatorname{TV}(P,Q_\pi)=1-\mathbb E_Pw_\pi=\beta_\pi. \tag{2}
\]
With \(D_{\rm Hel}^2(P,Q)=\int(\sqrt p-\sqrt q)^2\), their affinity is \(\mathbb E_P\sqrt{w_\pi}\). The inequality \(1-w\le2(1-\sqrt w)\) for \(0\le w\le1\) gives \(\operatorname{TV}(P,Q_\pi)\le D_{\rm Hel}^2(P,Q_\pi)\). This is a deterministic-policy, common-transition assertion, not a general TV/Hellinger inequality.

The extended laws additionally sample \(U_h\sim\eta_h(\cdot\mid V_h,X_h)\) and evolve using \(T_h(\cdot\mid X_h,U_h)\). To verify projection identities even at zero probabilities, let \(m=|\mathcal V|\) and use a baseline extended law choosing each label uniformly, followed by these same kernels. The density of the extended law for any policy \(\pi\) relative to the baseline is
\[
m^H\prod_h\pi_h(V_h\mid X_h).
\]
It is a function of the state/label projection and, because \(V_h=q(U_h)\), of the state/raw-action projection. Integrating the absolute difference of these densities, or the squared difference of their square roots, proves preservation of TV and squared Hellinger under both projections. The expert extended law has raw marginal \(P_*\), whereas the candidate raw marginal is the auxiliary policy \(\eta\circ\pi\), not deployed \(\pi\).

In particular, (1) controls the relevant auxiliary extended-law TV. The remaining proof uses its equivalent disagreement form directly.

## 3. Causal shared-noise coupling

Condition on training data for which (1) holds, and fix \(\widehat\pi\). Put
\[
a=k\epsilon_q,\qquad D=(k+1)\epsilon_q,\qquad b=\kappa(\gamma(D)).
\]
We construct an expert trajectory \((X_h,A_h)\), a deployed learner trajectory \((Y_h,B_h)\), and auxiliary actions \(V_h\) at expert states.

At each pair of states \((x,y)\), choose a coupling of \(\widehat\pi_h(\cdot\mid x)\) and \(\widehat\pi_h(\cdot\mid y)\) minimizing \(\Pr\{\|V-B\|>a\}\). Such couplings exist measurably here without invoking a specialized coupling theorem: the alphabet is finite, so the optimization is a finite transportation linear program with a fixed cost matrix. Enumerating its finitely many possible bases, retaining feasible basic solutions, and selecting the first minimizer gives a Borel choice as the marginal probability vectors vary. The feasible transportation polytope is nonempty and compact and has an optimal vertex. RTVC bounds the selected optimum by \(\kappa(\|x-y\|)\).

Start both trajectories with the same initial noise and therefore the same initial state. Given the joint past through \((X_h,Y_h)\):

1. Sample \((V_h,B_h)\) using the selected coupling at \((X_h,Y_h)\).
2. Independently of this pair conditional on the past, sample \(A_h\sim\pi_h^*(\cdot\mid X_h)\).
3. Sample fresh transition noise with its prescribed law, independently of the past and these actions, and use it for both state updates.

The expert marginal is its original rollout law. The learner action marginal given the joint past is \(\widehat\pi_h(\cdot\mid Y_h)\), and the fresh noise has the correct law, so the learner marginal is its deployed rollout law. The two trajectories form a shared-noise coupling to which the stipulated expert-side global stability applies.

The expert/auxiliary marginal samples \(V_h\sim\widehat\pi_h(\cdot\mid X_h)\) independently of the raw expert action and next transition conditional on the expert state. Its joint factorization therefore gives
\[
\Pr\{\exists h:V_h\ne v_h^*(X_h)\}
=1-\mathbb E_{P_*}\prod_h\widehat\pi_h(v_h^*(X_h)\mid X_h)
=\beta_{\widehat\pi}. \tag{3}
\]
Although \(V_h\) is coupled to the deployed learner, this marginal factorization remains valid because its first marginal at every joint history is exactly \(\widehat\pi_h(\cdot\mid X_h)\).

Let \(G_h\) be the event that at every stage \(s<h\), both \(V_s=v_s^*(X_s)\) and \(\|V_s-B_s\|\le a\). Since \(q(A_s)=v_s^*(X_s)\) almost surely, binning implies on \(G_h\)
\[
\|A_s-B_s\|\le\|A_s-q(A_s)\|+\|V_s-B_s\|\le D\quad(s<h).
\]
Global stability, its maximum-input form, and equality of initial states imply
\[
\|X_h-Y_h\|\le\gamma(D)\quad\text{on }G_h
\]
almost surely. The construction gives the conditional transport estimate with respect to the actual joint past \(\mathcal F_h\):
\[
\Pr\{\|V_h-B_h\|>a\mid\mathcal F_h\}
\le\kappa(\|X_h-Y_h\|).
\]
Since \(G_h\in\mathcal F_h\) and \(\kappa\) is nondecreasing,
\[
\Pr\{G_h,\ \|V_h-B_h\|>a\}\le b.
\]
If \(G_H\) fails, the first failure is either a label mismatch, included in (3), or a transport failure at a stage with good preceding history. Thus
\[
\Pr(G_H^c)\le\beta_{\widehat\pi}+Hb. \tag{4}
\]
This is a first-failure estimate, not an assertion that raw action discrepancies exceed \(\epsilon_q\) only with this probability. The controlled raw-action threshold is \(D\).

## 4. Reward comparison

On \(G_H\), every action discrepancy is at most \(D\) and every reward-stage state discrepancy is at most \(\gamma(D)\). Consequently,
\[
\sum_{h=0}^{H-1}|r_h(X_h,A_h)-r_h(Y_h,B_h)|
\le H\{L_x\gamma(D)+L_uD\}.
\]
On the complement, the absolute reward difference is at most \(2RH\). Taking expectations and using (1) and (4) yields
\[
J(\pi^*)-J(\widehat\pi)
\le 2RH\frac{\log(|\Pi|/\delta)}{n}
+2RH^2\kappa(\gamma(D))
+H\{L_x\gamma(D)+L_uD\}.
\]
Taking, for example, \(C=2R+L_x+L_u\) proves the required statement.

## Source-proof audit notes

The zero-probability and projection repairs in Section 2 close the local source issues recorded under theory_016. The general source proof of theory_021 conditions after gluing on an enlarged filtration without establishing preservation of the needed conditional law; theory_007 inherits that unsupported step. Neither general result is a premise here. Section 3 explicitly closes the required specialization with a causal construction. Accordingly, no public-target proof obligation remains unresolved, while the broader source claims are not falsely marked as proved.
