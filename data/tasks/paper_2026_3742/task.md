# Problem

## Setup

Let $K\geq 1$ be the number of ordered arms. Each arm $j$ has an i.i.d. sequence of real rewards with mean $\mu_j$ and finite variance $\sigma_j^2$; the sequences for distinct arms are independent. A fixed, known set $\Theta\subseteq\mathbb R^K$ contains $\mu=(\mu_1,\ldots,\mu_K)$. Assume that $\mu$ has a unique maximizer $j^*$, and write $\Delta_j=\mu_{j^*}-\mu_j>0$ for $j\ne j^*$. Define $\Theta_j=\{v\in\Theta:v_j\geq v_i\text{ for every }i\}$.

After $t$ pulls, let $D_t$ be the observed history, $N_j(t)$ the number of pulls of arm $j$, and $\widehat\mu_j(t)$ its empirical reward mean when $N_j(t)>0$. Set $\widehat\mu_j(t)=0$ when $N_j(t)=0$; this zero-weight convention does not supply the policy with an unobserved mean. Define the unit-variance Gaussian pseudo-likelihood and profile likelihood by
$$
L_t(v)=\exp\!\left[-\frac12\sum_{s=1}^{t}(Y_s-v_{A_s})^2\right],\qquad
\bar L_t(j)=\begin{cases}\sup_{v\in\Theta_j}L_t(v),&\Theta_j\ne\varnothing,\\0,&\Theta_j=\varnothing.\end{cases}
$$
Start with the uniform prior $Q_0(j)=1/K$ and draw $A_1$ from $Q_0$. For each $t\geq1$, after observing the reward from round $t$, set
$$
Q_t(j)=\frac{\bar L_t(j)Q_0(j)}{\sum_{k=1}^{K}\bar L_t(k)Q_0(k)}
$$
and draw $A_{t+1}$ from $Q_t$ conditional on $D_t$, using fresh sampling randomness independent of future rewards. The denominator is positive because $\mu\in\Theta_{j^*}$. Let $R(T)=\sum_{t=1}^T(\mu_{j^*}-\mu_{A_t})$.

For the unimodal case, $\Theta$ consists of the vectors that are nondecreasing up to some arm and nonincreasing thereafter; assume $\mu$ belongs to this set and has the stated unique maximizer.

## Task

For each fixed constraint set $\Theta$ containing $\mu$, prove that, almost surely for the run using that set,
$$
\limsup_{T\to\infty}\frac{R(T)}{\log T}\leq\sum_{j\ne j^*}\frac{2}{\Delta_j}.
$$
Prove also that, when the fixed set is $\Theta=\mathbb R^K$,
$$
\lim_{T\to\infty}\frac{R(T)}{\log T}=\sum_{j\ne j^*}\frac{2}{\Delta_j},
$$
whereas for the unimodal constraint set,
$$
\lim_{T\to\infty}\frac{R(T)}{\log T}=\sum_{j:\,|j-j^*|=1}\frac{2}{\Delta_j},
$$
where the last sum includes only existing neighbors. Empty sums are zero.
