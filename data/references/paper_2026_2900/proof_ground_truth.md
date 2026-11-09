# Reference Proof

## Contract and Obligations

The claim is at each fixed time, not a uniform-in-time or time-averaged assertion. The score is exactly the score of the marginal used in both objectives. The obligations are: (1) establish integrability of the mixed term and directional derivative; (2) justify vanishing of the boundary flux weighted by the scalar head in both model settings; (3) apply the product rule and divergence theorem and pass to the limit; (4) establish the exact risk identity and its minimizer consequences.

The standard-independent result recorded as theory_012 is the divergence theorem: for a C1 vector field F on a neighborhood of the closed ball B_R, the integral of div F over B_R equals the integral of its outward normal component over the boundary. In dimension one this is the fundamental theorem of calculus. We also use dominated convergence in its usual form: pointwise convergence to zero together with an integrable absolute envelope implies convergence of the integrals to zero. The relevant regularity and envelopes are verified below.

## Complete Proof

Fix t and suppress t in p, s, v, r and b. Write m=m_t, h=q+m, and k=D-1+h. Set (a,tau)=(nu_t,eta_t) in setting (D), and (a,tau)=(alpha_t,sigma_t) in setting (F). Thus tau>0 and

p(x)=E[phi_tau(x-aY)],

where phi_tau(z)=(2*pi*tau^2)^(-D/2) exp(-||z||^2/(2*tau^2)). All constants below may depend on this fixed time, D, the growth degrees and bounds, and the chosen delta, but not on R or Y.

### 1. Integrability

The assumed k-th target moment implies the h-th target moment because k>=h. The mixture representation is the law of aY+tau Z, with Z standard Gaussian independent of Y. For integer h>=0,

(1+||aY+tau Z||)^h <= C[(1+||Y||)^h+(1+||Z||)^h].

The Gaussian moment on the right is finite: in polar coordinates its tail integral is bounded by a polynomial times exp(-rho^2/2), which is integrable. Consequently E_p[(1+||X||)^h]<infinity. The growth assumptions then give

E_p[|<grad delta,v>|] <= C E_p[(1+||X||)^h] < infinity.

Also delta and r belong to L2(p), so Cauchy-Schwarz gives E_p[|delta r|]<infinity. The regression risk is finite since (delta-r)^2<=2delta^2+2r^2. Hence every term used in the risk expansion and the limiting mixed-term identity is integrable.

### 2. Weighted Boundary Flux

Let B_R be the ball of radius R and n its outward unit normal. For R>=1, define

J_R = integral_{partial B_R} |delta(x)| p(x) ||v(x)|| dS.

The growth bounds, the surface area of the sphere, the mixture formula, and the reverse triangle inequality imply

J_R <= C R^(D-1)(1+R)^(q+m) E[exp(-(R-|a| ||Y||)^2/(2*tau^2))]
    <= C E[R^k exp(-(R-|a| ||Y||)^2/(2*tau^2))].

This uses nonnegative integrands, so exchanging the surface integral and the mixture expectation is justified by Tonelli's theorem. For D=1 the boundary consists of two points with counting surface measure, and the same estimate holds with R^(D-1)=1.

For a fixed y, set u=|a| ||y|| and z=R-u. The integrand R^k exp(-z^2/(2*tau^2)) tends to zero as R tends to infinity. If k>=1, R<=u+|z| yields

R^k exp(-z^2/(2*tau^2))
 <= C_k[u^k exp(-z^2/(2*tau^2))+|z|^k exp(-z^2/(2*tau^2))]
 <= C_{k,tau}(1+u)^k.

The last inequality follows because a polynomial times a Gaussian exponential is bounded on the real line. If k=0, the integrand is at most 1, so the same conclusion holds. Finally, (1+|a| ||Y||)^k<=C_a(1+||Y||)^k, whose expectation is finite by hypothesis. Dominated convergence therefore gives J_R->0. In particular,

|integral_{partial B_R} delta p <v,n> dS| <= J_R -> 0.

This argument applies to both settings with their respective a and tau. It does not assert that an arbitrary Gaussian mixture has Gaussian unconditional tails. It remains valid when a=0, when either growth degree is zero, and in dimension one. No lower variance bound uniform in time is used.

### 3. Mixed-Term Identity

Since p>0 and s=grad log p, we have p s=grad p. On every finite ball, the product rule gives

p delta r = delta div(pv) = div(p delta v)-p<grad delta,v>.

The vector field p delta v is C1 on all of R^D, so it satisfies the hypotheses of theory_012 on every closed ball. Therefore

integral_{B_R} p delta r dx
 = integral_{partial B_R} delta p <v,n> dS
   - integral_{B_R} p<grad delta,v> dx.

The boundary term tends to zero by Step 2. The two volume integrands are absolutely integrable by Step 1, so their integrals over expanding balls converge to their whole-space integrals. Thus

E_p[delta r] = -E_p[<grad delta,v>].

No separate global integrability of the two summands defining r is needed: their sum is used on each compact ball, and delta r is integrable globally.

### 4. Risks and Minimizers

Expanding the finite regression risk and substituting Step 3 gives

E_p[(delta-r)^2]
 = E_p[delta^2]-2E_p[delta r]+E_p[r^2]
 = E_p[delta^2+2<grad delta,v>]+E_p[r^2]
 = L_t(delta)+E_p[r^2].

The constant is independent of delta. Thus the two objectives have identical minimizer sets over H, including the possibility that both minimizer sets are empty. No existence assertion is made merely from this equivalence.

If r_t belongs to H, choosing delta=r_t gives zero regression risk, its minimum possible value. Hence a minimizer exists, and every minimizer satisfies E_{p_t}[(delta_t^*-r_t)^2]=0. This is recovery in L2(p_t), unique up to p_t-null sets. The defining decomposition then gives

b_t+delta_t^*=-<v_t,s_t>+r_t=div v_t

p_t-almost surely. These conclusions hold for each permitted t in both settings; no common null set across times is asserted.

## Source-Local Corrections

The appendix's diffusion calculation must use x=R n, so <f_t(x),n>=-beta_t R/2 for the VP/sub-VP drift. Its conditional Gaussian-gradient component is

<grad p_t(x|y),n>=-p_t(x|y)(R-nu_t<y,n>)/eta_t^2.

The source omits R in both places. These are local algebraic corrections, not additional hypotheses. The factors R^(D-1) in its spherical discussion belong to surface measure. The proof above keeps all polynomial factors explicitly and completes the mixture limiting argument with an integrable envelope. All four theorem-critical obligations are closed.
