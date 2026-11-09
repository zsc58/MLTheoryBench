# Reference Proof

## Contract and proof obligations

All probabilities and expectations are under the joint law of the observed sequence. The predictive kernels are the fixed measurable versions in the public setup. No exchangeability or future-covariate independence is assumed. The target is the finite-grid limiting predictive vector, not a fixed frequentist parameter.

The obligations are: (1) construct the limiting random probability kernel and identify its grid evaluations; (2) prove covariance consistency, including all weights and index shifts; (3) establish the conditional Gaussian limit using a uniformly integrable martingale tail, vanishing maximal increments, realized quadratic variation, and conditional negligibility of the drift; (4) pass to the multivariate conditional kernel on one probability-one event; and (5) prove conditional studentization and coverage of the defined sets. Each obligation is discharged below.

## Independent probability results used

We use ordinary bounded-martingale convergence, convergence of conditional expectations along an increasing filtration, weak compactness/tightness in finite-dimensional Euclidean space, and the continuity-set characterization of weak convergence.

The external conditional martingale-array CLT recorded in theory_008 is used in its nested-tail setting. For each n, let M_{n,j} be a real martingale for F_{n,j}, starting at zero and converging in L1 to M_{n,infinity}. Write X_{n,j}=M_{n,j}-M_{n,j-1}. If sup_j|X_{n,j}| tends to zero almost surely and is bounded by an integrable random variable, and sum_j X_{n,j}^2 tends almost surely to a finite nonnegative S, its terminal conditional laws tend almost surely to N(0,S). Our initial sigma-algebra is F_{n,0}=F_{n,1}=G_n, and the row filtrations are the compatible nested tail filtrations displayed below.

The external weighted law recorded in theory_009 states the following. Suppose W_k is G_k-adapted, E[W_{n+1}|G_n] tends almost surely to W, c_k,d_k are positive deterministic numbers, d_k increases to infinity, and sum_k E[W_k^2]/(c_k^2 d_k^2) is finite. If d_n^{-1}sum_{k<=n}c_k^{-1} tends to c, then d_n^{-1}sum_{k<=n}W_k/c_k tends almost surely to cW. If instead d_n sum_{k>=n}(c_k d_k^2)^{-1} tends to c, then d_n sum_{k>=n}W_k/(c_k d_k^2) tends almost surely to cW.

## 1. Limiting predictive kernel

Fix x and t, write b_k(x,t)=E[Delta_k(x,t)|G_{k-1}], A_n(x,t)=sum_{k=1}^n b_k(x,t), and

M_n(x,t)=F_n(x,t)-F_0(x,t)-A_n(x,t).

This is a martingale starting at zero. Its increments are F_n(x,t)-E[F_n(x,t)|G_{n-1}], bounded in absolute value by one. The signed-tail assumption says that the drift series converges almost surely. Because F_n(x,t) lies in [0,1], the paths of M_n(x,t) are almost surely bounded.

This is not a claim that M_n has one deterministic bound. For an integer C, stop it at the first time its absolute value exceeds C. The stopped process is bounded by C+1 and therefore converges almost surely. On the event sup_n|M_n|<C it agrees with the unstopped process. Taking the union over C proves convergence of M_n, and hence of F_n(x,t), almost surely.

Choose a countable dense subset D of the covariate space. Intersect the convergence events for x in D and rational thresholds, together with the equicontinuity events for those thresholds. If a rational threshold lies outside the response space, compactness implies that its CDF evaluation is either constant or equals evaluation at the largest response-space point below it, so the source's equicontinuity assumption on response thresholds suffices. On this common event, for every rational q and every covariate x, equicontinuity extends convergence from D to x. Indeed, choose r in D close enough to x that sup_n|F_n(x,q)-F_n(r,q)| is small and then use convergence at r to make F_n(x,q) Cauchy. Denote the resulting limit by h(x,q).

Define H(x,t)=inf_{q>t, q rational}h(x,q). It is nondecreasing and right-continuous in t. Compact response support supplies the limits zero and one at the two ends of the real line. The functions h(x,q) are measurable limits, and the infimum is countable, so H is jointly measurable in the random outcome and covariate for each t. On the exceptional null event choose any fixed probability measure supported on the nonempty response space. Thus H is the CDF of a random probability kernel supported on that space.

For a continuity point t of H(x,·), rational bracketing proves F_n(x,t) tends to H(x,t). To keep the raw rational limits distinct from the right-continuous modification, choose u<r<t<s with r,s rational, H(x,u)>H(x,t)-epsilon, and H(x,s)<H(x,t)+epsilon. Then h(x,r)>=H(x,u) and h(x,s)<=H(x,s), giving the desired lower and upper bounds on the limit inferior and limit superior. This proves weak convergence for every x on the same probability-one event. Write this limiting CDF as tilde F(x,t).

For each grid coordinate, continuity of t↦E[tilde F(x_i,t)] at t_i implies

E[tilde F(x_i,t_i)-tilde F(x_i,t_i-)]=0.

The jump is nonnegative, so it is zero almost surely. Consequently the grid vector bold F_n converges almost surely to bold tilde F. This also explains why pointwise convergence at arbitrary discontinuity thresholds was not inferred from weak convergence.

## 2. Covariance consistency

Fix u in R^m and put delta_k=u^T Delta_k. The coordinatewise fourth-moment assumption implies

sum_k k^{2gamma} E[delta_k^4]<infinity,

by the finite-dimensional inequality |sum_i u_i a_i|^4 <= (sum_i|u_i|)^3 sum_i |u_i||a_i|^4. The zero projection is immediate.

Set W_k=k^{gamma+1}delta_k^2/gamma. This variable is G_k-measurable, unlike a definition using Delta_{k+1} at index k. For k>=2,

E[W_k|G_{k-1}]=(k/(k-1))^{gamma+1} u^T U_{k-1}u -> u^T V u.

For the tail conclusion choose d_k=k^gamma and c_k=k^{1-gamma}/gamma. Then

sum_k E[W_k^2]/(c_k^2 d_k^2)=sum_k k^{2gamma}E[delta_k^4]<infinity,

and d_n sum_{k>=n}(c_k d_k^2)^{-1}=gamma n^gamma sum_{k>=n}k^{-gamma-1}->1. The weighted law yields n^gamma sum_{k>=n}delta_k^2 -> u^T V u. In addition, Tonelli's theorem gives sum_k k^{2gamma}delta_k^4<infinity almost surely, so n^gamma delta_n^2->0. Removing that one term proves u^T R_n u -> u^T V u. The nonnegative series is finite almost surely; cross-coordinate series are then absolutely convergent by Cauchy-Schwarz.

For the average conclusion use d_k=k and c_k=1 with the same W_k. The summability condition becomes gamma^{-2}sum_k k^{2gamma}E[delta_k^4]<infinity, and n^{-1}sum_{k<=n}1=1. Thus u^T V_nu -> u^T V u.

Apply these arguments to the finitely many vectors e_i and e_i+e_j. Polarization recovers every matrix entry on one probability-one event, proving R_n->V and V_n->V. Convergence U_n->V is the stated hypothesis. All three convergences are ordinary almost-sure matrix convergence, not distributional convergence of the matrices.

## 3. Martingale tail and conditional scalar CLT

Fix u and put Z_n=u^T bold F_n, delta_k=Z_k-Z_{k-1}, d_k=E[delta_k|G_{k-1}]=u^T b_k, and A_n=sum_{k=1}^n d_k. All projection drift assumptions and their integrable envelopes follow by finite linear combinations; the squared-drift condition follows by Cauchy-Schwarz in the finite coordinate index.

Let T_n=sum_{k>n}d_k and r_n=n^{gamma/2}T_n. By assumption, r_n->0 almost surely and |r_n| is bounded by an integrable random variable. Therefore T_n->0 in L1. The total drift sum is integrable because it equals d_1+T_1. It follows that A_n converges almost surely and in L1 and is uniformly integrable.

Define L_n=Z_n-A_n, with A_0=0 and L_0=Z_0. This corrects the source's harmless initial-value inconsistency. The sequence L_n is a martingale. Since Z_n is bounded and A_n is uniformly integrable, L_n is uniformly integrable and converges almost surely and in L1 to L. The already identified limit Z=u^T bold tilde F satisfies Z=L+A_infinity.

For n>=1 set F_{n,0}=F_{n,1}=G_n and F_{n,j}=G_{n+j-1} for j>=2. Set M_{n,0}=M_{n,1}=0 and

M_{n,j}=n^{gamma/2}(L_n-L_{n+j-1}), j>=2.

Each row is a martingale, its terminal value is n^{gamma/2}(L_n-L), and convergence along the row holds in L1. The filtrations satisfy F_{n,j} subset F_{n+1,j}. For j>=2 the increment is n^{gamma/2}(d_{n+j-1}-delta_{n+j-1}).

Write Q_n=n^gamma sum_{k>n}delta_k^2=u^T R_nu. The covariance result gives Q_n->u^T V u. The identity

(n-1)^gamma delta_n^2=Q_{n-1}-((n-1)/n)^gamma Q_n

shows n^{gamma/2}|delta_n|->0. Therefore sup_{k>=n}k^{gamma/2}|delta_k|->0. This tail supremum is dominated by an integrable random variable by the increment assumption. Together with the dominated drift-supremum hypothesis,

sup_j |M_{n,j}-M_{n,j-1}| <= n^{gamma/2}sup_{k>n}|d_k| + sup_{k>n}k^{gamma/2}|delta_k|

tends to zero almost surely and is dominated in L1.

The realized sum of squared array increments is

n^gamma sum_{k>n}(delta_k-d_k)^2.

Its delta-square term tends to u^T V u, its drift-square term tends to zero, and the absolute cross term is at most twice the product of the square roots of those two terms. Thus the realized quadratic variation tends to u^T V u. Every hypothesis of the external conditional martingale-array CLT has now been checked, and it gives

Law(n^{gamma/2}(L_n-L)|G_n) => N(0,u^T V u) almost surely.

It remains to justify conditional transfer through the drift. Mere almost-sure smallness would not suffice. Let H_N=sup_{k>=N}|r_k|. Then H_N decreases to zero almost surely and is integrable. All H_N are G_infinity-measurable, where G_infinity=sigma(union_n G_n). For fixed N, the increasing-filtration conditional-expectation theorem gives E[H_N|G_n]->H_N almost surely. For n>=N,

E[|r_n||G_n] <= E[H_N|G_n].

Taking a limit superior and then letting N tend to infinity proves E[|r_n||G_n]->0 almost surely. Since n^{gamma/2}(Z_n-Z)=n^{gamma/2}(L_n-L)-r_n, conditional expectations of bounded Lipschitz functions differ by a quantity tending to zero. The desired scalar conditional Gaussian limit follows.

## 4. Multivariate conditional convergence

Apply the scalar argument to every u in Q^m, including the coordinate directions, and intersect the resulting countably many probability-one events. For each path in this event, the coordinate conditional laws converge, which makes the vector conditional laws tight: a union bound controls the complement of a sufficiently large coordinate box. Any subsequential weak limit has the Gaussian characteristic function at every rational vector. Continuity of its characteristic function identifies it uniquely as N_m(0,V). Hence the entire vector sequence converges weakly on this common event. This establishes

Law(n^{gamma/2}(bold F_n-bold tilde F)|G_n) => N_m(0,V) almost surely.

Symmetry gives the same limit with the sign reversed.

## 5. Studentization and coverage

Let A_n be either U_n or V_n. It is G_n-measurable and converges almost surely to V. Since V is positive definite, eigenvalue continuity gives eventual positive definiteness of A_n, and A_n^{-1/2}->V^{-1/2}. Values assigned on the G_n-measurable event that A_n is not positive definite are asymptotically irrelevant on every path in the convergence event.

Fix such a path. The conditional error law converges weakly to N_m(0,V), and the matrices A_n on that path are deterministic convergent matrices. The continuous-mapping argument with these convergent linear maps therefore yields the standard-normal conditional limit. Equivalently, the joint conditional kernel of the error and estimator is the product of the error kernel with the point mass at A_n, which converges to the corresponding product with the point mass at V. No independence assumption is used.

Let q_{m,1-alpha} be the (1-alpha)-quantile of the Euclidean norm of a standard m-variate Gaussian. Its distribution is continuous and strictly increasing on positive radii. The studentized norm and the continuity-set theorem show that the public ellipsoid E_n(A_n) has conditional coverage tending to 1-alpha.

For each coordinate, the conditional law of n^{gamma/2}(tilde F_i-F_{n,i})/sqrt(A_{n,ii}) tends to N(0,1). Therefore the public marginal interval I_{n,i}(A_n), calibrated with z_{1-alpha/2}, has conditional coverage tending to 1-alpha. The coordinate projection of E_n(A_n) instead has half-width q_{m,1-alpha}sqrt(A_{n,ii}/n^gamma). Its limiting coverage is 2 Phi(q_{m,1-alpha})-1, which is at least 1-alpha because ||G||_2>=|G_i|. For m>1 it is generally larger than 1-alpha. Thus ellipsoid projections must not be confused with nominally calibrated marginal intervals.

Finally let D(A) be the diagonal matrix with diagonal entries sqrt(A_jj), and C(A)=D(A)^{-1} A D(A)^{-1}. These maps are continuous on positive-definite matrices. For G distributed as N_m(0,A), the statistic max_j |G_j|/sqrt(A_jj) has the same law as the maximum absolute coordinate of N_m(0,C(A)). This distribution has no atoms and is strictly increasing on positive arguments: its Gaussian density is strictly positive, box boundaries have zero probability, and every nonempty difference between concentric positive-radius boxes has positive probability. Gaussian weak convergence as A varies therefore implies continuity of its (1-alpha)-quantile c_{1-alpha}(A).

The coordinate-standardized conditional error vector converges to N_m(0,C(V)), while c_{1-alpha}(A_n)->c_{1-alpha}(V). The continuity-set theorem, with a sandwich by thresholds just above and below the limit, proves that the public simultaneous band B_n(A_n) has conditional coverage tending to 1-alpha. The quantile here is exact; no claim about a fixed-size simulation estimate of that quantile or an approximate U_n is needed.

All obligations are closed. The only source-local correction used is the martingale initial value in theory_007, in addition to the previously recorded limiting-CDF notation correction in theory_006.
