# Reference Proof

## Proof Structure

The proof closes four obligations: construct a common transition using the shared embedding factorization and the observed carrier; prove the exact feature-equality criterion by channel injectivity and density ratios; transfer centered potentials using finite affine combinations; and eliminate the residual constant by probability normalization. The affine-representation hypothesis is used only for the third and fourth obligations, not for the transition construction or exact criterion.

## Complete Proof

If there is no observed-feature-equivalent model pair in the specified class, the assertions quantified over such pairs are vacuous. Otherwise fix m=(q,b,k) and m'=(q',b,k') in 𝓜 with the required observed agreement. Write μ=bq and μ'=bq', and use p_a and p'_a for their densities. The existence of μ_{a_0}≪ν implies ν is not the zero measure. All density and potential expressions below are interpreted on their conull domains, with arbitrary measurable extensions on null complements when needed.

### 1. Carrier alignment and observed transport

Choose the shared space Z, embedding class 𝒢, and channel h from the factorization hypothesis. For the fixed channels k and k', choose embeddings g,g'∈𝒢 such that
\[
k\lambda=h(T_g\lambda),\qquad
k'\lambda=h(T_{g'}\lambda)
\]
for every probability law λ≪ν. These embeddings are fixed for the model pair and do not depend on the attribute.

For each a∈A_obs, observed feature equality gives
\[
h(T_g\mu_a)=h(T_{g'}\mu'_a).
\]
Both inputs belong to the specified set 𝒮, so injectivity on that set gives
\[
T_g\mu_a=T_{g'}\mu'_a
\qquad(a\in A_{\mathrm{obs}}).
\]

Common positive support implies μ_{a_0}∼ν and μ'_{a_0}∼ν. Indeed, the integral of a positive ν-almost-everywhere density over a measurable set is zero exactly when that set is ν-null. Equivalence of measures is preserved by pushforward, since pushforward null sets are determined by preimages. Therefore the equality at the anchor implies
\[
\eta:=T_g\nu\ \sim\ T_g\mu_{a_0}
=T_{g'}\mu'_{a_0}\ \sim\ T_{g'}\nu=:\eta'.
\]
This is the carrier-alignment step. In the source's weaker mixture formulation, the same argument uses one common observed mixing measure. Here that condition follows automatically: π=δ_{a_0} works simultaneously for every q∈𝒬, because its mixture is (bq)(·|a_0)∼ν. No model-dependent choice of π is required.

The images g(C) and g'(C) are measurable. Define
\[
D'=\{c\in C:g'(c)\in g(C)\},\qquad
D=\{c\in C:g(c)\in g'(C)\}.
\]
The measure η is concentrated on g(C), and η' is concentrated on g'(C). Their equivalence implies ν(C\D')=ν(C\D)=0. The maps
\[
t=g^{-1}\circ g':D'\longrightarrow D,
\qquad
t^{-1}=g'^{-1}\circ g:D\longrightarrow D'
\]
are measurable inverses.

They preserve null sets in both directions. To see this explicitly, let E⊆D be measurable. Its image g(E) is measurable because g is a bimeasurable embedding. Then
\[
\nu(t^{-1}(E))=\eta'(g(E))=0
\quad\Longleftrightarrow\quad
\eta(g(E))=\nu(E)=0.
\]
The same reasoning with g and g' exchanged applies to the inverse. Thus t∈Aut_ν(C). In particular, T_tλ≪ν whenever λ≪ν, and
\[
T_gT_t\lambda=T_{g'}\lambda
\]
for every ν-dominated probability law λ.

Pushforward by a bimeasurable embedding is injective on measures: for any measurable E⊆C, its measurable image g(E) satisfies (T_gα)(g(E))=α(E). Applying this fact to the observed equalities yields
\[
T_g\mu_a=T_{g'}\mu'_a=T_gT_t\mu'_a
\quad\Longrightarrow\quad
\mu_a=T_t\mu'_a
\qquad(a\in A_{\mathrm{obs}}).
\]
Also, for every probability law λ≪ν,
\[
k'\lambda=h(T_{g'}\lambda)
=h(T_gT_t\lambda)=k(T_t\lambda),
\]
since T_tλ is again a ν-dominated probability law. This proves both required transition properties without requiring an everywhere-defined bijection of C.

### 2. Exact extrapolation criterion

First, k is injective on ν-dominated probability laws. If α,β≪ν are probability laws and kα=kβ, the factorization gives h(T_gα)=h(T_gβ). Both inputs lie in 𝒮, so T_gα=T_gβ; injectivity of embedding pushforward then gives α=β. Consequently, for each a∈A_test,
\[
P^m(\cdot\mid a)=P^{m'}(\cdot\mid a)
\quad\Longleftrightarrow\quad
k\mu_a=kT_t\mu'_a
\quad\Longleftrightarrow\quad
\mu_a=T_t\mu'_a.
\]
All measures used here are probability laws dominated by ν, exactly the domain covered by the assumptions.

Because t is a bimeasurable bijection between conull subsets, the measure T_{t^{-1}}ν is σ-finite: the inverse images, under t, of a countable finite-ν-measure cover of its range give a finite-T_{t^{-1}}ν-measure cover of its domain, and the remaining set is null. It is also equivalent to ν. The Radon–Nikodym theorem for equivalent σ-finite measures therefore gives
\[
r=\frac{d(T_{t^{-1}}\nu)}{d\nu},\qquad 0<r<\infty\quad\nu\text{-almost everywhere}.
\]
For any probability density p with respect to ν, the density of T_{t^{-1}}(pν) is (p∘t)r. Indeed, for every nonnegative measurable test function f,
\[
\begin{aligned}
\int f(c)p(t(c))r(c)\,\nu(dc)
&=\int f(c)p(t(c))\,(T_{t^{-1}}\nu)(dc)\\
&=\int f(t^{-1}(u))p(u)\,\nu(du)\\
&=\int f\,d\bigl(T_{t^{-1}}(p\nu)\bigr).
\end{aligned}
\]
The inverse identities used in the middle equality hold on conull sets. This proves the needed pushforward density formula, including its orientation.

It follows that, for each a,
\[
\mu_a=T_t\mu'_a
\quad\Longleftrightarrow\quad
\mu'_a=T_{t^{-1}}\mu_a
\quad\Longleftrightarrow\quad
p'_a(c)=p_a(t(c))r(c)\quad\nu\text{-almost everywhere}.
\]
At a_0 this identity already holds by observed transport. If it also holds at a, divide it by the identity at a_0 and take logarithms. Positivity and finiteness hold on a common conull set for these finitely many factors, giving
\[
V_{\mu'}(a,a_0;c)=V_\mu(a,a_0;t(c))
\quad\nu\text{-almost everywhere}.
\]
Conversely, this potential identity together with the anchored density identity gives
\[
\begin{aligned}
p'_a(c)
&=p'_{a_0}(c)\exp\{V_{\mu'}(a,a_0;c)\}\\
&=p_{a_0}(t(c))r(c)\exp\{V_\mu(a,a_0;t(c))\}\\
&=p_a(t(c))r(c),
\end{aligned}
\]
and hence μ_a=T_tμ'_a. Combining the equivalences for each a∈A_test proves the exact criterion. The exceptional ν-null set may depend on a; no intersection over all attributes is taken.

### 3. Affine extension of centered potentials

Now assume the additional fixed representation ψ, the measurable maps H_μ, and the affine-hull condition. Set
\[
F_\mu(a;c,c_0)
=V_\mu(a,a_0;c)-V_\mu(a,a_0;c_0).
\]
Fix one a∈A_test. By the definition of affine hull, there are finitely many observed attributes a_1,…,a_ℓ and real coefficients α_1,…,α_ℓ such that
\[
\psi(a)=\sum_{i=1}^{\ell}\alpha_i\psi(a_i),
\qquad \sum_{i=1}^{\ell}\alpha_i=1.
\]
The coefficients need not be nonnegative. For each of μ and μ', the assumed representation gives
\[
F_\mu(a;c,c_0)=\sum_{i=1}^{\ell}\alpha_iF_\mu(a_i;c,c_0),
\qquad
F_{\mu'}(a;c,c_0)=\sum_{i=1}^{\ell}\alpha_iF_{\mu'}(a_i;c,c_0)
\]
for ν⊗ν-almost every pair. Only the finitely many identities for a,a_1,…,a_ℓ are combined, so their exceptional sets can be removed together.

By the observed transport and the preceding density argument,
\[
V_{\mu'}(a_i,a_0;c)=V_\mu(a_i,a_0;t(c))
\quad\nu\text{-almost everywhere}
\]
for each i. These identities can be subtracted at c and c_0 outside a product-null set. In fact, if N is ν-null, then N×C and C×N are product-null because ν is σ-finite, as follows by covering C by countably many finite-measure sets.

The affine identities for μ can also be evaluated at (t(c),t(c_0)). To justify this, pushforward of the product measure by t×t is
\[
T_{t\times t}(\nu\otimes\nu)=(T_t\nu)\otimes(T_t\nu).
\]
This follows first on measurable rectangles and then by uniqueness of σ-finite product measures. Since T_tν∼ν and both are σ-finite, their product measures have the same null sets, by Tonelli's theorem applied to sections. Thus t×t preserves product-null sets.

Combining the finite affine identities with the observed transported identities now gives
\[
F_{\mu'}(a;c,c_0)=F_\mu(a;t(c),t(c_0))
\quad\text{for }\nu\otimes\nu\text{-almost every }(c,c_0).
\]
Define the measurable, almost-everywhere finite function
\[
R_a(c)=V_{\mu'}(a,a_0;c)-V_\mu(a,a_0;t(c)).
\]
The last display says R_a(c)=R_a(c_0) for ν⊗ν-almost every pair. Tonelli's theorem applied to the indicator of the exceptional set shows that, for ν-almost every c_0, this equality holds for ν-almost every c. Since ν is nonzero and R_a is finite almost everywhere, choose such a c_0 with R_a(c_0) finite. Therefore
\[
R_a(c)=\beta_a\quad\nu\text{-almost everywhere}
\]
for the real number β_a=R_a(c_0). This argument requires no integrability assumption on the logarithms.

### 4. Normalization and integrated conclusion

Use the anchored density identity and the preceding constant relation to obtain
\[
\begin{aligned}
p'_a(c)
&=p'_{a_0}(c)\exp\{V_{\mu'}(a,a_0;c)\}\\
&=p_{a_0}(t(c))r(c)
\exp\{V_\mu(a,a_0;t(c))+\beta_a\}\\
&=e^{\beta_a}p_a(t(c))r(c)
\end{aligned}
\]
ν-almost everywhere. The density formula already proved shows that p_a(t(c))r(c) is the density of the probability law T_{t^{-1}}μ_a, so its integral is one. Integrating the display therefore gives 1=e^{β_a}, hence β_a=0.

Thus the transported potential identity holds for the fixed target a. Repeating the argument separately for each a∈A_test proves the required per-attribute almost-everywhere identities. Section 2 then gives feature equality at every target attribute, for the same transition constructed from the observed pair.

No rank assumption, convex-hull condition, or common exceptional set across all attributes is needed. Singleton observed sets, constant attribute representations, and A_test=A_obs are covered by the same argument. If ν=0, no model pair with the stipulated dominated probability laws exists, so that case is vacuous rather than an unaddressed exception.
