# Problem

## Verifier and successful-certificate laws

Consider a verifier with deterministic transitions, a set G of solved states, and a finite evaluation horizon T. A student policy is combined with a fixed finite-candidate search procedure. Define V_T^pi(s0) to be the probability that this procedure accepts a verified proof within the horizon, conditional on the initial state s0. For a hierarchical student use the notation V_T^(mu,pi_hi,pi_lo)(s0). These quantities lie in [0,1]; their probabilities include any test-time search or graph-proposal randomization.

Teacher certificates are sampled from a base teacher protocol conditioned on successful verification within its prescribed horizon. Assume the conditioning event has positive probability. Let P_flat be the resulting law of an initial state and a successful flat trace (s0,Y_flat), and let nu_flat be its initial-state marginal. Let P_hier be the resulting law of (s0,M,Y_hi,Y_lo,Y_flat) for a hierarchical teacher, where M is a reusable proof DAG and Y_flat is the fully unfolded trace; let nu_hier be its initial-state marginal. The first two success inequalities below use their respective laws.

For the trace-count comparison, P_flat is specifically the marginal law of (s0,Y_flat) under P_hier. Both students observe only N independent samples of (s0,Y_flat) from this common law, not the teacher DAG labels. They are evaluated on fresh initial states from the same marginal nu_hier. Hierarchical training may infer graph structure from completed training traces, but the test-time graph proposer mu receives only s0. Student decision policies receive only their current represented decision state, not the completed test-time teacher trace or a hidden teacher graph. The flat representation includes an occurrence identifier, so copied subgoals are distinct flat states, and its action space and search procedure provide no memoization or shared-block reuse operation. Include the remaining horizon in represented states when needed to specify finite-horizon kernels.

## Reusable certificates and decision counts

A hierarchical proof object is a finite rooted DAG of blocks. Each block has an interface consisting of finitely many premise-conclusion obligations. An edge from v to w means that v may use the certificate of w. A hierarchical state records a partial DAG, unresolved and solved blocks, and stored certificates. High-level actions may select, expand, order, reuse, or close blocks. A local block certificate is a finite word of ordinary tactics and calls to solved dependency blocks. Recursively replacing calls by the called certificates gives a flat action word. A hierarchical certificate is accepted only when its unfolded word drives the ordinary verifier from the root obligation to a solved state.

For tau in {flat,hi,lo}, write

Y_tau=((S_tau,1,A_tau,1),...,(S_tau,m_tau,A_tau,m_tau)).

Here m_tau is a random nonnegative integer, with 0 <= m_tau <= M_tau < infinity and L_tau=E[m_tau]>0. The flat count includes every unfolded action occurrence. The high-level count includes all high-level decision occurrences of the chosen memoized execution. The low-level trace concatenates the local tactic decisions used to solve each distinct terminal block once. Repeated uses of a stored block do not repeat its internal low-level decisions; repeated action labels within a local proof are nevertheless separate decisions. Individual traces may have zero decisions of a given type, but each L_tau is positive.

For the final construction, use this counting convention: the graph is proposed before the counted execution; each unique block-closing action counts as one high-level decision; the ordinary tactic steps solving terminal blocks count as low-level decisions; and the bounded structural assembly within a nonterminal block is included in its closing action, not counted again as low-level work. Deterministic bookkeeping is not a ranked decision. In the flat representation, count every copied terminal-proof step and every binary conjunction-introduction step.

## Decision distributions and ranking

All states, transitions, candidate maps, and kernels are measurable. For each type tau, define the occurrence-weighted joint decision law D_tau by

E_D_tau[f(S,A)] = E[sum_{i=1}^{m_tau} f(S_tau,i,A_tau,i)] / L_tau

for nonnegative measurable f, using P_flat for tau=flat and P_hier for tau=hi,lo. Let D_tau^S be its state marginal, and let q_tau(.|s) be the conditional teacher-action distribution under this joint law.

Fix an integer k>=1. At every ranked state s, the search procedure supplies a finite candidate set A_tau(s) with |A_tau(s)|>=k+1. Teacher and student distributions are normalized and supported on this same candidate set. Top_k(r(.|s)) denotes the k candidates with greatest r-probability, using a fixed deterministic tie-breaking rule. Let Delta_k,tau(s) be the difference between the kth and (k+1)st largest teacher probabilities. Define

eta_tau = E_{S~D_tau^S}[1-sum_{a in Top_k(q_tau(.|S))} q_tau(a|S)],

e_tau(pi_tau) = E_{S~D_tau^S}[KL(q_tau(.|S) || pi_tau(.|S))].

KL uses natural logarithms, with zero teacher-mass summands interpreted as zero. For every tau assume that there are C_tau>0 and beta_tau>0 such that

P_{S~D_tau^S}(Delta_k,tau(S)<=u) <= C_tau u^(beta_tau)  for every u>0,

and put p_tau=beta_tau/(beta_tau+2).

Retain the following regularity of the student classes: the represented state spaces are compact metric spaces of finite doubling dimension, the relevant action alphabets are finite, and each class is uniformly Lipschitz in total variation and has a positive probability floor rho_tau on the support of teacher actions. In particular, the displayed KL errors are finite. No learning-rate derivation from these regularity assumptions is requested.

## Search completeness and graph coverage

A proposed DAG covers a teacher certificate if the certificate embeds into it in a way that preserves block interfaces, dependency edges, and the candidate sets required for its high-level actions. Given s0, the proposal is sampled using mu(.|s0), without access to the hidden teacher certificate. In the joint experiment consisting of a draw from P_hier and this proposal, let Delta_graph in [0,1] be the probability of failure to cover the teacher certificate, or a specified upper bound on that probability.

Assume flat top-k search is complete: if every action of a successful teacher trace belongs to the student's top-k list at its corresponding certificate decision state, search accepts within the horizon. Assume the analogous completeness property for hierarchical search with memoization: if the proposed graph covers the teacher certificate and all its required high- and low-level actions belong to the corresponding student lists at the certificate decision states, search accepts within the horizon. These are the decision states used in D_tau.

Search-budget and horizon-overflow failure terms are zero. The horizon is large enough for each representation being evaluated; it may vary across members of a growing theorem family.

## Learning-curve assumption

For each positive integer N, assume the fitted policies being evaluated satisfy the total-error bounds

e_tau(hat pi_tau,N) <= a_tau N^(-gamma_tau),

where a_tau,gamma_tau>0 and N counts independent successful theorem traces, not individual decision occurrences. These inequalities concern e_tau itself, including any approximation or inference error. Conclusions for fitted policies are conditional on these assumed inequalities; the success probabilities below concern a fresh test example and test-time randomization, not an unstated training-confidence guarantee.

## Task

Prove that there exist constants c_tau=c(C_tau,beta_tau)>0, independent of the student policies, decision counts, N, and the target failure level, such that

E_{s0~nu_flat}[V_T^pi_flat(s0)] >= 1-L_flat(eta_flat+c_flat e_flat(pi_flat)^(p_flat)),

and

E_{s0~nu_hier}[V_T^(mu,pi_hi,pi_lo)(s0)] >= 1-Delta_graph-L_hi(eta_hi+c_hi e_hi(pi_hi)^(p_hi))-L_lo(eta_lo+c_lo e_lo(pi_lo)^(p_lo)).

Fix delta in (0,1). In the common-data comparison assume

L_flat eta_flat <= delta/2,

Delta_graph+L_hi eta_hi+L_lo eta_lo <= delta/2.

Show that the positive real-valued thresholds

bar N_flat = (2 L_flat c_flat a_flat^(p_flat)/delta)^(1/(p_flat gamma_flat)),

bar N_hier = max_{tau in {hi,lo}} (4 L_tau c_tau a_tau^(p_tau)/delta)^(1/(p_tau gamma_tau))

certify success probability at least 1-delta: the flat conclusion holds for every positive integer N>=bar N_flat, and the hierarchical conclusion holds for every positive integer N>=bar N_hier, provided the stated learning and intrinsic-error assumptions hold for those fitted policies. Thus an actual trace count can be chosen by taking the ceiling and at least one trace.

Finally, in a verifier supporting implication elimination and binary conjunction introduction, construct a depth-d reusable conjunction family with terminal proof-chain length ell, for integers d>=0 and ell>=1. Use the stated counting convention and show

L_hi=d+1,  L_lo=ell,  L_flat=2^d ell+(2^d-1).

For the asymptotic comparison, impose the preceding statistical hypotheses and intrinsic-error budgets at each depth. Assume

p_flat gamma_flat=p_hi gamma_hi=p_lo gamma_lo=alpha>0,

where alpha is independent of d. Write b_tau=c_tau a_tau^(p_tau), and make comparability precise by assuming that one K>=1, independent of d, satisfies

K^(-1)b_flat <= b_tau <= K b_flat  for tau in {hi,lo}.

Prove that a constant C0>0 independent of d satisfies

bar N_flat/bar N_hier >= C0 (L_flat/max{L_hi,L_lo})^(1/alpha).

Conclude an exp(Omega(d)) lower bound on this ratio for fixed or polynomially growing positive ell. This ratio concerns the displayed real-valued sufficient certificates. State clearly that neither the decision accounting nor the certificate ratio is a minimax lower bound or a claim about the unknown minimal number of training traces.
