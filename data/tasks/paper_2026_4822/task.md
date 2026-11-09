# Problem

## Setup

Consider a stochastic bandit with a finite set of arms $\{1,\ldots,K\}$. Pulls of arm $a$ produce independent rewards with law $P_a$, mean $\mu_a$, and finite variance $\sigma_a^2$. Assume there is a unique optimal arm $a^*\in\{1,\ldots,K\}$, so $\mu_{a^*}>\mu_a$ for every $a\ne a^*$. Two policies $\pi_0$ and $\pi_1$ choose arms from their own past histories (and may randomize); their randomizations are independent.

For horizon $T$, let $N_{i,a}(T)$ be the number of pulls of arm $a$ and let $Y_i(T)=\sum_{t=1}^T R_{i,t}$ be the cumulative reward of an ordinary run of policy $\pi_i$. Define the naive estimator from two independent ordinary runs by $\widehat\theta_{\mathrm{ind}}(T)=Y_1(T)-Y_0(T)$.

Define the coupled reuse experiment as follows. First run $\pi_0$ for $T$ rounds, recording its actions and rewards. Then run $\pi_1$ for $T$ rounds with independent policy randomization. On the treatment run, when arm $a$ is pulled for the $(m+1)$st time, use the recorded $(m+1)$st reward of arm $a$ from the control run if that reward exists; if the control run pulled arm $a$ at most $m$ times, draw a fresh independent reward from $P_a$. Let $\widehat\theta_{\mathrm{cpl}}(T)$ be treatment cumulative reward minus control cumulative reward in this experiment. All variances below are over the policy and reward randomness.

Assume that for each policy $i\in\{0,1\}$ and every suboptimal arm $a\ne a^*$, $\mathbb E[N_{i,a}(T)]=o(T)$ and $\operatorname{Var}(N_{i,a}(T))=o(T)$ as $T\to\infty$.

## Task

Prove that
\[
\lim_{T\to\infty}\frac{\operatorname{Var}(\widehat\theta_{\mathrm{ind}}(T))}{T}=2\sigma_{a^*}^2,\qquad
\lim_{T\to\infty}\frac{\operatorname{Var}(\widehat\theta_{\mathrm{cpl}}(T))}{T}=0.
\]
