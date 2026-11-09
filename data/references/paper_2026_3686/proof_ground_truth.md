# Reference Proof

## Proof Structure

For each fixed potential test, obtain a conditional, time-uniform error bound at its pre-start history. For a strong-null test, a predictably truncated wealth process handles even a null that holds only on a subset of realized paths. For a weak-null test, a false commitment entails failure of simultaneous coverage. Take expectations over the random levels, then use the fixed countable index set and the pathwise allocation.

## Complete Proof

Fix \(j\in I\). Work on its instantiation event and condition on \(\mathcal G_j=\mathcal F_{\sigma_j-1}\); its level and test type are then fixed. Predictability of \(\sigma_j\) permits the post-start filtration \((\mathcal F_{\sigma_j+n-1})_{n\ge0}\), whose initial sigma-field is \(\mathcal G_j\).

Suppose \(j\) uses the strong-null test. For \(n\ge1\), put \(B_{j,n}=\mathbf1\{\delta_{j,r}\le0\text{ for all }1\le r\le n\}\). This indicator is \(\mathcal F_{\sigma_j+n-2}\)-measurable, since each conditional advantage is known immediately before its corresponding observation. Define \(\widetilde W_{j,0}=1\) and
\[
\widetilde W_{j,n}=\widetilde W_{j,n-1}\bigl(1+B_{j,n}\beta_{j,n}\Delta_{j,n}\bigr).
\]
Its factors are nonnegative. Moreover,
\[
\mathbb E[\widetilde W_{j,n}\mid\mathcal F_{\sigma_j+n-2}]
=\widetilde W_{j,n-1}(1+B_{j,n}\beta_{j,n}\delta_{j,n})
\le\widetilde W_{j,n-1}.
\]
Thus \(\widetilde W_j\) is a nonnegative supermartingale starting at one, whether or not the strong null holds on every path. On the event that the strong null is true for \(j\), all \(B_{j,n}=1\), so \(\widetilde W_{j,n}=W_{j,n}\) for every \(n\). Conditional Ville's inequality, applied with the \(\mathcal G_j\)-measurable threshold \(1/\alpha_j\), therefore gives
\[
\Pr\{\text{strong null true and }\tau_j<\infty\mid\mathcal G_j\}\le\alpha_j.
\]
If the strong null is understood instead as a condition holding almost surely under the conditional law, the same result follows directly from the untruncated wealth; the truncation also covers pathwise null truth.

Suppose \(j\) uses the weak-null test. Let \(C_j=\{\mu_{j,n}\in[L_{j,n},U_{j,n}]\text{ for every }n\}\). The stated conditional guarantee gives \(\Pr(C_j^c\mid\mathcal G_j)\le\alpha_j\). If the weak null is true and \(C_j\) holds, then \(L_{j,n}\le\mu_{j,n}\le0\le m_j\) at every \(n\), so no commitment occurs. Hence
\[
\Pr\{\text{weak null true and }\tau_j<\infty\mid\mathcal G_j\}\le\alpha_j.
\]
This argument uses the confidence-sequence coverage assumed in the public setup; it does not require validity of any particular proposed radius formula.

Let \(A_j\) be the event that \(j\) is instantiated, its preselected tested null is true, and it commits. The appropriate conditional bound, followed by the tower property and the convention \(\alpha_j=0\) off instantiation, yields \(\Pr(A_j)\le\mathbb E[\alpha_j]\). Since \(I\) is fixed and countable, countable subadditivity and monotone convergence give
\[
\Pr\left(\bigcup_{j\in I}A_j\right)
\le\sum_{j\in I}\Pr(A_j)
\le\sum_{j\in I}\mathbb E[\alpha_j]
=\mathbb E\left[\sum_{j\in I}\alpha_j\right]
\le\alpha.
\]
The union includes every false commitment, regardless of later tree growth or the times at which tests are inspected.
