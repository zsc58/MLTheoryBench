# Reference Proof

Put a_G=rho^2/(1-rho^2), a_F=eta^2/(1-eta^2), and S=a_G n+a_F d. Changing the sign of B or Y changes a negative correlation to its absolute value by an invertible transformation of the observations. Work henceforth with nonnegative correlations. Equivariance permits conditioning on pi*=id. Write E for the unordered edges, D_pi={i:pi(i)!=i}, D_pi^E={e:pi(e)!=e}, and S_{n,t}={pi:|D_pi|=t}. For pi in S_n set V(pi)=log p(A,B,X,Y|id)-log p(A,B,X,Y|pi). For n>=3 and S>0, every nonidentity permutation moves an observed coordinate with nonzero correlation: a vertex-feature coordinate if eta>0, or an unordered-edge coordinate if rho>0. Its likelihood score therefore differs from that of the identity almost surely. Thus, for all sufficiently large n in the positive-signal case, MAP fails exactly when some nonidentity V(pi)<0. At n=2 with eta=0, a graph-only signal can leave the two permutations tied; this finite-size exception has no effect on either asymptotic conclusion. When S=0, the data are independent of pi*, every estimator succeeds with probability 1/n!, and the converse follows directly.

For a permutation with t moved vertices, let c_2(pi) count its two-cycles. The exact moved-edge count is
|D_pi^E|=t(n-(t+1)/2)-c_2(pi)>=t(n-t/2-1).
This replaces the source's incorrect lower bound. Write V=V_G+V_F, where
V_G=rho/(1-rho^2) sum_{e in D_pi^E} A_e(B_e-B_{pi(e)}),
V_F=eta/(1-eta^2) sum_{i in D_pi,k} X_ik(Y_ik-Y_{pi(i)k}).
Conditioning on B,Y and using A=rho B+sqrt(1-rho^2)Z and X=eta Y+sqrt(1-eta^2)Z' gives
V(pi) | B,Y = M_pi+sqrt(2M_pi)G,
M_pi=(a_G/2) sum_{e in D_pi^E}(B_e-B_{pi(e)})^2+(a_F/2) sum_{i in D_pi,k}(Y_ik-Y_{pi(i)k})^2,
where G is standard normal when M_pi>0. Thus P(V(pi)<0|B,Y)=Phi(-sqrt(M_pi/2)).

Achievability estimates. Define V_G^*(pi)=sum_{e in D_pi^E}A_e B_e and V_F^*(pi)=sum_{i in D_pi,k}X_ikY_ik. Their expectations are rho|D_pi^E| and eta d t. Let H1 be the event that, simultaneously for all pi in S_{n,t},
|V_G^*(pi)-rho|D_pi^E||<=C t sqrt(n log(en/t)),
|V_F^*(pi)-eta d t|<=C t sqrt(max{d,log(en/t)} log(en/t)).
Here and below C is a sufficiently large numerical constant. To verify P(H1)=1-o(1), write each centered expression as a Gaussian quadratic form. Its operator norm is O(1), and its squared Frobenius norm is O(tn) for edges or O(td) for features. The feature expression depends only on D_pi, so union-bound over at most binom(n,t) sets. For edges, permutations with the same D_pi differ in their starred sums only on edges fixed by two-cycles, at most t edges. Hanson-Wright applied first to one representative per moved set and then to these differences, followed by |S_{n,t}|<=n^t, gives the two displayed widths and an o(1) total failure probability. The Gaussian Hanson-Wright bound used here is P(|z^TQz-E z^TQz|>u)<=2exp[-c u^2/(||Q||_F^2+||Q||_op u)] for deterministic Q and standard Gaussian z; the indicated norms and counts verify its hypotheses and the union bounds.

Let H2=H2G cap H2F, where H2G depends only on B and H2F only on Y. For every pi in S_{n,t}, H2G requires both
|sum_{e in D_pi^E}B_e^2-|D_pi^E||<=C t sqrt(n log n),
|sum_{e in D_pi^E}B_e B_{pi(e)}|<=C t sqrt(n log n).
H2F imposes the analogous inequalities on sum_{i in D_pi,k}Y_ik^2 and sum_{i in D_pi,k}Y_ikY_{pi(i)k}, centered at dt and zero respectively, with width C t sqrt(d log n). Each fixed-permutation expression is a standard-Gaussian quadratic form of operator norm O(1) and squared Frobenius norm O(tn), respectively O(td). Hanson-Wright at these widths gives probability at most 2exp(-c' C t log n) per expression. Summing over |S_{n,t}|<=n^t and t>=2 proves P(H2)=1-o(1). H2 is independent of the noises Z,Z'; its graph and feature components are independent. It is a subcollection of the covariance comparisons needed from the locally corrected auxiliary event, not its source's false unrestricted quantification over a second permutation.

For small displacement set alpha_0=epsilon/(1+epsilon). The four inequalities defining H2 and the edge count give, uniformly for 2<=t<=alpha_0 n,
M_pi>=a_G|D_pi^E|+a_Fdt-Ct[a_G sqrt(n log n)+a_F sqrt(d log n)]
>=tS(1-alpha_0/2-o(1)).
The final error is uniform: relative to its graph and feature leading terms it is O(sqrt(log n/n)+sqrt(log n/d)), and d=omega(log n). Gaussian tail bounding now yields
P(V(pi)<0,H2)<=exp[-tS(1-alpha_0/2-o(1))/4]
<=exp[-(1+epsilon)(1-alpha_0/2-o(1))t log n].
Since (1+epsilon)(1-alpha_0/2)=1+epsilon/2, summation against |S_{n,t}|<=n^t, plus P(H2^c)=o(1), gives o(1) for all small classes.

For large displacement, put k_G=rho/(1-rho^2) and k_F=eta/(1-eta^2), and let V_G(pi)=sum_{e in D_pi^E}A_eB_{pi(e)} and V_F(pi)=sum_{i in D_pi,k}X_ikY_{pi(i)k}. Then V=k_G(V_G^*-V_G)+k_F(V_F^*-V_F). Conditional Gaussian moment calculation on H2G gives
E[exp(k_G V_G)1_{H2G}]<=exp[(a_G/2)|D_pi^E|+C a_G t sqrt(n log n)].
Indeed its conditional exponent is a_G sum B_e B_{pi(e)}+(a_G/2)sum B_{pi(e)}^2; the moved-edge set is invariant under pi, so H2G bounds both terms. Similarly,
E[exp(k_F V_F)1_{H2F}]<=exp[(a_F/2)dt+C a_F t sqrt(d log n)].
Independence of (A,B) and (X,Y), including the separate H2 components, permits multiplication of these bounds. When t>alpha_0 n, log(en/t)=O_epsilon(1), so H1 bounds the starred-score error in the exponent by
Ct[sqrt(a_G(1+a_G)n)+sqrt(a_F(1+a_F)d)]=o(tS).
For the last equality, S>=4(1+epsilon)log n and the ratio to tS is O(S^{-1/2}+n^{-1/2}+d^{-1/2}). The H2 moment errors are also o(tS), since their ratios are at most O(sqrt(log n/n)+sqrt(log n/d)). Consequently
E[exp(-V(pi))1_{H1 cap H2}]<=exp[-(a_G|D_pi^E|+a_Fdt)/2+o(tS)]
<=exp[-tS(1-o(1))/4]
<=exp[-(1+epsilon)t log n(1-o(1))].
The corrected edge count justifies the second inequality even at t=n. Summing this bound against n^t for t>alpha_0 n gives o(1) for the expected unnormalized sum of exp(-V(pi)) on H1 cap H2. Markov's inequality makes that sum less than one with probability 1-o(1); any negative score would contribute more than one. This finishes MAP achievability without inferring absence of negative scores from posterior mass alone.

Converse. Count N_0=sum_{tau transposition}1{V(tau)<0}, without an H2 indicator. First prove the boundary case S=4log n-log log n-b_n with b_n tending to infinity and b_n=o(log log n). For one transposition, the conditional formula above has
M_tau/2=W=a_G Q_{n-2}+a_F Q_d,
where the independent Q variables are chi-square with the indicated degrees of freedom. Hence p=P(V(tau)<0)=E Phi(-sqrt W). At this boundary a_G=O(log n/n), a_F=O(log n/d), and a_G^2 n+a_F^2 d=o(1). Exponential tilting by exp(-W/2) gives
L=E exp(-W/2)=(1+a_G)^(-(n-2)/2)(1+a_F)^(-d/2)=exp(-S/2+o(1)).
Under the tilted law, W has mean S+o(1) and variance o(1); its lower and upper deviations away from, for example, [S/2,2S] have negligible contribution to the tilted Gaussian-tail integral. Mills' estimate uniformly on that interval therefore gives
p=(1+o(1))L/sqrt(2 pi S)=(1+o(1))exp(-S/2)/sqrt(2 pi S).
Thus E N_0=binom(n,2)p~exp(b_n/2)/(4sqrt(2 pi))->infinity. This calculation applies to the count actually defined; no unquantified H2-complement subtraction is made.

For two disjoint transpositions, their scores share only the four graph edges between their respective vertex pairs. Delete those four edges from each score. The resulting core scores U and U' are independent of each other and of those shared edges; each retains all feature terms and n-4 graph outsider terms. Since a_G=O(log n/n), on the event that the finitely many shared Gaussian coordinates have magnitude at most sqrt(C_K log n), each deleted contribution has absolute value at most delta_n=O((log n)^{3/2}/sqrt n)=o(1). For any fixed K, choosing C_K large makes the complementary probability O(n^{-K}).

The core lower tail is stable under this deletion and these small shifts. Explicitly, its conditional variance satisfies M_core/2=W_core=a_G Q_{n-4}+a_F Q_d. For |u|<=delta_n,
P(U<u)=E Phi(-sqrt(W_core)+u/(2sqrt(W_core))).
Tilt by exp(-W_core/2) as above. Its tilted mean is S+o(1) and variance o(1); on its concentrating region Mills' formula makes the integrand exp(u/2+o(1)) times the zero-shift integrand, uniformly over these u. The complementary tilted contribution is negligible by chi-square concentration. The two deleted degrees of freedom change the Laplace transform by a factor 1+o(1). Hence P(U<u)=(1+o(1))p uniformly for |u|<=delta_n. Conditional independence of the cores now gives, for each disjoint pair,
P(V(tau)<0,V(sigma)<0)<=(1+o(1))p^2+O(n^{-K}).
Choose K>8. This establishes the required relative bound for all O(n^4) disjoint pairs without using the insufficient uniform H2 correlation error.

For two transpositions sharing one vertex, use conditional Gaussianity given B,Y. Their noise covariance is a_G times the inner product of their moved-edge B-difference vectors plus a_F times the corresponding Y-difference inner product. The expectations of these inner products are n+O(1) and d, while each score's noise variance is 2M_tau=4S(1+o(1)) on a suitable simultaneous event. Each inner product and variance is a Gaussian quadratic form with operator norm O(1) and squared Frobenius norm O(n) or O(d). Hanson-Wright, a union bound over O(n^3) pairs, and a sufficiently large constant in deviations O(sqrt(n log n)) and O(sqrt(d log n)) produce an event with complement O(n^{-K}) for any prescribed fixed K. On that event the standardized noise correlation is at most
[a_G(n+O(1))+a_Fd+O(a_G sqrt(n log n)+a_F sqrt(d log n))]/[4S(1-o(1))]=1/4+o(1).
The equality uses d=omega((log n)^2); this calculation is a weighted-average bound, not a sum of separate component ratios. The two conditional negative-score cutoffs are each sqrt(S)(1+o(1)), uniformly. Bounding the joint event by a lower tail of the sum of its two standardized Gaussian variables gives
P(V(tau)<0,V(sigma)<0)<=exp[-S/(5/4+o(1))]+O(n^{-K})=n^{-16/5+o(1)}+O(n^{-K}).
Its sum over O(n^3) intersecting pairs is o(1). The diagonal contribution is E N_0=o((E N_0)^2), while the disjoint contribution is at most (1+o(1))(E N_0)^2. Therefore E[N_0^2]<=(1+o(1))(E N_0)^2, and Paley-Zygmund gives P(N_0>0)->1.

For an arbitrary signal satisfying the stated converse inequality, choose b_n tending to infinity but o(log log n) such that S'=4log n-log log n-b_n>=S. Increase the absolute graph correlation, leaving the feature correlation fixed, to make its signal S'. The original graph observation can be obtained from this more informative one by independent Gaussian degradation, so optimal exact-recovery probability in the original experiment cannot exceed that at S'. The proved boundary case therefore covers the entire inequality, including sequences with zero signal. Finally, conditional on the observed data, choosing a posterior maximizer maximizes the probability of guessing pi* correctly. MAP failure with probability tending to one implies that every estimator has exact-recovery probability o(1).
