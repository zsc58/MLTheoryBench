# Problem

## Setup

Let $T,K$ be positive integers, let $d\ge2$ be an integer, and write $[K]=\{1,\ldots,K\}$. Let $S,L$ be finite nonnegative constants. A fixed unknown parameter $\theta_*\in\mathbb R^d$ satisfies $\|\theta_*\|_\infty\le S$.

At each round $t$, the learner observes contexts $X_{t,a}\in\mathbb R^d$ for $a\in[K]$, chooses an arm $a_t$, and then receives the reward
\[
r_{t,a_t}=\theta_*^\top X_{t,a_t}+\eta_t.
\]
The contexts satisfy $\|X_{t,a}\|_2\le L$ almost surely. Choices and tie-breaking are measurable functions of the contexts observed through round $t$, the previously selected arms and their observed rewards, and any independent internal randomization of the learner. They do not use the unknown parameter or unobserved rewards or noises.

Let $(\mathcal F_t)_{t=0}^T$ be a filtration such that $\mathcal F_{t-1}$ contains the contexts observed through round $t$, the actions and rewards from earlier rounds, the earlier noises, and any learner randomization used for the round-$t$ choice. The contexts and the round-$t$ choice are $\mathcal F_{t-1}$-measurable, and $\eta_t$ is $\mathcal F_t$-measurable. The noises $(\eta_t)_{t=1}^T$ are i.i.d., mean zero, and each $\eta_t$ is independent of $\mathcal F_{t-1}$. For a known finite constant $\eta_{\max}\ge0$, assume $|\eta_t|\le\eta_{\max}$ almost surely.

Assume there are constants $\epsilon_0,c_0>0$ and a function $q:[0,\epsilon_0]\to(0,1]$ such that, for every $\epsilon\in[0,\epsilon_0]$,
\[
\Pr(\eta_t\ge\eta_{\max}-\epsilon)\ge q(\epsilon),\qquad
\Pr(\eta_t\le-\eta_{\max}+\epsilon)\ge q(\epsilon),\qquad
q(\epsilon)\ge c_0\epsilon.
\]

Initialize $\Theta_0=[-S,S]^d$. At each round, after observing the contexts and before receiving the reward, choose a measurable maximizer $(\theta_t,a_t)$ of $\theta^\top X_{t,a}$ over $\theta\in\Theta_{t-1}$ and $a\in[K]$, with any tie-breaking rule satisfying the information restriction above. After receiving $r_{t,a_t}$, update
\[
\Theta_t=\Theta_{t-1}\cap\{\theta\in\mathbb R^d:|r_{t,a_t}-\theta^\top X_{t,a_t}|\le\eta_{\max}\}.
\]
Let $a_t^*\in\arg\max_{a\in[K]}\theta_*^\top X_{t,a}$ and define
\[
R(T)=\sum_{t=1}^T\big(\theta_*^\top X_{t,a_t^*}-\theta_*^\top X_{t,a_t}\big).
\]

## Task

Fix any $\delta\in(0,1)$, $\mu>0$, and $\xi\in(0,1)$. Prove that, with probability at least $1-\delta$,
\[
R(T)\le \frac{4d\mu LT}{\xi}+\left(1+\frac{\xi L(2S\sqrt d+\mu)}{2d\epsilon_0}\right)\left[\frac{16d^2(d+1)}{c_0\xi(1-\xi)^2}\log\left(\frac{2S\sqrt d}{\mu}+1\right)+\frac{32d}{3c_0\xi}\log\frac1\delta\right].
\]
