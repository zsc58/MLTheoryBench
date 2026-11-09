# Reference Proof

## Definitions used in the bound

Let \(\Pi=[J]\times[K]_0\). For a realization \(z=(x,a,y)\), write \(c_{(j,k)}(z)=c_{j,k}(x,a,y)\). Let \(\mathcal H_\Pi\) be the stated composite score class, let
\[
\pi_s(x)=\arg\max_{i\in\Pi}s(x,i),
\]
with the fixed finite tie-breaking convention, and define
\[
L_{\rm def}(s;z)=c_{\pi_s(x)}(z),\qquad
L_{\rm aug}(s;z)=\ell_{\rm aug}(s;x,a,y).
\]
For either loss \(L\), let \(R_L(s)=\mathbb E[L(s;X,A,Y)]\), let \(R_L^{B}(\mathcal H_\Pi)=\inf_{s\in\mathcal H_\Pi}R_L(s)\), and let
\[
R_L^*(\mathcal H_\Pi)=\mathbb E\left[\inf_{s\in\mathcal H_\Pi}\mathbb E[L(s;X,A,Y)\mid X]\right].
\]
The corresponding quantities are
\[
\mathcal E_L(s)=R_L(s)-R_L^{B}(\mathcal H_\Pi),\qquad
\mathcal M_L(\mathcal H_\Pi)=R_L^{B}(\mathcal H_\Pi)-R_L^*(\mathcal H_\Pi).
\]
Thus the notation in the claim is \(\mathcal E_{\rm def}=\mathcal E_{L_{\rm def}\!}\), \(\mathcal M_{\rm def}=\mathcal M_{L_{\rm def}\!}\), and analogously for the augmented loss.

## Separated construction

For \((u,v)\in(0,C]^2\), define
\[
F(u,v)=\inf_t\{\nu(u)G(t)\Phi_0(U(t))+\nu(v)G(t)\Phi_1(U(t))\}.
\]
The query assumptions give a unique minimizer \(t^*(u,v)\), and its continuous dependence on \((u,v)\). Since the router weights are positive, profiling the two query scores gives
\[
\Psi_1(s)F(c_{1,0},c_{1,1})+\Psi_2(s)F(c_{2,0},c_{2,1}).
\]

For fixed \(u\in(0,C)\), Danskin's theorem applies because the minimizer is unique. It gives
\[
\frac{\partial F}{\partial v}(u,v)
=\nu'(v)G(t^*(u,v))\Phi_1(U(t^*(u,v)))>0,
\]
so \(v\mapsto F(u,v)\) is strictly increasing. The same assumptions imply continuity of \(F\).

For positive \(A,B\), the router objective \(A\Psi_1(s)+B\Psi_2(s)\) is strictly convex. Its first-order equation is
\[
\rho(s)=\frac BA.
\]
Because \(\rho\) is a decreasing bijection and \(\rho(0)=1\), its unique minimizer is positive when \(A>B\), zero when \(A=B\), and negative when \(A<B\). Under the stipulated decoder, a positive score selects expert 2.

Fix \(b\in(0,C)\) and \(\varepsilon\in(0,C-b)\). Strict increase in the second argument gives
\[
F(b,C)>F(b,b+\varepsilon).
\]
By continuity in the first argument, choose \(\delta\in(0,b)\) sufficiently small that
\[
F(b-\delta,C)>F(b,b+\varepsilon).
\]
The row minima of
\[
\begin{pmatrix}b-\delta&C\\ b&b+\varepsilon\end{pmatrix}
\]
are \(b-\delta\) and \(b\), so the Bayes policy selects expert 1. After query profiling, however, \(A=F(b-\delta,C)\) and \(B=F(b,b+\varepsilon)\) satisfy \(A>B\), so the unique router minimizer is positive and decodes to expert 2. The query minimizers are unique as well, hence the full pointwise separated-surrogate minimizer is unique and incorrect. Taking a one-point input distribution with this table realizes the conditional construction and proves Bayes inconsistency.

## Augmented construction

For each realization, set
\[
M=\max_{i\in\Pi}c_i,\qquad w_i=M-c_i,\qquad
D=\sum_{i\in\Pi}c_i-(|\Pi|-1)M.
\]
If the executed composite action is \(i_\pi=\pi_s(x)\), then
\[
\begin{aligned}
D+\sum_iw_i\mathbf 1\{i_\pi\ne i\}
&=\sum_i c_i-(|\Pi|-1)M+\sum_{i\ne i_\pi}(M-c_i)\\
&=c_{i_\pi}.
\end{aligned}
\]
Therefore
\[
L_{\rm def}(s;z)=D(z)+\sum_iw_i(z)\mathbf 1\{\pi_s(X)\ne i\},
\]
and the augmented surrogate is precisely the weighted comp-sum loss in the task.

Define
\[
\bar w_i(x)=\mathbb E[w_i(X,A,Y)\mid X=x],\qquad
W(x)=\sum_i\bar w_i(x).
\]
If \(W(x)>0\), set \(p_i(x)=\bar w_i(x)/W(x)\); if \(W(x)=0\), choose any probability vector, for example the uniform vector. Also set \(d(x)=\mathbb E[D(X,A,Y)\mid X=x]\). Conditional on \(X=x\),
\[
\mathbb E[L_{\rm def}(s;X,A,Y)\mid X=x]
=d(x)+W(x)\sum_i p_i(x)\mathbf 1\{\pi_s(x)\ne i\},
\]
and
\[
\mathbb E[L_{\rm aug}(s;X,A,Y)\mid X=x]
=W(x)\sum_i p_i(x)\Phi_{01}^{\tau}(s(x),i).
\]
When \(W(x)=0\), all \(\bar w_i(x)\) vanish and both action-dependent terms are zero, so the identities remain valid.

Let \(\alpha=\mathbb E[W(X)]\). If \(\alpha=0\), nonnegativity implies \(W(X)=0\) almost surely, hence every predictor has the same true risk and the augmented surrogate risk is zero; the asserted inequality is immediate. Assume henceforth \(\alpha>0\). Define a probability law \(\widetilde P\) on \(\mathcal X\times\Pi\) by
\[
\widetilde P(X\in B,I=i)=\frac{\mathbb E[\bar w_i(X)\mathbf 1\{X\in B\}]}{\alpha}.
\]
Its total mass is one because \(\sum_i\mathbb E[\bar w_i(X)]=\alpha\). The conditional identities integrate to
\[
R_{L_{\rm aug}}(s)=\alpha R_{\Phi_{01}^{\tau}}(s;\widetilde P),
\]
and
\[
R_{L_{\rm def}}(s)=\mathbb E[D]+\alpha R_{01}(\pi_s;\widetilde P).
\]
Taking infima over \(\mathcal H_\Pi\), and then taking the conditional infima defining the minimizability gaps, gives the same affine scaling for best-in-class risks and gaps:
\[
\mathcal E_{\rm aug}+\mathcal M_{\rm aug}
=\alpha\bigl(\mathcal E_{\Phi_{01}^{\tau}}+\mathcal M_{\Phi_{01}^{\tau}}\bigr),
\]
\[
\mathcal E_{\rm def}+\mathcal M_{\rm def}
=\alpha\bigl(\mathcal E_{01}+\mathcal M_{01}\bigr).
\]
The additive \(\mathbb E[D]\) cancels from true excess risks and gaps.

The audited standard comp-sum multiclass H-consistency theorem applies to \(\Phi_{01}^{\tau}\) under the assumed symmetry and completeness hypotheses of \(\mathcal H_\Pi\), for the probability law \(\widetilde P\). Hence
\[
\mathcal E_{01}+\mathcal M_{01}
\le \Gamma_\tau(\mathcal E_{\Phi_{01}^{\tau}}+\mathcal M_{\Phi_{01}^{\tau}}).
\]
Multiplying by \(\alpha\) and using the scaling identities yields
\[
\mathcal E_{\rm def}+\mathcal M_{\rm def}
\le \alpha\Gamma_\tau\left(\frac{\mathcal E_{\rm aug}+\mathcal M_{\rm aug}}\alpha\right)
=\widetilde\Gamma_\tau(\mathcal E_{\rm aug}+\mathcal M_{\rm aug}),
\]
where \(\widetilde\Gamma_\tau(u)=\alpha\Gamma_\tau(u/\alpha)\). For \(\tau=1\), the supplied external theorem gives \(\Gamma_1(u)=\sqrt{2u}\).
