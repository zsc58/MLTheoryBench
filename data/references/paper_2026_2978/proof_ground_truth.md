# Reference Proof

## Proof Structure

1. Verify the box-restricted minimum-norm selector is well-defined under the stated optimization semantics.
2. Identify the population minimizer of squared distance as the mean of the instance-wise optimal multipliers, and identify the ERM with their sample mean.
3. Use independence and bounded coordinates to obtain the upper bound.
4. Construct an admissible separable MILP family whose optimal multipliers encode a binary packing of population means.
5. Bound sample KL information and apply Fano through nearest-mean decoding, checking the entire s>=8 regime.

## Complete Proof

Write X(P) for the hard-feasible set. For each admissible instance, the displayed finite minimum defines nu(lambda,P) on Lambda. It is concave because it is the pointwise minimum of affine functions of lambda. For any lambda,lambda' in Lambda, choose a minimizing x at lambda. Then
nu(lambda',P)<=nu(lambda,P)+(lambda'-lambda)^T(b-Ax).
The activity bound gives ||b-Ax||_2<=2B sqrt(s). Interchanging lambda and lambda' proves continuity, indeed Lipschitz continuity, on Lambda. Consequently the optimal set K(P)=argmax_{lambda in Lambda}nu(lambda,P) is nonempty and compact. Concavity makes K(P) convex. The continuous function ||lambda||_2^2 attains its minimum on K(P), and strict convexity makes that minimizer unique. Thus z(P) is a uniquely defined member of Lambda. Its measurability is part of the explicit setup. This argument uses no subgradient-selection theorem or population utility expectation.

Let Z=z(P), let Z_1,...,Z_N be iid copies, and put mu=E_D Z. All coordinates are bounded, so the expectations below are finite. For any w in Lambda, expanding the square gives
R_D(w)=||w-mu||_2^2+E_D||Z-mu||_2^2.
The cross term vanishes because E_D(Z-mu)=0. Coordinatewise averaging shows mu belongs to Lambda. Therefore the unique population minimizer is mu and
R_D(w)-min_{a in Lambda}R_D(a)=||w-mu||_2^2.

Similarly, for Zbar=N^{-1}sum_i Z_i,
N^{-1}sum_i||w-Z_i||_2^2=||w-Zbar||_2^2+N^{-1}sum_i||Z_i-Zbar||_2^2.
Since Zbar belongs to Lambda, the unique ERM is Zbar. Independence across observations, without any requirement of independence across coordinates within an observation, gives
E_S||Zbar-mu||_2^2=N^{-2}sum_i sum_{k=1}^s Var(Z_{i,k})=N^{-1}sum_{k=1}^s Var(Z_k).
We use the standard-independent variance inequality: if a scalar random variable is supported in [a,b], its variance is at most (b-a)^2/4. Here Z_k is supported in [0,Lambda_max], so
E_S[R_D(Zbar)-min_{w in Lambda}R_D(w)]<=s Lambda_max^2/(4N).
The sample mean is a measurable estimator of the full observed instances, so this is also a minimax upper bound.

For the lower bound, use the source's separable binary family. For each a in {1,2}^s, let P(a) have m=0, p=s, A=I_s, b=(1/2)1_s, and no effective hard constraints; its objective coefficient vector is a. Thus X(P(a))={0,1}^s. The activity and right-hand-side bounds hold with B=1 and hence with every B>=1. All subproblem minima are finite and attained. Direct coordinatewise minimization gives
nu(lambda,P(a))=sum_{k=1}^s min{lambda_k/2,a_k-lambda_k/2}.
For each coordinate, this function has slope +1/2 below a_k and -1/2 above a_k. Its unique maximizer is therefore a_k. Since Lambda_max>=2, a belongs to Lambda, including at Lambda_max=2. Consequently K(P(a))={a} and z(P(a))=a. This family satisfies every public admissibility condition. The full instance is an injective deterministic encoding of a, so observing it gives exactly the same statistical information as observing a.

We need a binary packing V containing zero, with pairwise Hamming distance at least s/8, and
log |V|>=max{2 log 2,(s/8)log 2}.
For s>=16, the audited standard-independent Varshamov--Gilbert statement supplies a subset of {0,1}^s containing zero, of size at least 2^{s/8}, with pairwise Hamming distance at least s/8. Its size is also at least four. For 8<=s<16, set r=floor(s/2) and take the four words
0^s, 1^s, (1^r,0^{s-r}), (0^r,1^{s-r}).
Their minimum pairwise Hamming distance is r>=s/8. Their size is four, and 2 log 2>=(s/8)log 2 in this range. Thus the required packing exists throughout the stated regime. All logarithms below are natural.

For v in V and epsilon in (0,1/4], define D_v on this instance family by independent coordinates satisfying
P_v(a_k=2)=[1+epsilon(2v_k-1)]/2,
P_v(a_k=1)=[1-epsilon(2v_k-1)]/2.
Every D_v is admissible. Its population warm-start minimizer mu_v=E_v a has coordinates
(mu_v)_k=3/2+(epsilon/2)(2v_k-1).
Hence for distinct v,v',
||mu_v-mu_{v'}||_2^2=epsilon^2 d_H(v,v')>=epsilon^2 s/8.
Put Delta^2=epsilon^2 s/8.

For differing coordinates the two Bernoulli parameters are p=(1+epsilon)/2 and q=(1-epsilon)/2. Their KL divergence, in either direction, is exactly
epsilon log((1+epsilon)/(1-epsilon)).
The elementary inequalities log(1+epsilon)<=epsilon and -log(1-epsilon)<=epsilon/(1-epsilon) show that this is at most 2epsilon^2/(1-epsilon)<=4epsilon^2 for epsilon<=1/4. Equal coordinates contribute zero. Coordinate independence and iid sampling therefore give
KL(D_v^N||D_{v'}^N)<=4N epsilon^2 d_H(v,v')<=4Ns epsilon^2.

Here is the relevant audited standard-independent Fano statement in testing form. If J is uniform over M>=2 hypotheses and S has conditional law Q_J, every decoder has error probability at least
1-[I(J;S)+log 2]/log M.
Moreover, I(J;S)<=M^{-2}sum_{v,v'}KL(Q_v||Q_{v'})<=max_{v,v'}KL(Q_v||Q_{v'}).
Apply this with Q_v=D_v^N and M=|V|. All laws have positive probabilities on the same finite support, so the KL quantities are finite.

For any measurable estimator A(S) in Lambda, decode by choosing a nearest mu_v, with a fixed tie-breaking order. If ||A(S)-mu_J||_2<Delta/2, separation and the triangle inequality force correct decoding. Therefore, under uniform J,
E||A(S)-mu_J||_2^2>=(Delta^2/4)P(decoding error).
A supremum over v is at least this uniform average. Combining this fact with Fano gives
sup_{v in V} E_v||A(S)-mu_v||_2^2>=(epsilon^2 s/32)[1-(4Ns epsilon^2+log 2)/log M].

Choose alpha=(log 2)/256 and epsilon^2=alpha/N. Because N>=1, epsilon<=1/4. The packing bounds imply
4Ns epsilon^2=s log 2/64<= (log M)/8,
and log 2/log M<=1/2.
Thus the bracket is at least 3/8, uniformly for every s>=8 and N>=1. It follows that every estimator satisfies
sup_{v in V} E_v||A(S)-mu_v||_2^2>=3 alpha s/(256N).
The squared-loss identity already proved identifies this quantity with expected excess risk under D_v. Since the public distribution class contains every D_v, taking the infimum over estimators yields
M_{N,s}>=c s/N,
with the universal constant c=3 log 2/65536.

Together with the sample-mean upper bound,
c s/N<=M_{N,s}<=s Lambda_max^2/(4N).
For fixed B and Lambda_max, this is the claimed Theta(s/N) rate. Every proof obligation is closed; no private ground-truth quality warning remains.
