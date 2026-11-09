# Reference Proof

## Proof Structure

1. Verify the weighted integral bounds and the Hilbert-space setting, express the kernel quadratic form as an integral of a square, and prove convexity.
2. Add the weighted L2 and gradient penalties to obtain strong convexity, coercivity, existence, and uniqueness. Derive the variational equation for every test in W.
3. Establish local Lipschitz regularity of the nonlocal forcing and apply explicitly stated interior elliptic estimates and embeddings in a finite bootstrap.
4. Use the full variational equation to prove linearity and both quantitative stability estimates, including differences.

## Complete Proof

All spaces and functions are real, and functions in the Lebesgue and Sobolev spaces are identified up to almost-everywhere equality. Set
\[
A=\|1+|x|\|_{L^2(D)},\qquad
B=\int_\Omega\frac{(1+|\theta|)^2}{\omega(\theta)}\,d\theta.
\]
The assumptions imply that A is finite and 0<=B<=c_omega. Weighted Cauchy-Schwarz gives, for every u in L2_omega,
\[
\int_\Omega(1+|\theta|)|u(\theta)|\,d\theta
\le \sqrt B\,\|u\|_{L^2_\omega}.
\]
Consequently the linear map T defined by Tu=f_u is well-defined and satisfies
\[
|Tu(x)|\le C_h(1+|x|)\sqrt B\,\|u\|_{L^2_\omega},\qquad
\|Tu\|_{L^2(D)}\le C_0\|u\|_{L^2_\omega},
\quad C_0=C_h A\sqrt B.
\]
Continuity of the activation ensures measurability of the feature and of the represented functions. These bounds also show that changing a representative of u does not change Tu.

The space W with the stated norm is Hilbert. Indeed, a Cauchy sequence in W converges in weighted L2 and its gradients converge in L2. Since omega>=1, the functions also converge in ordinary L2 to the same limit. Passing to the limit in the distributional derivative identities shows that the limiting gradient is the weak gradient of that limit. Thus the limit belongs to W and convergence holds in W.

The definitions of Q and K and the growth assumption give
\[
|Q(\theta)|\le C_h A\|f\|_2(1+|\theta|),\qquad
|K(\theta,\vartheta)|\le C_h^2A^2(1+|\theta|)(1+|\vartheta|).
\]
In particular, writing
\[
\|Q\|_{L^2_{\omega^{-1}}}^2
:=\int_\Omega\frac{|Q(\theta)|^2}{\omega(\theta)}\,d\theta,
\]
we have
\[
\|Q\|_{L^2_{\omega^{-1}}}\le C_0\|f\|_2.
\]
The same estimates imply absolute integrability of all kernel pairings used below. Fubini therefore gives, for u,v in W,
\[
\iint_{\Omega\times\Omega}K(\theta,\vartheta)u(\theta)v(\vartheta)\,d\theta d\vartheta
=\langle Tu,Tv\rangle_{L^2(D)},\qquad
\int_\Omega Qu=\langle f,Tu\rangle_{L^2(D)}.
\]
Taking v=u proves kernel positivity. Expanding the risk yields
\[
R(f,u)=\|f\|_2^2-2\int_\Omega Qu+\|Tu\|_2^2,
\]
so the risk is continuous and convex on W.

Let m=min(alpha,beta)>0. The functional
\[
F_{\alpha,\beta}^{(f)}(u)-m\|u\|_W^2
=R(f,u)+(\alpha-m)\|u\|_{L^2_\omega}^2
 +(\beta-m)\|\nabla u\|_2^2
\]
is convex. Thus F is 2m-strongly convex. Moreover,
\[
F_{\alpha,\beta}^{(f)}(u)\ge
\alpha\|u\|_{L^2_\omega}^2+\beta\|\nabla u\|_2^2
\ge m\|u\|_W^2,
\]
which proves coercivity. A minimizing sequence is bounded in the Hilbert space W and has a weakly convergent subsequence. The weighted inclusion, the gradient map, and T are bounded linear maps from W into their respective Hilbert spaces. Their images therefore converge weakly. Weak lower semicontinuity of squared Hilbert norms shows that all three terms in F are weakly lower semicontinuous, including the risk norm squared \(\|f-Tu\|_2^2\). The weak limit is a minimizer. Strong convexity makes it unique; denote it by u_f^*.

For every v in W, the real function t -> F(u_f^*+tv) has derivative zero at t=0. Dividing its derivative by two gives the full variational equation
\[
\beta\int_\Omega\nabla u_f^*\cdot\nabla v
+\alpha\int_\Omega\omega u_f^*v
+\langle Tu_f^*,Tv\rangle_{L^2(D)}
=\int_\Omega Qv,\qquad v\in W.
\tag{V}
\]
Every compactly supported smooth test belongs to W, since omega is bounded on its support. Applying (V) to such tests and using the kernel pairing proves the required distributional equation
\[
-\beta\Delta u_f^*+\alpha\omega u_f^*-Q
+\int_\Omega K(\cdot,\vartheta)u_f^*(\vartheta)\,d\vartheta=0.
\]
No boundary regularity assumption and no density of compactly supported tests in W have been used.

We next prove regularity. Define
\[
\ell(\theta)=-Q(\theta)
+\int_\Omega K(\theta,\tau)u_f^*(\tau)\,d\tau.
\]
For theta,eta in Omega intersected with B_R, the local feature assumption gives
\[
|Q(\theta)-Q(\eta)|
\le c_{h,R}A\|f\|_2|\theta-\eta|.
\]
Likewise,
\[
|K(\theta,\tau)-K(\eta,\tau)|
\le c_{h,R}C_h A^2(1+|\tau|)|\theta-\eta|.
\]
Integrating the second estimate against |u_f^*| gives
\[
|\ell(\theta)-\ell(\eta)|
\le c_{h,R}\left(A\|f\|_2+C_hA^2\sqrt B\,\|u_f^*\|_{L^2_\omega}\right)
|\theta-\eta|.
\]
The earlier growth estimates also make ell bounded on bounded parameter sets. Hence ell is locally Lipschitz and belongs to W^{1,infinity}_loc(Omega).

Here are the standard-independent interior results used in the bootstrap, in dimension n=d+1:

- For 1<p<infinity and k=0 or 1, if v belongs to Lp_loc and Delta v belongs to W^{k,p}_loc distributionally, then v belongs to W^{k+2,p}_loc. These are interior estimates on relatively compact nested sets and impose no condition on the boundary of Omega.
- The local Sobolev embedding W^{3,p} -> W^{1,q} holds for finite q>=p whenever 1/q>1/p-2/n.
- For p>n, the local Morrey embedding W^{3,p} -> C^{2,s} holds for 0<s<1-n/p.

The distributional equation is
\[
\beta\Delta u_f^*=\alpha\omega u_f^*+\ell.
\tag{E}
\]
Initially u_f^* belongs to W^{1,2}_loc. Smoothness of omega implies omega u_f^* belongs to W^{1,2}_loc, since omega and its first derivatives are bounded on compact subsets. The same is true of ell. Because beta>0, the k=1 interior estimate applied to (E) gives u_f^* in W^{3,2}_loc.

To make the iteration explicit, suppose u_f^* belongs to W^{1,p}_loc for some finite p>=2. Equation (E) first gives W^{3,p}_loc. If p<=n, choose q by
\[
\frac1q=\max\left\{\frac1p-\frac1n,\frac1{2n}\right\}.
\]
Then q>p and 1/q>1/p-2/n, so the stated Sobolev embedding gives W^{1,q}_loc. Ell belongs to W^{1,q}_loc and smooth multiplication preserves W^{1,q}_loc, so (E) gives W^{3,q}_loc. Starting at p=2, this procedure reaches a finite exponent P>n after finitely many iterations: the reciprocal exponent decreases by 1/n until it reaches 1/(2n), unless it has already become less than 1/n.

For this P>n, Morrey embedding makes u_f^* and its first derivatives locally bounded. Thus u_f^* belongs to W^{1,p}_loc for every finite p>1. Equation (E), with ell in W^{1,infinity}_loc and omega smooth, now gives
\[
u_f^*\in W^{3,p}_{\mathrm{loc}}(\Omega)
\qquad\text{for every finite }p>1.
\]
Given 0<s<1, choose p>n/(1-s). The Morrey embedding then gives u_f^* in C^{2,s}_loc. The representatives on overlapping interior sets agree, since they represent the same Sobolev function. In particular, the distributional equation also holds classically for this representative.

For linearity, retain the full variational equation (V). Its left side is a symmetric bilinear form in u_f^* and v, and Q is linear in f. A solution of its homogeneous version must vanish: testing with the solution itself gives a sum of nonnegative terms, including alpha times its weighted L2 norm squared. Thus (V) has at most one solution in W. The sums and scalar multiples of minimizers satisfy (V) for the sums and scalar multiples of their targets. Therefore
\[
u_{f_1+f_2}^*=u_{f_1}^*+u_{f_2}^*,\qquad
u_{cf}^*=c u_f^*\quad(c\in\mathbb R).
\]
This argument uses uniqueness of the full variational problem, not uniqueness of the distributional equation without a boundary condition.

Finally, test (V) with v=u_f^*. Set a=||u_f^*||_{L2_omega}, b=||grad u_f^*||_2, and q=||Q||_{L2_{omega^{-1}}}. Kernel positivity and weighted Cauchy-Schwarz give
\[
\alpha a^2+\beta b^2\le qa.
\]
If a=0, u_f^*=0 almost everywhere and its weak gradient is zero. Otherwise division gives a<=q/alpha. In both cases,
\[
\|u_f^*\|_{L^2_\omega}\le\frac{C_0}{\alpha}\|f\|_2.
\]
Substituting this bound into beta b^2<=qa gives
\[
\|\nabla u_f^*\|_2\le\frac{C_0}{\sqrt{\alpha\beta}}\|f\|_2.
\]
Taking C=1+C_0 provides a positive constant depending only on D, Omega, omega, and h, independent of alpha, beta, and f. Linearity implies u_{f_1}^*-u_{f_2}^*=u_{f_1-f_2}^*, so the same estimates prove both difference bounds.

If Omega is empty, W is the zero space and all claims are immediate. If D has zero measure, T and Q vanish and the unique minimizer is zero. These cases are also covered by the preceding estimates with the positive choice C=1+C_0. This closes every claimed conclusion.
