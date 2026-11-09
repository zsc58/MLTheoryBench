# Reference Proof

Fix w for the population calculations. Constants in this part may depend on w and the fixed data, intensity, imputation, and lambda objects, but not on pi. Coordinates whose missingness probability is identically zero throughout the admissible family can be omitted; their masks are always observed.

## Direct bias expansion and coefficient integrability

First verify coefficient integrability rather than invoking only matching-set weighted moments. For each coordinate that can have a positive admissible missingness probability, choose an admissible reference probability with that coordinate positive. Admissibility gives a finite almost-sure upper bound on its fixed intensity a_j(V). Since there are finitely many coordinates, all products of these active intensities are bounded. Thus E||Gamma_T(w)||^2<infinity implies E[a_S(V)||Gamma_T(w)||]<infinity for every pair of active subsets S,T. These constants do not depend on pi. A sufficiently small positive reference vector on all active coordinates is admissible, and may be chosen so that lambda pi_j a_j(V)<=1/2.

For a deterministic missing set A, define D_S(w)=sum over T subseteq S of (-1)^{|S minus T|} Gamma_T(w), with D_emptyset=Gamma_emptyset. Summing D_S over S subseteq A leaves coefficient 1 for Gamma_A and coefficient 0 for every other Gamma_T, by the alternating subset sum. Hence Gamma_A=sum over S subseteq A of D_S.

Conditional on complete data and xi, the mask has independent coordinates with probabilities pi_j a_j(V). Therefore

E[Gamma_{S(M)}(w) | X,Y,xi,V]=Gamma_emptyset(w)+sum over nonempty S of pi_S a_S(V)D_S(w),

where pi_S is the product of pi_j over S and a_S(V) is the product of a_j(V) over S. All terms are integrable by the preceding verification. Taking expectations gives

B(w,pi)=A(w)pi+R(w,pi),

where the j-th column of A(w) is E[a_j(V)(Gamma_{ {j} }(w)-g(w))] and

R(w,pi)=sum over |S|>=2 of pi_S E[a_S(V)D_S(w)].

There are finitely many finite coefficients. For rho=||pi||_1<=1, pi_S<=rho^{|S|}, so ||R(w,pi)||<=K(w)rho^2. The singleton sum is at most K_1(w)rho. This proves ||B(w,pi)||=O(rho) for every fixed w, including zero coordinates and the case of no potentially missing coordinates.

## Joint linked law and restoration discrepancy

Write J=S(M^(pi)) and H=S(M^(lambda pi)). For one coordinate, conditional on complete data, the mutually exclusive states 'originally missing', 'missing only after thinning', and 'observed at the higher scale' have probabilities

pi_j a_j(V), (lambda-1)pi_j a_j(V), and 1-lambda pi_j a_j(V).

The coordinate states are conditionally independent and independent of xi. In particular H has the independent scale-lambda pi law. More precisely, for J subseteq H,

P(J,H | X,Y,xi,V)=(lambda-1)^{|H minus J|} pi_H a_H(V) product over j outside H of (1-lambda pi_j a_j(V)).

Define privately K_{J,H}(w) as the gradient obtained by imputing under H and restoring H minus J. The linked lower gradient is K_{J,H}, and the higher gradient is Gamma_H. If J=emptyset, all missing entries are restored and K_{J,H}=g. If J=H, nothing is restored and K_{J,H}=Gamma_J. In particular, whenever |H|<=1, K_{J,H}=Gamma_J. For H={j}, the two cases are K_{{j},{j}}=Gamma_{ {j} } and K_{emptyset,{j}}=g; they must not be conflated.

We next verify the moments of the hybrids actually used. Choose a fixed positive admissible reference vector u on the active coordinates with lambda u_j a_j(V)<=1/2. The public finite-first-moment assumption gives E||ghat^(u)(w)||<infinity. Its finite joint-pattern sum is a sum of nonnegative expectations. For every J subseteq H, its pattern probability at u is bounded below by a positive deterministic constant times a_H(V), because u_H>0, lambda>1, and every outside-H factor is at least 1/2. Consequently

E[a_H(V)||K_{J,H}(w)||]<infinity

for every relevant pair J,H. Also E[a_H(V)||Gamma_J(w)||]<infinity by bounded active intensities and the direct moments. This establishes, rather than assumes, the finite constants needed for the restoration discrepancy.

Let E_link(w,pi)=E[ghat^(pi)(w)]-E[Gamma_J(w)]. Using the joint law, it equals the sum over J subseteq H of the pattern probability times K_{J,H}-Gamma_J. Every term with |H|<=1 vanishes. For the remaining terms, the outside-H factors lie in [0,1], and the verified moments give

||E_link(w,pi)||<=sum over |H|>=2 and J subseteq H of (lambda-1)^{|H minus J|} pi_H E[a_H(V)||K_{J,H}(w)-Gamma_J(w)||]<=K_link(w,lambda)rho^2.

Summing the joint law over H leaves J with its original scale-pi law, so E Gamma_J=nabla L+B(w,pi). Similarly E Gamma_H=nabla L+B(w,lambda pi). The valid Richardson identity is therefore

E ghat_R(w)-nabla L(w)=[lambda B(w,pi)-B(w,lambda pi)+lambda E_link(w,pi)]/(lambda-1).

Insert the direct expansions. Their linear terms cancel exactly, and their remainders and E_link are all O(rho^2) for fixed lambda. Hence ||E ghat_R(w)-nabla L(w)||=O(rho^2). This does not identify the restored lower mean with direct lower-scale imputation.

## Variance obligation

Whenever both component centered second moments are finite, the squared-norm inequality gives

Var(ghat_R)<=2[lambda^2 Var(ghat^(pi))+Var(ghat^(lambda pi))]/(lambda-1)^2.

No independence between the linked components is needed. Pointwise direct-gradient moments do not imply uniform component variance along SGD. For the optimization conclusion, the public task explicitly supplies a pi-uniform centered conditional second-moment bound for the actual plain or Richardson update estimator. That bound, not an unsupported inference from the component moments, is used below.

## Conditional biased-SGD recursion and initialization

For either algorithm, put e_k=w_k-w*. The stated conditional sampling law and trajectory hypotheses give

E[ghat_k | F_k]=nabla L(w_k)+Delta_k, ||Delta_k||<=b(pi),

and ghat_k=nabla L(w_k)+Delta_k+zeta_k with E[zeta_k | F_k]=0 and E[||zeta_k||^2 | F_k]<=sigma^2. Here b(pi) is bounded by C_plain rho or C_R rho^2, respectively, and sigma^2 and these constants are independent of pi and k.

Strong convexity and smoothness give <e_k,nabla L(w_k)> >=alpha||e_k||^2 and ||nabla L(w_k)||<=beta||e_k||. Expanding the update, use

-2<e_k,Delta_k><=(alpha/2)||e_k||^2+(2/alpha)b(pi)^2

and ||nabla L(w_k)+Delta_k||^2<=2 beta^2||e_k||^2+2b(pi)^2. Thus

E[||e_{k+1}||^2 | F_k]<=(1-3alpha eta_k/2+2beta^2 eta_k^2)||e_k||^2+[(2/alpha)eta_k+2eta_k^2]b(pi)^2+eta_k^2 sigma^2.

Since eta_k<=alpha/(6beta^2), the coefficient is at most 1-alpha eta_k. For a constant C_b independent of pi and k, taking expectations yields

u_{k+1}<=(1-alpha eta_k)u_k+C_b eta_k b(pi)^2+eta_k^2 sigma^2,

where u_k=E||e_k||^2. The coefficient is nonnegative under the stated step sizes.

Set a=alpha c>1 and h=(C_b/alpha)b(pi)^2. Choose K independent of pi with K>=gamma C_0 and (a-1)K>=c^2 sigma^2. We prove u_k<=h+K/(k+gamma). It holds at k=0 by the initialization assumption. If t=k+gamma and it holds at k, the recursion gives

u_{k+1}<=h+K/t-(aK-c^2 sigma^2)/t^2<=h+K/(t+1),

because aK-c^2 sigma^2>=K and K/t-K/t^2<=K/(t+1). This proves

E||w_n-w*||^2<=C b(pi)^2+K/(n+gamma).

The initialization has been explicitly accounted for; it is not hidden in a pi-dependent big-O constant. The separate trajectory-uniform bias hypothesis is used here and is not inferred from the fixed-w expansion.

For plain SGD, b(pi)<=C_plain rho, giving O(rho^2)+O(1/n). For Richardson-SGD, b(pi)<=C_R rho^2, giving O(rho^4)+O(1/n). Finally, smoothness and nabla L(w*)=0 imply 0<=L(w_n)-L(w*)<=(beta/2)||w_n-w*||^2. Taking expectations proves the same excess-loss orders. All theorem-critical obligations have explicit derivations; no specialized external result is needed.
