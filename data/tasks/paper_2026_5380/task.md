# Problem

## Setup

Let \(A\in\mathbb R^{n\times p}\), let \(L(A\theta)\) be a convex differentiable loss, and fix \(M>0\), \(\lambda>0\), and an integer \(k\). Partition \(\{1,\ldots,p\}\) into disjoint sets \(J_0,J_1,J_f\), with \(|J_1|\le k\), and put \(\bar k=k-|J_1|\) and \(p_f=|J_f|\).

Use the perspective convention \(\theta_j^2/u_j=0\) at \((\theta_j,u_j)=(0,0)\), and \(+\infty\) when \(u_j=0\) and \(\theta_j\ne0\). Define
\[
 g(\theta)=\inf_u\ \frac12\sum_{j=1}^p\frac{\theta_j^2}{u_j},
\]
where the infimum is over \(u\) satisfying
\[
 u_j=0\ (j\in J_0),\qquad u_j=1\ (j\in J_1),\qquad 0\le u_j\le1\ (j\in J_f),
\]
\[
 \mathbf 1^\top u\le k,\qquad |\theta_j|\le M u_j\quad(1\le j\le p).
\]
Let
\[
 \Phi(\theta)=L(A\theta)+2\lambda g(\theta),
\]
and let \(\theta^\star\) be a finite optimal solution of \(\min_\theta\Phi(\theta)\).

## Task

Prove that one can recover an optimal indicator vector \(u^\star\) paired with \(\theta^\star\), meaning that \((\theta^\star,u^\star)\) minimizes
\[
 L(A\theta)+\lambda\sum_{j=1}^p\frac{\theta_j^2}{u_j}
\]
over the constraints in the setup, as follows. Set \(u_j^\star=0\) on \(J_0\) and \(u_j^\star=1\) on \(J_1\).

On \(J_f\), if \(\bar k=0\), set \(u_j^\star=0\) for all \(j\in J_f\). If \(\bar k>0\) and at most \(\bar k\) free coordinates have \(\theta_j^\star\ne0\), set \(u_j^\star=1\) for those nonzero coordinates and \(u_j^\star=0\) for the remaining free coordinates.

In the remaining case, sort the free magnitudes in nonincreasing order:
\[
 |\theta_{\pi(1)}^\star|\ge\cdots\ge|\theta_{\pi(p_f)}^\star|,
\]
and write \(|\theta_{\pi(0)}^\star|=+\infty\). Prove that there is an \(s\in\{0,\ldots,\bar k-1\}\) for which
\[
 \tau=\frac{\sum_{r=s+1}^{p_f}|\theta_{\pi(r)}^\star|}{\bar k-s},
 \qquad
 |\theta_{\pi(s)}^\star|\ge\tau\ge|\theta_{\pi(s+1)}^\star|,
\]
and that an optimal paired indicator vector is
\[
 u_{\pi(r)}^\star=
 \begin{cases}
 1,&r\le s,\\
 |\theta_{\pi(r)}^\star|/\tau,&r>s.
 \end{cases}
\]
Equivalently, on every free coordinate in this case, \(u_j^\star=\min\{1,|\theta_j^\star|/\tau\}\).
