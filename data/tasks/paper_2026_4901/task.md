# Problem

## Setup

Let $\mathcal O$ be a connected metric observation space equipped with a sigma-algebra $\mathcal B$. All measures below are on $(\mathcal O,\mathcal B)$. Let $k,m$ be integers with $2\le k\le m$. There are $k$ latent actions and $m$ demonstrators. For each $o\in\mathcal O$ and action $a\in\{1,\ldots,k\}$, let $t_a^o$ be a probability measure; for each demonstrator $e\in\{1,\ldots,m\}$, let $\pi_e^*(\cdot\mid o)\in\mathbb R^k$ be a probability vector. The observable conditional law is
\[
p_e^o=\sum_{a=1}^k\pi_e^*(a\mid o)t_a^o.
\]
Write $\Pi^*(o)=[\pi_1^*(\cdot\mid o)\ \cdots\ \pi_m^*(\cdot\mid o)]\in\mathbb R^{k\times m}$ and $T^*(o)=[\Phi(t_1^o)\ \cdots\ \Phi(t_k^o)]$, where $\Phi$ is an injective linear embedding of the vector space of finite signed measures on $(\mathcal O,\mathcal B)$ into a real Hilbert space $\mathcal H$. Let $P(o)=[\Phi(p_1^o)\ \cdots\ \Phi(p_m^o)]$ and
\[
G_\Phi(s_1,\ldots,s_k)=[\langle\Phi(s_i),\Phi(s_j)\rangle]_{i,j=1}^k.
\]
Assume that $\det G_\Phi(t_1^o,\ldots,t_k^o)>0$ for every $o$, each map $o\mapsto\Phi(t_a^o)$ is continuous in the Hilbert norm, and the $k$ true components are pairwise distinct at every $o$.

For a cone $D\subseteq\mathbb R^k$, write $D^*=\{y\in\mathbb R^k:y^Tx\ge0\text{ for all }x\in D\}$, and let $\operatorname{bd}(D)$ denote its boundary in $\mathbb R^k$. Let $\mathbf1\in\mathbb R^k$ be the all-ones vector and $e_j$ the $j$th standard basis vector. Assume each $\Pi^*(o)$ is column-stochastic and sufficiently scattered in the following sense: for $H=(\Pi^*(o))^T$, let $\operatorname{cone}(H^T)$ be the nonnegative conic hull of the columns of $H^T$, let
\[
C_k=\{x\in\mathbb R^k:\mathbf1^Tx\ge\sqrt{k-1}\|x\|_2\},\qquad
C_k^*=\{x\in\mathbb R^k:\mathbf1^Tx\ge\|x\|_2\},
\]
and require
\[
C_k\subseteq\operatorname{cone}(H^T),\qquad
\operatorname{cone}(H^T)^*\cap\operatorname{bd}(C_k^*)
=\{\lambda e_j:\lambda\ge0,\ j=1,\ldots,k\}.
\]
Column-stochastic means nonnegative columns summing to one.

For each $o$, consider the optimization over probability measures $\bar t_1^o,\ldots,\bar t_k^o$ and a column-stochastic matrix $\Pi(o)\in\mathbb R^{k\times m}$ satisfying
\[
P(o)=[\Phi(\bar t_1^o)\ \cdots\ \Phi(\bar t_k^o)]\Pi(o),
\]
that minimizes $\det G_\Phi(\bar t_1^o,\ldots,\bar t_k^o)$. Suppose a family of such minimizers is given with each map $o\mapsto\Phi(\bar t_a^o)$ continuous in the Hilbert norm and $o\mapsto\Pi(o)$ continuous in the usual Euclidean topology.

For a permutation matrix $\Sigma$, use $\Sigma(a)$ for the index specified by $\Sigma e_a=e_{\Sigma(a)}$.

## Task

Prove that there exists a single permutation matrix $\Sigma$ such that, for every $o\in\mathcal O$,
\[
\bar t_a^o=t^o_{\Sigma(a)}\quad(a=1,\ldots,k),\qquad \Pi(o)=\Sigma^T\Pi^*(o).
\]
Moreover, if on some nonempty subset $\mathcal S\subseteq\mathcal O$ the true action labeling is known and the minimizer agrees with it (so $\bar t_a^o=t_a^o$ and $\Pi(o)=\Pi^*(o)$ there), prove that $\Sigma=I_k$ and recovery is exact for all $o$.
