# Problem

## Setup

Fix distributions $F_0,F_1$, a measurable real-valued score $S$, a number $\delta\in(0,1/2)$, and $\alpha\in(0,1)$ as the change time $T\to\infty$. For each integer $T\ge2$, consider a possibly different detector $\tau=\tau^{(T)}\in\mathbb N\cup\{\infty\}$. It is a stopping time based on the observations available so far. Under $P_{F_0,T,F_1}$, the observations are independent, with $X_1,\ldots,X_{T-1}\sim F_0$ and $X_T,X_{T+1},\ldots\sim F_1$; under $P_{F_0,\infty}$ they are independent with law $F_0$. The score values are almost surely distinct under these laws, and for independent $Y\sim F_0$ and $Z\sim F_1$,
\[
\left|P\{S(Z)>S(Y)\}-\tfrac12\right|=\delta.
\]
Write $r_t=P_{F_0,\infty}(\tau\ge t)$, with the detector for the current $T$ understood. Require, for each detector in the sequence, every time $t$ and every change location $u$, that
\[
P_{F_0,u,F_1}(\tau\ge t)\le P_{F_0,\infty}(\tau\ge t).
\]

Let all the variables $U_{t,j},V_{t,j}$ be mutually independent $\mathrm{Unif}(0,1)$ variables, independent of the observations. For $2\le t\le j$ and $1\le j\le t$, respectively, define
\[
p_t^j=\frac{\sum_{i=t}^{j-1}{\bf1}\{S(X_i)<S(X_j)\}+U_{t,j}}{j-t+1},\qquad
q_t^j=\frac{\sum_{i=j+1}^{t}{\bf1}\{S(X_i)<S(X_j)\}+V_{t,j}}{t-j+1}.
\]
For each $T,t,j$, use the deterministic oracle coefficients
\[
\lambda^*_{t,j}\in\underset{\lambda\in[-1,1]}{\arg\max}\ E_{F_0,T,F_1}\!\left[\log\{1+\lambda(p_t^j-\tfrac12)\}\right],\quad j\ge t,
\]
\[
\mu^*_{t,j}\in\underset{\mu\in[-1,1]}{\arg\max}\ E_{F_0,T,F_1}\!\left[\log\{1+\mu(q_t^j-\tfrac12)\}\right],\quad j\le t,
\]
where expectations include the independent uniforms. Set $f_{t,j}(p)=1+\lambda^*_{t,j}(p-\tfrac12)$ and $g_{t,j}(p)=1+\mu^*_{t,j}(p-\tfrac12)$. These fixed oracle choices are predictable.

On $\{\tau<\infty\}$ define
\[
C_{\rm low}^{\alpha}=\left\{2\le t\le\tau:\max_{t\le i\le\tau}\prod_{j=t}^{i}f_{t,j}(p_t^j)\le\frac1{\alpha r_t}\right\},
\]
\[
C_{\rm up}^{\alpha}=\left\{2\le t\le\tau:\max_{1\le i\le t-1}\prod_{j=i}^{t-1}g_{t-1,j}(q_{t-1}^j)\le\frac1{\alpha r_t}\right\},\qquad C=C_{\rm low}^{\alpha}\cap C_{\rm up}^{\alpha}.
\]
Use the convention $1/(\alpha r_t)=+\infty$ if $r_t=0$, and set $C=\varnothing$ when $\tau=\infty$. The latter convention does not affect the finite-stopping event below.

## Task

Let $C_0=160+128(1+\log 2)^2$. Prove that for any $s>0$ and any $s'>\max\{8/\delta^2,C_0/\delta^4\}$, if
\[
\liminf_{T\to\infty}P_{F_0,T,F_1}\!\left(T+s\log T\le\tau\le T+\exp(T/s')\right)>0,
\]
then, with $E_T=\{T+s\log T\le\tau\le T+\exp(T/s')\}$,
\[
E_{F_0,T,F_1}[|C|\mid E_T]=
\begin{cases}
O(1),&s\delta^4>C_0,\\
O(\log T),&s\delta^4=C_0,\\
O\!\left(T^{1-s\delta^4/C_0}\right),&s\delta^4<C_0,
\end{cases}
\]
and $E_{F_0,T,F_1}[|C|/T\mid E_T]=o(1)$. Integer rounding of the time boundaries is allowed.
