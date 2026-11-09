# Reference Proof

## Contract and obligations

The public task assumes an approximating comparator in the bounded hypothesis class. It does not ask us to prove the specialized external approximation theorem. We must establish: well-defined and measurable oscillator losses; the comparator/ERM baseline; temporal-output contraction; the parameter-to-trajectory and parameter-to-readout estimates; a cover with admissible centers; the entropy bound with its constants; and the uniform high-probability substitution.

Throughout, write
\[
w=w_{\max},\quad h=h_\Pi,\quad B=B_{\max},\quad U=B_K,\quad a=wB,\quad L=a^2,\quad E=e^{T(L+1)}.
\]
The specified architecture gives \(w\ge2\), \(h\ge2\), and \(p,q\le w\). All vector norms in the ODE estimates below are \(\ell^1\) norms. Temporal \(L^2\) uses the Euclidean norm, exactly as in the task.

## 1. Well-definedness and the ERM baseline

An affine map with at most \(w\) rows and entries bounded by \(B\) has induced \(\ell^1\) operator norm at most \(wB=a\). ReLU is 1-Lipschitz and vanishes at zero. Consequently \(\Gamma\) is globally Lipschitz in its arguments with constant at most \(L=a^2\), and each readout layer is Lipschitz with constant at most \(a\). The first-order system for \((x,x')\) is continuous in time and globally Lipschitz in its state. The standard global existence and uniqueness theorem therefore applies on \([0,T]\).

The parameter set is a closed subset of a finite-dimensional compact box. Indeed, each constraint \(|\Pi_j(z)|\le B_\Pi\) at a fixed \(z\) is closed in the parameters, and the uniform constraint is their intersection. The set includes the zero network. Continuous dependence of the ODE solution on parameters and on the continuous input, obtained from the same Gronwall estimate used below, makes \((\theta,u,t)\mapsto F_\theta[u](t)\) continuous on the relevant compact sets. Thus the losses are measurable, the empirical objective is continuous in parameters, and its minimum exists. Population loss is also continuous in parameters by bounded convergence. Suprema over parameters can be taken over a countable dense subset, so the uniform empirical-process events used below are measurable.

For the stipulated comparator,
\[
\|\Phi[u]-F^*[u]\|_{L^2}^2
\le T\sup_t|\Phi[u](t)-F^*[u](t)|_1^2
\le T\varepsilon_{\rm app}^2.
\]
Both its empirical and population losses obey this bound. Every ERM therefore satisfies
\[
\widehat\ell(\widehat F)\le T\varepsilon_{\rm app}^2.
\]
Every individual loss lies in \([0,b]\), where \(b=TqB_{\rm loss}^2\).

## 2. State and parameter perturbation estimates

We use Gronwall in the elementary form: if \(s(t)\le c+\lambda\int_0^t s(\tau)d\tau\), then \(s(t)\le ce^{\lambda t}\). Also, subtracting two first-order systems with common Lipschitz bound \(L+1\), common initial value, and forcing difference at most \(d\), gives state difference at most \(TdE\) on the time interval.

The vector-field value at zero satisfies
\[
|\Gamma(0)|_1\le wB(wB+1)=a(a+1).
\]
Integrating both state equations gives
\[
S:=\sup_t(|x(t)|_1+|x'(t)|_1)
\le TE\{pUL+a(a+1)\}
\le3wU(L+1)TE,
\]
where \(a(a+1)\le2(L+1)\), \(U,T\ge1\), and \(p\le w\).

Consider two admissible parameter vectors differing by at most \(\eta\) in every coordinate. Splitting the two-layer vector-field difference into its two weight changes and its bias changes gives, for every argument \(z\),
\[
|\Gamma_2(z)-\Gamma_1(z)|_1
\le\eta\{2w^2B(|z|_1+1)+w\}.
\]
Along either trajectory, \(|z|_1=|(x,x',u)|_1\le S+pU\le4wU(L+1)TE\). Hence
\[
\sup_t|\Gamma_2(z(t))-\Gamma_1(z(t))|_1
\le11\eta w^3(B+1)U(L+1)TE.
\]
Subtracting the first-order systems and applying Gronwall yields
\[
\sup_t|x_2(t)-x_1(t)|_1
\le11\eta w^3(B+1)U(L+1)T^2E^2. \tag{1}
\]
This derives directly the solution-difference estimate that the source also cites from prior work; that citation is not an unresolved dependency here.

For the readout, let \(z\) be fixed. A hidden activation after \(k\) layers has norm at most
\[
a^k|z|_1+wB\sum_{j=0}^{k-1}a^j.
\]
Telescoping the parameter changes layer by layer therefore gives
\[
|\Pi_2(z)-\Pi_1(z)|_1
\le\eta w\left[h a^{h-1}|z|_1+\sum_{j=0}^{h-1}a^j
+wB\sum_{j=0}^{h-2}(j+1)a^j\right]
\le\eta w h^2(a^{h-1}+1)(|z|_1+wB+1). \tag{2}
\]
This uses readout widths, not vector-field widths. All sums are finite, so the cases \(a=0\) and \(a=1\) require no division by \(1-a\).

For \(z=(x(t),u(0),t)\), we have
\[
|z|_1\le5wU(L+1)TE,
\qquad |z|_1+wB+1\le7w(B+1)U(L+1)TE.
\]
Since \(a^{h-1}+1\le2(a^h+1)\), (2) bounds the fixed-state readout change by
\[
14\eta w^2h^2(a^h+1)(B+1)U(L+1)TE.
\]
The state-change contribution is bounded by \(a^h\) times (1). Adding the two contributions, using \(B+1\le2(B^3+1)\), \(h\ge2\), \(w\ge2\), and \(TE\ge1\), gives
\[
\sup_{u\in K,t}|F_2[u](t)-F_1[u](t)|_1
\le\eta C,
\]
where
\[
C=30w^4h^2(a^h+1)(L+1)T^2E^2U(B^3+1). \tag{3}
\]
For clarity, the numerical comparison is
\[
2(11w^3+14w^2h^2)
\le h^2(5.5w^3+28w^2)\le30w^4h^2.
\]
The task's corrected entropy scale satisfies
\[
B_\Pi\Delta=30w^{11/2}h^2(a^h+1)(L+1)T^2E^2U(B^3+1).
\]
Thus \(C\le\sqrt q B_\Pi\Delta\). For the sample metric
\[
d(F,G)^2=\sum_{i=1}^N\|F[u_i]-G[u_i]\|_{L^2}^2
\]
and \(R=\sqrt{NTq}B_\Pi\), (3) implies
\[
d(F_1,F_2)\le\eta R\Delta. \tag{4}
\]
In addition, \(d(F,0)\le R\), and the diameter is at most \(2R\).

## 3. Admissible covering numbers and the entropy integral

Let \(D\) be the number of scalar weight and bias parameters. The source's exact counts are
\[
D_\Gamma=w_\Gamma(3pM+p)+w_\Gamma+pM,
\]
\[
D_\Pi=(h-2)w_\Pi^2+w_\Pi[pM+p+q+1]+q+(h-1)w_\Pi.
\]
Equivalently, counting the two affine vector-field layers and the \(h\) affine readout layers immediately gives
\[
D=D_\Gamma+D_\Pi\le(h+2)(w^2+w)\le4hw^2. \tag{5}
\]
Partition each parameter interval into cells of length at most \(\eta\). A coordinate with bound \(B_c\) needs at most \(\max(1,\lceil2B_c/\eta\rceil)\le1+2B_c/\eta\) cells. From each product cell meeting the admissible parameter set, choose one admissible representative. This preserves the output restriction and ensures cover centers belong to the class. Two parameters in one cell are coordinatewise within \(\eta\), so (4) gives
\[
\mathcal N(\mathcal F,d,\epsilon)
\le\left(1+\frac{2BR\Delta}{\epsilon}\right)^D. \tag{6}
\]
Strict-radius covers follow by using slightly smaller cells and taking a limit. When \(B=0\), the class has one parameter vector and its covering number is one.

The entropy integral satisfies
\[
I:=\int_0^R\sqrt{\ln\mathcal N(\mathcal F,d,\epsilon)}\,d\epsilon
\le R\sqrt D\sqrt{\ln(3+6B\Delta)}. \tag{7}
\]
Here is an elementary verification, so no specialized integral estimate is left implicit. Set \(A=2B\Delta\). For \(A>0\), Jensen and direct integration give
\[
\int_0^1\sqrt{\ln(1+A/t)}dt
\le\sqrt{\ln(1+A)+A\ln(1+1/A)}
\le\sqrt{\ln(1+A)+1}
\le\sqrt{\ln(3+3A)}.
\]
For \(A=0\), the integral is zero. Substitute \(t=\epsilon/R\) into (6).

## 4. Temporal coefficients, contraction, and chaining

Fix the inputs for this section. Let \((e_k)\) be an orthonormal basis of real \(L^2([0,T])\), and let \(P_J\) denote projection onto its first \(J\) elements, componentwise. Write
\[
\alpha_{ijk}(F)=\langle F[u_i]_j,e_k\rangle,
\qquad
\kappa_J(F)=\sum_{i=1}^N\sum_{j=1}^q\sum_{k=1}^J\widetilde\sigma_{ijk}\alpha_{ijk}(F),
\]
where the signs are independent. Parseval implies square summability of the full coefficient arrays. The infinite series exists in mean square at every fixed \(F\), is centered, and has increment second moment \(d(F,G)^2\). The inequality \(\cosh(s)\le e^{s^2/2}\), applied to finite sums and then Fatou along an almost-surely convergent subsequence, gives the sub-Gaussian increment bound
\[
\mathbb E e^{\lambda(\kappa(F)-\kappa(G))}
\le e^{\lambda^2d(F,G)^2/2}.
\]
For the proof below it is enough to work with \(\kappa_J\); its increment scale is at most \(d(F,G)\), and its anchor at the zero network is zero.

The finite-class maximal inequality used here states that centered variables \(Z_1,\ldots,Z_n\) with \(\mathbb E e^{\lambda Z_j}\le e^{\lambda^2s^2/2}\) satisfy \(\mathbb E\max_j Z_j\le s\sqrt{2\ln n}\). This follows by bounding the exponential of the maximum by the sum of exponentials and minimizing over \(\lambda>0\).

To check the entropy constant, take nets at radii \(r_m=2R2^{-m}\), \(m\ge1\), and use the zero network at level zero. Assign each point in a level-\(m\) net one parent in the preceding net. The distance to its parent is at most \(r_{m-1}\); at the first level use \(d(F,0)\le R\). For any terminal approximation, telescope along these parents. For the finite projection, the residual is at most \(\sqrt{NqJ}\,r_M\), by Cauchy-Schwarz, and tends to zero. The finite-class bound at each level consequently gives
\[
\mathbb E\sup_F\kappa_J(F)
\le\sum_{m\ge1}r_{m-1}\sqrt{2\ln\mathcal N(\mathcal F,d,r_m)}
\le4\sqrt2\int_0^R\sqrt{\ln\mathcal N(\mathcal F,d,\epsilon)}d\epsilon.
\]
The last inequality follows by comparing each summand with the integral over \([r_{m+1},r_m]\). This argument verifies the needed chaining statement without presuming continuity of an infinite Rademacher series.

Using (5)-(7), \(q\le w\), and \(h\ge2\), we obtain, uniformly in \(J\),
\[
\mathbb E\sup_F\kappa_J(F)
\le8\sqrt2\,B_\Pi w^{3/2}\sqrt h\sqrt{NT\ln(3+6B\Delta)}
\le32\sqrt2\,B_\Pi w^{3/2}h\sqrt{NT\ln(3+6B\Delta)}. \tag{8}
\]
The same bound holds for the infinite coefficient process on a countable dense index set, by taking finite subsets, passing to the mean-square limit, and then using monotone convergence of maxima including the zero anchor. We do not need that passage for the loss bound.

For each sample, the projected squared loss is
\[
z_{i,J}(F)=\|P_J(v_i-F[u_i])\|_{L^2}^2.
\]
The difference-of-squares identity and Cauchy-Schwarz show
\[
|z_{i,J}(F)-z_{i,J}(G)|
\le2\sqrt{Tq}B_{\rm loss}\,\|P_J(F[u_i]-G[u_i])\|_{L^2}.
\]
Indeed, each projected residual has norm at most \(\sqrt{Tq}B_{\rm loss}\), because orthogonal projection is a contraction. Thus the loss is \(2\sqrt{Tq}B_{\rm loss}\)-Lipschitz as a function of the finite coefficient vector on its relevant domain.

The standard vector-contraction inequality, in the form used here, states that for coefficient maps \(a_i(\theta)\) and scalar functions \(z_i\) with common Euclidean Lipschitz constant \(C\),
\[
\mathbb E_\sigma\sup_\theta\sum_i\sigma_i z_i(a_i(\theta))
\le\sqrt2 C\,\mathbb E_{\widetilde\sigma}\sup_\theta\sum_{i,k}\widetilde\sigma_{ik}a_{ik}(\theta).
\]
It also applies when the functions are specified on the coefficient images, by Lipschitz extension; additive constants have zero expected Rademacher sum. All coefficient spaces here are finite dimensional, and their images are compact. Applying this statement gives
\[
\widehat{\mathfrak R}_N(\mathcal L_J)
\le\frac{2\sqrt{2Tq}B_{\rm loss}}N\,\mathbb E\sup_F\kappa_J(F).
\]
For a fixed sample, the output set indexed by the compact parameter space is compact in the product temporal \(L^2\) space. Orthogonal projections converge uniformly on compact sets: a finite net and the contraction property reduce this assertion to convergence at finitely many points. Therefore \(z_{i,J}\) converges uniformly in \(F\) to the original loss, and its empirical Rademacher complexity converges as well. Taking \(J\to\infty\) and using (8) yields
\[
\widehat{\mathfrak R}_N(\mathcal L)
\le\frac{128T\sqrt q B_{\rm loss}B_\Pi}{\sqrt N}
 w^{3/2}h\sqrt{\ln(3+6B\Delta)}. \tag{9}
\]

## 5. Uniform high-probability conclusion

The standard empirical-Rademacher generalization inequality for a fixed measurable class of losses in \([0,b]\), evaluated on iid data, states that with probability at least \(1-\delta\), simultaneously for every member,
\[
\ell(F)\le\widehat\ell(F)+2\widehat{\mathfrak R}_N(\mathcal L)
+3b\sqrt{\frac{\ln(2/\delta)}{2N}}.
\]
Its hypotheses were verified in Section 1, with \(b=TqB_{\rm loss}^2\). The bound (9) is deterministic and uniform over the sampled inputs in \(K\). On this event, apply the inequality to every ERM and use its empirical baseline. Finally,
\[
256\sqrt q B_{\rm loss}B_\Pi\le256qB_{\rm loss}^2\le3\cdot86\,qB_{\rm loss}^2.
\]
Substitution gives precisely
\[
\ell(\widehat F)\le T\varepsilon_{\rm app}^{2}
+\frac{3TqB_{\rm loss}^{2}}{\sqrt N}
\left[86w_{\max}^{3/2}h_\Pi\sqrt{\ln(3+6B_{\max}\Delta)}
+\sqrt{\tfrac12\ln(2\delta^{-1})}\right].
\]
This includes zero parameter bounds, a zero target, singleton input supports, \(H=1\), and readout layer Lipschitz constant equal to zero or one. No unresolved proof obligation remains.
