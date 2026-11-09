# Reference Proof

## Audited obligations and source corrections

The proof must establish: (i) wedge concentration, including diagonal wedges; (ii) the operator subspace estimate and Procrustes alignment; (iii) the row-wise estimate through an actual independent leave-one-out argument; (iv) projector delocalization; (v) conditional projected-noise concentration and its Frobenius conversion; and (vi) projection bias and the final simultaneous probability. All six obligations are proved below.

The source's principal-angle formulas contain incorrect powers. Its fixed-matrix row-variance estimate is also too small in general, and its printed final row-wise calculation gives a κ^4 rate rather than the stated κ^2 rate. We use the corrected elementary principal-angle formulas, a maximum-row Bernstein estimate, and the same eigenvector equations projected onto the orthogonal complement of the signal space. These local repairs preserve the original assumptions and targets. Leave-one-out matrices remove centered perturbations, not the underlying signal. The projected-noise probability is conditional on the wedge samples. The tensor-product telescoping expansion includes preceding projection factors.

## 1. Background results and notation

All unqualified matrix norms are operator norms. Write
\[
S=AA^\top,
\quad P=UU^\top,
\quad \Delta=Z-S,
\quad \lambda=\sigma_r^2,
\quad \alpha=\frac{\mu_1\mu_2r^2}{mn},
\quad \eta=\sqrt{\frac{a\alpha\log n}{p}},
\quad \tau=\kappa^2\eta.
\]
The sampling condition implies \(\tau\le C_0^{-1/2}\). All choices of a sufficiently large \(C_0\) below are universal.

We use the following audited standard results.

**Matrix Bernstein.** For independent centered rectangular matrices \(X_j\), assume \(\|X_j\|\le B\) almost surely and
\[
v\ge\max\left\{\left\|\sum_j\mathbb E X_jX_j^\top\right\|,
\left\|\sum_j\mathbb E X_j^\top X_j\right\|\right\}.
\]
For \(t\ge2\log(d_1+d_2)\),
\[
\left\|\sum_jX_j\right\|\le C(\sqrt{vt}+Bt)
\]
except with probability at most \(e^{-t}\). This is the source's Bernstein statement with its confidence parameter set to \(t/\log(d_1+d_2)\). We also apply it conditionally, verifying conditional independence and the same bounds.

**Residual Davis–Kahan.** If a symmetric matrix \(M\) has top-\(r\) gap \(\delta>0\), \(\widehat M=M+E\), and \(\|E\|\le\delta/2\), then the top-\(r\) projectors satisfy
\[
\|\widehat P-P_M\|\le\frac{2\|EU_M\|}{\delta}\le\frac{2\|E\|}{\delta}.
\]
We use this only when \(r<n\).

**Alignment facts.** For orthonormal bases \(B,C\), let \(H=B^\top C=L\operatorname{diag}(\cos\theta_j)V^\top\), and set \(R=LV^\top\). Maximizing \(\operatorname{tr}(O^\top H)\) shows that \(R\) minimizes \(\|BO-C\|_F\). Principal two-dimensional planes give
\[
\|BB^\top-CC^\top\|=\max_j\sin\theta_j=:s.
\]
Also \(H^\top R=(H^\top H)^{1/2}\), so
\[
\|H-R\|\le s^2,
\qquad \|C^\top BR-I\|\le s^2.
\]
Since
\[
(BR-C)^\top(BR-C)=2[I-(H^\top H)^{1/2}],
\]
we obtain \(\|BR-C\|\le\sqrt2s\). In Frobenius norm the corresponding relations are \(\|BB^\top-CC^\top\|_F=\sqrt2\|\sin\Theta\|_F\) and \(\|BR-C\|_F\le\sqrt2\|\sin\Theta\|_F\), not a dimension-free equivalence with the operator norm.

The incoherence assumptions and the SVD imply
\[
\max_i\|A_{i,:}\|_2^2\le\frac{\mu_1r}{n}\sigma_1^2,
\qquad
\max_\ell\|A_{:,\ell}\|_2^2\le\frac{\mu_2r}{m}\sigma_1^2,
\qquad
\|A\|_{\max}\le\sqrt\alpha\,\sigma_1.
\]
Indeed, apply the singular-vector row bounds to \(e_i^TU\Sigma V^T\), its transpose, and \(e_i^TU\Sigma V^Te_\ell\), respectively. In particular, \(\|A\circ A\|_{\max}\le\alpha\sigma_1^2\). Orthonormality also implies \(\mu_1,\mu_2\ge1\).

## 2. Wedge concentration and operator accuracy

For \(i<j\), define
\[
X_{i\ell j}=(\delta_{i\ell j}/p-1)A_{i\ell}A_{j\ell}(e_ie_j^\top+e_je_i^\top),
\]
and for \(i=j\), define
\[
X_{i\ell i}=(\delta_{i\ell i}/p-1)A_{i\ell}^2e_ie_i^\top.
\]
These matrices are independent, centered, and sum to \(\Delta\). Thus \(\mathbb EZ=S\). Every summand has norm at most
\[
L=\frac{\alpha\sigma_1^2}{p}.
\]
Their squared expectations sum to the diagonal matrix whose \(i\)-th diagonal entry is
\[
\frac{1-p}{p}\sum_{j,\ell}A_{i\ell}^2A_{j\ell}^2.
\]
Using row and column energies,
\[
\sum_{j,\ell}A_{i\ell}^2A_{j\ell}^2
\le\left(\sum_\ell A_{i\ell}^2\right)
\max_\ell\sum_jA_{j\ell}^2
\le\alpha\sigma_1^4.
\]
Hence a variance bound is \(v=\alpha\sigma_1^4/p\).

Use Bernstein with \(t=(a+4)\log(2n)\). Since \(a\ge2\) and \(n\ge2\), this parameter is at most \(6a\log n\). Except with probability at most \((2n)^{-(a+4)}\),
\[
\|\Delta\|\le C\sigma_1^2(\eta+\eta^2)\le C\sigma_1^2\eta.
\]
Choose \(C_0\) large enough that on this event
\[
e:=\|\Delta\|\le\lambda/16.
\]

If \(r<n\), the population gap is \(\lambda\). Davis–Kahan and the alignment facts give
\[
s:=\|Q-P\|\le C\tau,
\qquad
\|\widehat UR-U\|\le C\tau,
\]
where \(R\) is the Frobenius Procrustes minimizer. The estimated top eigenvalues are at least \(\lambda-e\), and the remaining eigenvalues are at most \(e\).

If \(r=n\), then \(P=Q=I\), and \(R=\widehat U^TU\) gives \(\widehat UR=U\) exactly. Both subspace targets are therefore immediate. We prove the row-wise estimate below for \(r<n\), and return to all ranks in the denoising argument.

## 3. The leave-one-out row-wise estimate

Set \(D_i=I-e_ie_i^\top\), and define
\[
\Delta^{(i)}=D_i\Delta D_i,
\qquad Z^{(i)}=S+\Delta^{(i)},
\qquad E_i=\Delta-\Delta^{(i)}.
\]
Let \(\widehat U^{(i)}\) be a top-\(r\) orthonormal eigenbasis of \(Z^{(i)}\), chosen using only that matrix. It is independent of all wedge indicators incident to row \(i\). Crucially, the deterministic signal \(S\) is retained. Since \(\|\Delta^{(i)}\|\le e\), its top-\(r\) gap is at least \(\lambda-2e\).

### Incident-row Bernstein estimates

Fix \(i\), and let \(F\in\mathbb R^{n\times r}\) be independent of the incident wedges. Conditional on \(F\), put \(f_F=\|F\|_{2,\infty}\). Write
\[
b_{j\ell}=(\delta_{i\ell j}/p-1)A_{i\ell}A_{j\ell}.
\]
The row vector \(e_i^T\Delta F\) is the sum of independent centered vectors \(b_{j\ell}F_{j,:}\). Each has norm at most \(Lf_F\). Both variance parameters are bounded by the sum of expected squared Euclidean norms, which is at most
\[
\frac1p\sum_{j,\ell}A_{i\ell}^2A_{j\ell}^2\|F_{j,:}\|_2^2
\le vf_F^2.
\]

For \(E_iF\), the off-diagonal summands are
\[
b_{j\ell}(e_iF_{j,:}+e_jF_{i,:}),\qquad j\ne i,
\]
and diagonal summands are \(b_{i\ell}e_iF_{i,:}\). Their norms are at most \(2Lf_F\). The sum of their expected squared Frobenius norms is at most \(2vf_F^2\), which bounds both matrix variance parameters.

Bernstein, again with \(t=(a+4)\log(2n)\), therefore yields
\[
\|e_i^T\Delta F\|_2\le C\sigma_1^2\eta f_F,
\qquad
\|E_iF\|\le C\sigma_1^2\eta f_F,
\tag{1}
\]
with conditional failure probability at most \(2(2n)^{-(a+4)}\). Here the dimensions are at most \(n\times r\), \(r\le n\), and \(\eta\le1\). The case \(f_F=0\) is immediate. These bounds use maximum row norms; no unsupported replacement by \(\|F\|_F/\sqrt n\) is made.

Apply (1) conditionally with \(F=\widehat U^{(i)}\), then integrate and take a union bound over \(i\). Together with wedge concentration, all these estimates hold with probability at least \(1-Cn^{-a}\).

### Comparison with the leave-one-out bases

Write
\[
f=\|\widehat U\|_{2,\infty},
\qquad f_i=\|\widehat U^{(i)}\|_{2,\infty}.
\]
We have \(\|E_i\|\le2e\le(\lambda-2e)/2\). Thus residual Davis–Kahan applies to \(Z^{(i)}\) and \(Z=Z^{(i)}+E_i\). The alignment facts provide an orthogonal \(O_i\) for which
\[
d_i:=\|\widehat U-\widehat U^{(i)}O_i\|
\le\frac{C}{\lambda}\|E_i\widehat U^{(i)}\|
\le C\tau f_i.
\]
Row norms are unchanged by right orthogonal multiplication, so \(f_i\le f+d_i\). Taking \(C_0\) sufficiently large to ensure \(C\tau\le1/2\), we obtain
\[
f_i\le2f,
\qquad d_i\le C\tau f.
\tag{2}
\]
For each row,
\[
\begin{aligned}
\|e_i^T\Delta\widehat U\|_2
&\le\|e_i^T\Delta\widehat U^{(i)}O_i\|_2
 +\|e_i^T\Delta\|_2d_i\\
&\le C\sigma_1^2\eta f_i+ed_i
\le C\sigma_1^2\eta f,
\end{aligned}
\]
where (1), (2), and boundedness of \(\tau\) were used. Consequently,
\[
\|\Delta\widehat U\|_{2,\infty}\le C\sigma_1^2\eta f.
\tag{3}
\]

### Closing the aligned row error

Let \(u=\|U\|_{2,\infty}\), and let \(\widehat\Lambda\) contain the selected eigenvalues of \(Z\). Since \((I-P)S=0\), its eigenvector equation gives the exact identity
\[
(I-P)\widehat U\widehat\Lambda=(I-P)\Delta\widehat U.
\]
The inverse eigenvalue bound is \(\|\widehat\Lambda^{-1}\|\le2/\lambda\). For each row,
\[
\|e_i^TP\Delta\widehat U\|_2
\le\|e_i^TU\|_2\|U^T\Delta\widehat U\|
\le ue.
\]
Combining this with (3),
\[
\|(I-P)\widehat U\|_{2,\infty}\le C\tau(f+u).
\tag{4}
\]
For the same Procrustes minimizer \(R\) used in the operator estimate, decompose
\[
\widehat UR-U=(I-P)\widehat UR+U(U^T\widehat UR-I).
\]
The second term has row norm at most \(us^2\le C\tau^2u\), by the alignment facts. Thus, with \(x=\|\widehat UR-U\|_{2,\infty}\),
\[
x\le C\tau(f+u)+C\tau^2u
\le C\tau x+C\tau u+C\tau^2u,
\]
because \(f\le u+x\). A further universal enlargement of \(C_0\) absorbs the \(x\)-term and gives
\[
\|\widehat UR-U\|_{2,\infty}\le C\kappa^2\eta\|U\|_{2,\infty}.
\]
This proves the claimed row-wise rate with its stated condition-number dependence.

Choose \(C_0\) large enough also that \(x\le u\). Then
\[
\|Q\|_{2,\infty}=\|\widehat U\|_{2,\infty}
\le2u\le2\sqrt{\mu_1r/n}
\le2\kappa^2\sqrt{\mu_1r/n}.
\tag{5}
\]
For \(r=n\), (5) holds directly since \(Q=I\) and \(\mu_1,\kappa\ge1\). The fixed numerical factor 2 is important: no unspecified constant is raised to the \(k\)-th power.

## 4. Projection bias

Let \(K=Q^{\otimes(k-1)}\), and set
\[
T^*=\operatorname{fold}(QAK),
\qquad \widehat T=\operatorname{fold}(QYK).
\]
For \(d=k-1\), the correct telescoping identity is
\[
I^{\otimes d}-Q^{\otimes d}
=\sum_{h=1}^dQ^{\otimes(h-1)}\otimes(I-Q)\otimes I^{\otimes(d-h)}.
\]
Apply this identity to \(A-QAK\), including its left-factor error. The other mode factors are contractions in Frobenius norm. Symmetry identifies every unprojected one-mode error with \(\|(I-Q)A\|_F\), up to reindexing. Therefore
\[
\|T-T^*\|_F\le k\|(I-Q)A\|_F
\le k\sqrt r\|(I-Q)A\|
\le k\sqrt r\|(I-Q)U\|\|A\|.
\]
The operator subspace estimate, \(m=n^{k-1}\), and \(\|A\|\le\|T\|_F\) give
\[
\|T-T^*\|_F
\le Ck\sqrt r\,\kappa^2
\sqrt{\frac{a\mu_1\mu_2r^2\log n}{pn^k}}\,\|T\|_F.
\tag{6}
\]
When \(r=n\), this bias is zero, so the same bound holds.

## 5. Conditional projected sampling concentration

Condition on the entire wedge sample. The projector \(Q\) is now fixed and the independent entry indicators \(\xi_{i\ell}\) remain independent Bernoulli-\(q\) variables. Put \(\beta=\|Q\|_{2,\infty}\). Then
\[
M:=Q(Y-A)K
=\sum_{i,\ell}(\xi_{i\ell}/q-1)A_{i\ell}(Qe_i)(Ke_\ell)^T.
\]
These are conditionally independent centered rank-one matrices. If \(\ell\) corresponds to \((i_2,\ldots,i_k)\), then
\[
\|Ke_\ell\|_2=\prod_{h=2}^k\|Qe_{i_h}\|_2\le\beta^{k-1}.
\]
Every summand consequently has norm at most
\[
B_q=q^{-1}\|A\|_{\max}\beta^k
\le q^{-1}r\sigma_1\sqrt{\frac{\mu_1\mu_2}{n^k}}\,\beta^k.
\]
Each of the two variance matrices is bounded in norm by the sum of expected squared Frobenius norms. Thus
\[
v_q\le q^{-1}\sum_{i,\ell}A_{i\ell}^2\beta^{2k}
\le q^{-1}n^k\|A\|_{\max}^2\beta^{2k}
\le q^{-1}\mu_1\mu_2r^2\sigma_1^2\beta^{2k}.
\]
Bernstein with \(t=a\log(n+m)\), where
\[
\log(n+m)\le2(k-1)\log n,
\]
gives, conditionally with failure probability at most \((n+m)^{-a}\le n^{-a(k-1)}\),
\[
\|M\|\le Cr\sigma_1\beta^k\sqrt{\mu_1\mu_2}
\left[\sqrt{\frac{a(k-1)\log n}{q}}
+\frac{a(k-1)\log n}{q n^{k/2}}\right].
\]
Because \(q\ge a(k-1)\log n/n^k\), the second term in brackets is at most the first. Also \(\operatorname{rank}(M)\le r\), so \(\|M\|_F\le\sqrt r\|M\|\). On the good wedge event, substitute (5) and use \(\sigma_1\le\|T\|_F\). This yields
\[
\|T^*-\widehat T\|_F
\le C2^k r^{3/2+k/2}\kappa^{2k}
\sqrt{\frac{a(k-1)\mu_1^{k+1}\mu_2\log n}{qn^k}}\,\|T\|_F.
\tag{7}
\]
The conditional probability assertion holds for every wedge realization; the substituted bound holds jointly with the good wedge event. It is not assigned an unconditional failure probability of only \(n^{-a(k-1)}\).

## 6. Final probability and conclusion

The wedge concentration and all leave-one-out estimates hold simultaneously with failure probability at most \(Cn^{-a}\): there are at most \(2n+1\) applications with failure probability bounded by \((2n)^{-(a+4)}\). Integrating the conditional denoising failure bound adds at most \(n^{-a(k-1)}\le n^{-a}\), since \(k\ge2\). No independence between the derived good events is required.

The two aligned subspace estimates therefore hold simultaneously with (6) and (7), with probability at least \(1-cn^{-a}\). Adding (6) and (7) proves
\[
\|T-\widehat T\|_F\le C\left[
 k\sqrt r\,\kappa^2\sqrt{\frac{a\mu_1\mu_2r^2\log n}{pn^k}}
 +2^k r^{3/2+k/2}\kappa^{2k}
 \sqrt{\frac{a(k-1)\mu_1^{k+1}\mu_2\log n}{qn^k}}
\right]\|T\|_F.
\]
The constants are universal, including with respect to \(k\) and \(a\). Cases \(p=1\) or \(q=1\) have the relevant centered noise identically zero and are covered. If a stated lower sampling bound exceeds one, there is no admissible sampling rate and the implication is vacuous. No proof obligation remains unresolved.
