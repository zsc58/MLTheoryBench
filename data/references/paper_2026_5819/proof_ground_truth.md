# Reference Proof

## Contract and proof obligations

The distributions are accessed only through their prefix oracles. Every positive-probability conditional has support at most K, and each call uses fresh independent randomness, including repeated calls at the same prefix. The variance cap is an upper bound, so deterministic exact conditional oracles are admissible for every sigma^2>=0. At null prefixes an arbitrary conditional extension is allowed; a null response is also allowed.

The proof must establish: (i) exact trajectory sampling and independent likelihood estimation; (ii) an expected chi-square bound; (iii) stability of the plug-in integrand including zero denominators; (iv) multilevel bias, variance, integer sample counts, and query costs; (v) the confidence dependence for every delta in (0,1); (vi) the hidden-parent information bound and coin-testing reduction; and (vii) the rare-escape simulation, adaptive sample accounting, and finite-domain lower-bound transfer.

We use the following standard independent results. Hoeffding's inequality gives P(|N^-1 sum_j V_j-EV_j|>=a)<=2 exp(-2Na^2) for independent [0,1]-valued variables. Chebyshev gives P(|W-EW|>=a)<=Var(W)/a^2, and Markov gives P(W>=a)<=EW/a for nonnegative W. Pinsker's inequality gives TV(P,Q)<=sqrt(KL(P||Q)/2); KL tensorizes for independent samples. We also use the independent finite-domain TV-estimation lower bound stated in the source: on a d-point domain, d>=2, estimating TV(P,Q) uniformly over arbitrary P,Q to accuracy eta, with fixed success probability at least 2/3, requires Omega(d/(eta^2 log d)) total iid samples. Its application below has eta<1/5. This result is an external independent theorem, not an assumption of the public task.

## 1. Mixture representation and oracle implementation

Let M=(pi+mu)/2 and define Z(x)=|pi(x)-mu(x)|/(pi(x)+mu(x)), with value zero when the denominator is zero. Direct summation gives E_{X~M}Z(X)=TV(pi,mu).

One noisy query suffices to generate a true next-token sample: draw a token from the returned probability vector. Conditional on the current positive-probability prefix, its law is the expectation of that vector, hence the true conditional. Fresh calls therefore generate an exact trajectory in n queries. Choosing pi or mu with equal probability first generates X~M.

For likelihood evaluation, use fresh calls independent of all calls used to generate X. At each required prefix, average r independent vectors. The averaged vector is unbiased and satisfies sum_{a:p(a)>0} Var(hat p_r(a))/p(a)<=sigma^2/r. Nonnegativity and unbiasedness imply hat p_r(a)=0 almost surely whenever p(a)=0.

Conceptually draw independent averaged vectors at every positive-probability prefix and extend null-prefix conditionals arbitrarily. Their product defines a random probability distribution hat pi_r, absolutely continuous with respect to pi. Only vectors on the evaluated path need actually be queried. If a path factor is zero, terminate that likelihood evaluation and return zero. In particular, evaluation never needs to query beyond a true zero-probability transition. An evaluation costs at most nr calls. Define hat mu_r similarly.

## 2. Expected product chi-square bound

All expectations in this section include the evaluation-oracle randomness. For a positive-probability prefix s,

sum_a p_s(a) E[(hat p_{s,r}(a)/p_s(a))^2] = 1+sum_a Var(hat p_{s,r}(a))/p_s(a) <= 1+sigma^2/r,

where sums run over positive coordinates. Conditional backward induction on the remaining path length gives

E_{X~pi,oracle}[(hat pi_r(X)/pi(X))^2] <= (1+sigma^2/r)^n.

Indeed, at a prefix with k remaining positions, every child's remaining-path second moment is at most (1+sigma^2/r)^(k-1), independently of the current averaged vector; summing the current factor gives the displayed one-step bound.

Since hat pi_r is a probability distribution supported on supp(pi),

E_oracle chi^2(hat pi_r||pi) = E_{X~pi,oracle}[(hat pi_r(X)/pi(X)-1)^2] <= (1+sigma^2/r)^n-1.

For r>=c n sigma^2 and a sufficiently large universal c, this is at most C n sigma^2/r. The same bound holds for mu. This is an expected divergence bound, not an almost-sure bound for each realized empirical distribution. When sigma^2=0, the probability vectors are exact almost surely and the error is zero.

## 3. Plug-in stability

Define phi(u,v)=|u-v|/(u+v) for u+v>0 and phi(0,0)=0. Let s=a+b>0, t=c+d, and Delta=|c-a|+|d-b|. If t>0, then

|phi(c,d)-phi(a,b)| <= ||c-d|-|a-b||/s + |c-d||s-t|/(st) <= 2Delta/s.

If t=0, Delta=s and the left side is at most one, so the same bound holds. This also proves the source's weaker constant-four bound. In particular, the source's subsequent constant-six chi-square estimate can be justified without relying on its incomplete numerical arithmetic.

Let Z_r(x)=phi(hat pi_r(x),hat mu_r(x)). Squaring the constant-two bound and integrating against M gives, for fixed empirical distributions,

E_{X~M}[(Z_r(X)-Z(X))^2] <= 4 sum_x [(hat pi_r(x)-pi(x))^2+(hat mu_r(x)-mu(x))^2]/(pi(x)+mu(x)).

Each summand associated with pi is bounded using denominator pi(x) whenever pi(x)>0; when pi(x)=0 its numerator is zero almost surely. Apply the analogous argument to mu. Taking expectation over fresh evaluation noise therefore yields

E[(Z_r(X)-Z(X))^2] <= 4 E chi^2(hat pi_r||pi)+4 E chi^2(hat mu_r||mu) <= C n sigma^2/r.

Here X is independent of the evaluation noise. Both estimated likelihoods may vanish, and the convention phi(0,0)=0 covers that event.

## 4. A constant-confidence multilevel estimator

We first construct an estimator at any tolerance tau in (0,1/4]. Put F=n+n^2 sigma^2 and choose

r_ell=1+ceil(c n sigma^2 2^ell),  L=ceil(C_0+2 log_2(1/tau)),

with universal constants sufficiently large. Let Z_ell be the plug-in estimator at repetition count r_ell, and theta_ell=E Z_ell(X). The preceding bound gives

E[(Z_ell(X)-Z(X))^2]<=D 2^-ell,

and hence |theta_L-TV(pi,mu)|<=sqrt(D 2^-L)<=tau/2. Notice that this particular choice has both L+1=O(1+log(1/tau)) and 2^L=O(tau^-2).

For one level-ell increment, draw a fresh X~M and evaluate Z_ell(X) and, if ell>=1, Z_{ell-1}(X) on that same X. Use fresh evaluation randomness independent of X. The two evaluations may be independent conditional on X; sharing their inner randomness is not needed. Define Y_0=Z_0(X) and Y_ell=Z_ell(X)-Z_{ell-1}(X) for ell>=1. Then

E Y_0=theta_0,  E Y_ell=theta_ell-theta_{ell-1}.

For ell>=1, subtracting and adding Z(X) gives

Var(Y_ell)<=E Y_ell^2<=2E[(Z_ell-Z)^2]+2E[(Z_{ell-1}-Z)^2]<=D'2^-ell.

The same form holds at ell=0 after increasing D', since Y_0 is bounded. An increment uses at most n+2n(r_ell+r_{ell-1}) calls, omitting the lower-level term at zero, and thus costs O(n+n^2 sigma^2 2^ell).

Take mutually independent increments across samples and levels, with integer counts

N_ell=ceil(A(L+1)tau^-2 2^-ell).

The sum T of the sample means over all levels has E T=theta_L and

Var(T)=sum_ell Var(Y_ell)/N_ell <= D' tau^2/A.

Choose A so that Chebyshev and the bias bound imply P(|T-TV(pi,mu)|<=tau)>=3/4. Larger constant success probabilities are available by increasing A.

The sample-count ceilings contribute real costs and must be included. Direct summation gives

sum_ell N_ell O(n+n^2 sigma^2 2^ell)
<= O(n(L+1)tau^-2+n^2 sigma^2(L+1)^2 tau^-2+n(L+1)+n^2 sigma^2 2^L)
=O(F tau^-2(1+log(1/tau))^2).

This remains valid at sigma^2=0; no division by sigma^2 occurs.

## 5. Confidence amplification, including delta near one

The literal ceiling in the source's repetition schedule cannot simply be bounded by O(log(1/delta)) uniformly over delta in (0,1). We retain the public rate by the following local confidence wrapper.

If delta<=3/4, take an odd number R=O(log(1/delta)) of independent constant-confidence estimates at tolerance epsilon and return their median. Such an integer R exists with the stated bound because log(1/delta)>=log(4/3). Hoeffding applied to the failure indicators bounds median failure by exp(-cR), so choosing the universal constant sufficiently large gives failure at most delta. The query cost is the claimed bound.

Now suppose delta>3/4 and put s=1-delta<1/4. If s<=epsilon, output a uniform random number on [0,1] without querying. For every true TV value d in [0,1], the interval [d-epsilon,d+epsilon] intersects [0,1] in length at least epsilon, so success is at least s.

Otherwise epsilon<s<1/4. Put h=epsilon/(2s) and tau=h/2=epsilon/(4s). Then tau<1/4 and h>=2epsilon. Run the base estimator T at tolerance tau, and independently draw U uniformly on [-h,h]. Output T+U. On the event |T-d|<=h/2, the entire interval of U values giving |T+U-d|<=epsilon lies in [-h,h]. Its length is 2epsilon, so its conditional probability is epsilon/h=2s. Overall success is at least (3/4)2s>=s. Projection of the output onto [0,1], if desired, can only improve accuracy.

The cost is

O(F s^2 epsilon^-2(1+log(4s/epsilon))^2)
<= O(F s^2 epsilon^-2 log^2(1/epsilon))
<= O(F epsilon^-2 log^2(1/epsilon)log(1/delta)),

because epsilon<1/8, 4s<1, and s^2<=s<=-log(1-s)=log(1/delta). Thus the exact public upper bound holds for every delta in (0,1), without changing its logarithm.

## 6. Exact-oracle lower bound through hidden blocks

Use two symbols of the alphabet. Choose an integer r with L=2^r>=C epsilon^-2 and r=O(log(1/epsilon)). For a sufficiently large universal constant in the hypothesis on n, arrange n>=2r and t=n-r>=2. Index blocks by u in {0,1}^r. Independently draw X_u~Bern(p), a hidden parent Z_u uniform on {0,1}^{t-1}, and an orientation B_u uniform on {0,1}.

If X_u=0, both within-block laws put probability 1/2 on each of the two sibling leaves Z_u0,Z_u1. If X_u=1, put the two laws on opposite sibling leaves, with orientation B_u. Give each block mass 1/L. Then TV(pi,mu)=L^-1 sum_u X_u. Every positive-probability conditional has support at most two, hence at most K.

Choose the exact oracles to return a null symbol on inconsistent prefixes. Allow a query to reveal both distributions' answers, which only strengthens the algorithm by a constant factor. Before the parent uZ_u is queried, an answer within block u is either null or reports the next deterministic parent bit. It does not depend on X_u. At the parent, the answer distinguishes X_u=0 from X_u=1.

Let G be the set of blocks whose parent is queried by an algorithm using at most B paired queries. Condition on its independent random seed q, and pad the transcript to B answer slots. Answers lie in a constant-size alphabet. Queries are deterministic functions of q and previous answers, so I((Z_u)_u;Tr|q)<=h_0 B. The transcript identifies G: a query of full parent length is a hit precisely when its answer is non-null. Conditional on a transcript, every Z_u with u in G is determined, and each other Z_u has at most t-1 bits of entropy. Consequently

H((Z_u)_u|Tr,q)<=(t-1)(L-E|G|),

whereas H((Z_u)_u|q)=L(t-1). Thus E|G|<=h_0 B/(t-1)<=2h_0 B/t.

Set p_0=1/2 and p_1=1/2+4epsilon. Hoeffding gives P(|TV-p|>=epsilon)<=2 exp(-2L epsilon^2)<=1/100 after choosing C. On the strict complementary event, any epsilon-accurate estimate lies strictly on the correct side of the midpoint (p_0+p_1)/2. Thus an estimator with success at least 2/3 gives a test with success at least 2/3-1/100.

Simulate this test using an unknown Bernoulli(p) coin: draw all parent strings and orientations internally, and draw X_u from the coin only when its parent is first queried. This has exactly the required transcript law. The expected number of coin samples is at most C B/t. Truncate before exceeding a sufficiently large constant multiple of B/t samples; Markov loses at most 1/100 success. The threshold can be floored, aborting before the next sample would exceed it, so integer rounding does not introduce an additive sample-cost loophole.

For completeness, the coin lower bound follows from KL and Pinsker. Writing p_1-p_0=4epsilon, KL(Bern(p_1)||Bern(1/2))<=chi^2(Bern(p_1)||Bern(1/2))=64epsilon^2. With N independent coin samples, the KL is at most 64N epsilon^2, so their TV is at most sqrt(32N epsilon^2). A test with success bounded above 1/2 under both hypotheses requires a fixed positive TV separation. Therefore N=Omega(epsilon^-2). Independent simulation randomness cannot improve this separation. It follows that B=Omega(t/epsilon^2)=Omega(n/epsilon^2).

For the noisy minimax problem, choose deterministic exact conditional vectors as the noisy-oracle laws. They have variance zero and are admissible for every upper bound sigma^2. Hence the same lower bound holds. We do not claim that an arbitrary noisy oracle law can be simulated from exact conditional probabilities: its higher-order distribution could encode additional information.

## 7. Noise-dependent lower bound

If sigma^2=0, the previous section already proves the public lower bound. Assume sigma^2>0. Choose K symbols within the m-symbol alphabet, label them 0,1,...,K-1, and take arbitrary P,Q on {1,...,K-1}. Let q=1/n. At every alive prefix 0^i, use next-token laws

r_P=(1-q)e_0+qP,  r_Q=(1-q)e_0+qQ.

After any nonzero token, return deterministic zeros. Define the oracle answer at every non-alive prefix to be e_0, even if that prefix has zero probability. This is a valid conditional extension and does not require testing membership in supp(P) or supp(Q). All conditional supports have size at most K.

The all-zero string has equal mass under both laws. A string whose unique escape label is a at position i+1 has mass (1-q)^i qP(a) or (1-q)^i qQ(a). Therefore, summing over i=0,...,n-1,

TV(pi_P,mu_Q)=alpha_n TV(P,Q),  alpha_n=1-(1-1/n)^n.

For n>=2, alpha_n>=1-e^-1>5/8 and alpha_n<=1.

Set M=ceil((K-1)/sigma^2). At an alive prefix, return the empirical distribution of M fresh independent draws from r_P or r_Q. It is unbiased and its expected chi-square divergence from its mean is

sum_{a:r_P(a)>0} Var(Y(a))/r_P(a)=(|supp(r_P)|-1)/M<=(K-1)/M<=sigma^2,

and similarly for Q. All other answers are deterministic. This defines admissible independent noisy oracles.

Each draw from r_P can be simulated by an independent Bernoulli(q) escape decision, using a fresh P sample only on escape. Thus an alive query consumes Bin(M,q) ordinary samples, with conditional expectation M/n; non-alive queries consume none. Conditional expectation applies even when the queried oracle and prefix are chosen adaptively from the previous transcript. For at most B calls, the expected total consumption is at most BM/n.

Suppose an algorithm succeeds uniformly with probability at least 2/3. Amplify it to success at least 99/100 by a fixed number of independent repetitions and a median, changing B only by a universal factor. Truncate its sample simulation at a sufficiently large constant multiple of BM/n. Markov loses at most 1/100 success; implement the integer cap by aborting before the next sample would exceed that real threshold. Dividing the returned estimate by alpha_n gives a finite-domain estimator with accuracy eta=epsilon/alpha_n and success at least 98/100, using at most C BM/n samples.

The external finite-domain theorem applies: d=K-1>=2, the input laws P,Q are arbitrary, the samples used are fresh iid draws from the selected law, the success probability exceeds 2/3, and eta< (1/8)/(5/8)=1/5. An adaptive allocation can also be supplied from two independent pre-generated sample streams of length equal to the total budget, costing only a factor of two. Since d/log d is comparable to K/log K for K>=3, the theorem gives

BM/n=Omega(K/(epsilon^2 log K)).

Finally, the standing range sigma^2<=K implies

M<= (K-1)/sigma^2+1 <=2K/sigma^2.

Hence B=Omega(n sigma^2/(epsilon^2 log K)). Combining this with Omega(n/epsilon^2), and using log K>=log 3, proves Omega(n(1∨sigma^2)/(epsilon^2 log K)).

## Closure

All obligations listed at the beginning are discharged. The source-local corrections are confined to threshold ties, alphabet and summation indices, a zero-noise case split, an accuracy-variable typo, and confidence-endpoint accounting. The public upper and lower rates, accuracy range, confidence quantifier, and sequence-length regime are unchanged.
