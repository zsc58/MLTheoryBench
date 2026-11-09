# Problem

## Setup

Let a fixed measurable score take values in \(\mathbb R\), with larger values interpreted as more anomalous. Let \(F_{\rm tr}\), \(F_{\rm ID}\), and \(F_{\rm OOD}\) be continuous CDFs for training-ID, test-ID, and OOD scores, respectively. Fix integers \(m,n\ge1\) and \(0\le\pi<1\).

A reserve \(R=(r_1,\ldots,r_m)\) consists of iid draws from \(F_{\rm tr}\). Independently of this reserve, the calibration scores \(S_1,\ldots,S_n\) are iid from
\[
F_{\rm mix}=(1-\pi)F_{\rm ID}+\pi F_{\rm OOD}.
\]
All population tail probabilities below concern a fresh score with the indicated law, independent of the reserve and calibration window.

For a score \(z\), define its upper-tail conformal p-value against the reserve by
\[
p_R(z)=\frac{1+\sum_{j=1}^m\mathbf1\{r_j\ge z\}}{m+1}.
\]
Fix \(\alpha,\eta,\eta_1\in(0,1)\) and \(\lambda=k/(m+1)\) for an integer \(1\le k\le m\). For \(p_i=p_R(S_i)\), define
\[
\widehat\pi_\lambda
=1-\frac{n^{-1}\sum_{i=1}^n\mathbf1\{p_i>\lambda\}}{1-\lambda},
\qquad
c_n=\frac{\sqrt{\log(2/\eta_1)/(2n)}}{1-\lambda},
\]
\[
\widehat\pi_{\rm up}
=\min\{1,\max\{0,\widehat\pi_\lambda+c_n\}\}.
\]
Let \(F_n\) be the empirical CDF of the calibration scores, and set
\[
\varepsilon_n=\sqrt{\frac{\log(2/\eta)}{2n}}+\frac1n,
\qquad
q_n=1-\alpha(1-\widehat\pi_{\rm up})+\varepsilon_n.
\]
For any CDF \(G\) and \(u>0\), use the extended generalized inverse
\[
G^{-1}(u)=\inf\{t\in\mathbb R:G(t)\ge u\},\qquad \inf\varnothing=+\infty.
\]
The threshold is
\[
\widehat\tau=F_n^{-1}(q_n).
\]
In particular, \(q_n>1\) produces \(\widehat\tau=+\infty\), not the sample maximum. A fresh score is flagged precisely when it exceeds the threshold; no score is flagged at threshold \(+\infty\).

For a realized reserve, define
\[
\varepsilon_{\rm dr}(R)
=(1-\lambda)-\Pr_{F_{\rm ID}}(p_R(S)>\lambda\mid R),
\qquad
\kappa_\lambda(R)
=\Pr_{F_{\rm OOD}}(p_R(S)>\lambda\mid R).
\]
The calibration assertions are conditional on any realized reserve satisfying
\[
(1-\pi)\varepsilon_{\rm dr}(R)\ge\pi\kappa_\lambda(R).
\]
If this condition holds almost surely over the reserve draw, the same assertions also hold unconditionally over reserve and window.

For the power assertion, put
\[
\tau^*=F_{\rm ID}^{-1}(1-\alpha),\qquad
u_n=1-\alpha(1-\widehat\pi_{\rm up})+2\varepsilon_n,
\qquad
B_n=F_{\rm mix}^{-1}(u_n).
\]
Fix constants \(\underline\kappa>0\) and \(0\le\overline f_{\rm OOD}<\infty\) before drawing the window. Let \(H\) be the event that the mixture and OOD laws are absolutely continuous on \([\tau^*,B_n]\), with densities satisfying
\[
f_{\rm mix}(t)\ge\underline\kappa,
\qquad
f_{\rm OOD}(t)\le\overline f_{\rm OOD}
\]
for Lebesgue-almost every \(t\) in that interval. If \(B_n<\tau^*\), the interval is empty and the condition is vacuous; if \(B_n=+\infty\), it refers to the entire half-line. This is a condition on each realized interval, not an instruction to condition the window distribution on \(H\).

## Task

Prove the following integrated theorem.

For every reserve satisfying the stated conservativity condition, with conditional probability at least \(1-\eta/2-\eta_1\) over the calibration window,
\[
\Pr_{F_{\rm ID}}(S>\widehat\tau)\le\alpha.
\]

With conditional probability at least \(1-\eta-\eta_1\), the following implication holds: if \(H\) occurs, then
\[
\Pr_{F_{\rm OOD}}(S>\tau^*)-\Pr_{F_{\rm OOD}}(S>\widehat\tau)
\le
\frac{\overline f_{\rm OOD}}{\underline\kappa}
\left[\alpha\widehat\pi_{\rm up}+(1-\alpha)\pi+2\varepsilon_n\right].
\]
Equivalently, the conditional probability that \(H\) occurs and this inequality fails is at most \(\eta+\eta_1\). In particular, if the density condition holds almost surely, the displayed power bound holds with probability at least \(1-\eta-\eta_1\).

Moreover, no label-free threshold procedure can avoid the following converse. Let \(P\) be any continuous score law, let
\[
\tau_B=P^{-1}(1-\alpha),\qquad
Q=P(\,\cdot\mid S>\tau_B),\qquad
P'=(1-\pi)P+\pi Q.
\]
Compare world A, whose test-ID law is \(P'\) and which has no contamination, with world B, whose test-ID law is \(P\) and in which each window point is independently contaminated with probability \(\pi\) by a draw from \(Q\). In both worlds the reserve consists of \(m\) iid draws from \(P\), independently of the window. The procedure observes only this reserve and the \(n\) unlabeled window scores.

A possibly randomized label-free threshold procedure is the same measurable function in both worlds of these observations and an auxiliary random seed independent of them and having the same law in both worlds. It takes values in \(\mathbb R\cup\{-\infty,+\infty\}\), receives neither labels nor the identity of the world, and flags a score precisely when it exceeds its output. Couple the worlds using the same observable reserve, window, and auxiliary seed.

For every such output \(\widehat\tau\), prove
\[
\{P'(S>\widehat\tau)\le\alpha\}
\subseteq
\left\{Q(S>\widehat\tau)\le
\frac{\alpha}{\pi+\alpha(1-\pi)}\right\}
\]
almost surely under the common coupling. Consequently, for every \(\beta\in[0,1]\), FPR control with probability at least \(1-\beta\) in world A implies world-B TPR at most \(\alpha/[\pi+\alpha(1-\pi)]\) with probability at least \(1-\beta\).
