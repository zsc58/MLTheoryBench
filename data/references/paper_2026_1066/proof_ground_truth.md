# Reference Proof

## Achievability

Write r=dnu/dmu, so E_mu[r]=1. The estimator is the median of the means of the observed oracle values lambda(X_i). Because lambda=Zr, it suffices to analyze the corresponding means of r and then rescale the analysis by Z.

Fix M>0 with ICov_M<=epsilon M/4. Define

Y=r·1{r<=M},  H=r·1{r>M}.

By change of measure,

E_mu[H]=nu{r>M}<=Cov_M<=ICov_M/M<=epsilon/4.

Consequently E_mu[Y]=1-E_mu[H]>=1-epsilon/4. Also 0<=Y<=M. Tail integration, with the endpoint handled using the strict event {r>M}, gives

E_mu[Y^2]=E_mu[r^2·1{r<=M}]
=∫_0^M nu{t<=r<=M}\,dt
=∫_0^M(Cov_t-nu{r>M})\,dt
<=ICov_M<=epsilon M/4.

Thus the centered variables Y-E_mu[Y] have variance at most epsilon M/4 and absolute value at most M. Bernstein's inequality implies that, for a sufficiently large universal constant C_0, every group of m>=C_0M/epsilon iid samples satisfies

|m^{-1}Σ_i Y_i-E_mu[Y]|<=epsilon/8

with probability at least 7/8. Markov's inequality and E_mu[H]<=epsilon/4 imply

P(m^{-1}Σ_i H_i>3epsilon/4)<=1/3.

On the intersection of these events, which has probability at least 1-1/8-1/3=13/24>1/2,

1-epsilon <= m^{-1}Σ_i(Y_i+H_i)=m^{-1}Σ_i r_i <=1+epsilon.

Indeed, the lower bound is at least 1-epsilon/4-epsilon/8, and the upper bound is at most 1+epsilon/8+3epsilon/4. Hence one group mean of the oracle values is within the required multiplicative interval with probability strictly larger than 1/2. Partition the samples into k=ceil(C_1 log(1/delta)) independent groups of such size and return the median of their oracle-value means. A Chernoff bound for the number of successful groups, with a sufficiently large universal C_1, gives success probability at least 1-delta. Taking C sufficiently large to account for the grouping yields n>=C M log(1/delta)/epsilon.

## Converse

Fix a nonatomic probability measure mu and 0<epsilon<=1/2. Choose a measurable set A with mu(A)=p, where p=epsilon^3/100. Define two oracle instances

lambda_0=1,  and  lambda_1=1+alpha·1_A,  where alpha=6epsilon/p.

Their normalizing constants are Z_0=1 and Z_1=1+6epsilon. For the second instance, write

b=1/(1+6epsilon),  a=(1+alpha)/(1+6epsilon),

and let q=nu_1(A)=(p+6epsilon)/(1+6epsilon). The likelihood ratio r_1=dnu_1/dmu equals b off A and a on A. Set M=6a. Since M>a>b, the coverage profile gives

ICov_M(nu_1||mu)=b+(a-b)q.

Therefore

ICov_M(nu_1||mu)/M=[q+(1-q)/(1+alpha)]/6.

Using

q=(p+6epsilon)/(1+6epsilon),  1-q=(1-p)/(1+6epsilon),

and 1/(1+alpha)=p/(p+6epsilon), we obtain

ICov_M(nu_1||mu)/M
=\frac{1}{6(1+6epsilon)}\left(p+6epsilon+\frac{p(1-p)}{p+6epsilon}\right)
<=\frac{1}{6(1+6epsilon)}\left(p+6epsilon+\frac{p}{p+6epsilon}\right).

It is enough to show p+p/(p+6epsilon)<=36epsilon^2. For p=epsilon^3/100 and epsilon<=1/2,

p/(p+6epsilon)<=p/(6epsilon)=epsilon^2/600,

and p=epsilon^3/100<=epsilon^2/200. Hence

p+p/(p+6epsilon)<=epsilon^2/150<36epsilon^2,

so ICov_M(nu_1||mu)<=epsilon M.

The baseline instance must satisfy the same coverage condition. For lambda_0=1, we have r_0=1 and nu_0=mu. Also

M=\frac{6(p+6epsilon)}{p(1+6epsilon)}
>=\frac{36epsilon}{4p}=\frac{9epsilon}{p}>1,

so

ICov_M(nu_0||mu)=∫_0^M 1{1>=t}\,dt=1.

Furthermore,

epsilon M=\frac{6epsilon(p+6epsilon)}{p(1+6epsilon)}
>=\frac{36epsilon^2}{4p}=\frac{9epsilon^2}{p}=\frac{900}{epsilon}>1.

Thus ICov_M(nu_0||mu)<=epsilon M as well, so both testing instances belong to the claimed family and satisfy the stated integrated-coverage condition. Moreover,

M/epsilon=\frac{6(p+6epsilon)}{p\,epsilon(1+6epsilon)}=Theta(1/p),

with universal implicit constants for 0<epsilon<=1/2.

The two n-sample observation laws, including oracle evaluations, agree whenever no proposal sample falls in A. Thus their total variation distance is at most 1-(1-p)^n<=np. The acceptable multiplicative intervals for Z_0 and Z_1 are disjoint, because

1+6epsilon>(1+epsilon)/(1-epsilon)

for 0<epsilon<=1/2. Therefore an estimator succeeding with probability at least 2/3 on both instances yields a test between the two observation laws with total variation distance at least 1/3. Consequently np>=1/3, so n>=1/(3p)=Omega(M/epsilon).
