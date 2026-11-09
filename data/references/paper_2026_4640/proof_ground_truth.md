# Reference Proof

## Audited contract and obligations

The initial-state distributions are marginals of successful-certificate laws, not the unconditioned base problem distributions. In the comparison both students use the same successful hierarchical source and observe only its inlined traces. Decision distributions are normalized by expected decision counts, not obtained by uniformly sampling a trace and then a position. Their conditional action kernels are the q_tau in the KL errors. The random trace lengths may be zero, but their finite means L_tau are positive. V_T denotes a conditional success probability; realized success or failure indicators are used before taking expectations.

The obligations are: (1) obtain the requested omission exponent, including zero KL; (2) transfer omissions to the flat search guarantee; (3) transfer graph coverage and both omission families to the hierarchical guarantee without changing their laws; (4) solve the two sufficient-count inequalities under the assumed total-KL curves; (5) construct and count the reusable family under the stipulated protocol; and (6) establish a depth-uniform ratio from the explicit certificates. Each is derived below.

The only imported inequality needed is Pinsker's inequality, classified as standard_independent in theory_020: for finite probability distributions Q,P, TV(Q,P)^2 <= KL(Q||P)/2, where TV(Q,P)=(1/2)sum_a |Q(a)-P(a)|. Here both distributions are normalized on the same finite candidate set, and the student floor on teacher support ensures finite KL. No geometric ERM theorem, posterior-learning theorem, or graph-prediction learning theorem is needed: the total-KL learning curves and graph-coverage budget are explicit hypotheses of this task.

## Step 1: Top-k omissions

Fix a decision type and suppress its subscript. Let (S,A) have joint law D, so A conditional on S=s has distribution Q=q(.|s). Write P=pi(.|s), T_Q=Top_k(Q), and T_P=Top_k(P). Define

r=P_D(A not in T_P).

At a fixed state,

Q(T_P^c) <= Q(T_Q^c)+1{T_Q != T_P}.

If T_Q != T_P, choose a in T_Q\T_P and b in T_P\T_Q. There are exactly k elements in each top-k set, so both differences are nonempty. The teacher ordering gives Q(a)-Q(b)>=Delta_k(s), while the student ordering gives P(b)>=P(a), including ties. Therefore

Delta_k(s) <= |Q(a)-P(a)|+|P(b)-Q(b)| <= 2 TV(Q,P).

For every u>0,

1{T_Q != T_P} <= 1{Delta_k(s)<=u}+1{TV(Q,P)>=u/2}.

The pointwise bound 1{TV>=u/2} <= 4 TV^2/u^2 and Pinsker imply

1{TV(Q,P)>=u/2} <= 2 KL(Q||P)/u^2.

Averaging with respect to D^S yields

r <= eta+C u^beta+2e(pi)/u^2.

If e(pi)=0, let u decrease to zero to obtain r<=eta. If e(pi)>0, choose

u_*=(4e(pi)/(beta C))^(1/(beta+2)).

This positive value is permitted because the margin condition holds for every u>0. Substitution yields

r <= eta+c(C,beta)e(pi)^(beta/(beta+2)),

where

c(C,beta)=C^(2/(beta+2))[(4/beta)^(beta/(beta+2))+2(beta/4)^(2/(beta+2))].

This is finite and positive and depends only on the margin parameters. It supplies suitable c_tau for all three decision types. The bound remains valid when its right-hand side exceeds one.

The squared-TV estimate is essential to this derivation. Optimizing C u^beta+O(sqrt(e)/u), as in the superseded GT, gives exponent beta/(2(beta+1)); that calculation does not establish the requested exponent. The corrected calculation is exactly the available source argument at L000350-L000358.

## Step 2: Flat success

Fix the student policy, or condition on the training data that produced it. Draw (s0,Y_flat) from P_flat and run the student search on the same initial state, using fresh search randomness when applicable. The teacher trace is an auxiliary certificate, not an input revealed to the student.

Let F_flat be the realized student failure event and define

O_i={A_flat,i not in Top_k(pi_flat(.|S_flat,i))}.

Completeness gives the event inclusion F_flat subset of the union of the O_i, hence

1{F_flat} <= sum_{i=1}^{m_flat} 1{O_i}.

This also handles an empty certificate: completeness then precludes failure without requiring a decision. Taking expectations gives

1-E_{nu_flat}[V_T^pi_flat(s0)] <= E[sum_{i=1}^{m_flat} 1{O_i}]

= L_flat P_{D_flat}(A not in Top_k(pi_flat(.|S)))

<= L_flat(eta_flat+c_flat e_flat(pi_flat)^(p_flat)).

The middle equality is precisely the defining normalization of the joint occurrence law. No independence of decisions within a trace is used. Rearranging proves the flat guarantee.

## Step 3: Hierarchical success

Fix mu, pi_hi, and pi_lo. Draw the successful teacher certificate from P_hier, then draw the proposal using mu(.|s0) with no access to the hidden teacher certificate, and include any search randomness. Let C_graph be the coverage event. Its complement has probability at most Delta_graph.

Define high- and low-level omission events on the teacher's memoized decision traces:

O_i^hi={A_hi,i not in Top_k(pi_hi(.|S_hi,i))},

O_j^lo={A_lo,j not in Top_k(pi_lo(.|S_lo,j))}.

Hierarchical completeness states that coverage together with the absence of all these omissions ensures acceptance. For the realized failure event F_hier,

1{F_hier} <= 1{C_graph^c}+sum_{i=1}^{m_hi}1{O_i^hi}+sum_{j=1}^{m_lo}1{O_j^lo}.

Average this inequality under the original joint experiment. In particular, do not replace D_hi or D_lo by their laws conditional on coverage. No independence of coverage and omissions is needed. The decision traces retain their P_hier marginal, so

1-E_{nu_hier}[V_T^(mu,pi_hi,pi_lo)(s0)]

<= Delta_graph+L_hi r_hi+L_lo r_lo,

where r_tau=P_{D_tau}(A not in Top_k(pi_tau(.|S))). Applying Step 1 to each type proves the hierarchical inequality. The low-level sum counts the work for distinct terminal blocks once; calls to a stored certificate do not create new local proof occurrences. Other actual high-level decisions, if present in a chosen protocol, remain included in m_hi.

## Step 4: Sufficient trace counts

Fix delta in (0,1). Apply the success inequalities to fitted policies satisfying the assumed total-KL learning curves. These are conditional assertions for the fitted policies; no probability over training is inferred from the mere availability of independent traces.

For the flat learner,

1-E[V_T^hat pi_flat,N] <= L_flat eta_flat+L_flat c_flat a_flat^(p_flat) N^(-p_flat gamma_flat).

The first term is at most delta/2. The second is at most delta/2 whenever

N >= (2 L_flat c_flat a_flat^(p_flat)/delta)^(1/(p_flat gamma_flat))=bar N_flat.

For the hierarchical learner, the sum of graph error and intrinsic losses is at most delta/2. It suffices to make each remaining learning term at most delta/4. For tau in {hi,lo}, this holds when

N >= (4 L_tau c_tau a_tau^(p_tau)/delta)^(1/(p_tau gamma_tau)).

Taking the maximum gives bar N_hier. Thus either advertised bound holds for every positive integer N above its respective real threshold, subject to the corresponding assumed error bounds. Choosing max{1,ceil(bar N)} handles integer trace counts and thresholds below one.

The pure-power inequalities concern total e_tau. The argument does not discard a positive approximation or inference floor. An N-independent positive floor cannot in general be absorbed into a fixed multiple of N^(-gamma) for arbitrarily large N; the task assumes the displayed total-error inequalities themselves. Likewise, if mu is learned, its fitted graph error must satisfy the stated intrinsic-error budget at the sample count being certified. No separate graph-learning rate is claimed.

## Step 5: Reusable conjunction family

Choose propositions A_0,...,A_ell and premises A_0 and A_{i-1} implies A_i for 1<=i<=ell. Set B=A_ell. There is a terminal proof of B using ell successive implication-elimination decisions. Under the chosen counting convention, premise access and deterministic bookkeeping require no additional ranked decisions. This constructs a particular proof of the desired length, not a lower bound on every possible proof.

Define B^(0)=B and B^(j+1)=B^(j) AND B^(j). For depth d use blocks v_0,...,v_d, root v_d, and dependency edges v_j to v_{j-1} for 1<=j<=d. Block v_j has the obligation to prove B^(j) from the same premises. The local certificate of v_0 is the ell-step terminal chain. For j>=1, the local certificate of v_j calls v_{j-1} twice and combines the two returned proofs by one conjunction introduction. An edge records the dependency; its two uses are recorded by the two calls, not by parallel edges.

Propose this DAG and use a fixed dependency-respecting execution. Solve the terminal chain once, close v_0, and then close v_1 through v_d in order, each time storing the certificate. There are exactly d+1 unique closing actions. Nonterminal assembly is included in those actions by the stipulated protocol, and the only separately counted low-level work is the terminal chain. Thus

L_hi=d+1 and L_lo=ell.

These are deterministic counts, so they also equal their averages. If additional selection actions or separately ranked assembly steps were used, their counts would have to be included; they are not part of this chosen execution.

Let F_j be the flat action-occurrence count of the unfolded certificate for v_j. Recursive expansion of calls gives

F_0=ell,  F_{j+1}=2F_j+1.

Induction yields F_j=2^j ell+(2^j-1). Hence

L_flat=2^d ell+(2^d-1).

The d=0 case gives one terminal block, one high-level closing decision, ell low-level decisions, and ell flat decisions, as required. The constructed local certificates verify by implication elimination and conjunction introduction, so their recursive unfolding is an accepted ordinary proof. The horizon can be chosen large enough for both representations.

The statistical comparison remains conditional on its margin, learning, and intrinsic-error assumptions; decision counting alone does not prove a learning rate. The construction is compatible with zero intrinsic teacher-tail and graph-coverage errors, for example with k=1, a deterministic teacher choosing the described certificates, and a graph proposer returning the described graph from the theorem input. Zero-teacher-mass alternative candidates can provide the required second candidate. The probability floor concerns student probabilities on teacher support, not a requirement that the teacher assign positive probability to every alternative. No assumption that all flat proof algorithms must use these unfolded certificates is made.

## Step 6: Depth-uniform certificate ratio

Set b_tau=c_tau a_tau^(p_tau). Under the common fixed exponent alpha, the explicit unrounded thresholds give

bar N_flat/bar N_hier

= [b_flat L_flat/(2 max{b_hi L_hi,b_lo L_lo})]^(1/alpha).

The uniform comparison b_tau<=K b_flat implies

bar N_flat/bar N_hier >= (1/(2K))^(1/alpha) [L_flat/max{L_hi,L_lo}]^(1/alpha).

Thus C0=(1/(2K))^(1/alpha) is positive and independent of depth. Uniform comparability of ratios suffices; the b_tau need not individually be constant across the family.

For ell>=1 and d>=0,

L_flat>=2^d ell,

max{d+1,ell}<=(d+1)ell.

Consequently

bar N_flat/bar N_hier >= C0 [2^d/(d+1)]^(1/alpha)

= exp((log(2)/alpha)d-O(log(d+1))).

This proves the required exp(Omega(d)) lower bound, in particular when ell is fixed or grows polynomially. The assumptions and intrinsic-error budgets must hold for the family members being compared, and alpha and K are fixed independently of d.

The ratio just derived concerns the explicitly defined real-valued certificates. It is not obtained by dividing two unspecified upper bounds, and no separate exponential claim about their integer ceilings is needed. These are sufficient certificates from the specified search analysis, not minimax lower bounds, necessary sample counts, or shortest-proof lower bounds. Alternative proofs or stronger flat representations may outperform these certificates.

## Closure

All six obligations are closed. The squared-TV/Pinsker calculation is explicit; the two search bounds use the correctly normalized laws and realized indicators; the threshold calculation retains every assumed error term; the family specifies its certificates and counting convention; and the ratio retains uniform constants and the sufficient-certificate qualification. No unresolved specialized or paper-specific proof dependency remains.
