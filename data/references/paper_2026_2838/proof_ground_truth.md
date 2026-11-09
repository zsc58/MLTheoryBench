# Reference Proof

## Contract and Obligations

Learning is improper and information-theoretic: the output may be any Boolean function, and only example and membership-oracle calls are bounded. There is one learner and one polynomial bound uniform over dimension, target, compatible distribution, and error/confidence parameters. Compression strategies are deterministic finite query trees, fixed from the input sample, and their version spaces contain all transcript-inducing concepts.

We explicitly establish confidence amplification, uniform success, a target-independent weak certificate, recursive certification, polynomial class-size control, the VC lower bound, and the converse closure learner. Empty samples, empty classes, singleton classes, zero budgets, and empty transcripts are handled below. General error boosting is also reconstructed at the end to close the selected supporting dependency, although confidence amplification alone suffices for the flagship forward implication.

Throughout the proof, logarithms in counting statements are base two; ln denotes the natural logarithm. Integer budgets may be rounded upward and padded. All probability spaces used below have finite observation alphabets; internal randomness is taken independently of fresh oracle samples.

## 1. Degenerate Cases

For S empty, the depth-zero tree certifies S. If H_d is empty, no S is realizable and there is no target-distribution pair to learn. If H_d consists of a single concept g, every realizable S is contained in supp(g); the empty transcript has version space {g} and certifies S. The learner can return g without oracle calls. An empty-support target has no compatible probability distribution and creates no learning requirement.

There is one further useful zero-budget fact. Suppose a learner at error 1/18 and failure probability 1/3 makes no oracle calls. Its output distribution is then independent of the target and example distribution. If two nonempty concepts a,b differ at x, say a(x)=1 and b(x)=0, use the point mass at x for target a. Success forces the output to label x positively, so that event has probability at least 2/3. For target b, choose any compatible distribution; one-sided success forces the output to label x negatively with probability at least 2/3. These are incompatible requirements on the same observation-free output distribution. Thus there is at most one distinct nonempty concept, which may be returned directly. Nevertheless, if the class also contains the empty concept, a nonempty positive sample can require one query to exclude it. This explains the constant floor in the supporting compression bound.

## 2. Confidence Amplification

Let a base learner at parameters (1/18,1/3) have budget m_0 for each oracle. Put b=max(1,m_0). For any fixed compatible target-distribution pair and eta in (0,1/2], run the base learner independently k times on fresh examples and independent internal randomness, where k is a sufficiently large integer multiple of ln(1/eta). Take the pointwise majority of its outputs.

Each run succeeds with probability at least 2/3. The elementary Chernoff lower-tail inequality for a sum Z of independent Bernoulli variables is P(Z<=(1-a)E Z)<=exp(-a^2 E Z/2), for 0<a<1. Applying it here shows that, except with probability eta, the successful set G has size at least 3k/5.

On that event, every point outside the target is labeled zero by more than half the outputs, so the majority has no false positives. If the majority misses a point, at least |G|-k/2 successful outputs miss it. Since |G|>=3k/5, this is at least |G|/6. Therefore its miss indicator is at most (6/|G|) times the sum of the successful outputs' miss indicators. Integrating gives false-negative mass at most 6/18=1/3. The cost is O(b ln(1/eta)) for each oracle. We may relax this error guarantee to 2/3 when constructing weak certificates.

## 3. Uniform Success for Surviving Concepts

Fix d with N=|H_d|>=1, a target h*, and a compatible D. Run an ordinary learner at error epsilon and failure probability beta=alpha/N. Prefetch a fixed upper-bound number M of examples before its queries, which can simulate any interleaved learner. For our later application we pad M to be at least one.

For every nonempty concept h, define D_h to be D conditioned on supp(h) when a_h=D(supp(h))>0. If a_h=0, choose any fixed distribution supported on supp(h). Let E_h be the event that h contains all prefetched examples, agrees with all membership answers, and the output fails the one-sided epsilon guarantee for (h,D_h).

Fix internal randomness rho. Let A_h^rho be the ordered sample sequences causing E_h in the actual run. Every such sequence lies in supp(h)^M. Because h agrees with the realized membership answers, rerunning the deterministic learner on the same sequence with target h gives the same queries, answers, and output. Hence A_h^rho is contained in the failure set F_h^rho of the counterfactual run with target h and example distribution D_h.

If a_h>0, the product measures satisfy

D^M(A_h^rho)=a_h^M D_h^M(A_h^rho)<=D_h^M(F_h^rho).

If a_h=0 and M>=1, survival of the examples has probability zero. If M=0, the identical membership-transcript argument gives the same domination without any sample factor. Averaging over rho and applying the ordinary guarantee gives P(E_h)<=beta. A union bound over the N concepts proves that, with probability at least 1-alpha, the output succeeds simultaneously for every surviving nonempty concept, with its false-negative guarantee evaluated under that concept's D_h.

This derivation is not a claim that every surviving concept contains the support of the original D. The conditional distributions are essential.

## 4. Polynomial VC Dimension and Class Cardinality

Let M be an integer polynomial upper bound on the original learner's calls to each oracle at epsilon=delta=1/3. We prove v=VC(H_d)<=9M+1.

Suppose a set B of size n=9M+2 is shattered. Put k=4M+1. For each k-subset U of B, choose h_U in H_d whose restriction to B is the indicator of U; no assumption is made about its values outside B. Give the learner target h_U and examples uniform on U, with U uniform over all such subsets.

Fix the learner's internal randomness. Prefetch exactly M examples and pad its membership phase to M answers. For a realized ordered sample P, let r be its number of distinct points. Its likelihood under U is k^{-M} when U contains those points and zero otherwise. Thus the posterior is uniform over exactly binom(n-r,k-r) candidates. Since r<=M and adding a required sample point multiplies this count by (k-r)/(n-r)<1, the candidate count is at least binom(8M+2,3M+1).

For fixed P, at most 2^M membership-response strings occur, even if queries are adaptive or lie outside B. At a fixed response string the output's positive set A on B is fixed. Successful one-sidedness requires A subseteq U. Error below one half, with |U|=4M+1, requires |A|>=2M+1. Consequently a response string can succeed on at most binom(7M+1,2M) candidates U. The ratio of the lower candidate count to this per-string upper count is

binom(8M+2,3M+1)/binom(7M+1,2M)
=product_{j=0}^M (7M+2+j)/(2M+1+j)
>=2^{M+1}.

Therefore conditional success is at most one half, and averaging over P preserves that bound. The calculation holds for every fixed internal seed, so averaging over seeds also bounds randomized success by one half. This contradicts the learner's success probability at least two thirds on every pair. Hence v<=9M+1, including M=0.

For completeness, the finite-domain Sauer counting bound is |H_d|<=sum_{i=0}^v binom(L,i), where L=2^d. Its elementary induction splits a set family by its last domain point: the union of the two trace families has VC dimension at most v, their intersection has VC dimension at most v-1, and their cardinalities add to the original cardinality. Pascal's identity completes the induction. For v>=1, the displayed binomial sum is at most (L+1)^v, by encoding each subset of size at most v as an ordered v-tuple padded with a sentinel. Thus

log_2 |H_d|<=(d+1)v.

When |H_d|>=2, v>=1 because two distinct concepts differ at some point. The preceding bound therefore makes log |H_d| polynomial in d. Singleton and empty classes were already handled separately.

## 5. A Single Weak Strategy Working for Every Target

Fix a nonempty realizable S and a dimension with N=|H_d|>=2. Let U_S be uniform on S. It is compatible with every target in V(S).

Use the amplified learner from Section 2 and then the uniform-success conversion from Section 3. Require uniform-success failure alpha=1/(2N); the underlying ordinary learner therefore runs at failure beta=1/(2N^2). Its error may be taken as 2/3, and its budget is O(b log(2N)) for each oracle. Prefetch at least one example, absorbing this padding in the same bound.

Put the internal seed and the entire iid U_S example stream in one common probability space. For each target a in V(S), the probability that its run fails the simultaneous guarantee is at most 1/(2N). A second union bound, now over the generating targets a in V(S), shows that all their runs satisfy uniform success together with probability at least 1-|V(S)|/(2N)>=1/2. Fix one such common seed and example stream. This selection depends on S and the class, not on which target will later be queried.

Compile the resulting learner into a deterministic tree. Query each prefetched example point before supplying the hardwired sample to the learner. If any compiled example query is negative, stop. Otherwise simulate the learner's ordinary adaptive membership queries with the fixed seed and sample. All branches have the stated bounded depth. A branch realizable by a target in V(S) answers every compiled example query positively and reproduces that target's successful run.

For such a branch r, let P be the hardwired example set and (q,a) the ordinary query transcript. The full transcript version space is exactly

W(r)=V(P) intersect {h in H_d:h(q)=a}.

This equality does not restrict W(r) to V(S). Since P is nonempty, every h in W(r) is a nonempty concept. Uniform success therefore places the simulated output g inside every h in W(r). For the generating target a in V(S), conditioning U_S on supp(a) leaves U_S unchanged, so the output covers at least one third of S. Hence

|S intersect intersection_{h in W(r)} supp(h)|>=|S|/3.

We have constructed a weak compression strategy, simultaneously on every V(S)-realizable branch. Its depth is O(b log(2N)). Choose a common integer q_d>=1 dominating that depth. By Section 4 it is bounded by C(m_0+1)(d v+1), and is polynomial in d. This is the constant-floor repair of the supporting source estimate.

## 6. Recursive Full Certification

Fix these weak strategies for all nonempty realizable sets. Define Sigma_S recursively. If |S|<=q_d, query every point of S and stop, including the depth-zero case S empty. Otherwise run its weak strategy. On each first-stage transcript r_0 realizable for V(S), let

I=S intersect intersection_{h in W(r_0)} supp(h), and R=S\I.

Then |R|<=2|S|/3, and the target realizing r_0 also witnesses realizability of R. Continue with Sigma_R. On first-stage branches not realizable for V(S), stop. The recursion is finite on every branch.

Induct on |S| to prove certification. The direct-query case is immediate. In the recursive case, take any complete transcript r_0 followed by r_1 that is induced by a target containing S. Its suffix is realizable for V(R), so the induction hypothesis certifies R from r_1. Every concept inducing the entire transcript induces r_0 and therefore contains I; it also induces the prescribed suffix strategy Sigma_R and therefore contains R. It contains I union R=S, as required, whether or not it was initially in V(S).

Every nonterminal round uses at most q_d queries and shrinks the unresolved set by a factor at most 2/3. For nonempty S, after ceil(log_{3/2}|S|) such rounds its size is at most one, so a final direct-query round costs at most q_d. Thus depth is at most q_d(1+ceil(log_{3/2}|S|)). Since |S|<=2^d, this is polynomial in d. Taking a polynomial envelope over dimensions proves the forward implication.

## 7. Compression Implies Learning

Suppose every realizable S in dimension d has a scheme of depth at most a common polynomial p(d). Let k_d be a nonnegative integer polynomial upper bound on p(d), and fix one such deterministic scheme for each realizable S. These choices require no polynomial-time computation.

For given epsilon,delta in (0,1), draw n iid positive examples and let S be their set of distinct values. Run its scheme against the target and record the realized labeled transcript T, including its query locations. Let

W(T)={h in H_d:h agrees with every labeled query in T},

C_T=intersection_{h in W(T)} supp(h).

The target belongs to W(T), so this version space is nonempty and C_T is contained in the target support. Compression gives S subseteq C_T. Output the Boolean indicator of C_T; it need not belong to H_d.

For a fixed nonnegative integer k, define Cl_k(H_d) using all labeled query sequences of lengths 0 through k whose version spaces are nonempty. In particular, length zero is allowed. A labeled sequence of length t has at most (2^{d+1})^t possibilities. Its version space, and hence its closure, depends only on that sequence, not on the entire strategy tree or the sample used to choose it. Therefore

|Cl_k(H_d)|<=sum_{t=0}^k 2^{(d+1)t}<=2^{(d+1)(k+1)}.

This counting bound also implies VC(Cl_k(H_d))<=(d+1)(k+1), although the cardinality bound alone suffices here.

For every fixed C in Cl_{k_d}(H_d) with D(X_d\C)>epsilon, the probability that all n independent observations lie in C is at most (1-epsilon)^n<=exp(-epsilon n). Union-bounding over the fixed closure class shows that any such C containing all observations exists with probability at most

2^{(d+1)(k_d+1)} exp(-epsilon n).

Choose

n=ceil(((d+1)(k_d+1) ln 2+ln(1/delta))/epsilon).

Then this probability is at most delta. Our output belongs to that class and contains every observation, so its false-negative mass is at most epsilon with probability at least 1-delta. One-sidedness holds on every realized run. There are at most k_d membership calls and n example calls, both bounded by a polynomial in d, 1/epsilon, and 1/delta. This proves the converse and completes the characterization.

## 8. Closure of the General Boosting Dependency

Here is the additional source-grounded derivation of the selected general error-boosting result. Its zero-budget case is handled in Section 1, so suppose m_0>=1. Use the confidence-amplified learner with error 1/3 from Section 2. It costs O(m_0 ln(1/eta)) for each oracle.

Fix epsilon in (0,1), delta in (0,1/2], T=ceil(log_3(1/epsilon)), tau_s=3^{-s}, w_s=3^s, W=sum_{s=0}^T w_s, and eta_s=delta w_s/(100W). Then W=O(1/epsilon) and sum_s eta_s=delta/100. Initialize H_0=0. At scale s use fresh examples to estimate p_s=D(H_s=0), with a test budget C ln(1/eta_s)/tau_s. Elementary Bernoulli Chernoff bounds give, except with probability eta_s, both implications p_s>=tau_s implies estimate>=2tau_s/3, and p_s<=tau_s/3 implies estimate<2tau_s/3. The upper-tail form used here is P(Z>=(1+a)E Z)<=exp(-a^2 E Z/(2+a)); the lower-tail form was stated in Section 2.

If the estimate is below threshold, retain H_s. Otherwise use rejection sampling to obtain the amplified learner's prefetched residual examples, with an original-example deadline C m_0 ln(1/eta_s)/tau_s. On the good test event, triggering implies p_s>tau_s/3. Conditional on the past, the probability of missing the required number of acceptances by that deadline is at most eta_s, by the Bernoulli lower-tail bound. Define the ideal retained sequence using an infinite fresh iid stream; its accepted points are iid from D conditioned on H_s=0. The ideal residual learner fails with probability at most eta_s. This probability is not asserted after conditioning on deadline success. Instead, union-bound the deadline and ideal-learner failures. When the deadline is met, the actual learner agrees with the ideal one.

OR the residual output into H_s. Conditional failure bounds and a union bound over scales show that all tests, simulations, and ideal learner guarantees hold together with probability at least 1-3 sum_s eta_s>=1-delta. On this event, outputs remain one-sided. A skipped scale has p_{s+1}=p_s<tau_s; a learned scale has p_{s+1}<=p_s/3. Starting with p_0=1 gives p_1<=1/3<=tau_0=1, and induction gives p_s<=tau_{s-1} for s>=1. Consequently p_{T+1}<=tau_T<=epsilon.

Each scale's original-example cost is O(m_0 w_s ln(1/eta_s)); its membership cost is O(m_0 ln(1/eta_s)), no larger than the former bound because w_s>=1. Finally,

sum_s w_s ln(1/eta_s)
=W ln(1/delta)+sum_s w_s ln(100W/w_s)
=O(W ln(1/delta)).

Indeed W/w_s<=C 3^{T-s}, and sum_s 3^s(T-s+1)=O(W) by the convergent geometric sum after substituting j=T-s. Thus both costs are O((m_0/epsilon) ln(1/delta)). This calculation includes all T+1 scales and remains valid as epsilon approaches one.

All theorem-critical and selected supporting obligations are closed. The recorded source-local repairs are the elementary boosting proof corrections and the constant-floor compression estimate; neither changes the public characterization.
