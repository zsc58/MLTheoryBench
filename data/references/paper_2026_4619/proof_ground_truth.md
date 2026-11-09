# Reference Proof

## Scope and proof obligations

This proof covers exactly the public range m>=6. It uses the source's message/code construction, with explicit verification of the parameter range needed after normalization. The obligations are: existence of the code and regularity of the loss; a sample event of probability at least 1/2; feasibility and empirical optimality of the explicit point; a population gap on that same event; and normalization and transfer to all approximate ERMs over the full stated curvature interval.

The only external result used is the following standard independent coding existence fact stated in the source: there is a universal rho in (0,1/2) such that, for every positive integer k, an injective map G:{-1,1}^k -> {-1,1}^{2k} exists with Hamming distance at least 2rho k between the images of distinct messages. We use only this existence and distance statement, not computational efficiency. Its hypothesis is satisfied by k=2m. All remaining obligations are derived below. In particular, the printed general exponential concentration inequality is not used.

## Step 1: Construction and regularity

Fix m>=6, put k=2m and d=3k=6m, and write w=(w^c,w^m) in R^{2k} x R^k. Choose the code just stated and put Gbar(v)=G(v)/sqrt(2k). Thus every normalized codeword has norm one, and, for distinct messages u,v,

<Gbar(u),Gbar(v)> <= 1-2rho < 1-rho/2.

For i in [k], let W_i={G(v):v(i)=1}. These are nonempty finite sets. For 0<zeta<=1 define

h^zeta(x,i)=max{zeta(1-rho/2), max_{y in W_i}<x,y/sqrt(2k)>}.

It is convex and 1-Lipschitz, being a finite maximum of affine functions whose slopes have norm at most one.

We first construct an unscaled loss for any auxiliary curvature 0<alpha<=7/sqrt(m). Set

beta=9/sqrt(m),
a=1/(2m),
b=min{1/(18m^{3/2}),alpha/3},
zeta=b/alpha.

All these quantities are positive. They satisfy

9/sqrt(m)<=beta<27/(2sqrt(m)),
a<=1/(2m),
b<=a/(9sqrt(m)),
alpha>=3b,
0<zeta<=1/3.

Take Z=[k] and let D be uniform on Z. Define delta_i(j)=1/m-2 if j=i and delta_i(j)=1/m otherwise. Put

p(w)=max_{v in {-1,1}^k}{a<v,w^m>-b<Gbar(v),w^c>},

and

tilde f(w,i)=h^zeta(w^c,i)-<w^m,delta_i>+max{p(w),0}+(beta/2)||w^m||^2+(alpha/2)||w^c||^2.

Write tilde F and tilde F_S for its population and empirical risks. Every term is convex. Since alpha<=7/sqrt(m)<beta, the block quadratic has strong-convexity modulus alpha, so each tilde f(.,i) is alpha-strongly convex.

The Lipschitz verification does not require the two quadratic coefficients to be at most one. Directly,

||delta_i||^2=4-2/m<=4.

Each nonzero affine branch of max{p,0} has slope norm sqrt(a^2 k+b^2), and

a^2 k+b^2 <= 1/(2m)+1/(324m^3) <= 9/(16m).

The block quadratic has gradient norm at most max{alpha,beta}=beta on W_d. Consequently tilde f is Lipschitz with constant at most

1+2+3/(4sqrt(m))+9/sqrt(m)=3+39/(4sqrt(m))<7,

where the last inequality holds already at m=6 and hence for all m>=6. All empirical and population objectives are continuous on the compact ball, so their minima are attained. Positive strong convexity gives uniqueness of every exact empirical minimizer.

## Step 2: The sample event and its deterministic consequences

Let N_i be the number of occurrences of i in S. Define

v_S=sum_{r=1}^m delta_{z_r}, so v_S(i)=1-2N_i,

and let s(i)=-1 when N_i>=1 and s(i)=1 when N_i=0. Then s(i)v_S(i)=|v_S(i)|>=1.

Uniformity of D and k=2m give E delta_z=0. Independence therefore gives

E||v_S||^2=sum_{r=1}^m E||delta_{z_r}||^2=4m-2.

For E={S:||v_S||<=3sqrt(m)}, Markov's inequality yields

P(E)>=1-(4m-2)/(9m)>5/9>1/2.

This is the only sample event used in the proof.

For every sample, G(s) is absent from W_{z_r} for every sampled index z_r. Conversely, G(s) belongs to W_i for every unobserved index i. At most m distinct indices are observed, so the fraction q_S of unobserved indices is at least (k-m)/k=1/2. Equivalently, conditional on any fixed sample, a fresh independent z~D satisfies P(G(s) in W_z | S)=q_S>=1/2. This is a probability inside a population expectation, not an additional event imposed on S.

## Step 3: The explicit empirical minimizer

Fix S in E and define

w_*^c=(b/alpha)Gbar(s),
w_*^m=(v_S/m-a s)/beta.

Its feasibility follows from

||w_*|| <= ||w_*^m||+||w_*^c||
<= (3/sqrt(m)+a sqrt(2m))/beta+b/alpha
<= 4/9+1/3=7/9<1.

For every sampled index i, every codeword in W_i is different from G(s). Hence

max_{y in W_i}<w_*^c,y/sqrt(2k)> < (b/alpha)(1-rho/2)=zeta(1-rho/2).

The constant branch of h^zeta(.,i) is therefore uniquely active at w_*^c, and its gradient there is zero.

For a message u, denote its affine link branch by

ell_u(w)=a<u,w^m>-b<Gbar(u),w^c>.

For each coordinate,

s(i)w_*^m(i)=(|v_S(i)|/m-a)/beta >= 1/(2m beta)>0.

If u differs from s in any coordinate, all differing coordinates contribute positively to <s-u,w_*^m>, and at least one contributes at least 1/(m beta). The possible code-term loss is at most 2b^2/alpha. Thus

ell_s(w_*)-ell_u(w_*) >= a/(m beta)-2b^2/alpha.

Using alpha>=3b, b<=a/(9sqrt(m)), and beta=9/sqrt(m), the right side is at least

a/(9sqrt(m))-2a/(27sqrt(m))=a/(27sqrt(m))>0.

The s branch also strictly exceeds the zero branch. Indeed, using one coordinate of the positive sum <s,w_*^m>,

ell_s(w_*) >= a/(2m beta)-b^2/alpha
= (1/2)(a/(m beta)-2b^2/alpha)>0.

This comparison is directly with the scalar zero branch; it does not introduce a message 0 or a normalized codeword Gbar(0), neither of which is defined.

It follows that max{p,0} is differentiable at w_* with gradient (-bGbar(s),a s). Since the empirical linear term is -<w^m,v_S>/m, the two gradient blocks of tilde F_S at w_* are

-bGbar(s)+alpha w_*^c=0,
-v_S/m+a s+beta w_*^m=0.

Thus the gradient of the convex empirical objective is zero at a feasible point. It is its global minimizer, and alpha-strong convexity makes this minimizer unique.

## Step 4: Population risk on the same sample event

Let H_0=zeta(1-rho/2). For every w, the mean-zero linear term disappears from the population objective, while h^zeta(w^c,i)>=H_0, max{p(w),0}>=0, and both quadratics are nonnegative. All these extra terms vanish at w=0 except the constant H_0. Therefore

tilde F(0)=H_0=min_{w in W_d} tilde F(w).

For an unobserved index i, the codeword G(s) belongs to W_i. At w_*^c=zeta Gbar(s), its correlation is zeta, and no unit normalized codeword can have greater correlation. Thus h^zeta(w_*^c,i)=zeta. For an observed index the constant branch is active, giving H_0. Consequently

E_{i~D} h^zeta(w_*^c,i)-H_0=q_S zeta rho/2>=zeta rho/4.

Dropping the other nonnegative population terms yields

tilde F(w_*)-tilde F(0) >= rho b/(4alpha)
= min{rho/(72alpha m^{3/2}),rho/12}.

No sample probability is lost in this calculation.

For completeness, if u is an epsilon_tilde-ERM of this unscaled instance, strong convexity and the zero empirical gradient at w_* give

||u-w_*||<=sqrt(2epsilon_tilde/alpha).

Its 7-Lipschitz population objective therefore satisfies

tilde F(u)-tilde F(0) >= min{rho/(72alpha m^{3/2}),rho/12}-7sqrt(2epsilon_tilde/alpha).

This proves the technical inequality on the entire auxiliary range 0<alpha<=7/sqrt(m), m>=6, rather than assuming an unavailable parameter extension.

## Step 5: Normalization and simultaneous approximate-ERM transfer

Now fix a public curvature lambda with m^{-3/2}<=lambda<=m^{-1/2}. In the construction set alpha=7lambda and define f=tilde f/7. The preceding verification applies, including both endpoints, because alpha<=7/sqrt(m). The normalized loss is 1-Lipschitz and lambda-strongly convex. Its risks are F=tilde F/7 and F_S=tilde F_S/7, and its exact minimizer is unchanged.

Here alpha>=7/m^{3/2}, so b=1/(18m^{3/2}). Put A=rho/3528. The exact population gap after normalization is

F(w_*)-F(0) >= (1/7)rho/(72alpha m^{3/2})=A/(lambda m^{3/2}).

Let u be any epsilon-ERM of the normalized loss. Its unscaled empirical error is at most 7epsilon. Equivalently, working directly with the normalized lambda-strongly convex objective gives

||u-w_*||<=sqrt(2epsilon/lambda).

Since F is 1-Lipschitz,

F(u)-min F >= A/(lambda m^{3/2})-sqrt(2epsilon/lambda).

Choose the universal constants

c=A^2/8 and C=A/2.

For every 0<=epsilon<=c/(lambda m^3), the last error term is at most A/(2lambda m^{3/2}), so

F(u)-min F >= C/(lambda m^{3/2}).

All these inequalities are deterministic once S belongs to E. They therefore hold simultaneously for every indicated epsilon and every corresponding approximate minimizer, without any union bound or algorithm-dependent choice of event.

## Step 6: The two public regimes and closure

The preceding step proves the full curvature-dependent statement. Taking lambda=m^{-3/2} in that same family gives curvature m^{-3/2}, accuracy threshold c m^{-3/2}, and excess risk at least C, proving the constant lower bound with the same constants.

The instance is chosen from m and lambda before sampling; d=6m, the observation space is finite, and the sample law is D^m. The good sample event has probability greater than 1/2. The endpoint m=6 and both curvature endpoints are covered by the explicit Lipschitz and curvature estimates. Epsilon=0 is included, and uniqueness for all samples follows from strong convexity independently of E. Every theorem-critical obligation is closed.

## Source-repair notes

The range and coefficient checks above repair the normalization gap between L000218 and L000223 and the unnecessary coefficient caps used at L000228-L000233. They also cover m=6 without the incorrect inequality asserted in L000220. The direct second-moment argument replaces the use of the erroneous general exponential bound at L000239 while preserving precisely the needed sample event. The positive-link comparison replaces the undefined zero-message normalization shorthand at L000342. None of these changes introduces a new public assumption or changes the source's ERM construction mechanism. The separate GD trajectory claim is not a dependency of this proof.
