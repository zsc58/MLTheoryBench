# Problem

## Setup

Let \(V=\{1,\ldots,n\}\), where \(n\ge2\). Arm \(i\) has an unknown distribution \(D_i\) supported on \([0,1]\), with mean \(\mu_i\). Assume there is a unique optimal arm
\[
i^\star=\arg\max_i\mu_i,
\qquad \Delta_i=\mu_{i^\star}-\mu_i,
\qquad \Delta_{\min}=\min_{i\ne i^\star}\Delta_i,
\qquad \Delta_{\max}=\max_i\Delta_i.
\]

For every integer \(t\ge1\), let \(G_t=(V,E_t)\) be a simple undirected graph. The graph sequence is chosen obliviously, possibly randomly, before interaction, independently of reward randomness and the learner's private randomization. Put
\[
\mathcal N_t(u)=\{u\}\cup\{v:\{u,v\}\in E_t\},
\qquad \deg_t(u)=|\mathcal N_t(u)|-1.
\]
The learner starts from an arbitrary fixed state \(X_0\in V\), with no initial reward observation. At round \(t\), it observes only its current closed neighborhood \(\mathcal N_t(X_{t-1})\), chooses \(X_t\) in that neighborhood using its past observations and private randomization, and then observes only the reward \(r_t\) drawn at \(X_t\). Conditional on the information and choice preceding that draw, \(r_t\) has distribution \(D_{X_t}\); draws use fresh reward randomness. In particular, rewards from repeated pulls of an arm are generated independently over time. The learner does not observe future graphs or unvisited rewards. Define
\[
R(T)=\sum_{t=1}^T(\mu_{i^\star}-r_t).
\]

For the graph at round \(t\), define the canonical local kernel
\[
P_t(u,v)=
\begin{cases}
(1+\deg_t(u))^{-1},&v\in\mathcal N_t(u),\\
0,&\text{otherwise}.
\end{cases}
\]
Assume that all \(P_t\) are reversible with the same fixed stationary distribution \(\pi\). Put \(\pi_{\min}=\min_i\pi_i\). Fix a positive integer \(W\) and \(\rho,\gamma\in(0,1]\), and assume that every interval of \(W\) consecutive rounds contains at least \(\lceil\rho W\rceil\) indices satisfying
\[
\operatorname{gap}_{\rm abs}(P_t)
=1-\max\{|\lambda_2(P_t)|,|\lambda_n(P_t)|\}\ge\gamma,
\]
where \(1=\lambda_1(P_t)\ge\cdots\ge\lambda_n(P_t)\) are the eigenvalues. This condition holds almost surely for the graph process.

Fix an integer horizon \(T\ge2\), confidence level \(\delta\in(0,1)\), inverse temperature \(\lambda\ge0\), and \(\varepsilon_0\in(0,1]\). Let
\[
N_s(i)=\sum_{t=1}^s\mathbf1\{X_t=i\}.
\]
Define the empirical mean by \(\widehat\mu_s(i)=0\) when \(N_s(i)=0\), and otherwise by the average of the observed rewards of arm \(i\). Set
\[
w_s(i)=
\begin{cases}
\sqrt{\dfrac{\log(4nT/\delta)}{2N_s(i)}},&N_s(i)\ge1,\\
1,&N_s(i)=0,
\end{cases}
\quad
\operatorname{LCB}_s(i)=\widehat\mu_s(i)-w_s(i),
\quad
\operatorname{UCB}_s(i)=\widehat\mu_s(i)+w_s(i).
\]
During exploration define
\[
\eta_{t-1}(i)=\widehat\mu_{t-1}(i)+w_{t-1}(i),
\qquad \bar w_{t-1}=\max_iw_{t-1}(i),
\]
\[
q_t(u,v)=
\begin{cases}
\dfrac{\exp(\lambda\eta_{t-1}(v))}
{\sum_{z\in\mathcal N_t(u)}\exp(\lambda\eta_{t-1}(z))},&v\in\mathcal N_t(u),\\
0,&v\notin\mathcal N_t(u),
\end{cases}
\]
\[
\varepsilon_t=
\max\left\{\varepsilon_0,\frac{2\bar w_{t-1}}{1+2\bar w_{t-1}}\right\},
\qquad
M_t=\varepsilon_tP_t+(1-\varepsilon_t)q_t.
\]
At round \(t\), sample from the row \(M_t(X_{t-1},\cdot)\). After observing its reward, let \(b_t\) be an empirical-mean maximizer, using any fixed tie-breaking rule, and stop exploration at the first \(t\in\{1,\ldots,T\}\) for which
\[
\operatorname{LCB}_t(b_t)\ge\max_{i\ne b_t}\operatorname{UCB}_t(i),
\]
using \(T\) if no certificate occurs. Denote this stopping time by \(\sigma\) and commit to \(b_\sigma\). In any remaining rounds, move directly to the committed arm whenever it is locally available and otherwise use \(P_t\); after reaching it, remain there using its self-loop. Call this the reward-biased local explore-then-commit procedure. Its learning regret is
\[
R_{\rm learn}=\sum_{t=1}^{\sigma}(\mu_{i^\star}-r_t).
\]

Define
\[
h_0=W+\left\lceil\frac{2}{\rho\gamma}\log\frac1{\pi_{\min}}\right\rceil,
\qquad
\vartheta_0=\frac{\varepsilon_0^{h_0}}2,
\]
\[
\Psi_0(\delta)=
\max\left\{
\frac{\log(4nT/\delta)}{\vartheta_0\pi_{i^\star}\Delta_{\min}^2},
\max_{i\ne i^\star}
\frac{\log(4nT/\delta)}{\vartheta_0\pi_i\Delta_i^2}
\right\}.
\]

For the gain statement, let \(\widetilde X_t\) denote the same exploration rule run perpetually, without stopping or navigation, with its own counts and reward estimates and with the fixed parameters \(T,\delta,\lambda,\varepsilon_0\). Let \(\widetilde{\mathcal F}_s\) be its history through round \(s\): the local neighborhoods observed, actions taken, rewards observed, and private randomization used through that round. Fix a deterministic \(t_g\in\{0,\ldots,T\}\) and set
\[
h_1=1+W+\left\lceil\frac1{\rho\gamma}
\log\frac{2}{\pi_{\min}^{3/2}}\right\rceil,
\qquad
\vartheta_1=\frac{\varepsilon_0^{h_1}}2.
\]
For \(j\ge1\), put \(s_j=t_g+(j-1)h_1\) and \(\mathcal G_{j-1}=\widetilde{\mathcal F}_{s_j}\). Assume there are a fixed set \(B\subseteq V\) containing \(i^\star\) and fixed numbers \(\kappa_i^{\rm gain}\ge\vartheta_1\pi_i\) such that, for every \(j\ge1\) with \(s_j+h_1\le T\) and every \(i\in B\), almost surely,
\[
\Pr(\widetilde X_{s_j+h_1}=i\mid\mathcal G_{j-1})\ge\kappa_i^{\rm gain}.
\]
Set \(\kappa_i=\kappa_i^{\rm gain}\) on \(B\), and \(\kappa_i=\vartheta_1\pi_i\) otherwise, and define
\[
\Psi_g(\delta)=
\max\left\{
\frac{\log(4nT/\delta)}{\kappa_{i^\star}\Delta_{\min}^2},
\max_{i\ne i^\star}
\frac{\log(4nT/\delta)}{\kappa_i\Delta_i^2}
\right\}.
\]
Finally, put \(g(i^\star)=\Delta_{\min}\), \(g(i)=\Delta_i\) for \(i\ne i^\star\),
\[
\Lambda_i=\frac1{\pi_i g(i)^2},
\qquad \Lambda_{\max}=\max_i\Lambda_i,
\qquad
H_\zeta=\left\{i:\Lambda_i\ge\frac{\Lambda_{\max}}{1+\zeta}\right\}
\quad(\zeta>0).
\]

## Task

Prove that there is a universal constant \(C>0\) for which the following integrated theorem holds.

1. **Worst-case safety and learnability.** If
\[
T\ge T_0:=h_0\left\lceil C\Psi_0(\delta)\right\rceil,
\]
then, with probability at least \(1-\delta\), the procedure identifies \(i^\star\), stops by \(\sigma\le T_0\), and has \(R_{\rm learn}\le T_0\). With \(\delta=T^{-2}\), whenever the displayed horizon condition holds,
\[
\mathbb E R(T)
\le T_0+\frac{2\Delta_{\max}h_0}{\pi_{i^\star}}+1,
\]
and hence \(\mathbb E R(T)=o(T)\) for fixed problem parameters.

2. **Conditional performance gain.** Under the post-burn-in block-end condition, if
\[
T\ge T_g:=t_g+h_1\left\lceil C\Psi_g(\delta)\right\rceil,
\]
then, with probability at least \(1-\delta\), the procedure identifies \(i^\star\), stops by \(T_g\), and has \(R_{\rm learn}\le T_g\). Moreover, under this same horizon condition, if \(H_\zeta\subseteq B\) and
\[
\kappa_i^{\rm gain}\ge(1+\zeta)\vartheta_1\pi_i
\qquad\text{for every }i\in H_\zeta,
\]
then
\[
\Psi_g(\delta)
\le
\frac{\log(4nT/\delta)\Lambda_{\max}}
{(1+\zeta)\vartheta_1},
\]
so
\[
T_g=O\!\left(t_g+
\frac{h_1\log(4nT/\delta)\Lambda_{\max}}
{(1+\zeta)\vartheta_1}\right),
\]
with an absolute implicit constant. Thus covering every near-bottleneck arm yields a factor \((1+\zeta)^{-1}\) reduction in the leading learning term relative to the baseline using only \(\kappa_i\ge\vartheta_1\pi_i\).
