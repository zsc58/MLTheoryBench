# Problem

## Setup

Fix \(T>0\). Let \(\mathcal N\) be the set of nondecreasing cadlag functions \(\eta:[0,T]\to\mathbb N_0\), where \(\mathbb N_0=\{0,1,2,\ldots\}\), with \(\eta(0)=0\), finitely many unit jumps, and no jump at \(T\). Write their event times as \(0<t_1<\cdots<t_m<T\), put \(t_0=0,t_{m+1}=T\), and define \(\tau_0=0\), \(\tau_k=t_k-t_{k-1}\) for \(1\le k\le m\), and \(\tau_{m+1}=T-t_m\). The case \(m=0\) is allowed.

For \(\eta,\xi\in\mathcal N\), set
\[
d_N(\eta,\xi)=\int_0^T|\eta(u)-\xi(u)|\,du,
\]
and equip \(\mathcal N\) with the Borel sigma-algebra of this metric. For continuous bounded-variation scalar paths set
\[
d_1(x,y)=\int_0^T|x(u)-y(u)|\,du.
\]

Define \(\Phi(\eta)\) as the unique continuous path affine on each \([t_k,t_{k+1}]\) and satisfying \(\Phi(\eta)(t_k)=\tau_k\) for \(k=0,\ldots,m+1\). Define the time-augmented path
\[
\overline\Phi(\eta)(u)=(u,\Phi(\eta)(u))\in\mathbb R^2.
\]

For a continuous bounded-variation path \(X:[0,T]\to\mathbb R^2\), define its signature levels by \(S^0(X)=1\) and
\[
S^k(X)=\int_{0<u_1<\cdots<u_k<T}dX(u_1)\otimes\cdots\otimes dX(u_k),\qquad k\ge1.
\]
Write \(S(X)=(S^0(X),S^1(X),\ldots)\). For an integer \(M\ge0\), write \(S^{\le M}(X)=(S^0(X),\ldots,S^M(X))\). Use the Euclidean norm in each tensor power with respect to the standard tensor basis, and the direct-sum Euclidean norm on degrees zero through \(M\).

Call a Borel probability law \(R\) on \(\mathcal N\) admissible if it satisfies all of the following conditions:
\[
\mathbb E_{\eta\sim R}\!\left[\int_0^T\eta(u)\,du\right]<\infty,
\qquad
\mathbb E_{\eta\sim R}\|S^k(\overline\Phi(\eta))\|_2<\infty\quad\text{for every }k\ge0,
\]
and its expected signature has infinite radius of convergence, meaning
\[
\sum_{k=0}^{\infty}r^k\left\|\mathbb E_{\eta\sim R}S^k(\overline\Phi(\eta))\right\|_2<\infty
\quad\text{for every }r>0.
\]
For admissible laws \(P,Q\), define
\[
\mathrm{SigW}_1^{(M)}(P,Q)=\left\|\mathbb E_{\eta\sim P}S^{\le M}(\overline\Phi(\eta))-\mathbb E_{\xi\sim Q}S^{\le M}(\overline\Phi(\xi))\right\|_2.
\]

For \(\delta>0\), let \(\mathcal N_\delta\subset\mathcal N\) consist of paths for which every gap \(\tau_1,\ldots,\tau_{m+1}\) is at least \(\delta\).

## Task

Prove the following single integrated theorem: the map \(\Phi\) satisfies
\[
d_1(\Phi(\eta),\Phi(\xi))\le5T\,d_N(\eta,\xi)\quad\text{for all }\eta,\xi\in\mathcal N,
\]
is injective and bijective onto its image, and for every \(\delta>0\) there is a finite constant \(\kappa(\delta,T)>0\), depending only on \(\delta,T\), such that
\[
d_N(\eta,\xi)\le\kappa(\delta,T)\,d_1(\Phi(\eta),\Phi(\xi))^{1/2}
\quad(\eta,\xi\in\mathcal N_\delta).
\]
Furthermore, for any two distinct admissible laws \(P\ne Q\), \(\mathrm{SigW}_1^{(M)}(P,Q)>0\) for at least one finite integer \(M\ge0\), while for each fixed integer \(M\ge0\), \(\mathrm{SigW}_1^{(M)}\) is a pseudometric on the class of admissible laws.
