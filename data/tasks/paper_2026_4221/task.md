# Problem

## Setup

At a fixed decision epoch, let \(I\), \(J\), and \(K\) be finite sets of item types, fulfillment locations, and carriers. For each \(i\in I\), demand \(q_i\) and inventories \(\operatorname{Inv}_{ij}\) are nonnegative integers. For each location \(j\), let \(K_j\subseteq K\) be its set of eligible carriers. These quantities are observed at the decision epoch.

A first-stage decision consists of nonnegative integer shipment variables \(z_{ijk}\) and unmet-demand variables \(u_i\). Its feasible set is
\[
Z=\prod_{i\in I}Z_i,
\]
where \((z_i,u_i)\in Z_i\) precisely when
\[
\sum_{j\in J}\sum_{k\in K}z_{ijk}+u_i=q_i,
\qquad
\sum_{k\in K}z_{ijk}\le\operatorname{Inv}_{ij}\quad(j\in J),
\qquad
z_{ijk}=0\quad(k\notin K_j).
\]
Empty sums are zero.

Let \(c_{ijk}\ge0\) be finite base shipping costs, let \(p>0\) be a finite unit unmet-demand penalty, let \(\beta\in(0,1)\), and let \(\gamma^+,\gamma^->0\) be finite delivery-deviation penalties. All these coefficients are known at the decision epoch. For a delivery-deviation vector \(\Delta\in\mathbb R^{J\times K}\), write \(\Delta_{jk}^+=\max\{\Delta_{jk},0\}\) and \(\Delta_{jk}^-=\max\{-\Delta_{jk},0\}\). Define
\[
C(z,u,\Delta)=\sum_{j\in J}\sum_{k\in K}\left[
\left(\sum_{i\in I}c_{ijk}z_{ijk}\right)
\left(1-\beta\mathbf1\left\{\sum_{i\in I}z_{ijk}\ge2\right\}\right)
+\left(\gamma^+\Delta_{jk}^++\gamma^-\Delta_{jk}^-\right)\sum_{i\in I}z_{ijk}
\right]+p\sum_{i\in I}u_i,
\]
where \(\mathbf1\) denotes the indicator.

For a finite nonnegative integer future-demand vector \(D\), define
\[
Q(z,D)=\min_{v,w\ge0}\left\{
\sum_{i,j,k}c_{ijk}v_{ijk}+p\sum_iw_i:
\sum_{j,k}v_{ijk}+w_i=D_i\ (i\in I),\quad
\sum_k(z_{ijk}+v_{ijk})\le\operatorname{Inv}_{ij}\ (i\in I,j\in J)
\right\}.
\]
Here \(v,w\) are real variables, all triple sums run over \(I\times J\times K\), and the displayed constraints are the complete recourse constraints.

After observing context \(X\), the stochastic program has objective
\[
V(X)=\min_{(z,u)\in Z}\mathbb E\left[C(z,u,\widetilde\Delta)+Q(z,\widetilde D)\mid X\right].
\]
The pair \((\widetilde\Delta,\widetilde D)\) has conditional law \(P_X\), supported on \(\mathbb R^{J\times K}\times\mathbb Z_+^I\). All observed decision-epoch data are held fixed when using this conditional law. Expectations of these nonnegative costs are understood in \([0,\infty]\).

The first-stage decision is made without access to the actual realization of \((\widetilde\Delta,\widetilde D)\). Decoder inputs may use observed context and simulated scenarios generated using randomness independent of the actual uncertainty conditional on \(X\). For the policy-value expression below, fix the realized decoder inputs and its tie choices: the conditional expectation integrates only \((\Delta,D)\) under \(P_X\), holding the returned decision fixed. It does not average over the scenario-generation randomness or evaluate the decision on the same simulated scenarios that produced it.

## Decoder

Apply the following decoder separately to each item type. For each processed item, it is given already-computed location probabilities \(a_j\) and eligible-carrier probabilities \(b_{jk}\). On each nonempty index set these are obtained from finite real logits by softmax, where \(\operatorname{softmax}(\ell)_h=e^{\ell_h}/\sum_g e^{\ell_g}\). The location index set is \(J\); at location \(j\), the carrier index set is \(K_j\). No probability vector on an empty index set is required. The probabilities may differ between item types; their item index is suppressed.

All shipment coordinates initially have value zero. If \(q_i=0\), return zero shipments and \(u_i=0\) without evaluating an adequacy ratio. Otherwise define
\[
E_i=\{j:\operatorname{Inv}_{ij}>0,\ K_j\ne\varnothing\},
\qquad
\rho_{ij}=\min\{\operatorname{Inv}_{ij}/q_i,1\}\quad(j\in E_i).
\]
Sort \(E_i\) in nonincreasing order of \(a_j\rho_{ij}\). Starting with residual \(r=q_i\), scan this order. At location \(j\), choose
\[
k_j\in\arg\max_{k\in K_j}b_{jk},
\]
set
\[
x_j=\min\{r,\operatorname{Inv}_{ij}\},\qquad z_{ij k_j}=x_j,
\]
and replace \(r\) by \(r-x_j\). All other shipment coordinates retain value zero. After the scan, set \(u_i=r\). Sorting and carrier ties may be resolved using any fixed input orderings.

For the runtime claim, use unit-cost arithmetic, comparisons, and indexed access. Each \(K_j\) is supplied as a list with constant-time access to whether it is empty. The shipment output is a list of assigned coordinates with every unlisted coordinate defined to be zero; dense output materialization is not required. The runtime starts after the probabilities are available.

## Task

Prove that the decoder's complete output \((z^{\mathrm d},u^{\mathrm d})\) belongs to \(Z\).

Prove also that, for each item type, the decoding operations run in
\[
O\!\left(1+|J|\log(1+|J|)+\sum_{j\in J}|K_j|\right)
\]
time. Thus, for \(|J|\ge2\), the bound is
\[
O\!\left(|J|\log|J|+\sum_{j\in J}|K_j|\right).
\]
Under universal eligibility \(K_j=K\), prove the corresponding bound
\[
O\!\left(1+|J|\log(1+|J|)+|J||K|\right),
\]
which is \(O(|J|\log|J|+|J||K|)\) for \(|J|\ge2\). The forms containing the constant term also cover empty and singleton location sets.

Finally, under the fixed-input evaluation convention stated above, prove
\[
\mathbb E\left[C(z^{\mathrm d},u^{\mathrm d},\widetilde\Delta)+Q(z^{\mathrm d},\widetilde D)\mid X\right]\ge V(X).
\]
