# Problem

## Setup

Let \(\Gamma\) be a compact metric graph: a finite connected graph whose edges are closed intervals of positive lengths, glued at their endpoints, equipped with its shortest-path metric. Let \(P_\Gamma,Q_\Gamma\) be Borel probability measures on \(\Gamma\).

Let \(\Psi:\Gamma\to M_\Psi\) be an injective embedding into either Euclidean space or a flat torus, and write
\[
P_\Psi=\Psi_\#P_\Gamma,\qquad Q_\Psi=\Psi_\#Q_\Gamma,
\]
with \(S=\Psi(\Gamma)\). Let \(\rho=\Psi^{-1}\circ\operatorname{proj}_S\), where \(\operatorname{proj}_S\) is a fixed measurable nearest-point projection (with measurable tie-breaking).

Fix \(\epsilon>0\). On \(M_\Psi\), use the quadratic cost \(c(x,y)=d(x,y)^2/2\). Let \(\pi^\star_{\epsilon,\Psi}\) be an optimizer of entropic optimal transport between \(P_\Psi\) and \(Q_\Psi\), minimizing
\[
\int c\,d\pi+\epsilon\,\mathrm{KL}(\pi\,\|\,P_\Psi\otimes Q_\Psi)
\]
over all couplings. Let \(K=\operatorname{spt}(Q_\Psi)\). For a continuous target potential \(g:K\to\mathbb R\), define its soft transform and Gibbs conditional by
\[
f_g^\epsilon(x)=-\epsilon\log\int_K \exp\!\left(\frac{g(y)-c(x,y)}{\epsilon}\right)dQ_\Psi(y),
\]
\[
\pi^\epsilon_{g,x}(dy)=\exp\!\left(\frac{f_g^\epsilon(x)+g(y)-c(x,y)}{\epsilon}\right)dQ_\Psi(y),\qquad y\in K.
\]
Assume there is a continuous injective feature map \(\phi:K\to\mathbb R^n\) and a function class \(\mathcal F\subset C(\mathbb R^n,\mathbb R)\) dense in the topology of uniform convergence on compact sets. The centered pullback potential class is
\[
\mathcal C_Q(\phi^*\mathcal F)=\left\{a\circ\phi-\int_K a(\phi(y))\,dQ_\Psi(y):a\in\mathcal F\right\}.
\]
For \(g\in\mathcal C_Q(\phi^*\mathcal F)\), let \(\pi^\epsilon_{g,\Psi}\) denote the corresponding embedded Gibbs joint law with first marginal \(P_\Psi\) and conditionals \(\pi^\epsilon_{g,x}\). Let \(H_t\) be the ambient heat Markov kernel. For \(t>0\), define
\[
\eta_{g,t}=(\operatorname{id}\times H_t)_\#\pi^\epsilon_{g,\Psi},\qquad
\widehat\pi_{g,t}=(\rho\times\rho)_\#\eta_{g,t},
\]
where \(\operatorname{id}\times H_t\) leaves the first coordinate unchanged and applies the heat kernel to the second coordinate.

## Task

Prove that there exists a sequence \(g_m\in\mathcal C_Q(\phi^*\mathcal F)\) such that
\[
\|\pi^\epsilon_{g_m,\Psi}-\pi^\star_{\epsilon,\Psi}\|_{\mathrm{TV}}\to0,
\]
and that there are indices \(m_k\to\infty\) and heat times \(t_k\downarrow0\) such that
\[
\widehat\pi_{g_{m_k},t_k}\Rightarrow
\pi^\star_{\epsilon,\Gamma}:=(\Psi^{-1},\Psi^{-1})_\#\pi^\star_{\epsilon,\Psi}
\]
weakly on \(\Gamma\times\Gamma\). Show also that \(\pi^\star_{\epsilon,\Gamma}\in\Pi(P_\Gamma,Q_\Gamma)\), where \(\Pi(P_\Gamma,Q_\Gamma)\) is the set of Borel probability measures on \(\Gamma\times\Gamma\) with these two marginals.
