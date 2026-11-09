# Reference Proof

All logarithms in entropy and relative entropy are base two; ln denotes the natural logarithm. Write d(p||q) for Bernoulli relative entropy. Fix lambda>0 and L* in (0,1/2).

## Audited Standard Concentration Statements

For iid observations, a sample-independent prior P, and measurable losses in [0,1], the uniform PAC-Bayes inequality states that, with probability at least 1-delta, simultaneously for every posterior R,

 d(L_S(R)||L_D(R)) <= [KL(R||P)+log_2((m+1)/delta)]/m.

The hypotheses hold for every admissible public experiment. They also hold for the fixed conditional bad-coordinate prior used below. Posteriors in this statement may depend on S.

We additionally use these standard bounded-observation statements. For independent variables in [0,1] with mean a, their average exceeds a+u with probability at most exp(-2mu^2). If a function of independent observations has bounded differences c_i, then its upper deviation from its mean exceeds u with probability at most exp[-2u^2/sum_i c_i^2].

## Upper Bound

Choose a fixed membership witness Q*, with population risk L* and KL(Q*||Pi)<=10. Write a_S=L_S(Q*). The comparator-feasibility event a_S<=1/2 fails with probability at most

 f_m=exp[-2m(1/2-L*)^2].

Indeed, a_S averages the iid [0,1]-valued losses E_{h~Q*}1{h(X_i)!=Y_i}.

Changing one observation changes a_S by at most 1/m. For m>=2, it changes H(a_S) by at most H(1/m): the entropy modulus follows by integrating the decreasing derivative H' and using symmetry about 1/2. Also E H(a_S)<=H(E a_S)=H(L*) by concavity. Consequently, outside an event of probability delta,

 H(a_S)<=H(L*)+s_m(delta),

where s_m(delta)=H(1/m)sqrt[(m/2)ln(1/delta)].

On the comparator-feasibility event, objective optimality and the uniform PAC-Bayes inequality yield, with r=L_D(Qhat_lambda),

 T_lambda(r)
 <=H(L_S(Qhat_lambda))+lambda KL(Qhat_lambda||Pi)/m+lambda log_2((m+1)/delta)/m
 <=H(a_S)+lambda[10+log_2((m+1)/delta)]/m.

Thus, except on an event of probability at most 2delta+f_m,

 T_lambda(r)<=H(L*)+A_m,

where A_m=lambda[10+log_2((m+1)/delta)]/m+s_m(delta).

This comparison is for a fixed sample-independent comparator; it does not claim simultaneous sampling concentration for data-dependent comparators.

## Correct Transform Inversion

The expression F(p,q)=lambda d(p||q)+H(p) equals

 (lambda-1)[p log_2 p+(1-p)log_2(1-p)]-lambda[p log_2 q+(1-p)log_2(1-q)].

If 0<lambda<=1, it is concave, or affine at lambda=1, in p. Its minimum on [0,1/2] is therefore

 T_lambda(q)=min{-lambda log_2(1-q),1+lambda d(1/2||q)}.

The second endpoint value is at least one. Hence whenever T_lambda(q)<=t<1, necessarily q<=1-2^{-t/lambda}. This is valid even when q>1/2 and is the missing case in the source's inversion discussion. For sufficiently large m, A_m<1-H(L*), so

 r<=ell_lambda(L*)+(ln 2)A_m/lambda.

If lambda>1, F is strictly convex in p. For q in (0,1/2), differentiating gives the unique minimizer p_lambda(q), and T_lambda(q)=U_lambda(q). For q>=1/2 the constrained minimizer is 1/2, so T_lambda(q)=1+lambda d(1/2||q)>=1. Endpoint limits give U_lambda(0)=0 and U_lambda(1/2)=1. On (0,1/2),

 U_lambda'(q)=lambda[q-p_lambda(q)]/[(ln 2)q(1-q)]>0.

Thus the specified inverse branch exists uniquely. Let ell=ell_lambda(L*), b=(ell+1/2)/2, and

 d_0=min_{q in [ell,b]} U_lambda'(q)>0.

For A_m<U_lambda(b)-H(L*), the transform inequality implies r<b and the mean value theorem gives r<=ell+A_m/d_0.

Set delta=1/m for m>=2. Then

 A_m=lambda[10+log_2(m(m+1))]/m+H(1/m)sqrt[(m/2)ln m]
 =O(lambda(10+log m)/m+sqrt(log^3(m)/m)).

For lambda<=1 take the inverse-sensitivity constant C_inv=(ln 2)/lambda; for lambda>1 take C_inv=1/d_0. Once the corresponding sublevel condition holds, define

 rho_{m,lambda,L*}=C_inv A_m+2/m+f_m.

For the finitely many earlier sample sizes set rho_{m,lambda,L*}=1. Since risk is bounded by one, integrating the preceding event bound gives

 E L_D(Qhat_lambda)<=ell_lambda(L*)+rho_{m,lambda,L*}.

This remainder tends to zero uniformly over M(L*); its constants depend only on lambda and L*, not on the experiment. Its displayed terms specify the PAC-Bayes/KL, sampling, confidence, feasibility, and inverse-sensitivity contributions.

## Fixed Lower-Bound Experiment

Fix L*<=L'<ell_lambda(L*). Let X={0,1}^{N_0}, with its product sigma algebra, and let h_i(x)=x_i. Draw Y as a fair binary bit and draw mutually independent error bits E_i, independently of Y, with E_0~Bern(L*) and E_i~Bern(L') for i>=1. Set X_i=Y xor E_i. Thus h_0 has population risk L* and every bad coordinate h_i, i>=1, has population risk L'. All empirical coordinate errors are independent scaled binomials.

For i>=1 let w_i=1/[i(log_2 i)^2+10] and B=sum_{i>=1}w_i. This sum is finite and positive. Define the fixed normalized prior by Pi(h_0)=0.1 and Pi(h_i)=0.9w_i/B. The witness delta_h0 has KL log_2 10<10. For i<=k,

 -log_2 Pi(h_i)<=log_2 k+O(log log(k+2)+1).

This is one experiment, independent of m. Only its prefixes used for comparison grow with m.

The experiment is admissible. For every m, each bad coordinate interpolates with positive probability (1-L')^m, so almost surely some positive-prior coordinate has empirical loss zero and finite point-mass objective. More generally, for a fixed sample, partition the countable hypotheses by their m+1 possible empirical errors. Conditionalizing Pi within any such cell minimizes KL for a prescribed cell mass. The optimization therefore reduces to a finite-dimensional compact simplex, with continuous entropy and lower-semicontinuous relative entropy, and a nonempty finite-objective feasible set. A finite minimum is attained. The cell probabilities are measurable functions of S, and a measurable finite-dimensional minimizing selection, followed by these conditional distributions, supplies the required posterior selection.

## Elementary Binomial-Minimum Derivation

For B_m~Bin(m,q), j in {0,...,m}, and a=j/m, binomial type bounds give

 (m+1)^{-1}2^{-m d(a||q)}<=Pr(B_m=j)<=2^{-m d(a||q)}.

To see the upper bound, use binom(m,j)<=2^{mH(a)}, obtained from the binomial expansion at parameter a. For the lower bound, j is a mode of Bin(m,a); its mass is at least 1/(m+1). Replacing a by q in that mass multiplies it by 2^{-m d(a||q)}. The endpoint cases follow directly.

If 0<p<q and k_m=ceil(2^{m d(p||q)}), the minimum of k_m independent copies of B_m/m converges in probability to p. For 0<epsilon<min(p,q-p), a union bound and the upper type bound show that the probability of a value at most p-epsilon is at most

 k_m(m+1)2^{-m d(p-epsilon||q)},

which tends to zero. Conversely, choose j_m/m approaching p+epsilon. Its probability is at least (m+1)^{-1}2^{-m d(j_m/m||q)}. Since d(p+epsilon||q)<d(p||q), k_m times this probability tends to infinity; independence makes the probability that all copies exceed p+epsilon tend to zero. This proves the exact consequence needed from the specialized external citation.

## Bad Competitors In Both Branches

For lambda<=1, use k_m=ceil(2sqrt(m)(1-L')^{-m}). The probability that none of its bad coordinates has zero empirical error is at most exp[-2sqrt(m)]. A zero-error point mass in this prefix is feasible, and its objective satisfies

 J_lambda(delta_hi,S)/m<=c+o(1),

where c=-lambda log_2(1-L'). The hypothesis L'<ell_lambda(L*) is exactly c<H(L*).

For lambda>1, the inverse branch implies L'<1/2. Set p=p_lambda(L'), so 0<p<L', and k_m=ceil(2^{m d(p||L')}). The elementary minimum result supplies a prefix minimizer with empirical error tending to p; it is feasible with probability tending to one. Its objective satisfies

 J_lambda(delta_hi,S)/m<=H(p)+lambda d(p||L')+o_p(1)=c+o_p(1),

where c=U_lambda(L')<H(L*).

In both branches, objective optimality gives J_lambda(Qhat_lambda,S)/m<=c+o_p(1), with a strict gap below H(L*).

## Comparison For Arbitrary Posteriors

Let t=Qhat_lambda(h_0), let a=L_S(h_0), and, when t<1, write Qhat_lambda=t delta_h0+(1-t)R, where R is supported on bad coordinates. Let P_B be the fixed conditional prior Pi(.|i>=1), and put v=L_S(R). Then L_D(R)=L' for every such R, even when R depends on S.

With probability tending to one, a<1/2, H(a)>c+gamma for some fixed gamma>0, and the learned objective per sample is below c+gamma/2. On this event t=1 is impossible. Also v>=1/2 is impossible: feasibility gives a<=L_S(Qhat_lambda)<=1/2, hence H(L_S(Qhat_lambda))>=H(a), and nonnegative KL contradicts the objective gap. Therefore v<1/2.

Apply the uniform PAC-Bayes inequality under P_B with failure probability 1/m. For every conditional bad posterior R with v<=1/2,

 H(v)+lambda KL(R||P_B)/m
 >=H(v)+lambda d(v||L')-epsilon_m
 >=T_lambda(L')-epsilon_m=c-epsilon_m,

where epsilon_m=lambda log_2(m(m+1))/m tends to zero. The last equality holds in both branches: for lambda<=1, c<H(L*)<1 makes the other endpoint irrelevant; for lambda>1, L'<1/2 permits the interior formula.

The exact mixture decomposition is

 KL(Qhat_lambda||Pi)=d(t||0.1)+(1-t)KL(R||P_B).

Concavity gives H(ta+(1-t)v)>=tH(a)+(1-t)H(v). Combining these and dropping nonnegative d(t||0.1),

 J_lambda(Qhat_lambda,S)/m
 >=tH(a)+(1-t)(c-epsilon_m)
 >=c+t[H(a)-c]-epsilon_m.

The bad-competitor upper comparison therefore implies t[H(a)-c]<=o_p(1)+epsilon_m. Since H(a) tends in probability to H(L*)>c, it follows that t tends to zero in probability. This argument covers arbitrary posterior supports and does not assert eventual exact zero mass.

Finally,

 L_D(Qhat_lambda)=tL*+(1-t)L'

converges in probability, and by boundedness in expectation, to L'. At the endpoint L'=L*, the population risk is identically L* for every posterior, so the conclusion is immediate without a continuity argument.

## Sharpness And Obligation Closure

The upper bound implies sup_{(Pi,D) in M(L*)}limsup_m E L_D(Qhat_lambda)<=ell_lambda(L*). The lower experiment is fixed before m tends to infinity and gives limiting expected risk L' for every allowed L'<ell_lambda(L*). Moreover ell_lambda(L*)>L*: for lambda<=1 this follows from H(L*)>-log_2(1-L*), and for lambda>1 from strict improvement of the interior minimizer over p=L*. Letting L' increase to ell_lambda(L*) establishes the reverse inequality and hence W_lambda(L*)=ell_lambda(L*).

All theorem-critical obligations are closed: standard concentration hypotheses, comparator feasibility, both constrained transform branches, inverse existence and sensitivity, a fixed normalized admissible experiment, both prefix events, arbitrary-posterior comparison, convergence of good mass, bounded-expectation passage, and the final supremum/limit quantifiers. The nonstandard prior-work and binomial citations are not used as unproved closure.
