# Problem

## Setup

Let $X$ and $Y$ be measurable context and feedback spaces, and let $S$ and $A$ be finite nonempty state and action sets, with $|A|=K$. Consider a horizon-$H$ episodic MDP, where $H\geq1$, with an unknown transition kernel independent of context and i.i.d. contexts. Write $S_H\subseteq S$ for its terminal-state set. The terminal reward is $r\in\{0,1\}$, with measurable mean function $f^*:X\times S_H\times A\to[0,1]$ satisfying
\[
\mathbb E[r\mid x,s_H,a_H]=f^*(x,s_H,a_H).
\]
After the trajectory, feedback $y\in Y$ is observed. Assume
\[
y\perp(s_1,a_1,\ldots,s_{H-1},a_{H-1},a_H)\mid(x,s_H,r),
\]
where the trajectory prefix is empty when $H=1$. A measurable decoder $\phi^*:X\times Y\times S_H\to\{0,1\}$ satisfies $\phi^*(x,y,s_H)=r$ almost surely.

Fix $M\in(0,K/2)$, $c\in[0,1]$, and $\theta\in(0,1)$ with $\sigma=\theta(K-M)/M>1$. Every terminal context-state pair $(x,s)$ is heterogeneous, meaning $\sum_a f^*(x,s,a)\leq M$ and $\max_a f^*(x,s,a)\geq\theta$, or homogeneous, meaning $f^*(x,s,a)=c$ for every $a$.

Use the episode experiment in which the terminal action $U:=a_H$ is sampled uniformly from $A$ using fresh randomization after the context and terminal state have been observed, and the reward and feedback are then generated according to the model. All the reward and feedback assumptions above apply to this experiment. Let $h^*:X\times Y\times S_H\to\Delta_A$ be a version of the conditional action distribution, so that
\[
h^*_a(x,y,s_H)=\Pr(U=a\mid x,y,s_H),\qquad a\in A,
\]
where $\Delta_A=\{v\in[0,1]^A:\sum_{a\in A}v_a=1\}$. All conclusions below involving the observed feedback, reward, or evaluated posterior are almost-sure conclusions under this experiment, simultaneously for all $a\in A$.

For $v\in\Delta_A$, let $\mathbf1$ be the all-one vector indexed by $A$ and define
\[
\Delta(v)=\left\|v-\frac1K\mathbf1\right\|_\infty,\quad \kappa=\frac{K\theta-M}{K(K-M)},\quad \xi=\frac12\left(\frac\theta M-\frac1{K-M}\right),
\]
\[
G(z,t,\xi)=\begin{cases}0&z\leq t,\\(z-t)/\xi&t<z<t+\xi,\\1&z\geq t+\xi,\end{cases}\qquad t=\theta/M-\xi,
\]
and
\[
J(v,a)=\begin{cases}c&\Delta(v)\leq\kappa/2,\\c+(2\Delta(v)/\kappa-1)(G(v_a,t,\xi)-c)&\kappa/2<\Delta(v)<\kappa,\\G(v_a,t,\xi)&\Delta(v)\geq\kappa.\end{cases}
\]

## Task

Write $Q(x,s):=\sum_b f^*(x,s,b)$. Prove that on the event $0<Q(x,s_H)<K$,
\[
h^*_a(x,y,s_H)=\frac{f^*(x,s_H,a)\phi^*(x,y,s_H)}{Q(x,s_H)}+\frac{(1-f^*(x,s_H,a))(1-\phi^*(x,y,s_H))}{K-Q(x,s_H)}.
\]
On the event that $(x,s_H)$ is heterogeneous, prove $\Delta(h^*(x,y,s_H))\geq\kappa$ and $J(h^*(x,y,s_H),a)\leq r$ for every action, with equality for every action maximizing $f^*(x,s_H,\cdot)$. On the event that $(x,s_H)$ is homogeneous, including $c=0$ and $c=1$, prove $h^*(x,y,s_H)=\mathbf1/K$ and $J(h^*(x,y,s_H),a)=c=f^*(x,s_H,a)$ for every action. Finally, prove that for every $a\in A$ and all $v,w\in\Delta_A$,
\[
|J(v,a)-J(w,a)|\leq\left(\frac4\kappa+\frac1\xi\right)\|v-w\|_\infty,
\]
or establish any smaller valid global Lipschitz constant.
