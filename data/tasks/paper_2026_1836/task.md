# Problem

## Setup

Let d>=1 be an integer. Write P_2(R^d) for the Borel probability measures on R^d with finite second moment. For mu,nu in P_2(R^d), let Pi(mu,nu) be their couplings and define

W_2(mu,nu)^2 = inf_{pi in Pi(mu,nu)} integral |x-y|^2 d pi(x,y).

A coupling attaining this infimum is called optimal. For a measurable map F, its pushforward is defined by (F#mu)(A)=mu(F^{-1}(A)) for Borel sets A. Write <a,b>_mu=integral <a(x),b(x)> dmu(x) and ||a||_mu^2=<a,a>_mu.

Let E:P_2(R^d)->R be Wasserstein differentiable, and write g_mu=grad_W E[mu] in L^2(mu;R^d). Here the Wasserstein gradient is the element of the L^2(mu)-closure of {grad phi: phi is smooth and compactly supported} representing the differential against compatible velocity fields: along an absolutely continuous measure curve rho_t with velocity v_t satisfying the continuity equation partial_t rho_t+div(rho_t v_t)=0, its differential is

d/dt E[rho_t] = <g_{rho_t},v_t>_{rho_t}

at times at which the curve has the indicated velocity. The continuity equation is understood weakly, so d/dt integral phi d rho_t=integral <grad phi,v_t> d rho_t for smooth compactly supported phi.

For each i in {1,...,d}, let U_i be orthogonal projection onto the ith coordinate axis. Assume constants L_i in (0,infinity) satisfy the following for every mu in P_2(R^d) and every T in L^2(mu;R^d): with nu=(Id+U_iT)#mu,

||U_i(g_nu composed with (Id+U_iT)-g_mu)||_mu <= L_i||U_iT||_mu.

Write L_sum=sum_{i=1}^d L_i. Assume that E has a global minimizer, and set E_*=min_mu E[mu] and S={mu:E[mu]=E_*}.

Fix an initial measure mu_0 in P_2(R^d). Let I_0,I_1,... be independent random variables taking values in {1,...,d} with P(I_k=i)=p_i=L_i/L_sum, and define

mu_{k+1}=(Id-L_{I_k}^{-1}U_{I_k}g_{mu_k})#mu_k.

All expectations below are over these coordinate draws.

For m>=0, call E m-geodesically convex if, for every mu,nu in P_2(R^d) and every optimal coupling pi of them,

E[nu]-E[mu] >= integral <g_mu(x),y-x> d pi(x,y)+(m/2)W_2(mu,nu)^2.

The case m=0 is geodesic convexity; m>0 is strong geodesic convexity. For m>0, the m-PL condition is

E[mu]-E_* <= ||g_mu||_mu^2/(2m) for every mu in P_2(R^d).

## Task

Prove the following for every integer K>=1:

1. Without assuming convexity, PL, or a bounded sublevel set,

   E[min_{0<=k<K} ||g_{mu_k}||_{mu_k}^2] <= 2L_sum(E[mu_0]-E_*)/K.

   Moreover, E[mu_{k+1}]<=E[mu_k] almost surely for every k>=0, and hence E[mu_K]<=E[mu_0] almost surely.

2. If E is geodesically convex and there is a constant R_0 in (0,infinity) such that

   sup_{mu:E[mu]<=E[mu_0]} inf_{nu in S} W_2(mu,nu) <= R_0,

   then

   E[E[mu_K]-E_*] <= 2L_sum R_0^2/K.

3. If m>0 and E either satisfies the m-PL condition or is m-geodesically strongly convex, then

   E[E[mu_K]-E_*] <= (1-m/L_sum)^K(E[mu_0]-E_*).
