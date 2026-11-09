# Reference Proof

## Contract and proof obligations

All trajectories below are population trajectories. Observation noise contributes only the additive constant \(\sigma^2\). The main-text initialization is \(\mu=1/(d\log d)\); it is not replaced by \(\rho_0/(d+\lambda)\). Fix the numerical constants in \(c_-\log d\le\lambda\le c_+d\). Constants in estimates may depend on these fixed bounds. The polar parameter \(\kappa\) is fixed independently of dimension; its first-stage bound is \(O(1+\kappa^{-1})\), hence \(O_\kappa(1)\).

We close the following obligations: the Gaussian loss and correctly normalized gradients; invariance for both algorithms, including singular polar factors; polar synchronization and turning, nuisance bounds, signal hitting and persistence; and GD barriers, escape and turning, early misalignment, bulk inflation, signal hitting, and uniform later alignment. No continuous-flow existence or specialized external theorem is used.

## 1. Loss, gradient, and invariant reduction

Let \(D=M-P_u\). If \(g\sim N(0,I_d)\), then \(x=Q^{1/2}g\). The standard Gaussian fourth-moment identity is
\[
\mathbb E[g_i g_j g_l g_m]
=\delta_{ij}\delta_{lm}+\delta_{il}\delta_{jm}+\delta_{im}\delta_{jl}.
\]
Expanding a quadratic form and summing these three pairings gives, for a deterministic symmetric matrix \(H\),
\[
\mathbb E[(g^\top Hg)^2]=(\operatorname{Tr}H)^2+2\operatorname{Tr}(H^2).
\]
Here \(H=Q^{1/2}DQ^{1/2}\) is symmetric, and all sums and Gaussian fourth moments are finite. Therefore
\[
\mathcal L=2\operatorname{Tr}(DQDQ)+(\operatorname{Tr}(DQ))^2+\sigma^2.
\]
Differentiating with respect to \(M\) gives
\[
\nabla_M\mathcal L=4QDQ+2\operatorname{Tr}(DQ)Q.
\]
Define
\[
G(M)=2\nabla_M\mathcal L=8QDQ+4\operatorname{Tr}(DQ)Q.
\]
Since \(dM=dW\,W^\top+W\,dW^\top\), the chain rule gives \(\nabla_W\mathcal L=G(M)W\).

The three mutually orthogonal projectors form a commutative algebra. For
\(M=sP_u+hP_q+zP_\perp\), set
\[
r=s+(1+\lambda)h+(d-2)z.
\]
Then \(G\) belongs to the same algebra, with eigenvalues
\[
g_u=4(r+2s-3),\qquad
g_q=4(1+\lambda)(r+2(1+\lambda)h-1),\qquad
g_\perp=4(r+2z-1).
\]
For GD,
\[
M^+=(I-tG)M(I-tG),\qquad t=\widetilde\eta,
\]
which preserves the algebra.

For the polar method choose an orthogonal left basis adapted to the projectors and write
\[
W=U\operatorname{diag}(\alpha,\beta,\gamma I_{d-2})V^\top,
\qquad (\alpha,\beta,\gamma)=(\sqrt s,\sqrt h,\sqrt z).
\]
The Moore-Penrose polar factor of \(GW\) has diagonal entries
\(\operatorname{Sign}(g_u\alpha),\operatorname{Sign}(g_q\beta),\operatorname{Sign}(g_\perp\gamma)\), with \(\operatorname{Sign}(0)=0\). Consequently the exact recursion is
\[
\alpha^+=|\alpha-\eta\operatorname{Sign}(g_u\alpha)|,
\quad \beta^+=|\beta-\eta\operatorname{Sign}(g_q\beta)|,
\quad \gamma^+=|\gamma-\eta\operatorname{Sign}(g_\perp\gamma)|.
\tag{1}
\]
In particular, a zero coordinate remains zero. The sign-only formula is valid at positive coordinates, not unconditionally. Squaring proves invariance. This calculation also shows that the matrix trajectory depends only on \(M_0\), not on the orthogonal factor of \(W_0\). Induction proves the asserted decomposition for both algorithms.

## 2. Polar synchronization and first turning

Write \(L=1+\lambda\), and define privately
\[
N_1=\inf\{k:r_k+2Lh_k\ge1\}.
\]
Initially all square roots equal \(\sqrt\mu>0\), and all three gradient eigenvalues are negative for sufficiently large \(d\). Suppose isotropy holds at an index before \(N_1\). Then
\[
r+2Lh=(d+3\lambda+2)\alpha^2<1,
\]
whereas \(r+2z=r+2s=(d+\lambda+2)\alpha^2\). Hence all three signs are negative, and (1) increases every square root by \(\eta\). Induction gives
\[
\alpha_k=\beta_k=\gamma_k=\sqrt\mu+k\eta,
\qquad 0\le k\le N_1.
\]
For large \(d\),
\[
N_1=\left\lceil\frac{(d+3\lambda+2)^{-1/2}-\sqrt\mu}{\eta}\right\rceil
\le 1+\kappa^{-1}.
\]
At \(N_1\), \(g_q\ge0\) and \(\beta_{N_1}\ge(d+3\lambda+2)^{-1/2}\). Choose a universal \(\kappa_0\) small enough that
\(\eta\sqrt{d+3\lambda+2}<1\). Thus \(\beta_{N_1}>\eta\). If \(g_q>0\), its next square root decreases by \(\eta\); if \(g_q=0\), it is unchanged. Before this index it strictly increases. Therefore \(T_1=N_1\), proving synchronization through \(T_1\) and \(T_1=O_\kappa(1)\).

## 3. Polar nuisance trapping

Set
\[
\bar\beta=\frac1{\sqrt{3L}}+\eta,
\qquad \bar\gamma=\frac1{\sqrt d}+\eta.
\]
The initial coordinates are below these bounds for large \(d\). If \(\beta=0\), it remains zero. If \(\beta>0\) and \(g_q\ge0\), then \(\beta^+\le\max\{\beta,\eta\}\). If \(g_q<0\), then
\(s+3Lh+(d-2)z<1\), so \(\beta<1/\sqrt{3L}\) and \(\beta^+\le\bar\beta\). Induction proves \(\beta_k\le\bar\beta\).

Likewise a zero bulk coordinate remains zero. At a positive bulk coordinate, a nonnegative gradient gives \(\gamma^+\le\max\{\gamma,\eta\}\); a negative gradient implies \(s+Lh+dz<1\), hence \(\gamma<1/\sqrt d\) and \(\gamma^+\le\bar\gamma\). Thus
\[
Lh_k\le\left(\frac1{\sqrt3}+\eta\sqrt L\right)^2\le C_b,
\qquad
(d-2)z_k\le\left(\sqrt{\frac{d-2}{d}}+\eta\sqrt{d-2}\right)^2\le C_c.
\tag{2}
\]
These bounds hold for every index, including any singular iterates.

## 4. Polar signal hitting, persistence, and alignment

Let
\[
A_0=1-\frac{C_b+C_c}{3},\qquad
N_2=\inf\{k:s_k\ge A_0\},\qquad
A=(\sqrt{A_0}-\eta)^2.
\]
Choose \(\kappa_0\) sufficiently small that \(A_0\) is uniformly bounded away from zero. For sufficiently large \(d\), \(\sqrt{A_0}>\eta\). By (2),
\[
r_k+2s_k\le3s_k+C_b+C_c<3\quad\text{if }s_k<A_0.
\]
Starting at \(\alpha_0>0\), (1) therefore gives \(\alpha_{k+1}=\alpha_k+\eta\) until \(N_2\). In particular positivity is proved along this segment, and
\[
N_2=\left\lceil\frac{\sqrt{A_0}-\sqrt\mu}{\eta}\right\rceil=O(\eta^{-1}).
\]
After \(N_2\), prove \(\alpha_k\ge\sqrt{A_0}-\eta>0\) inductively. If \(\alpha_k\ge\sqrt{A_0}\), (1) gives \(\alpha_{k+1}\ge\alpha_k-\eta\). If \(\sqrt{A_0}-\eta\le\alpha_k<\sqrt{A_0}\), its gradient is negative and it increases by \(\eta\). Hence \(s_k\ge A\) thereafter.

There is also a uniform upper signal bound: if its gradient is negative then \(3s<3\), so a positive signal square root can increase only from below one to at most \(1+\eta\); otherwise its next value is at most its current value or \(\eta\). Thus \(s_k\le(1+\eta)^2\).

Fix a universal sufficiently small \(\delta>0\), for example \(\delta=1/100\), and further decrease \(\kappa_0\) if necessary. For large \(d\), \(s_{T_1}=O(d^{-1})<\delta<A\). Exact signal growth gives \(T_2=O(\eta^{-1})\), with \(T_2\le N_2\). Once the signal reaches \(\delta\), it stays above \(\delta\): below \(A_0\) it increases, and a step starting at or above \(A_0\) ends at or above \(A>\delta\).

By the orthogonal decomposition,
\[
\operatorname{Align}(M_k)=\left(1+\frac{h_k^2+(d-2)z_k^2}{s_k^2}\right)^{-1/2}.
\]
For \(x\ge0\), integrating the derivative \(\tfrac12(1+x)^{-3/2}\le\tfrac12\) gives \(1-(1+x)^{-1/2}\le x/2\). Hence for all \(k\ge N_2\),
\[
1-\operatorname{Align}(M_k)
\le\frac1{2A^2}\left(\frac{C_b^2}{(1+\lambda)^2}+\frac{C_c^2}{d-2}\right).
\]
Take \(K_*=N_2\). For all \(k\ge T_2\), the same argument with \(\delta\) in place of \(A\) proves uniform \(1-o(1)\) alignment. The limits follow from \(\lambda\ge c_-\log d\). The sharper displayed constant is not claimed at the earlier small-delta hitting time.

## 5. Exact GD recursion and invariant box

For this section only, omit tildes from the GD coefficients, put \(t=\widetilde\eta>0\), and define
\[
B=Lh,\quad C=(d-2)z,\quad r=s+B+C,\quad K=(1-s-C)/3.
\]
The matrix update gives
\[
s^+=s[1+4t(3-2s-r)]^2,
\quad B^+=B[1+12tL(K-B)]^2,
\quad C^+=C[1+4t(1-r)-8tC/(d-2)]^2.
\tag{3}
\]
We prove that \(\mathcal R=[0,1]\times[0,1/3]\times[0,1]\) is invariant. The initialization belongs to it for large \(d\). On this box the three multiplier brackets are strictly positive: the signal bracket is at least \(1-16t/3\ge7/9\), the spike bracket is at least \(1-8tL\ge1/2\), and the bulk bracket is at least \(1-(16/3+8/(d-2))t>0\).

Consequently comparisons of brackets can be squared. The signal update is at most \(s[1+12t(1-s)]^2\), the bulk update is at most \(C[1+4t(1-C)]^2\), and, on writing \(y=3B\), the spike update satisfies \(y^+\le y[1+4tL(1-y)]^2\). For \(0\le a\le1/2\), the map
\[
f_a(x)=x[1+a(1-x)]^2
\]
has derivative \([1+a-ax][1+a-3ax]\ge0\) on \([0,1]\) and \(f_a(1)=1\). Apply this with \(a=12t,4t,4tL\). Nonnegativity follows from the squared updates, proving invariance. Strictly positive initial coordinates remain positive.

The spike bracket is positive, so
\[
B_{k+1}\le B_k\quad\Longleftrightarrow\quad B_k\ge K_k.
\tag{4}
\]

## 6. GD escape and actual turning time

Fix \(\rho=1/48\), and let \(n=\inf\{k:r_k\ge\rho\}\). For \(k<n\), (3) gives
\[
1+12t(1-\rho)\le\sqrt{s_{k+1}/s_k}\le1+12t,
\]
\[
1+4tL(1-3\rho)\le\sqrt{B_{k+1}/B_k}\le1+4tL,
\]
\[
1+4t(1-\rho)-8t\rho/(d-2)
\le\sqrt{C_{k+1}/C_k}\le1+4t.
\tag{5}
\]
These lower bounds also establish monotonicity before escape. Since \(4tL\le1/4\), the inequality \(\log(1+x)\ge x/(1+x)\) implies
\[
n=O\left(1+\frac{1}{tL}\log\frac{\rho}{B_0}\right)
=O((t\lambda)^{-1}\log d).
\]
Finiteness follows because otherwise geometric spike growth would contradict \(B_k<\rho\). Since \(tn=O(\log d/\lambda)=O(1)\), the upper comparisons give
\[
s_n=\Theta(\mu),\qquad C_n=\Theta(\rho_0).
\]
For sufficiently large \(d\), each one-step multiplier before escape is bounded by two, so \(\rho\le r_n\le2\rho\). Thus \(B_n=\Theta(\rho)\), and \(r_n+2B_n<1\) for large \(d\). There has not yet been a spike turn.

Let \(T\) be the actual first turning index and \(E_k=K_k-B_k\). While \(n\le k<T\), the spike increases and \(B_k\ge\rho/2\) for large \(d\). The exact identity is
\[
E_{k+1}=(1-24tLB_k)E_k-(K_k-K_{k+1})-144t^2L^2B_kE_k^2.
\tag{6}
\]
On a bootstrap interval with \(r_k\le1/2\), signal and bulk increase. For large \(d\), the bulk bracket is at least \(1+t\), so
\[
K_k-K_{k+1}\ge(C_{k+1}-C_k)/3\ge c t\rho_0.
\]
Consequently, while \(E_k>0\),
\[
E_{k+1}\le(1-a)E_k-b,
\qquad a=12\rho tL\in(0,1),\quad b=c t\rho_0.
\]
Iteration yields
\[
E_{n+m}\le(1-a)^m(E_n+b/a)-b/a.
\]
This becomes nonpositive after at most
\[
m_*=O\left(1+\frac1{tL}\log\frac{L}{\rho_0}\right)
\tag{7}
\]
steps. This logarithm includes \(L\); omitting it is unjustified. Since
\[
tm_*=O\left(\frac{\log(L/\rho_0)}{L}\right)=o(1),
\]
the crude upper bounds in (3) imply \(s_k+C_k\le(s_n+C_n)e^{24tm_*}=o(1)\) throughout the candidate interval. Together with \(B_k\le1/3\), this prevents an exit through \(r=1/2\) and closes the bootstrap. Therefore \(T\le n+m_*\),
\[
T=O((t\lambda)^{-1}\log d),\qquad
s_T=\Theta(\mu),\quad C_T=\Theta(\rho_0).
\]
By (4), \(B_T\ge K_T=(1-s_T-C_T)/3\), while \(B_T\le1/3\), so \(B_T=1/3+o(1)\). This also gives
\[
\frac{h_T}{\max\{s_T,z_T\}}\ge c\frac{d}{L\rho_0}\longrightarrow\infty.
\]
This is spike dominance at the end of the first phase, not an assertion of dominance at the isotropic initialization.

For early alignment, both inequalities
\[
\|M_T\|_F\ge B_T/L,\qquad
\|M_T\|_F\ge C_T/\sqrt{d-2}
\]
hold simultaneously. They imply respectively
\[
\operatorname{Align}(M_T)\le C\rho_0\lambda/d,
\qquad
\operatorname{Align}(M_T)\le Cd^{-1/2}.
\]
Taking their minimum proves the target at \(T=\widetilde T_1\).

## 7. Valid fixed-epsilon bulk-inflation comparison

For completeness, recover the intermediate bulk phase without the invalid last-phase contraction assertions. Fix \(\varepsilon=1/8\), and let \(J=\inf\{k\ge T:r_k\ge1-\varepsilon\}\). Before \(J\), signal and bulk are nondecreasing: \(3-2s-r\ge3-3r\ge3\varepsilon\), and, for large \(d\), the bulk bracket is at least \(1+2\varepsilon t\). Therefore \(K\) is nonincreasing.

Set \(D_k=B_k-K_k\). Initially \(D_T\ge0\). Its exact recursion is
\[
D_{k+1}=(1-24tLB_k)D_k+(K_k-K_{k+1})+144t^2L^2B_kD_k^2.
\]
Since \(24tLB_k\le1/2\), this preserves \(D_k\ge0\). Thus \(B\) is nonincreasing. Also
\[
r_k\ge s_k+C_k+K_k=\frac{1+2s_k+2C_k}{3}
\]
implies \(K_k\ge\varepsilon/2\), so \(B_k\ge\varepsilon/2\). For \(x=12tLD_k\in[0,1/2]\), use \((1-x)^2\le1-x\), obtaining
\[
D_{k+1}\le(1-6\varepsilon tL)D_k+C_1t.
\]
The bound on the forcing follows directly from (3) and the box. Moreover \(D_T\le(s_T+C_T)/3=O(\rho_0)\). Iteration gives
\[
\sup_{T\le k\le J}D_k=O(\rho_0)+O(L^{-1})=o(1),
\]
where the same one-step inequality covers the exit index.

The bulk update directly gives \(C_{k+1}\ge(1+4\varepsilon t)C_k\) before \(J\). Since \(C_k\le1\) and \(C_T=\Theta(\rho_0)\), this proves
\[
J-T=O(t^{-1}\log(1/\rho_0)).
\]
Also \(\mu\le s_J\le C\mu\exp(24t(J-T))=d^{-1+o(1)}\), hence \(s_J=d^{-1+o(1)}\). The signal and bulk increments are \(O(t)\), whereas the spike is nonincreasing on the preceding step. Therefore
\[
1-\varepsilon\le r_J\le1-\varepsilon+O(t).
\]
Using the exact identity \(r=(1+2s+2C)/3+D\), we obtain
\[
C_J=1-3\varepsilon/2+o(1),\qquad B_J=\varepsilon/2+o(1).
\]
These are fixed-epsilon statements. They neither say \(1-C_J=o(1)\) nor establish a fixed negative gap \(K_J-B_J\).

## 8. GD signal hitting and uniform later alignment

The invariant box alone gives, at every index,
\[
3-2s-r=3-3s-B-C\ge5/3-3s.
\]
Below the fixed \(\delta=1/100\), this is larger than one. Thus, until the signal hits \(\delta\),
\[
s_{k+1}\ge s_k(1+4t)^2.
\]
Starting from \(s_T=\Theta(\mu)\), this proves
\[
\widetilde T_2-\widetilde T_1=O(t^{-1}\log d).
\]
It is also consistent with the preceding bulk phase, whose exit signal is still vanishing. Only the upper time bound is required; the global upper multiplier \((1+12t)^2\) additionally shows an order \(t^{-1}\log d\) delay from the turning signal scale.

We must prove persistence, not merely a hitting-time statement. If \(\delta\le s_k\le5/9\), the lower drift above is nonnegative, so \(s_{k+1}\ge s_k\). If \(s_k\ge5/9\), the positive signal bracket is at least \(7/9\), giving
\[
s_{k+1}\ge\frac59\left(\frac79\right)^2>\delta.
\]
Thus \(\delta\le s_k\le1\) for every \(k\ge\widetilde T_2\). At all indices the box gives
\[
h_k^2+(d-2)z_k^2\le\frac1{9(1+\lambda)^2}+\frac1{d-2}=o(1).
\]
Consequently, uniformly for \(k\ge\widetilde T_2\),
\[
1-\operatorname{Align}(M_k)
\le\frac1{2\delta^2}\left(\frac1{9(1+\lambda)^2}+\frac1{d-2}\right)=o(1).
\]
Restore tildes to all GD quantities. This proves every requested comparison, including all-future rather than merely at-hitting alignment.

## Source-repair notes

The proof intentionally does not claim geometric contraction of the scaled GD spike or of the bulk deficit during the final phase. The source inference producing those claims is invalid, and the frozen conclusions need only the already proved upper barriers. Likewise the early discrete alignment bound is proved at the actual discrete turning index. The source-local corrections to singular polar signs, the square-root barrier typography, and the saturation logarithm are explicit above. There are no unresolved theorem-critical obligations.
