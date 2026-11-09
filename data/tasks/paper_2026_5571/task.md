# Problem

## Setup

Let \(G\) be a compact group with normalized Haar measure \(dg\). It acts on finite-dimensional real Euclidean spaces \(X\) and \(Y\) through continuous orthogonal representations \(\rho_X\) and \(\rho_Y\).

Let \(\mathsf H,V,W,\Xi\) be finite-dimensional real Euclidean spaces. Equip spaces of linear maps with their induced Hilbert–Schmidt inner products and equip
\[
\Theta=\operatorname{Hom}(W,V)\times\Xi
\]
with the product Euclidean inner product. Write \(\theta=(P,\xi)\). The symbol \(^*\) denotes the Euclidean adjoint.

A tensorizable network has the form
\[
f_{P,\xi}(x)=M(P,\xi)T(x),
\]
where \(T:X\to\mathsf H\) is Borel measurable and parameter-independent, and
\[
M:\Theta\longrightarrow\operatorname{Hom}(\mathsf H,Y)
\]
is smooth. Assume that an orthogonal continuous representation \(\rho_{\mathsf H}\) of \(G\) satisfies
\[
T(\rho_X(g)x)=\rho_{\mathsf H}(g)T(x)
\qquad(g\in G,\ x\in X).
\]

An admissible data law is a compactly supported Borel probability measure \(\mu\) on \(X\times Y\) satisfying
\[
\mathbb E_{(x,y)\sim\mu}\bigl[\|T(x)\|_{\mathsf H}^{2}+\|y\|_Y^{2}\bigr]<\infty.
\]
For any such law, define the group-augmented mean-squared risk
\[
R_\mu(P,\xi)=\mathbb E_{(x,y)\sim\mu}\int_G
\big\|M(P,\xi)\rho_{\mathsf H}(g)T(x)-\rho_Y(g)y\big\|_Y^2\,dg.
\]
Its Euclidean gradient flow is
\[
\dot P=-\nabla_P R_\mu(P,\xi),\qquad
\dot\xi=-\nabla_\xi R_\mu(P,\xi).
\]

Define
\[
\operatorname{Sym}^2_G(\mathsf H)
=\{S\in\operatorname{Hom}(\mathsf H,\mathsf H):S^*=S,\ S\rho_{\mathsf H}(g)=\rho_{\mathsf H}(g)S\ \forall g\in G\}
\]
and
\[
\operatorname{Hom}_G(\mathsf H,Y)
=\{L\in\operatorname{Hom}(\mathsf H,Y):L\rho_{\mathsf H}(g)=\rho_Y(g)L\ \forall g\in G\}.
\]
Set
\[
\mathcal H=\{B\in GL(\mathsf H):BSB^*=S\ \forall S\in\operatorname{Sym}^2_G(\mathsf H),\ LB^*=L\ \forall L\in\operatorname{Hom}_G(\mathsf H,Y)\}.
\]
Suppose that for every \(a\in O(V)\) there exists \(B_a\in\mathcal H\) such that
\[
M(aP,\xi)=M(P,\xi)B_a
\qquad\text{for every }(P,\xi)\in\Theta.
\]

## Task

Prove that, for every admissible data law \(\mu\) and every classical solution \((P(t),\xi(t))\) of the augmented gradient flow on an interval \(J\) containing \(0\),
\[
\operatorname{Ran}P(t)=\operatorname{Ran}P(0)
\qquad\text{for every }t\in J.
\]

Consequently, prove that every smooth real-valued function of this subspace is an integral of motion in the following precise sense. If \(\Omega\subseteq\Theta\) is open and \(I:\Omega\to\mathbb R\) is smooth and depends only on \(\operatorname{Ran}P\)—meaning that \(I(P,\xi)=I(Q,\eta)\) whenever both parameter points belong to \(\Omega\) and \(\operatorname{Ran}P=\operatorname{Ran}Q\)—then \(I\) is constant on every augmented gradient-flow segment contained in \(\Omega\), for every admissible data law.
