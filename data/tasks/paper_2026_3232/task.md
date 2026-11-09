# Problem

## Setup

Let \(I\subseteq\mathbb N\) be a nonempty finite or countably infinite arm index set. For each \(i\in I\), let \(\mathsf O_i\) be a standard Borel observation space. Arm \(i\) has latent data
\[
Z_i=(\theta_i,Y_{i,1},Y_{i,2},\ldots)\in\mathbb R\times\mathsf O_i^{\mathbb N}.
\]
These data are sampled before interaction and are initially hidden. The score \(\theta_i\) is random under the posterior but remains fixed throughout interaction, as does the observation sequence. Under a posterior \(\mu\), the vectors \(Z_i\) are independent; within an arm, observations may depend arbitrarily on the score and on one another. Assume that the supremum of the scores is attained almost surely. Define \(b^\star\) to be the smallest index attaining that supremum. A posterior satisfying these independence and attainment conditions is called admissible.

At round \(t\), let \(N_i(t-1)\) be the number of previous plays of arm \(i\). A policy chooses an arm \(A_t\) measurably from past actions and observations, possibly using private randomness independent of all latent arm data. It then observes only
\[
Y_{A_t,N_{A_t}(t-1)+1}.
\]
It receives no other feedback, including no indication of whether the selected arm is \(b^\star\). Unplayed arms supply no observations, and observation indices advance only when their arm is played.

After any finite interaction history, use a regular conditional distribution of the residual vectors
\[
Z_i^{\mathrm{res}}=(\theta_i,Y_{i,N_i+1},Y_{i,N_i+2},\ldots),
\]
where \(N_i\) is the number of plays in that history. Reindex each residual observation sequence from one. These conditional posteriors are admissible almost surely; conditional distributions and their asserted properties are understood up to histories of probability zero.

At each round Thompson sampling draws a fresh score vector from the current posterior, conditionally independently of the actual latent data, and plays the smallest-index maximizing arm. Let
\[
q_i(\mu)=\Pr_\mu(b^\star=i).
\]
For a policy \(\pi\) and a nonnegative integer \(m\), define its expected number of mistakes in \(m\) rounds by
\[
L_m^\pi(\mu)=\mathbb E_\mu^\pi\!\left[\sum_{t=1}^m\mathbf1\{A_t\ne b^\star\}\right],
\]
where the expectation includes both the latent data and policy randomness. Set
\[
L_m^\star(\mu)=\inf_\pi L_m^\pi(\mu),\qquad
L_m^{TS}(\mu)=L_m^{\pi_{TS}}(\mu),
\]
with the infimum over all measurable \(m\)-round policies with the information access specified above. Selecting a maximizing arm other than the designated \(b^\star\) still counts as a mistake.

## Task

Prove that for every admissible posterior \(\mu\) and every finite nonnegative integer horizon \(T\),
\[
L_T^{TS}(\mu)\le2L_T^\star(\mu).
\]
