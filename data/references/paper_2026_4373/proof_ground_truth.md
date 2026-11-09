# Reference Proof

## Proof Structure

For each channel, rewrite the one-step scale update as a constant-coefficient EWMA. Analyze its mean recursion for asymptotic unbiasedness, then analyze its variance recursion using temporal independence. Finally substitute the variational relation between the forgetting factor and prior degrees of freedom, and identify the exponential decay time constant.

## Complete Proof

Fix a channel i and write s_k=(tau_{i,k|k})^2, E_k=E_{i,k}, sigma^2=sigma_i^2, eta^4=eta_i^4, rho=rho_i, and nu=nu_i^-. The initialization s_0 is a fixed finite constant, so Var(s_0)=0. The update gives

s_k=(nu s_{k-1}+E_k)/(nu+1)=rho s_{k-1}+(1-rho)E_k,

because rho=nu/(nu+1). Here 0<rho<1. Iterating,

s_k=rho^k s_0+(1-rho) sum_{j=1}^k rho^{k-j}E_j.

Each E_j has finite second moment by weak stationarity, and therefore this finite sum has finite second moment for every k. Under weak stationarity, E[E_j]=sigma^2 for every j. Therefore

E[s_k]=rho^k s_0+(1-rho^k)sigma^2
       =sigma^2+rho^k(s_0-sigma^2),

which converges to sigma^2 since rho^k tends to zero. Thus the tracker is asymptotically unbiased.

For the variance assertion, assume in addition that the errors E_k are temporally independent. Independence from the fixed initialization is automatic. The iterated formula shows that s_{k-1} is a measurable function of E_1,...,E_{k-1} and the fixed initialization. Thus E_k is independent of s_{k-1}, so

V_k:=Var(s_k)=rho^2V_{k-1}+(1-rho)^2 eta^4.

Solving this scalar recursion, with V_0=0, gives

V_k=rho^{2k}V_0+(1-rho)^2 eta^4 sum_{r=0}^{k-1}rho^{2r}
   =rho^{2k}V_0+(1-rho)^2 eta^4(1-rho^{2k})/(1-rho^2).

Because 0<rho<1, the initial term vanishes and hence

lim_{k->infinity}V_k=((1-rho)^2/(1-rho^2))eta^4
=(1-rho)/(1+rho)eta^4.

Using rho=nu/(nu+1),

(1-rho)/(1+rho)=[1/(nu+1)]/[(2nu+1)/(nu+1)]=1/(2nu+1),

so the limiting variance is eta^4/(2nu_i^-+1). These calculations also cover eta^4=0.

Finally, the contribution of an observation r samples in the past is weighted by rho^r. Writing rho^r=exp(r log rho)=exp(-r/T), the e-folding time T satisfies T=-1/log rho, which is positive because 0<rho<1. This is the stated EWMA tracking time constant, in sampling intervals.
