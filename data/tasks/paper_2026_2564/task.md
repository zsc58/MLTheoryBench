# Problem

## Setup

Let $(M,g)$ be a complete $p$-dimensional Riemannian manifold with geodesic distance $d$. Let $\mu,\nu$ be Borel probability measures with compact supports $K_\mu,K_\nu$, and let $\Pi(\mu,\nu)$ denote their couplings. Fix $\epsilon>0$ and set $c(x,y)=\tfrac12 d(x,y)^2$. For a coupling $\pi$ of $(\mu,\nu)$ define
\[
\mathcal E_\epsilon(\pi)=\int c\,d\pi+\epsilon\,\mathrm{KL}(\pi\,\|\,\mu\otimes\nu),
\qquad
\mathrm{OT}_\epsilon(\mu,\nu)=\inf_{\pi\in\Pi(\mu,\nu)}\mathcal E_\epsilon(\pi).
\]
For bounded measurable $h:K_\nu\to\mathbb R$ define the soft transform
\[
(Th)(x)=-\epsilon\log\!\int_{K_\nu}\exp\!\left(\frac{h(y)-c(x,y)}{\epsilon}\right)d\nu(y),\quad x\in K_\mu,
\]
and the semidual functional $J(h)=\int h\,d\nu+\int Th\,d\mu$. Let $\mathcal F$ be a class of continuous functions on $\mathbb R^n$ dense for uniform convergence on every compact subset, and let $\phi:K_\nu\to\mathbb R^n$ be continuous and injective. Write
\[
\phi^*\mathcal F=\{a\circ\phi:a\in\mathcal F\},\qquad
\mathcal C_\nu(\phi^*\mathcal F)=\left\{h-\int h\,d\nu:h\in\phi^*\mathcal F\right\}.
\]

## Task

Prove that the entropic problem has a unique optimizer $\pi_\epsilon^\star$ and that there exists a sequence $g_m\in\mathcal C_\nu(\phi^*\mathcal F)$ such that, with
\[
\frac{d\pi_m^\epsilon}{d(\mu\otimes\nu)}(x,y)=
\exp\!\left(\frac{Tg_m(x)+g_m(y)-c(x,y)}{\epsilon}\right),
\]
we have
\[
\epsilon\,\mathrm{KL}(\pi_\epsilon^\star\Vert\pi_m^\epsilon)\to0,\qquad
\|\pi_m^\epsilon-\pi_\epsilon^\star\|_{\mathrm{TV}}\to0,
\qquad
\pi_m^\epsilon\Rightarrow\pi_\epsilon^\star
\]
where weak convergence is on probability measures over $K_\mu\times K_\nu$.
