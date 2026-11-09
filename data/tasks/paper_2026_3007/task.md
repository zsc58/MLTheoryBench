# Problem

## Setup

Let $d\ge 1$. Let $D\subset\mathbb R^d$ be bounded and Borel, with Lebesgue measure, and let $\Omega\subset\mathbb R^{d+1}$ be open. Write $\theta=(\theta_0,\theta')$ and, for a continuous activation $\sigma:\mathbb R\to\mathbb R$, define
\[
h(\theta,x)=\sigma(\theta_0+\theta'\!\cdot x).
\]
Assume there is $C_h$ such that
\[
|h(\theta,x)|\le C_h(1+|x|)(1+|\theta|),
\]
and, for every $R>0$, a constant $c_{h,R}$ such that whenever $|\theta|,|\vartheta|\le R$,
\[
|h(\theta,x)-h(\vartheta,x)|\le c_{h,R}|\theta-\vartheta|(1+|x|).
\]
These feature inequalities are required for $\theta,\vartheta\in\Omega$ and $x\in D$. Let $f\in L^2(D)$. Let $\omega:\Omega\to[1,\infty)$ be smooth and satisfy
\[
c_\omega:=\int_\Omega\frac{(1+|\theta|)^4}{\omega(\theta)}\,d\theta<\infty.
\]
Set
\[
L^2_\omega(\Omega)=\{u:\int_\Omega u^2\omega<\infty\},\qquad
W=W^{1,2}(\Omega)\cap L^2_\omega(\Omega),
\]
with $\|u\|_W^2=\|u\|_{L^2_\omega}^2+\|\nabla u\|_2^2$. For $u\in W$, define
\[
f_u(x)=\int_\Omega h(\theta,x)u(\theta)\,d\theta,
\quad Q(\theta)=\int_D f(x)h(\theta,x)\,dx,
\quad K(\theta,\vartheta)=\int_D h(\theta,x)h(\vartheta,x)\,dx,
\]
\[
R(f,u)=\int_D(f-f_u)^2dx,
\quad F_{\alpha,\beta}^{(f)}(u)=R(f,u)+\alpha\|u\|_{L^2_\omega}^2+\beta\|\nabla u\|_2^2,
\]
where $\alpha,\beta>0$.

## Task

Prove that for every $f\in L^2(D)$ and $\alpha,\beta>0$, the functional $F_{\alpha,\beta}^{(f)}$ has a unique minimizer $u_f^*\in W$. Show that it satisfies, in distributions on $\Omega$,
\[
-\beta\Delta u_f^*+\alpha\omega u_f^*-Q+\int_\Omega K(\cdot,\vartheta)u_f^*(\vartheta)\,d\vartheta=0,
\]
that $u_f^*\in W^{3,p}_{\mathrm{loc}}(\Omega)$ for every $p>1$ (hence $u_f^*\in C^{2,s}_{\mathrm{loc}}(\Omega)$ for every $0<s<1$), and that the map $f\mapsto u_f^*$ is linear. Moreover, there is a constant $C=C(D,\Omega,\omega,h)$ such that for all $f,f_1,f_2\in L^2(D)$,
\[
\|u_f^*\|_{L^2_\omega}\le \frac{C}{\alpha}\|f\|_2,\qquad
\|\nabla u_f^*\|_2\le \frac{C}{\sqrt{\alpha\beta}}\|f\|_2,
\]
and the same two inequalities hold with $u_f^*$ replaced by $u_{f_1}^*-u_{f_2}^*$ and $f$ replaced by $f_1-f_2$.
