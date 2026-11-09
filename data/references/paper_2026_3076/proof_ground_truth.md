# Reference Proof

Write w=omega_* and r=r_{n,fit}. All function evaluations below use the measurable versions specified in the task. Constants C may change from line to line and depend only on R, B_0, B_+, and, where used, m_*.

## Population argument

One-step coverage propagates to every d_0 P_pi^t: if nu(A)=0, then P_pi(A|x)=0 for nu-almost every x and hence for every measure dominated by nu. Thus d_* is dominated by nu. Its measure recursion gives Bw=w and, for every bounded measurable g,

E_nu[(Bf)g]=(1-gamma)E_{d_0}g+gamma E_{Q_{nu,pi}}[f(X)g(X^+)].

For f,g in Delta_nu, joint convexity of relative entropy for the common d_0 component, followed by Markov-kernel data processing, yields D_nu(Bf||Bg)<=gamma D_nu(f||g). These are the standard inequalities D((1-t)a+tb||(1-t)a+tc)<=tD(b||c) and D(bP||cP)<=D(b||c), applied to probability measures. In particular, D_nu(Bf||w)<=gamma D_nu(f||w).

Center H to H^circ. This is a compact convex subset of L_2(nu), and its elements are bounded in absolute value by R on the stipulated common full-measure set. For h in H^circ, e^{-2R}<=omega_h<=e^{2R}. If f belongs to W, u=Bf is a probability density bounded by B_0+e^{2R}B_+. The objective F_u(h)=Lambda_nu(h)-E_nu[uh] is continuous on compact H^circ and attains its minimum. Its minimizer h_u and bar u=omega_{h_u} satisfy, for every g in H^circ, E_nu[(bar u-u)(g-h_u)]>=0. Expanding the three divergences therefore gives

D_nu(bar u||omega_g)<=D_nu(u||omega_g)-D_nu(u||bar u).

This also verifies the hypotheses of the information-projection inequality without assuming that W itself is convex as a set of densities.

To quantify approximation, fix v in W and put a=||log w-log v||_{L_2(nu)}. Expanding the preceding inequality around w gives

D_nu(bar u||w)<=D_nu(u||w)+E_nu[(u-bar u)(log w-log v)]-D_nu(u||bar u).

Because u is bounded and bar u lies in [e^{-2R},e^{2R}], the scalar inequality t log t-t+1>=c(t-1)^2 on the compact interval 0<=t<=e^{2R}(B_0+e^{2R}B_+) implies D_nu(u||bar u)>=c'||u-bar u||_{L_2(nu)}^2. Cauchy-Schwarz and ab-c'b^2<=a^2/(4c') bound the final two terms by Ca^2. Take the infimum over v and use contraction to obtain

D_nu(T_W^KL f||w)<=gamma D_nu(f||w)+C_app epsilon_KL^2.

All divergences used here are finite: u and class densities are bounded, while log w belongs to L_2(nu). Iterating this inequality proves part 1, including K=0.

## Uniform fitted-process argument

Set a_n(delta)=r^2+log(1/delta)/n. The following details establish the uniform event needed for the data-dependent iterations. The bounded centered difference class H_Delta and product class G_times are star-shaped: scaling a log difference scales a member of either class while retaining its other index. Consequently C_n(s)/s is nonincreasing. Their bounded envelopes ensure that the fixed-point set defining r is nonempty. The definition of r and this scaling imply, for fixed A,b>0, that C_n(At)<=bt^2 whenever t>=L_{A,b}r, and C_n(A)<=C_A r. These claims follow by choosing a fixed-point radius no larger than 2r and scaling upward; below that radius use monotonicity of C_n.

The empirical denominators have the deterministic lower bound P_{n,X}f>=e^{-2R} for every f in W. Uniform denominator deviations are also controlled. Taking 0 in H^circ as a reference, symmetrization and the standard Lipschitz Rademacher contraction inequality applied to omega_h-1 give an expected supremum bounded by C R_n(H_Delta,C;nu)+C/sqrt(n). The standard bounded-class maximal inequality, whose deviation is at most a constant times sqrt(u/n)+u/n here, and critical-radius scaling therefore give

sup_{f in W}|(P_{n,X}-nu)f|<=C{r+sqrt(u/n)+u/n}

with probability at least 1-e^{-u}. Likewise, apply contraction to e^h-1 and use that both empirical and population averages of e^h are between e^{-R} and e^R. Bounded-class concentration gives

sup_{h in H^circ}|widehat Lambda_n(h)-Lambda_nu(h)|<=C{r+sqrt(u/n)}

with probability at least 1-e^{-u}; when u>n the deterministic bound 2R absorbs the larger deviation term. These standard empirical inequalities apply to measurable bounded classes; the common envelope and measurable suprema are specified in the task.

For f in W let h_f^* minimize L_f(h)=Lambda_nu(h)-(1-gamma)E_{d_0}h-gamma E[f(X)h(X^+)] on H^circ, and put Delta_f(h)=L_f(h)-L_f(h_f^*). Projection first-order optimality and the second derivative Var_{omega_{h_t}}(h-h_f^*) along the segment h_t=h_f^*+t(h-h_f^*) show

||h-h_f^*||_{L_2(nu)}^2+||e^h-e^{h_f^*}||_{L_2(nu)}^2+E_{d_0}(h-h_f^*)^2+E[f(X)^2(h-h_f^*)(X^+)^2]<=C Delta_f(h).

Here centering and omega_{h_t}>=e^{-2R} give the first term; B_0, B_+, and f<=e^{2R} give the last two. Thus the differences on a shell Delta_f(h)<=t^2 have the localized L_2 radii required by the four terms of C_n.

For completeness, decompose the centered empirical-loss difference at h and h_f^* into its initial-sample term, self-normalized transition term, and log-partition term. The initial term is indexed by H_Delta under d_0. For q=h-h_f^*, the transition term equals

{(P_{n,+}-Q_{nu,pi})[f(X)q(X^+)]-E[f(X)q(X^+)](P_{n,X}f-1)}/P_{n,X}f.

The first numerator is indexed by G_times under Q_{nu,pi}; on the shell its second moment is at most Ct^2. The second numerator is bounded using |E[fq(X^+)]|<=Ct and the uniform denominator deviation. For the log partition, integrate its derivative along h_s=h_f^*+s q. The derivative difference is

{(P_{n,X}-nu)[omega_{h_s}q]-E_nu[omega_{h_s}q](P_{n,X}omega_{h_s}-1)}/P_{n,X}omega_{h_s}.

Its first numerator is indexed by G_times under Q_{nu,Delta}, with second moment at most Ct^2, and its second is controlled as above. Each centered shell class has a bounded envelope. Symmetrization, Rademacher contraction where a Lipschitz transform occurs, and the bounded-class maximal inequality therefore yield, simultaneously over f and h on that shell, a bound of the form

C{C_n(Ct)+tr+t sqrt(u/n)+u/n}

except on an event of probability at most 5e^{-u}. All four local complexities in the task are used here. Choose t at least a sufficiently large multiple of r, apply critical-radius scaling and Young's inequality, and peel over dyadic shells of Delta_f(h). Assign failure exponents log(C/delta)+2j log 2 to shell j. The geometric failure sum is at most delta, and j/n is absorbed by a small multiple of the shell excess plus Cr^2 because r^2>=1/n. The inner shell is absorbed into Ca_n(delta). The resulting uniform event satisfies, for every f in W and h in H^circ,

|{widehat L_f(h)-L_f(h)}-{widehat L_f(h_f^*)-L_f(h_f^*)}|<=Delta_f(h)/4+C a_n(delta).

The exact empirical minimizer exists by the operative assumption in the task. Its input can be rescaled by a positive constant without changing the self-normalized objective. Hence, for f equal to the population normalization of any fitted input, exact ERM and the last display give Delta_f(widehat h)<=C a_n(delta). Uniformity, rather than conditioning on a fitted iterate, makes this valid at every iteration on one event.

Here is the needed approximate-projection conversion. Put bar u=T_W^KL f and tilde u=omega_{widehat h}. Projection optimality implies D_nu(bar u||tilde u)<=Delta_f(widehat h). Both densities lie in [e^{-2R},e^{2R}], so comparison of scalar KL with a squared difference gives D_nu(tilde u||bar u)+E_nu[(tilde u-bar u)^2/bar u]<=C Delta_f(widehat h). Since w>=m_*, the scalar bound t(log t)^2<=C(t log t-t+1) on 0<=t<=e^{2R}/m_* gives E_nu[bar u(log(bar u/w))^2]<=C D_nu(bar u||w). Expanding D_nu(tilde u||w) around bar u, applying Cauchy-Schwarz to the cross term and then Young's inequality, proves, for lambda>0,

D_nu(tilde u||w)<=(1+lambda)D_nu(bar u||w)+C(1+lambda^{-1})Delta_f(widehat h).

## Iteration and empirical normalization

For each k define f_k=widehat omega^(k)/E_nu widehat omega^(k). The initialization is f_0=1 in W; every subsequent f_k belongs to W because it is the population normalization of an exponential fitted output. Self-normalization gives widehat L_{widehat omega^(k)}=widehat L_{f_k}. Intersect the uniform excess-loss and normalizer events, each at failure probability delta/2. Their definitions and bounds are independent of K.

Combining approximate projection with the population inequality gives

D_nu(f_{k+1}||w)<=(1+lambda)gamma D_nu(f_k||w)+C(1+lambda)epsilon_KL^2+C(1+lambda^{-1})a_n(delta).

For gamma>0 choose lambda=min{1,(rho-gamma)/(2gamma)}, and for gamma=0 choose lambda=1. Then (1+lambda)gamma<=rho, 1+lambda<=2, and 1+lambda^{-1}<=C/(rho-gamma). Thus

D_nu(f_K||w)<=rho^K D_nu(1||w)+C epsilon_KL^2/(1-rho)+C a_n(delta)/{(rho-gamma)(1-rho)}.

For K>=1 let ell_k=widehat Lambda_n(widehat h_k)-Lambda_nu(widehat h_k). Then widehat omega^(k)=e^{-ell_k}f_k, |ell_k|<=2R, and the normalizer event gives ell_k^2<=C a_n(delta). Direct expansion, using E_nu f_k=E_nu w=1, shows

D_nu^gen(e^{-ell_k}f_k||w)=e^{-ell_k}D_nu(f_k||w)-ell_k e^{-ell_k}-e^{-ell_k}+1<=e^{2R}D_nu(f_k||w)+C ell_k^2.

Apply this after, not inside, the population-normalized recursion. Since 1-rho=rho-gamma=(1-gamma)/2, the claimed bound follows with constants depending only on the specified parameters. At K=0 it holds directly because widehat omega^(0)=f_0=1 and C_fit can be chosen at least one. The same uniform event establishes all K>=0 simultaneously.
