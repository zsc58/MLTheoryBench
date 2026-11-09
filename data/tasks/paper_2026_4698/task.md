# Problem

## Setup

Let $p\ge5$ be an odd prime, let $M\ge1$ be an integer, and write $\mathbb Z_p$ for addition modulo $p$. Set $\omega_k=2\pi k/p$ and $K=(p-1)/2$. Consider the full modular-addition data set with labels $z=x+y\pmod p$. A two-layer quadratic network has logits
\[
f(x,y)=\sum_{m=1}^M\xi_m\,\langle e_x+e_y,\theta_m\rangle^2\in\mathbb R^p,
\]
where $e_x$ is the one-hot vector of $x$, and $\theta_m,\xi_m\in\mathbb R^p$. Define the full-data cross-entropy
\[
\ell(\Theta)=-\sum_{x,y\in\mathbb Z_p}\log\!\left(\operatorname{softmax}(f(x,y))_{x+y\,\mathrm{mod}\,p}\right),
\qquad
\operatorname{softmax}(v)_j=\frac{e^{v_j}}{\sum_i e^{v_i}}.
\]
Consider the ideal flow obtained from the loss-minimizing gradient flow $\dot\Theta=-\nabla\ell(\Theta)$ by replacing every softmax probability in the differentiated gradient by $1/p$. All time-dependent quantities below refer to this ideal flow, not to the exact cross-entropy flow.

Use the real orthonormal Fourier basis with constant vector $b_0[j]=p^{-1/2}$ and pairs
\[
b_{k,1}[j]=\sqrt{2/p}\cos(\omega_kj),\qquad
b_{k,2}[j]=\sqrt{2/p}\sin(\omega_kj),\qquad k=1,\ldots,K.
\]
For neuron $m$, let $g_m^k=(\langle b_{k,1},\theta_m\rangle,\langle b_{k,2},\theta_m\rangle)$ and $r_m^k=(\langle b_{k,1},\xi_m\rangle,\langle b_{k,2},\xi_m\rangle)$. With Euclidean norms, set
\[
\alpha_m^k=\sqrt{2/p}\,\|g_m^k\|,\qquad
\beta_m^k=\sqrt{2/p}\,\|r_m^k\|.
\]
At nonzero coefficient pairs define phases by
\[
\phi_m^k=\operatorname{atan2}(-g_{m,2}^k,g_{m,1}^k),\qquad
\psi_m^k=\operatorname{atan2}(-r_{m,2}^k,r_{m,1}^k).
\]
Initialize the constant coefficients to zero:
\[
\langle b_0,\theta_m(0)\rangle=\langle b_0,\xi_m(0)\rangle=0.
\]
For every nonzero frequency, initialize $\alpha_m^k(0)=\beta_m^k(0)=\kappa>0$, with all normalized coefficient directions $g_m^k(0)/\|g_m^k(0)\|$ and $r_m^k(0)/\|r_m^k(0)\|$ iid uniform on the unit circle.

Let
\[
\delta_m^k(0)=\operatorname{dist}_{2\pi}\!\bigl(2\phi_m^k(0)-\psi_m^k(0),0\bigr)\in[0,\pi]
\]
be the shortest circular distance, and define $k_m^\star=\arg\min_{1\le k\le K}\delta_m^k(0)$. Ties have probability zero; on a tie choose the smallest index.

For each neuron $m$, let $[0,T_m)$ be its own maximal existence interval in the ideal model. Its solution is considered on this interval rather than stopped when a different neuron's solution ceases to exist. For $\epsilon\in(0,1)$, define
\[
t_{m,\epsilon}=\inf\left\{t\in[0,T_m):
\max_{k\ne k_m^\star}\frac{\beta_m^k(t)}{\beta_m^{k_m^\star}(t)}\le\epsilon\right\},
\]
where the set includes only times with positive denominator and $\inf\varnothing=+\infty$.

## Task

Prove the following integrated theorem. There is a universal constant $C$ such that, for every fixed $c\in(0,1)$, every sufficiently large odd prime $p$ satisfying
\[
1-2c^2\pi^2\left(\frac{\log p}{p}\right)^2>0,
\]
and every $\epsilon\in(0,1)$, the following holds for each fixed neuron $m$, with probability at least $1-\widetilde O(p^{-c})$ over the stated independent initialization:
\[
\beta_m^{k_m^\star}(t)>0,\qquad
\beta_m^{k_m^\star}(t)\ge\beta_m^k(t)
\quad\text{for every }k\text{ and }0\le t<T_m,
\]
the dominance time is attained before $T_m$, and
\[
t_{m,\epsilon}\le C\left[\frac{\pi^2}{\kappa}p^{-(2c+3)}+
\frac{(c+1)\log p+\log(1/(1-\epsilon))}
{p\kappa\left(1-2c^2\pi^2(\log p/p)^2\right)}\right].
\]
Here $\log$ is the natural logarithm, $\widetilde O(\cdot)$ hides universal polylogarithmic factors, and the sufficiently-large-$p$ threshold may depend on $c$. The constant $C$ is independent of $c,p,M,\kappa,\epsilon$, and $m$. The probability statement is for each fixed neuron, not a simultaneous assertion over all neurons.
