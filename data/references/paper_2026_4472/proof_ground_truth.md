# Reference Proof

## Proof Structure

Expand the discrepancy between the two classifier-conditioned distributions. The definition of conditional probability and the partition by the classifier outputs reduce it to the weighted parity disparity divided by a classifier-output factor independent of the subgroup. Treat null subgroups separately, then use the resulting constant-factor relation on the full conjunction class to transfer maximizers and suprema and derive the threshold bound.

## Complete Proof

Let \(p_1=\Pr_D(h(X)=1)\) and \(p_0=\Pr_D(h(X)=0)=1-p_1\), with \(p_1p_0>0\). Set \(D_1=D(\cdot\mid h(X)=1)\) and \(D_0=D(\cdot\mid h(X)=0)\). These conditional distributions are well-defined.

For an arbitrary \(S\in\mathcal S_A^+\), write \(q=\Pr_D(S)>0\). Then
\[
\operatorname{SD}(S;D_1,D_0)
=\left|\frac{\Pr_D(S,h(X)=1)}{p_1}-\frac{\Pr_D(S,h(X)=0)}{p_0}\right|
=\frac{|p_0\Pr_D(S,h(X)=1)-p_1\Pr_D(S,h(X)=0)|}{p_1p_0}.
\]
Since \(\Pr_D(S,h(X)=0)=q-\Pr_D(S,h(X)=1)\), the numerator is
\[
\left|\Pr_D(S,h(X)=1)-p_1q\right|
=q\left|\Pr_D(h(X)=1\mid S)-p_1\right|
=\Phi_h(S).
\]
Thus
\[
\operatorname{SD}(S;D_1,D_0)=\frac{\Phi_h(S)}{p_1p_0}
\]
for every positive-mass conjunction subgroup. The argument applies to each subgroup under the same fixed distribution and classifier, establishing the claimed simultaneous identity.

If \(S\in\mathcal S_A\setminus\mathcal S_A^+\), then \(\Pr_D(S)=0\). Each event \(S\cap\{h(X)=i\}\) is contained in \(S\), so its probability is zero. Consequently \(\Pr_{D_1}(S)=\Pr_{D_0}(S)=0\), and \(\operatorname{SD}(S;D_1,D_0)=0=\Phi_h(S)\). The same proportionality therefore holds on all of \(\mathcal S_A\).

The factor \(1/(p_1p_0)\) is positive and independent of \(S\). For any two members of \(\mathcal S_A\), comparing their disparities is therefore equivalent to comparing their SD values. It follows that the sets of subgroups attaining the two suprema over \(\mathcal S_A\) are identical. In particular, if all disparities vanish, every member of \(\mathcal S_A\), including every null subgroup, maximizes both objectives. No separate assumption of attainment is needed for equality of the maximizing sets.

The empty conjunction gives the subgroup \(\mathcal X\), which has probability one. Thus \(\mathcal S_A^+\) is nonempty. Since SD is nonnegative and null subgroups have SD zero, removing null subgroups does not change its supremum. By the definition of \(\mathsf M\),
\[
\mathsf M(D_1,D_0;A)
=\sup_{S\in\mathcal S_A}\operatorname{SD}(S;D_1,D_0)
=\sup_{S\in\mathcal S_A^+}\operatorname{SD}(S;D_1,D_0)
=\frac{1}{p_1p_0}\sup_{S\in\mathcal S_A^+}\Phi_h(S).
\]
Finally, if \(\gamma\in[0,1]\) and \(\Phi_h(S)\le\gamma\) for every \(S\in\mathcal S_A^+\), taking the supremum and using the preceding identity gives
\[
\mathsf M(D_1,D_0;A)\le\frac{\gamma}{p_1p_0}.
\]
