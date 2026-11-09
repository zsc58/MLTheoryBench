# Reference Proof

Let q=P(S), Q=P(.|S), s=||Sigma_P||_op, and gamma=2 nu_{P,p} epsilon^(1-1/p). Since q>=1/2, for every unit vector v,

<mu_P-mu_Q,v> = q^(-1) E_P[1_S <mu_P-X,v>] = -q^(-1) E_P[1_{S^c} <X-mu_P,v>].

Holder's inequality gives |<mu_P-mu_Q,v>| <= 2 nu_{P,p} epsilon^(1-1/p). Taking the supremum over unit vectors gives ||mu_P-mu_Q||_2<=gamma.

If X and Y are independent with law P, then Sigma_P=(1/2)E[(X-Y)(X-Y)^T]. Restricting this positive-semidefinite expectation to X,Y in S gives Sigma_P >= q^2 Sigma_Q. Hence ||Sigma_Q||_op<=4s and tr(Sigma_Q^2)<=d||Sigma_Q||_op^2.

For iid X_1,...,X_n~Q, E[F]=||mu_Q||_2^2. To obtain the variance bound, let F^(i) replace X_i by an independent copy X_i'. With Delta_i=X_i-X_i',

F-F^(i) = binom(n,2)^(-1) sum_{j!=i} <Delta_i,X_j>.

Conditionally on X_i,X_i', its mean is (2/n)<Delta_i,mu_Q> and its variance is 4/[n^2(n-1)] Delta_i^T Sigma_Q Delta_i. Since E[Delta_i Delta_i^T]=2 Sigma_Q, Efron-Stein yields

Var_Q(F) <= 4/n <mu_Q,Sigma_Q mu_Q> + 4/[n(n-1)] tr(Sigma_Q^2).

Therefore, for a universal K and m=||mu_Q||_2,

sqrt(Var_Q(F)) <= K(m sqrt(s/n)+s sqrt(d)/n).

Set r=alpha/2 and delta=alpha-2gamma>0. Under H0, m<=gamma and

r^2-m^2 >= r^2-gamma^2 = delta(alpha+2gamma)/4 >= alpha delta/4.

Under H1, m>=a0=alpha-gamma=r+delta/2. For m>=a0,

m^2-r^2 >= a0^2-r^2,
m/(m^2-r^2) <= 2/delta,
1/(m^2-r^2) <= 2/(alpha delta).

The sample-size condition n>=C s sqrt(d)/delta^2, with C sufficiently large and universal, makes the standard deviation at most (r^2-gamma^2)/sqrt(3) under H0 and at most (m^2-r^2)/sqrt(3) uniformly under H1. Chebyshev's inequality then gives P_0(F>r^2)<=1/3 and P_1(F<=r^2)<=1/3. Thus T=1{F>alpha^2/4} succeeds with probability at least 2/3 under both hypotheses. The case s=0 is immediate from the same variance bound.

For the converse, fix p>=2, 0<epsilon<=1/2, and alpha>0. In one dimension let a=alpha/epsilon and define

P_1=(1-epsilon) delta_0 + epsilon delta_a,
P_0=delta_0,
S={0}.

Then P_1(S)=1-epsilon, P_1(.|S)=P_0, mu_{P_1}=alpha, and mu_{P_0}=0. The centered p-moment of P_1 is finite and equals

nu_{P_1,p}=a epsilon^(1/p) B^(1/p),
where B=(1-epsilon)epsilon^(p-1)+(1-epsilon)^p.

Since 1-epsilon>=1/2, B^(1/p)>=1/2, so alpha=a epsilon <= 2 nu_{P_1,p} epsilon^(1-1/p). Thus a universal positive constant c, for example c=2, satisfies the claimed signal-scale relation. Embedding this construction in one coordinate gives the result in R^d. The observed laws under the alternative truncation and the null are identical, so every test has maximum error at least 1/2, even with arbitrarily many observations.
