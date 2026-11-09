# Problem

## Setup

Let \((\Omega,\mathcal A,\mathbb P)\) be a probability space and let \(Y\) be a real-valued random variable. Let \(\mathcal P\) be a convex class of Borel probability measures on \(\mathbb R\), equipped with the Borel structure inherited from the topology of weak convergence, and assume that this measurable space is standard Borel. Let \(Q\) be a measurable random forecast taking values in \(\mathcal P\).

Let
\[
T(R)=[T^-(R),T^+(R)],\qquad R\in\mathcal P,
\]
where \(T^-\) and \(T^+\) are measurable, finite real-valued maps satisfying \(T^-(R)\le T^+(R)\). Thus the intervals are nonempty and may be singletons. Equip the space \(\mathscr I\) of these intervals with the Borel structure obtained by identifying \([a,b]\) with \((a,b)\in\{(a,b)\in\mathbb R^2:a\le b\}\). Set \(X:=T(Q)\). Assume that a regular conditional law \(G_X\) of \(Y\) given \(X\) belongs to \(\mathcal P\) almost surely.

Let \(V:\mathbb R\times\mathbb R\to\mathbb R\) be jointly Borel measurable, with \(x\mapsto V(x,y)\) nondecreasing and left-continuous for every \(y\).

The following conventions specify existence of the signed integrals used here. For a real number \(u\), write \(u_+=\max(u,0)\) and \(u_-=\max(-u,0)\). Signed expectations are allowed to take values in \([-\infty,\infty]\), but not to involve an undefined difference \(\infty-\infty\). Specifically, assume:

- For every \(R\in\mathcal P\), every \(\varepsilon>0\), and each \(a\in\{T^-(R)+\varepsilon,T^+(R)-\varepsilon\}\),
  \[
  \min\left\{\int V(a,y)_+\,R(dy),\int V(a,y)_-\,R(dy)\right\}<\infty.
  \]
- For every \(\varepsilon>0\) and each random variable \(A\in\{T^-(Q)+\varepsilon,T^+(Q)-\varepsilon\}\),
  \[
  \min\left\{\mathbb E[V(A,Y)_+],\mathbb E[V(A,Y)_-]\right\}<\infty.
  \]

Assume that \(V\) identifies \(T\) in the following sense: for every fixed \(R\in\mathcal P\) and every \(\varepsilon>0\),
\[
\int V(T^-(R)+\varepsilon,y)\,R(dy)\ge0,
\qquad
\int V(T^+(R)-\varepsilon,y)\,R(dy)\le0.
\]

Assume also that \(V\) has at least one of the following forms:

- **Prediction-error form:** \(V(x,y)=v(x-y)\), where \(v:\mathbb R\to\mathbb R\) is nondecreasing and left-continuous, and there exists \(r>0\) such that \(v(-r)<0<v(r)\).
- **Expectation form:** \(T\) is singleton-valued on \(\mathcal P\), with scalar value \(\tau(R)\), and \(V(x,y)=x-\tau(\delta_y)\). Here \(\delta_y\) is the Dirac probability measure at \(y\); the same scalar functional \(\tau\) is also specified at every \(\delta_y\), with finite values and with \(y\mapsto\tau(\delta_y)\) Borel measurable. This does not require \(\delta_y\in\mathcal P\).

Assume the following mixture-level-set closure: for every Borel probability law \(\Lambda\) on \(\mathcal P\) and every \(t\in\mathscr I\) such that
\[
\Lambda(\{R\in\mathcal P:T(R)=t\})=1,
\]
the barycenter defined by
\[
M(B):=\int_{\mathcal P}R(B)\,\Lambda(dR),\qquad B\in\mathcal B(\mathbb R),
\]
belongs to \(\mathcal P\) and satisfies \(T(M)=t\).

Distribution calibration means that, for every \(B\in\mathcal B(\mathbb R)\),
\[
G_X(B)=\mathbb E[Q(B)\mid X]\quad\text{almost surely}.
\]
Conditional \(T\)-calibration means
\[
T(G_X)=T(Q)\quad\text{almost surely}.
\]
Unconditional \(T\)-calibration means that, for every \(\varepsilon>0\),
\[
\mathbb E[V(T^-(Q)+\varepsilon,Y)]\ge0,
\qquad
\mathbb E[V(T^+(Q)-\varepsilon,Y)]\le0.
\]

## Task

Prove the integrated theorem: distribution calibration implies conditional \(T\)-calibration, and conditional \(T\)-calibration implies unconditional \(T\)-calibration. Therefore distribution calibration implies unconditional \(T\)-calibration as well.
