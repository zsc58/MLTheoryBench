# Problem

## Setup

Let \(d\ge1\) be an integer, \(T>0\), and \(h\ge0\). If \(h>0\), assume \(m:=T/h\) is a positive integer. All probability laws and Markov kernels below are on \(\mathbb R^d\).

Let
\[
Z:=\int_{\mathbb R^d}e^{-f(x)}\,dx\in(0,\infty),\qquad \nu(dx)=Z^{-1}e^{-f(x)}dx,
\]
where \(f\in C^3\), \(f(0)=0\) is a global minimum, and, for finite constants \(L>0\) and \(M\ge0\),
\[
\|\nabla^2f(x)\|_{\rm op}\le L,\qquad \|\nabla^3f(x)\|_{\rm op}\le M
\]
for every \(x\). Here the norm of a multilinear form is its supremum on tuples of Euclidean unit vectors.

Define \(\psi(r)=e^{r^2}-1\). For a random vector \(U\), define
\[
\|U\|_\psi:=\inf\{a>0:\mathbb E\,\psi(\|U\|/a)\le1\},
\]
with the infimum of the empty set equal to \(+\infty\). Define \(W_\psi(\rho,\pi)\) to be the infimum of \(\|X-Y\|_\psi\) over all couplings with \(X\sim\rho\) and \(Y\sim\pi\). Assume \(\|X\|_\psi\le K_\nu\) for \(X\sim\nu\), where \(0<K_\nu<\infty\).

For initial position and velocity \((x,v)\), let \(q_T(x,v)\) be the time-\(T\) position of
\[
\dot x_t=v_t,\qquad \dot v_t=-\nabla f(x_t),\qquad (x_0,v_0)=(x,v).
\]
This is the flow with Hamiltonian \(H(x,v)=f(x)+\|v\|^2/2\). Let \(P_T\) be the position kernel that independently samples \(v\sim N(0,I_d)\) and returns \(q_T(x,v)\).

For \(h>0\), initialize \((x_0,v_0)=(x,v)\) and run \(m\) velocity-Verlet steps:
\[
 v_{j+1/2}=v_j-\tfrac h2\nabla f(x_j),\quad
 x_{j+1}=x_j+h v_{j+1/2},\quad
 v_{j+1}=v_{j+1/2}-\tfrac h2\nabla f(x_{j+1}),\qquad 0\le j<m.
\]
Denote the resulting position by \(\widetilde q_{T,h}(x,v)\). Let \(P_h\) independently sample \(v\sim N(0,I_d)\) and return \(\widetilde q_{T,h}(x,v)\). At \(h=0\), define \(P_0:=P_T\).

Let \(Q\) be a Markov kernel with invariant probability law \(\bar\nu\). Suppose there are constants \(c_1\ge1\), \(c_2>0\), and \(\Delta_h\ge0\) such that, for every probability law \(\eta\) and every integer \(k\ge0\),
\[
W_\psi(\eta Q^k,\bar\nu)\le c_1e^{-c_2k}W_\psi(\eta,\bar\nu),\qquad W_\psi(\bar\nu,\nu)\le\Delta_h.
\]
Here \(Q^0\) is the identity kernel. Assume also \(L(T^2+Th)\le1/12\). Define
\[
 p_{xy}=\frac3{2T},\quad p_v=\frac7{25T},\quad p_x=\frac{49L}{180},
\]
\[
 j_{xy}=\frac{11MT^2}{2},\quad j_c=\frac{44}{135T},\quad j_v=\frac{440MT^2}{135},\quad j_x=\frac{352MT}{675}.
\]
For a fixed real \(q>1\), set \(s=2q-1\) and \(u=\sqrt{1+1/(4s)}\), and define
\[
 \delta_1=s\left(8dMT^2+\frac{3\sqrt d}{2T}\right),\qquad
 \delta_2=\frac{9qs}{4T^2}.
\]
Assume
\[
\Delta_h\le\min\left\{\frac{\sqrt{2\log2}}{4s\left(\frac{\sqrt d(6\sqrt d\,j_{xy}+p_{xy}u)}{\sqrt2}+h\sqrt d(6\sqrt d\,j_x+p_xu)\right)},
\frac1{\sqrt{8s[p_{xy}^2(1+3su^2)+2h^2p_x^2(1+3su^2)]}}\right\},
\]
\[
 h\le\min\left\{\frac{u-1}{p_v},\frac{\sqrt{\log2}}{2\sqrt2\,s\sqrt d(6\sqrt d\,j_x+p_xu)K_\nu},
\frac1{4K_\nu p_x\sqrt{(1+3su^2)s}}\right\}.
\]

For probability laws \(\rho,\pi\) and real \(r>1\), define
\[
R_r(\rho\|\pi)=\frac1{r-1}\log\int\left(\frac{d\rho}{d\pi}\right)^r d\pi
\]
when \(\rho\ll\pi\), with value \(+\infty\) if absolute continuity fails or the integral is infinite. All logarithms are natural.

## Task

Prove that, for every probability law \(\mu\) and every nonnegative integer \(k\) satisfying
\[
 k\ge c_2^{-1}\log\left(\frac{c_1W_\psi(\mu,\bar\nu)}{4\sqrt{\log2}}\left[\delta_1+\sqrt{\delta_1^2+16(\log2)\delta_2}\right]\right),
\]
one has
\[
R_q(\mu Q^kP_h\|\nu)\le
\frac{3(\delta_1+\delta_2)}{2(2q-1)}\sqrt{\log2}\,c_1^2e^{-c_2k}\max\{1,W_\psi(\mu,\bar\nu)^2\}+B,
\]
where
\[
\begin{aligned}
B={}&dh[6j_c+6\sqrt d\,j_v+108sdh j_v^2+hp_v^2+2p_v]\\
&+2\sqrt d[6\sqrt d\,j_{xy}+p_{xy}u]\Delta_h
+p_{xy}^2(1+3su^2)\Delta_h^2\\
&+2h\sqrt d[6\sqrt d\,j_x+p_xu]\bigl(\Delta_h+K_\nu+\sqrt{\Delta_h^2+K_\nu^2}\bigr)\\
&+2h^2p_x^2(1+3su^2)(\Delta_h^2+K_\nu^2).
\end{aligned}
\]
In the threshold, use \(\log0=-\infty\) and \(\log(+\infty)=+\infty\): zero initial distance imposes no additional restriction on nonnegative \(k\), while infinite initial distance admits no finite \(k\).
