# Problem

## Setup

Let \(Z\) be a finite context space with metric \(M\), let \(\varnothing\ne S\subseteq Z\) be the training support, and define
\[
d(z,S):=\inf_{s\in S}M(z,s).
\]
Equip \(Z\) with its power-set sigma-algebra. All output laws are defined on a common measurable space \((Y,\mathcal F)\).

For finite signed measures \(A,B\) on \((Y,\mathcal F)\) with equal total mass, use the convention
\[
\operatorname{TV}(A,B):=\sup_{F\in\mathcal F}|A(F)-B(F)|.
\]
In particular, this is the usual total-variation distance for probability measures.

For any nonempty class \(\mathcal C\) of conditional probability laws and any \(r\geq0\), define
\[
U_{\mathcal C,S}(r):=
\sup_{\substack{z\in Z:\ d(z,S)\leq r\\
R,R'\in\mathcal C:\ R(\cdot\mid s)=R'(\cdot\mid s)\ \forall s\in S}}
\operatorname{TV}\bigl(R(\cdot\mid z),R'(\cdot\mid z)\bigr).
\]

Let \(\Theta\ne\varnothing\) and let
\(\mathcal P=\{P_\theta(\cdot\mid z):\theta\in\Theta\}\)
be a base class of conditional probability laws. Let \(K(\cdot\mid z)\) be a fixed probability kernel from \(Z\) to \(Z\), common to all parameters, and define
\[
\widetilde P_\theta(\cdot\mid z):=
\int_Z P_\theta(\cdot\mid u)\,K(du\mid z),
\qquad
\widetilde{\mathcal P}:=\{\widetilde P_\theta:\theta\in\Theta\}.
\]
Write
\[
\operatorname{supp}K(\cdot\mid z):=\{u\in Z:K(\{u\}\mid z)>0\}.
\]

For \(\delta>0\), define
\[
\eta_K(\delta):=
\sup_{\substack{z\in Z:\ d(z,S)\leq\delta}}
\inf_{s\in S}
\operatorname{TV}\bigl(K(\cdot\mid z),K(\cdot\mid s)\bigr),
\]
\[
\rho_K(\delta):=
\sup_{\substack{z\in Z:\ d(z,S)\leq\delta}}
\sup_{u\in\operatorname{supp}K(\cdot\mid z)}d(u,S).
\]
Finally, define the perturbation cost
\[
\begin{aligned}
E_{K,\mathcal P,\delta}:={}&
\sup_{\substack{z\in Z:\ d(z,S)\leq\delta}}
\sup_{u\in\operatorname{supp}K(\cdot\mid z)}
\sup_{\substack{\theta,\theta'\in\Theta:\
\widetilde P_\theta(\cdot\mid s)=\widetilde P_{\theta'}(\cdot\mid s)\ \forall s\in S}}
\inf_{\substack{a,b\in\Theta:\
P_a(\cdot\mid s)=P_b(\cdot\mid s)\ \forall s\in S}}
\\[-2pt]
&\operatorname{TV}\Bigl(
P_\theta(\cdot\mid u)-P_a(\cdot\mid u),
P_{\theta'}(\cdot\mid u)-P_b(\cdot\mid u)
\Bigr).
\end{aligned}
\]
The two arguments of the last total-variation expression are finite signed measures of total mass zero.

## Task

Prove that for every \(\delta>0\),
\[
U_{\widetilde{\mathcal P},S}(\delta)\leq2\eta_K(\delta),
\]
and
\[
U_{\widetilde{\mathcal P},S}(\delta)
\leq U_{\mathcal P,S}\bigl(\rho_K(\delta)\bigr)+E_{K,\mathcal P,\delta}.
\]
