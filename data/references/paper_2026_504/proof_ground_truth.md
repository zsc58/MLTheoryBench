# Reference Proof

## Source Contract and Audited Background

The selected theorem uses completeness, connectedness, a smooth Riemannian metric, and absolute continuity of the endpoint coupling. It does not assume independence, compactness, any moment condition, or regularity of the target density beyond its stated integrability. H3 and the later implementation assumptions are not dependencies of this chain.

Conditional densities are probability-density kernels. Their values at conditioning endpoints of zero probability are version choices, not uniquely determined conditional laws. The source fixes the initial conditional density by the quotient where meaningful and by p_0 on zero-marginal fibers, and uses its pushforward to select the later conditional laws. See L000119, L000214, and L000258–L000264. Normalizing exceptional fibers does not restrict the coupling.

The cut locus is used in the standard cut-time sense established by the source's injectivity-domain and cut-time definitions at L000081–L000093 and its polar-coordinate domain at L000269. The informal description in terms of nonunique minimizing geodesics at L000075 is not an extra definition that discards other cut endpoints.

The following standard independent results are the background represented by theory_015 and theory_011:

1. On a complete connected smooth Riemannian manifold, geodesics exist for all real times, Exp is smooth, and any two points can be joined by a minimizing geodesic. For each y, ID(y) is an open star-shaped neighborhood of zero, Exp_y restricts to a diffeomorphism from ID(y) onto M\C(y), and C(y) is closed and rho-null. In positive dimension,

   ID(y)={0} union {s u: u in S_yM, 0<s<c_y(u)},

   where S_yM is the unit sphere in T_yM. The non-cut relation is open, and Log depends smoothly on (y,x) there. These joint regularity facts are the parameter-dependent form of the exponential/logarithm result: smooth dependence of geodesics and the inverse function theorem give the local inverse on the open injectivity domain. In particular, the cut relation is measurable. The source invokes this geometry at L000073–L000093 and L001264–L001276.

2. In positive dimension, let mu_y be the ordinary Riemannian surface measure on S_yM, not its normalization to probability. For every nonnegative Borel function h, or every integrable h,

   integral_M h(x)d rho(x)
   = integral_{S_yM} integral_0^{c_y(u)} h(Exp_y(su)) det B_{y,u}(s) ds d mu_y(u).

   Here B acts on the (d-1)-dimensional normal space and has initial data B(0)=0, B'(0)=Id. Its determinant is positive for 0<s<c_y(u). In dimension one the normal determinant is 1 and mu_y counts the two unit directions. This is the polar integration result stated at L000279–L000299 and explained at L000887–L000993. Its extension from integrable functions to nonnegative functions follows by monotone convergence.

3. For a diffeomorphism between open subsets of a Riemannian manifold, change of variables uses its positive volume Jacobian. This Jacobian is smooth, including at points where a particular polar chart is singular. In ordinary coordinates it is the absolute coordinate determinant multiplied by the ratio of the smooth positive metric-volume factors. This is the change-of-variables principle underlying L000913–L000941 and L000323.

All the manifold hypotheses of these results are supplied by the public setup. No specialized nonstandard external result is required.

## Complete Proof

### 1. Product-null cut pairs and well-defined random variables

First suppose d>=1. Let

N={(x,y): x in C(y)}.

The geometric background makes N measurable. The Riemannian volume is sigma-finite, since the manifold has a countable cover by relatively compact coordinate neighborhoods. Tonelli's theorem and the cut-locus nullity for every y give

(rho tensor rho)(N)=integral_M rho(C(y))d rho(y)=0.

This proves the product-volume assertion directly; it is not inferred from a joint-law null statement. H2 then also gives pi_{0,1}(N)=0.

For every (x,y) outside N, set v=Log_y x. The function t maps to Exp_y((1-t)v) is smooth on an open interval containing [0,1], by geodesic completeness and smoothness of the exponential map. It runs from x to y along the reversed radial minimizing geodesic. The same exceptional set N works for all t. When x=y, v=0 and the curve is constant.

The map is jointly measurable off N. Defining it, for example, to equal y on N gives a measurable extension. Any other measurable extension has the same coupled law at each time, because pi_{0,1}(N)=0. This justifies the definition of X_t and pi_t.

The initial normalized conditional kernel required in the public setup is available under H2. Indeed, for a Borel representative p_{0,1}, put m(y)=integral p_{0,1}(x,y)d rho(x). For almost every y, m(y)=p_1(y). On the measurable set where 0<p_1(y)=m(y)<infinity, use p_{0,1}(x,y)/p_1(y); on its complement use a probability-density representative of p_0. Every section is then normalized, the kernel is jointly measurable, and p_{0,1}=p_1 p_{0|1} holds product-almost everywhere. Any fixed kernel satisfying the public requirements may be used in the rest of the proof.

### 2. Diffeomorphism, inverse, and image

Fix y and t in [0,1), and put a=1-t, so 0<a<=1. Multiplication by a is a diffeomorphism from ID(y) onto a ID(y). The latter set is open and is contained in ID(y) by star-shapedness. It need not equal ID(y).

Consequently the composition

M\C(y) --Log_y--> ID(y) --v maps to av--> a ID(y) --Exp_y--> U_t(y)

is a smooth diffeomorphism. Since a ID(y) is open and Exp_y is a diffeomorphism on ID(y), U_t(y) is open in M. In particular, U_t(y) is contained in M\C(y) and contains y.

If z belongs to U_t(y), then Log_y z belongs to a ID(y); hence

H_t(z;y)=Exp_y(Log_y z/a)

belongs to M\C(y). The exponential/logarithm inverse identities give H_t(F_t(x;y);y)=x and F_t(H_t(z;y);y)=z. This proves the asserted inverse, with its domain restricted to U_t(y).

For z outside C(y) and different from y, write Log_y z=ru, where r=dist(y,z)>0 and u is a unit vector. Then

z in U_t(y)
iff (r/a)u in ID(y)
iff r/a<c_y(u)
iff r<a c_y(u).

This also covers c_y(u)=infinity, since a>0. The point y is handled by 0 in a ID(y), without assigning a direction to the zero vector.

### 3. Conditional versions and the density computation

Fix t in [0,1). Using a measurable extension of F_t, define for every Borel set A

Q_t(A|y)=integral_M 1_A(F_t(x;y))p_{0|1}(x|y)d rho(x).

For every y this is a probability measure, and it depends measurably on y. Each initial conditional measure assigns mass zero to C(y), so the extension used there has no effect, even on conditioning endpoints where p_1(y)=0.

For Borel sets A and E, the defining factorization of the joint density gives

integral_E Q_t(A|y)p_1(y)d rho(y)
= integral_{M times E} 1_A(F_t(x;y))p_{0,1}(x,y)d rho(x)d rho(y)
= P(X_t in A, X_1 in E).

Thus Q_t is a regular conditional-distribution version. This is a construction of the required version, not a claim about every possible version on null conditioning endpoints.

Now fix y and write a=1-t. For a nonnegative Borel test function phi, the polar integration theorem gives

integral_M phi(z)Q_t(dz|y)
= integral_{S_yM} integral_0^{c_y(u)} phi(Exp_y(a s u)) p_{0|1}(Exp_y(su)|y) det B_{y,u}(s) ds d mu_y(u).

With r=a s this becomes

integral_{S_yM} integral_0^{a c_y(u)} phi(Exp_y(ru)) p_{0|1}(Exp_y((r/a)u)|y) det B_{y,u}(r/a) dr/a d mu_y(u).

On this integration domain, 0<r/a<c_y(u) and 0<r<c_y(u). In particular both normal Jacobi determinants are positive. Using the polar volume element det B_{y,u}(r) dr d mu_y(u) for z=Exp_y(ru), the last integral equals

integral_{U_t(y)\{y}} phi(z) p_{0|1}(H_t(z;y)|y) [det B_{y,u}(r/a)/(a det B_{y,u}(r))] d rho(z).

There is no mass at y in positive dimension: F_t is injective on M\C(y), its only preimage of y there is y, and the initial conditional law is absolutely continuous. This proves absolute continuity and the stated formula, with zero density outside U_t(y). No inverse is evaluated outside its domain. The calculation for phi=1 also proves that the resulting density integrates to one for every y.

A jointly measurable density representative, including its value at the center, can be chosen using the volume-Jacobian description in the next step. Thus the density represents the kernel Q_t, not merely separate unrelated measures for individual y.

### 4. Smoothness at the center, marginals, and boundary cases

For fixed y, let j_y(v) be the positive volume Jacobian of Exp_y at v in ID(y), using Euclidean volume on T_yM induced by g_y. It is smooth and positive on ID(y), including v=0. Since the curve s maps to Exp_y(sw) has initial velocity w, d Exp_y at zero is the identity; hence j_y(0)=1.

The Jacobi-field differential relation in L000897–L000900 gives, for a unit u and a normal vector w,

J_w(r)=d Exp_y at ru applied to r w.

In parallel orthonormal frames, the radial derivative of Exp_y is the unit radial velocity, while the normal block is B_{y,u}(r)/r. Therefore, for 0<r<c_y(u),

j_y(ru)=det B_{y,u}(r)/r^(d-1).

This identity is general; the later locally symmetric assumption in the source is needed for explicit closed-form evaluation, not for the differential identity. The determinant is positive before the cut time because the differential is nonsingular there and its sign agrees near zero with the initial Jacobi data.

For z in U_t(y), put v=Log_y z. Change of variables and the chain rule applied to H_t=Exp_y composed with multiplication by 1/a composed with Log_y show that its volume Jacobian is

JH_t(z;y)=a^(-d) j_y(v/a)/j_y(v).

All arguments lie in ID(y), so this is a smooth positive function on the entire open set U_t(y). For z different from y, substitution of the preceding normal-Jacobi identity gives

JH_t(z;y)=det B_{y,u}(r/a)/(a det B_{y,u}(r)),

exactly the factor already obtained by radial rescaling. At z=y it has value a^(-d).

Consequently a density representative on U_t(y) is

p_{t|1}(z|y)=p_{0|1}(H_t(z;y)|y)JH_t(z;y),

with zero extension outside U_t(y). For nonsmooth initial densities this is simply a measurable representative. Smooth joint dependence of the exponential/logarithm maps and their local volume factors, together with measurability of p_{0|1}, gives joint measurability in (z,y); the set of such pairs with z in U_t(y) is measurable by the open injectivity-domain description. If p_{0|1}(.;y) is smooth, the displayed product is smooth on all of U_t(y), including y. This argument does not claim that distance or the unit radial direction is smooth at y.

The unconditional law has a density for t<1 by mixing these kernels:

p_t(z)=integral_M p_{t|1}(z|y)p_1(y)d rho(y).

Tonelli's theorem verifies this identity and normalization. At t=1, X_t=X_1 almost surely, so the already prescribed density is p_1. At t=0, F_0 is the identity off the null cut locus and the Jacobian factor is 1; all conclusions recover the initial law. No conditional absolute-continuity assertion is made at t=1, and no smooth extension across the boundary of U_t(y) is claimed.

For d=1 the same proof applies with empty normal determinant 1. If dimension zero is admitted, connectedness and the existence of a probability density force M to be a single point, whose Riemannian volume is 1. Then C(y) is empty, ID(y)={0}, F_t is the identity, U_t(y)=M, and every probability density is 1. All conclusions hold directly, and there are no unit directions or points z different from y on which the polar formula must be evaluated.

## Obligation Closure

- Product-volume nullity and simultaneous smooth interpolation: proved by Tonelli and the audited complete-manifold geometry in Step 1.
- Correct contraction domain, open image, inverse, and cut-time equivalence: proved in Step 2.
- A normalized measurable conditional version for every endpoint: constructed and verified against the joint law in Step 3.
- The normal Jacobi determinant ratio, zero extension, absolute continuity, and total mass one: derived by the explicit polar substitution in Step 3.
- Smoothness at every point of the image, including the center: proved by the nonsingular volume-Jacobian calculation in Step 4.
- Marginal-density notation and temporal, dimensional, and infinite-cut-time cases: verified in Steps 2 and 4.

Every theorem-critical obligation is closed. There is no unresolved nonstandard dependency or private ground-truth gap.
