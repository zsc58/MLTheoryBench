# Reference Proof

## Proof Structure and Obligations

The proof must establish: (1) well-defined bounded conditional means and the label-mixture expansion; (2) the exact cross-group residual decomposition; (3) cancellation and range control within clusters, including zero-probability cluster/group cells; (4) the cross-cluster range bound with its correct constant; and (5) assembly of the exact stated inequality. All five obligations are proved below. No conformal coverage theorem or specialized external result is used.

## Complete Proof

All probabilities and expectations use the joint law specified in the task. The score and clustering map are fixed; the calibrated thresholds may be random. Since \(S(Z)\subseteq[m]\), its cardinality is measurable and lies in \([0,m]\). Thus every positive-event conditional expectation below is finite. The stipulated zero values handle null events.

For a group \(g\), let
\[
p_g(\ell)=\Pr(L=\ell\mid B=g),\qquad e_g=\mathbb E[|S(Z)|\mid B=g].
\]
Because \(\Pr(B=g)>0\), \(p_g\) is a probability distribution. Total expectation gives
\[
e_g=\sum_{\ell=1}^m p_g(\ell)r_{\ell,g}.
\]
The zero-event convention is compatible with this identity because each null label/group cell has zero mixture weight.

Fix \(u,v\), and set \(d_\ell=p_u(\ell)-p_v(\ell)\). Inserting the mixture with weights \(p_v\) and means \(r_{\ell,u}\) yields
\[
e_u-e_v=R+\sum_{\ell=1}^m d_\ell r_{\ell,u},
\qquad
R=\sum_{\ell=1}^m p_v(\ell)(r_{\ell,u}-r_{\ell,v}).
\]
For each cluster, write
\[
D_j=\sum_{\ell\in\mathcal L_j}d_\ell.
\]
Adding and subtracting \(\mu_{j,u}\) in each cluster gives
\[
\sum_\ell d_\ell r_{\ell,u}=T+U,
\]
where
\[
T=\sum_j\sum_{\ell\in\mathcal L_j}d_\ell(r_{\ell,u}-\mu_{j,u}),
\qquad U=\sum_jD_j\mu_{j,u}.
\]

We verify the cluster-mean facts used to bound \(T\). Set
\[
w_{j,u}=\sum_{\ell\in\mathcal L_j}p_u(\ell)=\Pr(c(L)=j\mid B=u).
\]
If \(w_{j,u}>0\), total expectation within the cluster gives
\[
\mu_{j,u}=\sum_{\ell\in\mathcal L_j}\frac{p_u(\ell)}{w_{j,u}}r_{\ell,u}.
\]
This is a convex combination, so \(\mu_{j,u}\) lies between the smallest and largest \(r_{\ell,u}\) in the cluster, and
\[
\sum_{\ell\in\mathcal L_j}p_u(\ell)(r_{\ell,u}-\mu_{j,u})=0.
\]
If \(w_{j,u}=0\), all \(p_u(\ell)\) in the cluster vanish. Since \(\Pr(B=u)>0\), each corresponding label/group event and the cluster/group event have probability zero. The task therefore sets all those \(r_{\ell,u}\) and \(\mu_{j,u}\) to zero. Both the range assertion and cancellation identity still hold.

Consequently, for every cluster and every label in it,
\[
|r_{\ell,u}-\mu_{j,u}|\leq\varepsilon_{j,u},
\]
and the cancellation identity gives
\[
T=-\sum_j\sum_{\ell\in\mathcal L_j}p_v(\ell)(r_{\ell,u}-\mu_{j,u}).
\]
It follows that
\[
|T|\leq\sum_\ell p_v(\ell)\varepsilon_{c(\ell),u}
\leq\max_j\varepsilon_{j,u}.
\]

For the remaining component, define
\[
R_\mu=\max_j\mu_{j,u}-\min_j\mu_{j,u},\qquad
m_\mu=\frac{\max_j\mu_{j,u}+\min_j\mu_{j,u}}2.
\]
Since the clusters partition the label set,
\[
\sum_jD_j=\sum_\ell d_\ell=0,
\]
so
\[
U=\sum_jD_j(\mu_{j,u}-m_\mu).
\]
Moreover,
\[
\sum_j|D_j|\leq\sum_\ell|d_\ell|
\leq\sum_\ell(p_u(\ell)+p_v(\ell))=2.
\]
Together with \(|\mu_{j,u}-m_\mu|\leq R_\mu/2\), this proves
\[
|U|\leq R_\mu.
\]

Finally,
\[
\begin{aligned}
\Delta_{u,v}
&=|e_u-e_v|\\
&\leq |R|+|T|+|U|\\
&\leq \max_j\varepsilon_{j,u}
+\left(\max_j\mu_{j,u}-\min_j\mu_{j,u}\right)
+\left|\sum_{\ell=1}^m\Pr(L=\ell\mid B=v)(r_{\ell,u}-r_{\ell,v})\right|.
\end{aligned}
\]
This is the exact target for arbitrary \(u,v\). No division by a range was used, so zero ranges, \(K=1\), \(K=m\), identical groups, and empty prediction sets are included.

## Scope of the Threshold Interpretation

The rule uses the same cluster-indexed threshold for a candidate label in every sensitive group. This describes the predictor but is not an additional algebraic proof obligation. The proof does not infer comparative superiority over a group-specific method, vanishing within-label disparity, or elimination of all calibration randomness. The source's subsequent Lipschitz comparison is not needed for the requested inequality.
