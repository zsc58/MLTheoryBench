# Reference Proof

## Proof Structure and Obligations

The proof establishes: (i) population score centering and the pooled-to-target discrepancy; (ii) the two score bounds and a uniform entrywise Hessian bound; (iii) the shifted-cone pooled estimator bounds, including tolerance absorption and the minimum term; (iv) the target correction bounds, with its effective support, localization, and tolerance checked explicitly; and (v) the final rates on one common high-probability event. The only imported probabilistic result is the independent bounded-variable inequality stated below. No specialized transfer-learning or nonconvex-optimization theorem is used as a black box.

Write
\[
\Delta_w=\widehat w-w^\circ,\qquad v=\widehat d-d^\circ,
\qquad q_P=\frac{\log p}{N},\qquad q_0=\frac{\log p}{n_0}.
\]
Constants may change from line to line and depend only on the fixed constants in the public task. All deterministic asymptotic bounds below hold for sufficiently large indices.

## 1. Population discrepancy

The specified Ising normalization gives, in domain \(r\),
\[
\mathbb P_r(X_j=1\mid X_{-j})
=\sigma\!\left(2\sum_{k\ne j}\Theta^{(r)}_{jk}X_k\right),
\qquad \sigma(t)=(1+e^{-t})^{-1}.
\]
To verify score centering explicitly, let \(\beta\) be the true nodewise vector in that domain, set \(\eta=2X_{-j}^T\beta\), and put \(\pi=\sigma(\eta)\). Since \(f'(t)=\sigma(t)-1\), the coordinate score is
\[
2X_jX_k\{\sigma(X_j\eta)-1\}.
\]
Conditional on \(X_{-j}\), its expectation is
\[
2X_k\{\pi(\pi-1)+(1-\pi)\pi\}=0.
\]
Population risks are smooth finite sums, so differentiation and expectation commute. Convexity and the preceding calculation give
\[
\nabla L_0(\vartheta)=0,\qquad
\nabla L_r(b^{(r)})=0\quad(r\in\mathcal A).
\]
The unrestricted population minimizer also satisfies \(\nabla L_P(w^\circ)=0\).

Use the averaged Hessians defined in the task, with
\[
H_r=\overline H_r[b^{(r)},\vartheta],\qquad
H_P=\overline H_P[\vartheta,w^\circ].
\]
The endpoints lie in \(\mathcal U\), and its convexity contains the segments. Integral Taylor expansion gives
\[
\nabla L_r(\vartheta)=H_r(\vartheta-b^{(r)}),
\qquad
0=\nabla L_P(\vartheta)+H_P(w^\circ-\vartheta).
\]
The target contribution to \(\nabla L_P(\vartheta)\) is zero. Therefore
\[
w^\circ-\vartheta
=-H_P^{-1}\sum_{r\in\mathcal A}\alpha_r H_r(\vartheta-b^{(r)}).
\]
Invertibility and integrated comparability apply to precisely these averages. Consequently,
\[
\|d^\circ\|_1=\|w^\circ-\vartheta\|_1
\le C_H\sum_{r\in\mathcal A}\alpha_r\|\vartheta-b^{(r)}\|_1
\le C_Hh.
\]
In particular, since \(\vartheta_{S^c}=0\),
\[
B:=\|(w^\circ)_{S^c}\|_1\le\|d^\circ\|_1\le C_hh. \tag{1}
\]
The last bound is also directly available from the stated choice of \(C_h\). When \(\mathcal A\) is empty, the displayed sum is zero and the same argument gives \(w^\circ=\vartheta\).

## 2. Scores and Hessians

The bounded-variable inequality used here is the following form of Hoeffding's inequality: if \(Y_1,\ldots,Y_m\) are independent, each taking values in \([-2,2]\), then, without any identical-distribution requirement,
\[
\mathbb P\!\left(\left|\frac1m\sum_{i=1}^m(Y_i-\mathbb EY_i)\right|\ge t\right)
\le2\exp(-mt^2/8),\qquad t>0. \tag{2}
\]
This is the standard independent concentration input indexed by theory_025 and used in the source's score-concentration proof.

For any fixed nodewise vector \(u\), each coordinate of a single-observation score is \(z_k f'(z^Tu)\), whose absolute value is at most two. The target score at \(\vartheta\) is centered by Section 1. The pooled score at \(w^\circ\) is an average of \(N\) independent such contributions because \(\alpha_r/n_r=1/N\). Its domain-specific means need not vanish, but their total sum does vanish by \(\nabla L_P(w^\circ)=0\). Thus (2) applies to the centered pooled sum as well as to the target sum. The evaluation vectors and source set are population quantities fixed independently of the samples.

Applying (2) at \(t=A\sqrt{\log p/m}\), taking a union bound over at most \(p-1\) coordinates, and then over the two scores, gives an event \(\mathcal H\) with
\[
\mathbb P(\mathcal H)\ge1-4p^{-c},\qquad c=A^2/8-1>0,
\]
on which
\[
\|\nabla\ell_0(\vartheta)\|_\infty\le A\sqrt{q_0},
\qquad
\|\nabla\ell_P(w^\circ)\|_\infty\le A\sqrt{q_P}. \tag{3}
\]
Choose the fixed \(C_w\) sufficiently large that \(C_w\ge2A\).

For every empirical domain loss and all \(u\),
\[
[\nabla^2\ell_r(u)]_{k\ell}
=\frac1{n_r}\sum_i f''((z_i^{(r)})^Tu)z_{ik}^{(r)}z_{i\ell}^{(r)}.
\]
Because \(0\le f''\le1/4\) and \(|z_{ik}^{(r)}z_{i\ell}^{(r)}|=4\),
\[
\|\nabla^2\ell_r(u)\|_{\max}\le1,
\qquad \|H\|_{\max}:=\max_{k,\ell}|H_{k\ell}|.
\]
Integration along a segment consequently gives
\[
\|\nabla\ell_r(u)-\nabla\ell_r(v)\|_\infty
\le\|u-v\|_1. \tag{4}
\]
Averaging and taking expectations give the same entrywise Hessian and gradient bounds for the pooled and population losses. This is a bounded-Hessian argument yielding gradient Lipschitz control, not an assumption of Hessian Lipschitz continuity.

In the remaining sections, work on the intersection of \(\mathcal H\) with the event \(\mathcal E\) on which (E1)–(E4) hold. No independence between these events is needed.

## 3. Pooled initializer

Set \(\Delta=\Delta_w\), \(x=\|\Delta\|_2\), and \(\lambda_w=\lambda_w\). Define the convex loss remainder
\[
R_P=\ell_P(w^\circ+\Delta)-\ell_P(w^\circ)
-\langle\nabla\ell_P(w^\circ),\Delta\rangle\ge0.
\]
Optimality of \(\widehat w\), decomposability of the \(\ell_1\) norm, and (3) yield
\[
R_P\le\lambda_w\bigl(\|w^\circ\|_1-\|w^\circ+\Delta\|_1\bigr)
-\langle\nabla\ell_P(w^\circ),\Delta\rangle
\]
and
\[
\|w^\circ\|_1-\|w^\circ+\Delta\|_1
\le\|\Delta_S\|_1-\|\Delta_{S^c}\|_1+2B.
\]
Since \(\|\nabla\ell_P(w^\circ)\|_\infty\le\lambda_w/2\), it follows that
\[
0\le R_P\le
\frac{3\lambda_w}{2}\|\Delta_S\|_1
-\frac{\lambda_w}{2}\|\Delta_{S^c}\|_1+2\lambda_wB.
\]
Hence
\[
\|\Delta_{S^c}\|_1\le3\|\Delta_S\|_1+4B,
\qquad
\|\Delta\|_1\le4\sqrt{s}\,x+4B. \tag{5}
\]
This also holds when \(s=0\).

Localization in (E1) places the segment from \(w^\circ\) to \(\widehat w\) in its stated neighborhood. Applying (E1) to \(\Delta\), which satisfies (5), and integrating the Hessian remainder gives
\[
R_P\ge\frac{\kappa_P}{2}x^2-\tau_P q_P\|\Delta\|_1^2.
\]
We have harmlessly enlarged the negative tolerance relative to its exact integral coefficient. Dropping the nonpositive off-support term in the preceding upper bound gives
\[
\frac{\kappa_P}{2}x^2
\le\frac{3\lambda_w}{2}\sqrt{s}\,x+2\lambda_wB
+\tau_Pq_P\|\Delta\|_1^2. \tag{6}
\]
From (5),
\[
\|\Delta\|_1^2\le32s x^2+32B^2.
\]
The coefficient \(32\tau_Ps q_P\) is \(o(1)\). Also, by (1) and \(q_Ph^2=o(1)\),
\[
\sqrt{q_P}\,B=o(1),\qquad
q_PB^2=\frac{\sqrt{q_P}\,B}{C_w}\lambda_wB=o(\lambda_wB)
\]
when \(B>0\); both terms are zero if \(B=0\). Absorbing the quadratic coefficient in (6) therefore yields
\[
x^2\le C\bigl(\lambda_w\sqrt{s}\,x+\lambda_wB\bigr).
\]
An elementary quadratic estimate gives
\[
x\le C\bigl(\lambda_w\sqrt{s}+\sqrt{\lambda_wB}\bigr). \tag{7}
\]
The minimum term follows with all support cases accounted for. If \(B\ge\lambda_w\), then \(\sqrt{\lambda_wB}\le B\). If \(B<\lambda_w\) and \(s\ge1\), the square-root term in (7) is at most \(\lambda_w\le\lambda_w\sqrt{s}\), so it can be absorbed into the leading term. If \(s=0\), (5) additionally gives \(x\le\|\Delta\|_1\le4B\); combining this with (7) gives the smaller of the two bounds. Thus in all cases,
\[
\|\Delta_w\|_2
\le C\bigl(\lambda_w\sqrt{s}+\min\{\sqrt{\lambda_wB},B\}\bigr). \tag{8}
\]
For the \(\ell_1\) bound, (5) and (7), followed by \(2\sqrt{uv}\le u+v\), give
\[
\|\Delta_w\|_1
\le C\bigl(s\lambda_w+\sqrt{s\lambda_wB}+B\bigr)
\le C\bigl(s\lambda_w+B\bigr). \tag{9}
\]
Using \(B\le C_hh\) and the tuning choice, (8)–(9) become
\[
\|\Delta_w\|_2
\le C\left[\sqrt{\frac{s\log p}{N}}
+\min\left\{\left(\frac{\log p}{N}\right)^{1/4}h^{1/2},h\right\}\right], \tag{10}
\]
\[
\|\Delta_w\|_1
\le C\left(s\sqrt{\frac{\log p}{N}}+h\right)
\le CK\lambda_d. \tag{11}
\]
The constants in replacing \(B\) by \(h\) and \(\lambda_w\) by \(C_w\sqrt{q_P}\) are fixed. No exact sparsity of \(w^\circ\) was used.

## 4. Target-only correction

Put
\[
\theta^\dagger=\widehat w+d^\circ=\vartheta+\Delta_w,
\qquad a_n=\lambda_d=C_d\sqrt{q_0}.
\]
By (3), (4), and (11),
\[
\|\nabla\ell_0(\theta^\dagger)\|_\infty
\le A\sqrt{q_0}+\|\Delta_w\|_1
\le C a_n. \tag{12}
\]
There is no independence assertion about \(\theta^\dagger\) and the target sample: (4) holds for every pair of arguments for each realized sample.

For positive arguments, the derivative of the SCAD penalty is respectively \(\lambda\), \((a\lambda-t)/(a-1)\), and zero on its three regions. The derivatives match at the nonzero junctions, and the penalty is continuous at zero. Its absolute slope is therefore at most \(\lambda\), which implies
\[
|P_\lambda(u+b)-P_\lambda(u)|\le\lambda|b|. \tag{13}
\]
Taking \(d=d^\circ\) in the objective comparison of (E3) gives \(Q(d^\circ+v)\le Q(d^\circ)\). Its exact consequence for the target loss remainder
\[
R_0=\ell_0(\theta^\dagger+v)-\ell_0(\theta^\dagger)
-\langle\nabla\ell_0(\theta^\dagger),v\rangle
\]
is
\[
R_0\le a_n\bigl(\|d^\circ\|_1-\|d^\circ+v\|_1\bigr)
+\bigl(\lambda+\|\nabla\ell_0(\theta^\dagger)\|_\infty\bigr)\|v\|_1. \tag{14}
\]
Here (13) bounds the entire SCAD difference without requiring any comparison between the target curvature and SCAD's concavity.

Let
\[
T=\{k:|d_k^\circ|>a_n\},\qquad t=|T|.
\]
The assumed choice of \(C_h\) gives
\[
t\le\frac{\|d^\circ\|_1}{a_n}\le\frac{C_hh}{a_n}\le t_0. \tag{15}
\]
Decomposability gives
\[
\|d^\circ\|_1-\|d^\circ+v\|_1
\le\|v_T\|_1-\|v_{T^c}\|_1+2\|d^\circ_{T^c}\|_1
\le\sqrt t\,\|v\|_2+2C_hh. \tag{16}
\]
Condition (E4) also gives
\[
\|v\|_1\le4\|v_T\|_1+3C_hh
\le4\sqrt t\,\|v\|_2+3C_hh. \tag{17}
\]
The bound uses an effective support, not an assertion that \(d^\circ\) is exactly sparse.

The two endpoints \(\theta^\dagger\) and \(\theta^\dagger+v\) belong to the target \(\ell_1\)-ball by (E3); the entire segment belongs to it by convexity. Equations (15) and (E4) verify the set-size and cone hypotheses of (E2). Integrating (E2) along the segment yields, with \(x=\|v\|_2\),
\[
R_0\ge\frac{\kappa_0}{2}x^2-\tau_0q_0\|v\|_1^2.
\]
Since \(\lambda/a_n=C_\lambda/C_d\) is fixed, equations (12), (14), (16), and (17) give
\[
x^2\le C\left[a_n\sqrt t\,x+a_nh
+a_n^2(\sqrt t\,x+h)^2\right]. \tag{18}
\]
We used \(q_0=a_n^2/C_d^2\); all tuning factors remain fixed constants.

For completeness, expand the tolerance using \((u+w)^2\le2u^2+2w^2\). Compatibility gives \(h\le Ka_n\), while \(a_n^2=C_d^2q_0=o(1)\). Equation (15) implies
\[
a_n^2t\le C_ha_nh\le C_hK a_n^2=o(1).
\]
Thus the coefficient of \(x^2\) contributed by (18) can be absorbed. Moreover,
\[
a_n^2h^2=(a_nh)^2\le a_nh
\]
for sufficiently large indices, and
\[
a_n\sqrt t\le\sqrt{C_ha_nh}.
\]
Consequently,
\[
x^2\le C\left(\sqrt{a_nh}\,x+a_nh\right),
\qquad
\|v\|_2\le C\sqrt{a_nh}. \tag{19}
\]
Substituting (19) and (15) into (17) gives
\[
\|v\|_1\le C\sqrt{h/a_n}\sqrt{a_nh}+3C_hh\le Ch. \tag{20}
\]
Since \(a_n>0\), these calculations do not divide by \(h\). When \(h=0\), one may also read the conclusion directly: \(d^\circ=0\), \(T=\varnothing\), and (E4) forces \(v=0\). When \(T=\varnothing\) and \(h>0\), (17) remains valid.

Finally, \(\|v\|_2\le\|v\|_1\), so (19)–(20) prove
\[
\|v\|_2\le C\min\left\{\left(\frac{\log p}{n_0}\right)^{1/4}h^{1/2},h\right\},
\qquad \|v\|_1\le Ch. \tag{21}
\]
Approximate stationarity remains part of the estimator's assumed contract, but this rate argument uses the objective comparison and neighborhood clauses of (E3), together with (E4); it needs no additional rate requirement on \(\epsilon_n\).

## 5. Final rates and probability

The definitions give
\[
\widehat\vartheta-\vartheta=\Delta_w+v.
\]
The triangle inequality, (10), and (21) prove
\[
\|\widehat\vartheta-\vartheta\|_2
\le C\left[
\sqrt{\frac{s\log p}{N}}
+\min\left\{\left(\frac{\log p}{N}\right)^{1/4}h^{1/2},h\right\}
+\min\left\{\left(\frac{\log p}{n_0}\right)^{1/4}h^{1/2},h\right\}
\right].
\]
Similarly, (11) and (20) give
\[
\|\widehat\vartheta-\vartheta\|_1
\le C\left(s\sqrt{\frac{\log p}{N}}+h\right).
\]
All deterministic steps hold on \(\mathcal E\cap\mathcal H\). A union bound yields
\[
\mathbb P(\mathcal E\cap\mathcal H)
\ge1-C_1p^{-C_2}-4p^{-c}
\ge1-C_0p^{-c_0},
\]
where, for example, \(c_0=\min\{C_2,c\}\) and \(C_0=C_1+4\). The two stages use overlapping data, but no independence of their events was invoked. The bounds cover \(s=0\), \(h=0\), zero off-support mass, and an empty source set. Every listed proof obligation is closed.
