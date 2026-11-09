# Reference Proof

## Proof Structure and Obligations

The proof must establish: (1) the expectation-level row-swap identity under the selected-coordinate kernel and conditional row exchangeability; (2) the square-root correlation bound with scalar conditional mutual information; (3) conditional data processing and aggregation across rounds; (4) the bounded signed-variable exponential-moment estimate and its Bernstein envelope; and (5) application to excess losses, exact absorption, and the zero-excess case. Each obligation is discharged below. The only information-theoretic results invoked without proof are the standard variational inequality and conditional data processing, recorded privately in theory_025 with their relevant statements.

Throughout, write \(\varepsilon_t=1-2U_t\), consistently with the public convention \(\operatorname{Err}_n^{\rm seq}=R_n^{\rm tr}-R_n^{\rm ho}\). All information quantities use natural logarithms.

## 1. Row-swap identity

Fix a round \(t\). Predictability gives a measurable version \(Q_t=q_t(H_{t-1})\). Define
\[
\varphi_t(h,z,\bar z)=q_t(h)\int\ell(w,\bar z)K_t(dw\mid h,z).
\]
The regular conditional laws exist by the standard-Borel setup, and this integral is measurable and bounded. Abbreviate \(\varphi_{ij}=\varphi_t(H_{t-1},Z_{t,i},Z_{t,j})\). Conditional fairness and the selected-coordinate kernel give
\[
\mathbb E[Q_t\ell(W_t,Z_{t,U_t})]=\tfrac12\mathbb E[\varphi_{00}+\varphi_{11}],
\qquad
\mathbb E[Q_t\ell(W_t,Z_{t,1-U_t})]=\tfrac12\mathbb E[\varphi_{01}+\varphi_{10}].
\]
Conditional row exchangeability, followed by averaging over the history, gives
\[
\mathbb E\varphi_{00}=\mathbb E\varphi_{11},\qquad
\mathbb E\varphi_{01}=\mathbb E\varphi_{10}.
\]
Consequently the selected-minus-ghost expectation is \(\mathbb E[\varphi_{00}-\varphi_{10}]\). On the other hand, averaging over the fair selector yields
\[
2\mathbb E[\varepsilon_t L_t^+]=\mathbb E[\varphi_{00}-\varphi_{10}].
\]
Summing and using the tower property proves
\[
\operatorname{Err}_n^{\rm seq}
=\frac2n\sum_{t=1}^n\mathbb E[\varepsilon_tL_t^+]
=\frac2n\sum_{t=1}^n\mathbb E\!\left[\mathbb E[\varepsilon_tL_t^+\mid G_{t-1}]\right].
\]
The row exchangeability step is an equality after averaging over the row, not an assertion of symmetry after a particular ordered row has been fixed.

The same calculation applies to the measurable signed loss \(\ell(w,z)-\ell(w^\star,z)\): the comparator is fixed, the update kernel is unchanged, and all terms are integrable. Thus, for the excess risks,
\[
R_n^{\rm tr}-R_n^{\rm ho}=\frac2n\sum_{t=1}^n\mathbb E[\varepsilon_t e_{t,0}].
\]

## 2. Variational inequality and scalar conditional information

For probability laws \(P,Q\) and bounded measurable \(f\), the standard variational inequality states
\[
\mathbb E_P f\leq D(P\Vert Q)+\log\mathbb E_Q e^f.
\]
Apply it under the regular conditional law given \(G_{t-1}\). For a bounded real variable \(X\), let \(P_g\) be the conditional joint law of \((X,U_t)\), let \(Q_g=P_{X\mid g}\otimes\operatorname{Unif}\{0,1\}\), and write \(d_X(g)=D(P_g\Vert Q_g)\). Conditional fairness makes \(Q_g\) the product of the conditional marginals. By definition,
\[
\mathbb E[d_X(G_{t-1})]=I(X;U_t\mid G_{t-1}).
\]
Under \(Q_g\), the sign \(\varepsilon'_t=1-2U'_t\) is independent of \(X\) and fair. In particular, \(d_X(G_{t-1})\), rather than scalar CMI, is the divergence that appears in a pointwise conditional inequality.

## 3. Slow-rate bound

Suppose \(0\leq X\leq1\), set \(m=\mathbb E[\varepsilon_tX]\), and choose a deterministic \(s\in\{-1,1\}\) with \(sm=|m|\). For \(a>0\), use \(f(x,u)=sa(1-2u)x\). This is bounded. Under the product reference law,
\[
\mathbb E_{Q_g}e^{sa\varepsilon'_tX}=\mathbb E[\cosh(aX)\mid G_{t-1}=g]\leq e^{a^2/2}.
\]
For completeness, \(\log\cosh y\leq y^2/2\): for \(y\geq0\), \(\tanh y\leq y\), so integration gives the inequality, and both sides are even. Here \(|X|\leq1\) supplies the final uniform bound.

Average the conditional variational inequality over \(g\). It gives
\[
a|m|\leq I(X;U_t\mid G_{t-1})+a^2/2.
\]
If the information is positive and finite, choose \(a=\sqrt{2I(X;U_t\mid G_{t-1})}\); if it is zero, let \(a\downarrow0\). An infinite information value makes the desired inequality immediate. Therefore
\[
|\mathbb E[\varepsilon_tX]|\leq\sqrt{2I(X;U_t\mid G_{t-1})}.
\]
Applying this to \(X=L_t^+\), using the row-swap identity and the triangle inequality, yields
\[
|\operatorname{Err}_n^{\rm seq}|\leq\frac2n\sum_{t=1}^n\sqrt{2I(L_t^+;U_t\mid G_{t-1})}.
\]
The standard conditional data-processing inequality states that \(I(X;U\mid G)\leq I(Y;U\mid G)\) whenever \(X\) is a measurable function of \((Y,G)\). Here \(Q_t\) and \(Z_{t,0}\) are \(G_{t-1}\)-measurable and the loss is measurable, so
\[
I(L_t^+;U_t\mid G_{t-1})\leq I(W_t;U_t\mid G_{t-1}).
\]
Finally, finite-sum Cauchy--Schwarz gives
\[
\frac2n\sum_{t=1}^n\sqrt{2I(W_t;U_t\mid G_{t-1})}
\leq2\sqrt{\frac2n\sum_{t=1}^nI(W_t;U_t\mid G_{t-1})}.
\]
These inequalities also hold when all weights vanish or when \(n=1\).

## 4. Bennett--Bernstein estimate

Assume \(b>0\), \(|X|\leq b\), and \(0<\lambda<3/b\). Set
\[
\psi_b(\lambda)=\frac{e^{\lambda b}-\lambda b-1}{b^2}.
\]
The exponential remainder has the integral representation
\[
e^v-v-1=v^2\int_0^1(1-r)e^{rv}\,dr.
\]
The integral on the right is increasing as a function of \(v\). Hence, for \(|y|\leq b\),
\[
e^{\lambda y}\leq1+\lambda y+\psi_b(\lambda)y^2.
\]
Under \(Q_g\), take \(Y=-\varepsilon'_tX\). Its conditional mean is zero, its absolute value is at most \(b\), and its square is \(X^2\). Thus
\[
\mathbb E_{Q_g}e^{-\lambda\varepsilon'_tX}
\leq1+\psi_b(\lambda)\mathbb E[X^2\mid G_{t-1}=g]
\leq\exp\{\psi_b(\lambda)\mathbb E[X^2\mid G_{t-1}=g]\}.
\]
Use the bounded test function \(f(x,u)=-\lambda(1-2u)x\) in the conditional variational inequality and average over \(g\). This proves
\[
-\lambda\mathbb E[\varepsilon_tX]
\leq I(X;U_t\mid G_{t-1})+\psi_b(\lambda)\mathbb E[X^2].
\]
This is equivalently the positive-sign bound applied to \(-X\); negation preserves information because it is a measurable bijection.

To verify the scalar envelope, for \(0\leq u<3\) set
\[
F(u)=\frac{u^2}{2(1-u/3)}-(e^u-u-1).
\]
Then \(F(0)=F'(0)=0\) and
\[
F''(u)=(1-u/3)^{-3}-e^u\geq0,
\]
because \(-3\log(1-u/3)\geq u\). Thus \(F(u)\geq0\), and substitution of \(u=\lambda b\) gives
\[
\psi_b(\lambda)\leq\frac{\lambda^2}{2(1-\lambda b/3)}.
\]

## 5. Excess risks and absorption

For \(b>0\), apply the preceding signed inequality to \(X=e_{t,0}\), sum over rounds, and use the excess row-swap identity. This yields
\[
R_n^{\rm ho}-R_n^{\rm tr}
\leq\frac{2}{\lambda n}\sum_{t=1}^n I(e_{t,0};U_t\mid G_{t-1})
+\frac{2\psi_b(\lambda)}{\lambda}\frac1n\sum_{t=1}^n\mathbb E[e_{t,0}^2].
\]
The tower property identifies the second-moment average with the average in the public assumption. The scalar envelope and that assumption therefore give
\[
R_n^{\rm ho}-R_n^{\rm tr}
\leq\frac{2}{\lambda n}\sum_{t=1}^n I(e_{t,0};U_t\mid G_{t-1})
+\frac{B\lambda}{1-\lambda b/3}R_n^{\rm ho}.
\]
Moving the final term to the left gives exactly
\[
\left(1-\frac{B\lambda}{1-\lambda b/3}\right)R_n^{\rm ho}
\leq R_n^{\rm tr}+\frac{2}{\lambda n}\sum_{t=1}^nI(e_{t,0};U_t\mid G_{t-1}).
\]
The task restricts to parameters for which the displayed left coefficient is positive. Since \(B>0\) and \(b>0\), this parameter range is nonempty; it is equivalent to \(0<\lambda<1/(B+b/3)\).

If \(b=0\), every \(e_{t,u}\) vanishes almost surely. Both excess risks and all evaluated-excess information terms are zero. This proves the separate degenerate conclusion without evaluating \(3/b\). No unresolved proof obligation remains.
