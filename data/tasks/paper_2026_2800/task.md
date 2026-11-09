# Problem

## Setup

Fix a finite nonempty node set \(N\), a destination \(d\in N\), a source set \(N_{\mathrm{src}}\subseteq N\setminus\{d\}\), and a positive integer \(C\) of item classes. Write \(J=\{1,\ldots,C\}\), \(\mathbb N_0=\{0,1,\ldots\}\), and \(\mathbb N_+=\{1,2,\ldots\}\). Let \(\mathrm{Lists}(E)\) denote the set of all finite lists with entries in \(E\), including the empty list. Define
\[
Q=(\mathbb N_0^{N\times J})^2
\times\bigl(\{\emptyset\}\cup(\mathbb N_+\times\mathbb N_+)\bigr)^{N\times J}
\times\mathrm{Lists}(\mathbb N_+\times J\times\mathbb N_+),
\qquad
X=Q\times\mathbb R_{>0}^{C}.
\]
At time \(t\), the simulator state is
\[
x_t=(H_t,B_t,O_t,I_t,s_t)\in X.
\]
Here \(H_t\) and \(B_t\) are the per-node, per-item inventory and backlog arrays; each entry of \(O_t\) is either empty or an outstanding replenishment order's due-time/quantity pair; \(I_t\) is a finite list of due-time/item/quantity triples for shipments scheduled to arrive at the destination; and \(s_t\) is a positive real \(C\)-vector of smoothed demand estimates. Equip \(Q\) with its discrete sigma-algebra and \(X\) with the product Borel sigma-algebra.

The input spaces are the countable discrete measurable spaces
\[
\mathcal Y=\mathbb N_0^{J},
\qquad
\mathcal L=\mathbb N_+^{N_{\mathrm{src}}\times J}.
\]
Fix deterministic finite rates \(\lambda_{i,t}>0\) for every \(i\in J\) and \(t\in\mathbb N_0\), and fixed parameters \(a^{n,i}>0\) for every \((n,i)\in N_{\mathrm{src}}\times J\). Let \(\Phi\) be the standard normal distribution function and define
\[
p_{n,i}(k)=
\begin{cases}
\displaystyle\Phi\!\left(\frac{1-a^{n,i}}{0.2a^{n,i}}\right),&k=1,\\[6pt]
\displaystyle\Phi\!\left(\frac{k-a^{n,i}}{0.2a^{n,i}}\right)
-\Phi\!\left(\frac{k-1-a^{n,i}}{0.2a^{n,i}}\right),&k\geq2.
\end{cases}
\]
Thus \(p_{n,i}\) is the mass function of \(\max(1,\lceil G\rceil)\) for \(G\sim\mathcal N(a^{n,i},(0.2a^{n,i})^2)\). Define product probability laws by
\[
\mu_t(y)=\prod_{i\in J}\frac{e^{-\lambda_{i,t}}\lambda_{i,t}^{y_i}}{y_i!},
\qquad
\nu_t(\ell)=\prod_{(n,i)\in N_{\mathrm{src}}\times J}p_{n,i}(\ell^{n,i}).
\]
The law \(\nu_t\) is the same for every \(t\). Empty products equal one; if \(N_{\mathrm{src}}\) is empty, \(\mathcal L\) is a singleton.

On a common probability space, let \(y_t\in\mathcal Y\) and \(L_t\in\mathcal L\) have laws \(\mu_t\) and \(\nu_t\). The pairs \((y_t,L_t)\) are jointly independent across times, and \(y_t\) and \(L_t\) are independent within each time. The initial state \(x_0\in X\) is fixed in advance.

With its configuration fixed, the simulator has a deterministic measurable update rule
\[
\Psi:\mathbb N_0\times X\times\mathcal Y\times\mathcal L\longrightarrow X,
\qquad
x_{t+1}=\Psi(t,x_t,y_t,L_t),
\]
where the time coordinate has the discrete sigma-algebra. For every \(t\in\mathbb N_0\), \(x\in X\), and Borel set \(A\subseteq X\), define
\[
P_t(x,A)=\sum_{y\in\mathcal Y}\sum_{\ell\in\mathcal L}
\mathbf 1_A(\Psi(t,x,y,\ell))\,\mu_t(y)\nu_t(\ell).
\]
Equivalently, these sums can be written as integrals against the same probability laws.

## Task

Prove that \((x_t)_{t\geq0}\) is a time-inhomogeneous Markov chain on \(X\) with transition kernels \(P_t\), i.e. for every \(t\in\mathbb N_0\) and Borel set \(A\subseteq X\),
\[
\mathbb P(x_{t+1}\in A\mid x_0,\ldots,x_t)=P_t(x_t,A)\quad\text{a.s.}
\]
Moreover, prove that the augmented process \(Z_t=(t,x_t)\) on \(\mathbb N_0\times X\), equipped with the product sigma-algebra, is time-homogeneous Markov.
