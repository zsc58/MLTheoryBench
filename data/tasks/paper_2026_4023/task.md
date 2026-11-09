# Problem

## Setup

Fix integers \(L\ge2\) and \(l_0\ge0\), and a memory capacity \(M>l_0+L\). A request has stages \(j=0,1,\ldots,L-1\). While at stage \(j\), it occupies weight
\[
w_j=l_0+1+j.
\]
The state space is the memory boundary
\[
B=\left\{x\in\mathbb R_+^L:\sum_{j=0}^{L-1}w_jx_j=M\right\},
\]
where coordinates are nonnegative continuous request masses.

There is always enough waiting work to fill any available memory. One update first advances every active request by one stage; requests at stage \(L-1\) complete and leave. If the post-execution active memory exceeds \(M\), remove mass from the smallest occupied stage first, proceeding to larger stages as necessary and allowing fractional removal at the cutoff, until active memory is exactly \(M\). Finally, admit stage-0 mass to fill any remaining memory. Waiting work does not occupy active memory before admission. This defines a deterministic map \(F:B\to B\).

A fixed point satisfies \(F(x)=x\). A limit cycle is a finite orbit \(C=\{x,Fx,\ldots,F^{p-1}x\}\), where \(p\ge2\) is the least positive integer satisfying \(F^px=x\). Call a limit cycle an \(r\)-level cycle if every state on it has exactly \(L-r\) positive coordinates. The maximal level is \(r=L-1\). A fixed point is eviction-free if its update removes no mass.

Use the Euclidean norm and write \(\operatorname{dist}(x,C)=\min_{y\in C}\|x-y\|\). A fixed point or cycle \(C\), regarded as a finite set, is Lyapunov stable relative to \(B\) if for every \(\epsilon>0\) there exists \(\delta>0\) such that
\[
x\in B,\quad \operatorname{dist}(x,C)<\delta
\quad\Longrightarrow\quad
\operatorname{dist}(F^nx,C)<\epsilon\quad\text{for all }n\ge0.
\]
It is unstable if this property fails. It is asymptotically stable if it is Lyapunov stable and there exists \(\delta_0>0\) such that every \(x\in B\) with \(\operatorname{dist}(x,C)<\delta_0\) satisfies \(\operatorname{dist}(F^nx,C)\to0\). For a set \(E\subseteq B\), asymptotic stability outside \(E\) means these stability and attraction conditions with the initial states restricted to \(B\setminus E\).

For each nonempty \(I\subseteq\{0,\ldots,L-1\}\), let
\[
B_I=\{x\in B:x_j>0\text{ for }j\in I,\ x_j=0\text{ for }j\notin I\}.
\]
Equip \(B_I\) with the \((|I|-1)\)-dimensional Lebesgue measure induced on its affine hull.

## Task

Prove that \(F\) has a unique eviction-free fixed point \(x^*\) and a unique maximal-level cycle \(C_{\max}\). Define the exact-capture set
\[
E=\left\{x\in B:\text{for some integer }N\ge0,\ F^Nx=x^*\text{ or }F^Nx\text{ belongs to an }r\text{-level cycle with }1\le r\le L-2\right\}.
\]
When \(L=2\), the range of intermediate levels is empty.

Prove all of the following:

1. The eviction-free fixed point \(x^*\) is unstable.
2. Every intermediate \(r\)-level cycle, \(1\le r\le L-2\), is unstable.
3. For every nonempty \(I\), the set \(E\cap B_I\) has relative Lebesgue measure zero in \(B_I\).
4. The maximal-level cycle \(C_{\max}\) is asymptotically stable outside \(E\). Every \(x\in B\setminus E\) reaches \(C_{\max}\) after finitely many updates and thereafter remains on that cycle; in particular, \(\operatorname{dist}(F^nx,C_{\max})\to0\).
