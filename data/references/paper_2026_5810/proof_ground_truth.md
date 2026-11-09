# Reference Proof

## Proof Structure and Obligations

1. Verify that the rank-one PSD lift has unit Frobenius norm and that its overlap is squared spherical correlation.
2. Derive the one-sided spherical-cap estimate, including its endpoints.
3. Establish finite termination of the antipodal greedy selection, use maximality to obtain coverage, and derive the capacity lower bound.
4. Verify the fixed-coefficient expected-power interpretation of pSNR and compute the linear and PSD distractor powers.
5. Solve the strict retrieval inequalities, locate the relevant quadratic root, and justify its asymptotic expansion.

All five obligations are closed below. The geometric packing result and the stipulated-correlation retrieval result are separate conclusions in the integrated theorem; the proof does not assert that the greedy dictionary realizes the stipulated retrieval correlations.

## Complete Proof

Let p be an integer with p >= 2 and let 0 < epsilon < 1. The cone S_+^p is closed, and its unit-Frobenius section is nonempty and compact. Therefore the continuous finite-dictionary interference objective attains its minimum. The T=1 convention is consistent with a dictionary containing one address.

### Rank-one geometry

For unit vectors u,v in R^p, the matrix uu^T is PSD, and
\[
\|uu^T\|_F^2=\operatorname{tr}(uu^Tuu^T)=1.
\]
Moreover,
\[
\langle uu^T,vv^T\rangle_F
=\operatorname{tr}(uu^Tvv^T)=(u^Tv)^2.
\]
Thus a rank-one PSD dictionary has interference at most epsilon exactly when its unit representatives satisfy |u_i^T u_j| <= sqrt(epsilon). This equivalence concerns the rank-one subclass, not arbitrary PSD matrices.

### Spherical-cap estimate

Let U be uniform on S^{p-1}, fix e in S^{p-1}, and let a in [0,1]. The claim is
\[
\Pr(U^Te\ge a)\le (1-a^2)^{(p-1)/2}.
\]
If a=0, the cap is a hemisphere and its probability is 1/2 <= 1. If a=1, the cap consists of the single point e and has surface measure zero because p >= 2.

For 0<a<1, rotational invariance permits taking e as the north pole. Put theta=arccos(a), s=sin(theta)=sqrt(1-a^2), and
\[
J_p=\int_0^\pi\sin^{p-2}(\phi)\,d\phi>0.
\]
The polar-angle surface density gives
\[
\Pr(U^Te\ge a)=\frac{\int_0^\theta\sin^{p-2}(\phi)\,d\phi}{J_p}.
\]
In the numerator substitute sin(phi)=s sin(psi). This yields
\[
\int_0^\theta\sin^{p-2}(\phi)\,d\phi
=s^{p-1}\int_0^{\pi/2}
\frac{\sin^{p-2}(\psi)\cos(\psi)}{\sqrt{1-s^2\sin^2(\psi)}}\,d\psi.
\]
For 0<=psi<pi/2,
\[
\sqrt{1-s^2\sin^2(\psi)}\ge\cos(\psi),
\]
so
\[
\int_0^\theta\sin^{p-2}(\phi)\,d\phi
\le s^{p-1}\int_0^{\pi/2}\sin^{p-2}(\psi)\,d\psi
\le s^{p-1}J_p.
\]
Dividing by J_p proves the estimate. Endpoint values of the integrand do not affect the integral.

### Finite greedy packing and coverage

Put a=sqrt(epsilon), so 0<a<1. Begin with any unit representative and repeatedly choose another unit vector outside all closed antipodal caps
\[
\{u:u^Tu_i\ge a\}\cup\{u:u^T(-u_i)\ge a\}.
\]
Every selected pair satisfies |u_i^T u_j|<a. In particular,
\[
\|u_i-u_j\|_2^2=2-2u_i^Tu_j>2(1-a).
\]
Let delta=sqrt(2(1-a))>0. Compactness of the sphere gives a finite covering by Euclidean balls of radius delta/3. No such ball contains two selected representatives, since its diameter is less than delta. Hence there is a finite upper bound on the number of selections, and the greedy procedure must terminate.

At termination, let m denote the number of selected representatives. Their antipodal caps cover the sphere; an uncovered point would permit another selection. Each one-sided cap has probability at most
\[
(1-a^2)^{(p-1)/2}=(1-\varepsilon)^{(p-1)/2}.
\]
The union bound consequently gives
\[
1\le 2m(1-\varepsilon)^{(p-1)/2},
\qquad
m\ge\tfrac12(1-\varepsilon)^{-(p-1)/2}.
\]
The m rank-one lifts are unit PSD matrices with pairwise interference below epsilon. They are therefore admissible for the full-cone capacity, proving
\[
C_\varepsilon(S_+^p)\ge\tfrac12(1-\varepsilon)^{-(p-1)/2}.
\]
For fixed epsilon in (0,1), this lower bound is
\[
\tfrac12\exp\!\left(\tfrac{p-1}{2}\log\frac1{1-\varepsilon}\right),
\]
which is exponential in p.

### Fixed-coefficient value experiment and retrieval formulas

Fix the unit addresses and matched query as in the public setup. Thus all attention coefficients are fixed while the values are drawn. For each independent value v_j~N(0,I_{d_v}/d_v),
\[
\mathbb E v_j=0,
\qquad
\mathbb E\|v_j\|_2^2=\operatorname{tr}(I_{d_v}/d_v)=1.
\]
Independence gives E<v_i,v_j>=0 for i!=j. Consequently,
\[
\mathbb E\|a_*v_*\|_2^2=|a_*|^2,
\qquad
\mathbb E\left\|\sum_{j\ne *}a_jv_j\right\|_2^2
=\sum_{j\ne *}|a_j|^2.
\]
The public pSNR is therefore the ratio of expected signal power to expected aggregate distractor power. It is neither an expectation of a realized ratio nor a guarantee of exact recall.

Now let T>p be an integer and put
\[
\varepsilon_*=\frac{T-p}{p(T-1)}.
\]
Its numerator and denominator are positive, and
\[
p(T-1)-(T-p)=(p-1)T>0,
\]
so 0<epsilon_*<1. The matched coefficient is one for both readouts. By the stipulated query-to-distractor correlations, each linear distractor coefficient has squared magnitude epsilon_*, whereas each PSD distractor coefficient has squared magnitude epsilon_*^2. Both aggregate powers are positive. Hence
\[
\mathrm{pSNR}_{\rm Lin}
=\frac1{(T-1)\varepsilon_*}
=\frac p{T-p},
\qquad
\mathrm{pSNR}_{\rm PSD}
=\frac1{(T-1)\varepsilon_*^2}
=\frac{p^2(T-1)}{(T-p)^2}.
\]
No assumption on correlations among distractors is used.

### Strict thresholds and asymptotics

Since T-p>0,
\[
\mathrm{pSNR}_{\rm Lin}>1
\iff p>T-p
\iff T<2p.
\]
Similarly,
\[
\mathrm{pSNR}_{\rm PSD}>1
\iff (T-p)^2<p^2(T-1).
\]
Writing the latter inequality as f_p(T)<0 gives
\[
f_p(T)=T^2-(p^2+2p)T+2p^2.
\]
The discriminant is p^2(p^2+4p-4)>0, and the roots are
\[
T_\pm=\frac{p^2+2p\pm p\sqrt{p^2+4p-4}}2.
\]
Because
\[
f_p(p)=p^2(1-p)<0,
\]
p lies strictly between the two roots. Thus, within the assumed regime T>p, ideal PSD retrieval holds exactly when T<T_+. At T=T_+, if this boundary is an integer, pSNR equals one and retrieval is not ideal under the strict criterion.

To justify the asymptotic expansion, write b_p=p^2+2p. Then
\[
T_+=\frac{b_p}{2}\left(1+\sqrt{1-\frac{8p^2}{b_p^2}}\right).
\]
The elementary expansion sqrt(1-x)=1-x/2+O(x^2) as x tends to zero gives
\[
T_+=b_p-\frac{2p^2}{b_p}
+O\!\left(\frac{p^4}{b_p^3}\right)
=p^2+2p-2+O(p^{-1}).
\]
Therefore T_+=Theta(p^2), while the linear upper boundary is 2p=Theta(p). These are the stipulated-correlation expected-power retrieval regimes, distinct from the fixed-interference dictionary capacity.

## Upstream Dependency Verification

The relevant standard-independent result indexed by theory_017 is the real Welch inequality: for T>D>=1 and unit vectors w_1,...,w_T in R^D,
\[
\max_{i\ne j}|w_i^Tw_j|^2\ge\frac{T-D}{D(T-1)}.
\]
Its relevant statement is also supplied in theory_007. It can be verified directly: the Gram matrix G is PSD, has trace T and rank at most D. Cauchy-Schwarz on its nonzero eigenvalues gives tr(G^2)>=T^2/D. Since its diagonal entries are one,
\[
\sum_{i\ne j}|w_i^Tw_j|^2=\operatorname{tr}(G^2)-T
\ge\frac{T(T-D)}D.
\]
Taking the maximum of the T(T-1) off-diagonal squared entries proves the bound. The hypotheses are exactly unit real vectors and T>D. Restricting the vectors to the orthant preserves this inequality, and rearrangement yields the source's orthant bound when epsilon<1/sqrt(D).

For the frozen retrieval theorem, this result motivates the numerical scale epsilon_*; the correlations themselves are an explicit hypothesis. Neither attainment of the Welch bound by every address pair nor existence of an equiangular tight frame is required. Cone classification, Rankin bounds, and other branches bundled in theory_017 do not close any obligation of this frozen proof and are not invoked here.
