# Reference Proof

## Proof Structure

Verify that the optimization values are defined, analyze one item type using the residual-demand invariant, combine itemwise feasibility, count the represented decoder operations, and compare the fixed decoded decision with the minimum of the same conditional objective.

## Complete Proof

### Optimization domains and evaluation convention

The first-stage feasible set is nonempty: zero shipments and \(u_i=q_i\) satisfy all constraints. It is finite because every shipment coordinate and \(u_i\) lies between zero and \(q_i\).

For any feasible \(z\) and finite nonnegative demand vector \(D\), the recourse choice \(v=0,w=D\) is feasible. Its feasible set is closed, and demand balance bounds every \(v_{ijk}\) and \(w_i\) by \(D_i\). Consequently it is compact. The linear recourse objective is continuous and finite, so its minimum is attained and finite. The source's recourse variables are real, and this argument does not require an integrality theorem.

The immediate cost and recourse cost are nonnegative under the stated coefficient domains. Their conditional integrals therefore exist as values in \([0,\infty]\). A minimum of these values over the nonempty finite set \(Z\) exists, even if every value is infinite. The policy-value expression evaluates the already returned decision under \(P_X\), holding the realized decoder inputs fixed. It does not let those inputs depend on the actual uncertainty realization being evaluated.

### Itemwise feasibility

Fix an item type \(i\). Initially every shipment coordinate is logically zero, including coordinates at locations that will not be scanned. If \(q_i=0\), zero shipments and \(u_i=0\) satisfy every constraint and no adequacy ratio is evaluated.

Suppose \(q_i>0\). Initially \(r=q_i\). At any visited location,
\[
x_j=\min\{r,\operatorname{Inv}_{ij}\}.
\]
Both arguments are nonnegative integers. Hence \(x_j\) is a nonnegative integer, \(x_j\le r\), and the updated residual \(r-x_j\) remains a nonnegative integer. Also \(x_j\le\operatorname{Inv}_{ij}\).

The chosen carrier belongs to the nonempty set \(K_j\). Only that coordinate at this location can become nonzero. Each location appears in the order at most once, so
\[
\sum_k z_{ijk}=x_j\le\operatorname{Inv}_{ij}
\]
for a visited location. Unvisited locations retain zero shipments. All inventory and carrier-eligibility constraints therefore hold.

Initially,
\[
q_i=r+\sum_{j,k}z_{ijk}.
\]
Each assignment increases the shipment sum by \(x_j\) and decreases \(r\) by exactly \(x_j\), preserving this identity. At termination, setting \(u_i=r\) gives
\[
\sum_{j,k}z_{ijk}+u_i=q_i.
\]
All output variables are nonnegative integers. This includes an empty eligible set: the scan makes no assignments and returns \(u_i=q_i\). If the residual reaches zero before the end, subsequent assignments are zero and do not change the argument.

Thus the output belongs to \(Z_i\). Repeating this argument for each item and using \(Z=\prod_i Z_i\) proves feasibility of the complete decision. This is separability of constraints only; the consolidation cost need not be separable across items. When \(I\) is empty, the empty tuple is feasible.

### Decoder runtime

Let \(n=|J|\) and \(m=\sum_j|K_j|\). Use the stated unit-cost model, listed eligible sets, and zero-default sparse shipment representation. Initializing an empty shipment list and storing the unmet quantity takes constant time; no dense \(J\times K\) array must be written.

For positive demand, testing eligibility and forming the scores takes \(O(n)\) operations. List emptiness can be checked in constant time per location. Sorting at most \(n\) eligible locations costs \(O(n\log(1+n))\). The allocation scan and recording assignments cost \(O(n)\). A direct carrier maximization scan at location \(j\) costs \(O(|K_j|)\), so their total cost is at most \(O(m)\). Fixed input orderings resolve ties within these counts.

Including constant-size and zero-demand cases gives
\[
O\!\left(1+n\log(1+n)+m\right).
\]
For \(n\ge2\), this is \(O(n\log n+m)\). If every \(K_j=K\), then \(m=n|K|\), giving both stated universal-eligibility forms. The constants do not depend on the numerical demands, inventories, or probability values in the unit-cost arithmetic model. Neural inference, probability computation, and optional dense output materialization are not included. Materializing a dense shipment array would require an additional \(O(|J||K|)\) time per item.

### Conditional policy-value comparison

Fix the observed context and any realized admissible decoder inputs. Let \((z^{\mathrm d},u^{\mathrm d})\) be the resulting complete decision. By feasibility it is one of the decisions in \(Z\). Define privately
\[
F_X(z,u)=\int\bigl[C(z,u,\Delta)+Q(z,D)\bigr]P_X(d\Delta,dD).
\]
The public evaluation convention gives the decoded policy value as \(F_X(z^{\mathrm d},u^{\mathrm d})\), and the program optimum is \(\min_{(z,u)\in Z}F_X(z,u)\). Therefore
\[
\mathbb E\!\left[C(z^{\mathrm d},u^{\mathrm d},\widetilde\Delta)+Q(z^{\mathrm d},\widetilde D)\mid X\right]
=F_X(z^{\mathrm d},u^{\mathrm d})
\ge \min_{(z,u)\in Z}F_X(z,u)=V(X).
\]
This comparison is valid also for extended nonnegative values and for every fixed realization of the simulated decoder inputs. It neither substitutes an in-sample scenario average for the conditional expectation nor allows anticipative selection using the actual evaluation realization.
