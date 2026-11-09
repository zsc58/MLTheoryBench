# Reference Proof

## Proof structure and obligations

We prove the following obligations explicitly: activation regularity and exact bounded-domain arithmetic; finite-table density and its network realization; active-cell addressing; local averaged-Taylor approximation with bounded coefficients; local network realization with the stated resource count, including degree zero; shifted gates with localization and finite-order derivative bounds; global network realization and Sobolev gluing; and extension, normalization, and affine rescaling. No paper-specific theorem is assumed as a black box.

Two standard independent analytic results are used. On a fixed cube, a bounded linear Sobolev extension operator maps W^{s,infinity} into W^{s,infinity}(R^d), with norm depending only on the finite order and the fixed cube. The Bramble--Hilbert averaged-Taylor estimate says that on an open bounded region star-shaped with respect to an averaging ball of radius at least half the supremal star-shaped radius, the order-r error seminorm of the degree-(s-1) averaged Taylor polynomial is at most C(s,d,gamma) h^{s-r}|f|_{W^{s,infinity}}, for 0<=r<=s. Here h is the diameter and gamma is the chunkiness. We verify this geometry below.

Throughout, n is fixed and every differentiation order is finite. Constants may depend on s,d,n, but never on the grid parameter K or a cell index. When n=infinity, constants controlling derivatives always include a finite derivative cutoff.

## 1. Activation primitives

Write sigma=sigma_n. Endpoint flatness of q_n shows that g_n, rho_n, and sigma are C^n, or C-infinity when n=infinity. The values and derivatives match at the displayed junctions; at zero both branches of sigma have vanishing derivatives through the required order. The definitions give

- sigma(t)=-2-1/t for -4<=t<=-13/11;
- sigma(t)=t for -1<=t<=-4/11;
- rho_n(u)=-sigma(-u-5)-14/5 for u>=0;
- sigma(t)=g_n(t) for t>0.

The linear interval realizes the identity on any prescribed bounded interval by an affine change of input and output. Applying this coordinatewise carries m bounded channels through any number of layers using width m. Thus subnetworks can be padded to equal depths on any fixed compact input domain. Every intermediate range used for padding is bounded because the subnetworks are continuous.

For |x|<=1 define

S(x)=-12 sigma(-2 sigma(x-3)-2 sigma(-x-3)-8)-15.

The first preactivations belong to [-4,-2]. Substitution of the rational branch makes the second preactivation -12/(9-x^2), which belongs to [-3/2,-4/3], again within the rational interval. A second substitution gives S(x)=x^2. This has width two and depth two. For M>0,

P_M(x,y)=2M^2[S((x+y)/(2M))-S(x/(2M))-S(y/(2M))]

therefore equals xy on [-M,M]^2 and has width six and depth two.

Sequential multiplication of d factors in [0,1], carrying unused factors by identity channels, has width at most d+4 and depth 2d-2; for d=1 the product is affine. For a positive integer a, x^a on [0,1] has width at most a+3 and depth at most 2a-2: a=1 is affine, a=2 uses S, and the induction multiplies x by x^{a-1} while carrying x. For a nonzero multi-index alpha of degree m, run the coordinate powers in parallel and then multiply them. Zero exponents give constant channels. This realizes x^alpha on [0,1]^d with width at most m+3d and depth at most 2m+2d-4. For d=1 this is the scalar construction; for d>=2 the product block fits because d+4<=m+3d. The monomial x^0=1 is affine and is handled separately below.

## 2. Finite-table density, without an unproved duality dependency

Fix a positive integer J and put z=2^{1/J}, b_i=1+i/J, and a_i=1/(z+b_i), for 1<=i<=J. These a_i are rationally independent. Indeed, a rational relation gives

P(z)=0,  P(X)=sum_i c_i product_{k!=i}(X+b_k),  deg P<=J-1.

The polynomial X^J-2 is irreducible by the elementary Eisenstein argument at 2: for J>1, a nontrivial monic integer factorization would reduce modulo 2 to two positive powers of X, making both constant terms even, contrary to their product being -2. The passage from rational to integer factors is Gauss's lemma. For J=1 the independence is immediate. Consequently P=0, and evaluation at X=-b_i forces c_i=0.

Here is a direct derivation of the torus-density consequence. Let a be any rationally independent real J-vector, and let H be the closure of {ta mod Z^J:t in R} in the torus. It is a closed subgroup. If H were proper, the translation-invariant torus metric would give a continuous, nonconstant, H-invariant function u(x)=dist(x,H).

A continuous function on this torus whose nonconstant Fourier coefficients all vanish is constant. To justify the assertion directly, use the one-dimensional kernels

F_R(t)=R^{-1}|sum_{k=0}^{R-1} exp(2 pi i k t)|^2.

They are nonnegative trigonometric polynomials of integral one. Outside any fixed neighborhood of the integers, the geometric-sum formula bounds F_R by a constant times R^{-1}. Products of these kernels in J coordinates therefore have integral one and mass tending to zero outside every neighborhood of zero. Uniform continuity shows that convolution with these products converges uniformly to any continuous function. Expanding the finite trigonometric polynomials shows that these convolutions are constant if all nonconstant Fourier coefficients vanish. This proves the assertion.

It follows that u has a nonzero Fourier coefficient at some nonzero m in Z^J. Translation invariance under h in H gives

u_hat(m)=exp(2 pi i m dot h) u_hat(m),

so exp(2 pi i m dot h)=1 for every h in H. Substituting h=ta gives exp(2 pi i t(m dot a))=1 for all real t, hence m dot a=0, a contradiction. Thus the real flow is dense in the torus.

Apply this to the vector (a_i/2). The map from the torus to [0,1]^J with coordinates g_n(2u_i) is continuous and onto, since g_n is continuous, two-periodic, and has range [0,1]. Hence the vectors (g_n(w a_i)) are dense in [0,1]^J.

For any desired table xi_i in [0,1] and any positive tolerance, choose w from this density statement. On 0<=x<=J, define

T(x)=sigma(w sigma(-z-1-x/J)+2w+2 floor(|w|)+2).

Its first preactivation belongs to [-4,-2]. The second is w/(z+1+x/J)+2 floor(|w|)+2, which is positive. Two-periodicity then gives T(i)=g_n(w a_i). Thus T is a width-one, depth-two table-fitting subnet. An affine output change fits arbitrary tables in any bounded interval. The length of the table changes only weights, not architecture.

## 3. Addressing active cells

For K>=1 set

I_k=[k/K,(2k+1)/(2K)],  0<=k<K,

and let Omega_K be the union of their d-fold product cells Q_i=product_j I_{i_j}. Norms on Omega_K in this proof mean maxima of Sobolev norms over the open cells, not distributional norms across their gaps.

On [0,1], set

A_K(t)=2K rho_n(t/2)-rho_n(Kt).

If t belongs to I_k, then rho_n(t/2)=t/2 and rho_n(Kt)=Kt-k, so A_K(t)=k. The identity for rho_n in Section 1 realizes this map with width two and depth one. Applying it coordinatewise and taking an affine combination gives the integer address

p(x)=sum_{j=1}^d K^{j-1} A_K(x_j).

On Q_i this is the unique integer p=sum_j i_j K^{j-1} in {0,...,K^d-1}. When K=1 there is just one cell and one address. Composing p+1 with the table subnet gives each coefficient readout with width at most 2d and depth three. On every open active cell the readout is exactly constant, including all its positive-order derivatives.

## 4. Local averaged-Taylor approximation and coefficients

Let H belong to W^{s,infinity}((0,1)^d), with norm at most M. Each open active cell has center x_i=((4i_j+1)/(4K))_j, side length 1/(2K), diameter sqrt(d)/(2K), and supremal star-shaped radius 1/(4K). Its chunkiness is 2sqrt(d). The closed Euclidean ball B_i of radius 1/(8K) at x_i lies inside the open cell and has half this supremal radius. These are precisely the Bramble--Hilbert hypotheses. The larger ball equal to the closed cell is an ell-infinity ball; there is no erroneous Euclidean-ball equality in the source.

Choose a nonnegative smooth unit-integral averaging bump on B_i and set

P_i(x)=integral_{B_i} sum_{|lambda|<=s-1} D^lambda H(y)(x-y)^lambda/lambda! b_i(y) dy.

Bramble--Hilbert gives, for 0<=r<=s,

||H-P_i||_{W^{r,infinity}(int Q_i)}<=C_{s,d} M K^{r-s}.

To pass from seminorms to this norm, apply the estimate to every derivative order j<=r and use K^{j-s}<=K^{r-s}, absorbing the fixed diameter factors into C_{s,d}.

Expanding (x-y)^lambda gives

P_i(x)=sum_{|alpha|<=s-1} c_{i,alpha} x^alpha,

where

c_{i,alpha}=sum_{|alpha+beta|<=s-1} integral_{B_i} D^{alpha+beta}H(y)(-y)^beta/(alpha! beta!) b_i(y) dy.

Because y belongs to (0,1)^d and the bump has integral one, |c_{i,alpha}|<=C_{s,d}M, uniformly in K and i. The formula and estimate use weak derivatives defined almost everywhere; no pointwise high-order representative is required.

## 5. Local networks and exact resource bounds

First take M<=1, and choose a positive coefficient bound C_0 depending only on s,d. Let

H_{s,d}=sum_{|alpha|<=s-1} max_{|beta|<=s-1} ||D^beta x^alpha||_{L^infinity((0,1)^d)}.

This is finite and at least one. Given delta>0, fit each coefficient table to absolute error less than min{C_0,delta/H_{s,d}}. The addressed readout, denoted c_alpha^net(x), is constant on every active cell. Therefore

||sum_alpha (c_alpha^net-c_{i,alpha})x^alpha||_{W^{r,infinity}(int Q_i)}<delta

for every 0<=r<=s-1. This also covers s=1 directly: only the constant monomial occurs.

On the active cells the coefficient readouts have magnitude at most 2C_0 and monomials have magnitude at most one. Use P_M with M>=max{1,2C_0} to multiply each nonconstant monomial by its readout. The resulting local network agrees with the polynomial expression on active cells; no identity outside those cells is needed. For alpha=0, output the coefficient readout directly, without a multiplier.

For m=|alpha|>0, the coefficient and monomial branches in parallel have width at most m+5d and depth at most max{3,2m+2d-4}. After multiplication, their width remains at most m+5d because m+5d>=6, and depth is at most max{5,2m+2d-2}. The degree-zero branch has width at most 2d and depth three, fitting its budget 5d. Identity padding equalizes depths on the compact unit cube.

Summing over alpha gives a local network B_{K,delta} with

W_loc=sum_{|alpha|<=s-1}(|alpha|+5d)
     =d(s+5d+4) binom(s+d-1,d)/(d+1)
     =4^{-d}N_{s,d}-d-4,

and depth

D_loc=max{2s+2d-4,5}.

The summation identity follows by grouping monomials by degree: their number is binom(s+d-1,d), and the sum of their degrees is d binom(s+d-1,d+1). Thus

||H-B_{K,delta}||_{W^{r,infinity}(Omega_K)}<=delta+C_{s,d}K^{r-s},  0<=r<=s-1.

For a target with norm at most a fixed C>=1, apply this result to H/C with tolerance delta/C and multiply the output by C. This gives delta+C'_{s,d}K^{r-s} with unchanged resources. In particular, the error tolerance is scaled as well as the function.

## 6. Shifted gates and their localization

Let F belong to W^{s,infinity}((0,1)^d), with norm at most one. By the cube extension theorem, choose an extension E F with W^{s,infinity}(R^d) norm at most a constant C=C(s,d)>=1. Fix an integer K>10. For nu in {1,2,3,4}^d put

tau_nu=nu/(4K),  F_nu(y)=E F(y-tau_nu),

and

G_nu(x)=product_{j=1}^d g_n(2Kx_j+nu_j/2).

The shifted targets have norm at most C on the unit cube, uniformly in K and nu. Apply Section 5 with delta=K^{-s}, including its normalization, to obtain B_nu for F_nu. Set A_nu(x)=B_nu(x+tau_nu).

The four half-period translates of g_n sum to one. To check this, for t in [0,1/2] the nonzero pair is q_n(2t) and 1-q_n(2t); the sum is invariant under translation by 1/2. Taking products gives sum_nu G_nu=1. Also 0<=G_nu<=1.

For each finite cutoff m<=n,

D^gamma G_nu(x)=(2K)^{|gamma|} product_j g_n^{(gamma_j)}(2Kx_j+nu_j/2),

so

||D^gamma G_nu||_infinity<=C_{n,d,m}K^{|gamma|},  |gamma|<=m.

All constants are finite because the derivatives are continuous and periodic. For n=infinity we use only m=s-1, not a nonexistent constant uniform over every derivative order.

For x in [0,9/10]^d, K>10 ensures x+tau_nu belongs to (0,1)^d. If a coordinate of this shifted point lies outside the active intervals, its gate is identically zero in a neighborhood. At active-interval endpoints, the gate and its derivatives through order n vanish. Consequently, except for cell boundaries of measure zero, whenever D^gamma G_nu(x) is nonzero, x+tau_nu lies inside an active cell. The local estimate for B_nu is valid there.

For x>=0 coordinatewise, every gate preactivation 2Kx_j+nu_j/2 is positive, so one activation layer produces the d one-dimensional gates. Sequential multiplication as in Section 1 realizes G_nu with width at most d+4 and depth 2d-1.

## 7. Global realization and the Sobolev estimate

On D=[0,9/10]^d, the continuous network A_nu has a finite supremum. Choose M_nu>max{1,sup_D |A_nu|}. This bound may depend on K and the fitted table parameters; the theorem places no constraint on these weights. The exact multiplier P_{M_nu} then realizes A_nu G_nu throughout D, including points outside the active region. This full-domain choice is needed because a bounded-domain multiplier is not automatically exact on arbitrary network outputs.

Run A_nu and G_nu in parallel, pad with identity channels, and append the multiplier. Their parallel width is at most W_loc+d+4=4^{-d}N_{s,d}, which is at least six. The depth after multiplication is

max{D_loc,2d-1}+2=max{2s+2d-2,2d+1,7}=L_{s,d}.

Run all 4^d branches in parallel and sum affinely. The resulting network Psi_K has width at most N_{s,d}, depth at most L_{s,d}, and equals sum_nu A_nu G_nu on D. Input and output layer sizes also lie below the width bound.

These are globally C^n networks. On compact sets their derivatives through s-1<=n are bounded, so the following are genuine Sobolev derivatives. The target F has a Sobolev extension, and multiplication by the smooth gates obeys the weak Leibniz rule. Thus no passage from a merely cellwise derivative to a global derivative is being assumed.

For |alpha|<=s-1, the partition identity and localization give, almost everywhere on the interior of D,

|D^alpha(Psi_K-F)|
 <=sum_nu sum_{beta<=alpha} binom(alpha,beta)
   |D^{alpha-beta}G_nu| |D^beta(A_nu-F)|
 <=C_{s,d,n} sum_{beta<=alpha} K^{|alpha|-|beta|}
   (K^{-s}+K^{|beta|-s})
 <=C'_{s,d,n} K^{|alpha|-s}
 <=C'_{s,d,n} K^{-1}.

Here all shifted target identities hold almost everywhere, and the finite union of shifted cell boundaries is null. Taking the maximum over the finitely many alpha yields

||Psi_K-F||_{W^{s-1,infinity}((0,9/10)^d)}<=C'_{s,d,n}/K.

Choosing K>10 sufficiently large gives any prescribed positive tolerance on this subcube. Dependence of K on the fixed n is allowed; neither width nor depth changes with K.

## 8. Arbitrary cube, arbitrary norm, and zero target

Let ell=b-a>0 and mu=10ell/9. Define T(z)=a times the all-ones vector+mu z, mapping (0,9/10)^d onto (a,b)^d. If f=0 as a Sobolev element, a network with zero affine output suffices.

Otherwise f composed with T belongs to W^{s,infinity}((0,9/10)^d). Extend this pulled-back function to a function H in W^{s,infinity}(R^d). The extension theorem on the fixed subcube gives a finite positive normalization bound

lambda=C_{s,d} max{1,mu^s} ||f||_{W^{s,infinity}((a,b)^d)}>0

such that ||H||_{W^{s,infinity}(R^d)}<=lambda. Apply Section 7 to H/lambda restricted to (0,1)^d, with tolerance strictly smaller than

epsilon/(lambda max{1,mu^{1-s}}).

This extension step is essential: simply changing inputs of an approximant to F on the smaller cube would approximate a rescaled F, not the original target on the larger cube.

Set Phi(x)=lambda Psi(T^{-1}(x)). Input and output affine maps are absorbed into the existing affine layers. For |alpha|<=s-1 the chain rule contributes the factor mu^{-|alpha|}, and H composed with T^{-1}=f almost everywhere on (a,b)^d. Therefore

||Phi-f||_{W^{s-1,infinity}((a,b)^d)}
 <=lambda max{1,mu^{1-s}}
   ||Psi-H/lambda||_{W^{s-1,infinity}((0,9/10)^d)}
 <epsilon.

The width and depth remain at most N_{s,d} and L_{s,d}. This proves every finite-order case, including s=1 and n=infinity.
