# Problem

## Setup

### Regime-local data

Let R be a regime set with |R| >= 2. For each r in R, let X_r, H_r, I_r, B_r, and Z_r be measurable state, retained-memory, interface, action, and outcome spaces. The local update and evaluator are measurable maps

F_r: X_r x H_r x I_r x B_r -> X_r x H_r,

e_r: X_r x H_r x I_r x B_r -> Z_r.

Candidate regime transports have specified source and target regimes and compatible component maps on state, memory, interface, and action spaces. A configuration records the regime and these local data. Fix an initial set of configurations; a reachable configuration is one obtained from that set by a finite sequence of the specified local operations and certified regime transports.

Write C_r = Phi(e_r) for the protected evaluator component, and write e_r approx_C e_s when their protected cores coincide or are certified equivalent. This is an equivalence relation. The ambient evaluator space is a separable metric space with its specified measurable structure; Phi is measurable, approx_C is closed, and the protected quotient is supplied with the measurable comparison structure used below. Certified transport preserves the protected component literally or up to this equivalence.

### Certification and protected comparison

For a reachable configuration k, let C(k) be its set of candidate continuations. A continuation occurrence is a pair (k,c), with c in C(k). Its applicable certificate is a(k,c) in {0,1}. Thus certification is evaluated at the current realization, including its retained memory; it is not a function of an update label alone. A continuation is legal exactly when a(k,c)=1.

A certificate may equal 1 only when the associated transport is well typed, realizable on the local components, evaluator-compatible, protected-core preserving, and compatible with the protected comparison data. Certified composition requires legal constituent segments, matching intermediate protected commitments, and coherent composition of the active memory and evaluator transports. Certified transitions remain realizations of the same typed process.

The outcome spaces have the specified orders, preorders, or transported comparison gauges used by the process. A comparison gauge is a specified monotone map between the outcome domains on which it is used. Let J be the specified set of evaluator-outcome records whose comparisons are to be represented. Protected comparison is supplied as a partial Boolean-valued query

b: D -> {0,1},    D subset of J x J.

For a pair in D, b records the truth value of the specified protected comparison, using its given order or gauge. For a pair outside D, the query is undefined, rather than false. These comparison data are invariant under certified changes of protected-equivalent evaluator representatives, with their outcomes transported by the specified gauges. Thus comparison is well defined at the protected-quotient level; the quotient alone is not being identified with a set of comparable pairs.

Let K(k,c) in {0,1} denote satisfaction of the protected requirement for a continuation occurrence. Legality implies K(k,c)=1, but satisfaction alone need not imply certification. The requirement is hard: every occurrence with K(k,c)=0 must be rejected, regardless of its local utility. Fix the given real-valued local utility q on continuation occurrences, with larger values preferred. This q is part of the process specification, not an arbitrary function chosen after a penalty weight.

### Fixed representations and boundary elimination

A fixed representation uses one experience description E, one fixed task family T, and one total real-valued performance function P on its encoded evaluation objects. Faithfulness means preserving exactly the legal continuations, the domain and truth values of protected comparison, and hard rejection of protected violations.

The following are the boundary-eliminating reductions considered here:

- When retained memory is treated only as passive experience, it does not supply an operational protected-memory gate. In particular, the legality decision for the same candidate continuation is unchanged between configurations with identical regime, current state, interface, and action data that differ only in retained memory. Their stored experience descriptions need not be identical.
- When protected comparison is replaced by ordinary scalar comparison, the representation uses the ordinary order of P without a separate test of whether a protected comparison is defined.
- When the hard requirement is replaced by a standard compensable scalar objective, the representation uses the specified utility q with one fixed finite penalty lambda > 0 subtracted for a protected violation. It does not additionally filter, project, or reject candidates on protected grounds. A strict scalar improvement over a legal alternative is therefore not itself disallowed by a hard protected gate.

Retaining and operationally using a protected-memory legality distinction, the protected comparison domain, or a hard rejection rule counts as reconstructing that boundary, including when it is implemented inside an enlarged state description, task restriction, or update rule. Passive storage by itself is not reconstruction. The claim below concerns elimination of these boundaries, not the impossibility of fixed-state simulation or optimization with explicitly retained feasibility constraints.

## Obstruction conditions

Assume at least one of the following holds:

1. There are two reachable configurations with identical regime, current state, interface, and action data but different retained memories, and a common candidate continuation whose certificates at those configurations are respectively 1 and 0.
2. There is a pair of records in J whose protected comparison is undefined, that is, a pair outside D.
3. For the fixed utility q, for every finite lambda > 0 there are a reachable configuration k and candidates c,c' in C(k) such that a(k,c)=1, K(k,c')=0, and

   q(k,c') - q(k,c) > lambda.

The third condition is a non-compensability assumption about the specified utility and available continuations. It is not asserted to follow merely from the word "hard," and it does not quantify over every real-valued proxy function.

## Task

Prove that, for each condition that holds, no faithful fixed representation can eliminate the corresponding boundary in the manner specified above. Consequently, if any of conditions 1-3 holds, no genuine faithful flattening that eliminates the applicable boundaries exists.

Explain why a semantics-preserving representation must instead retain the operational memory gate, the protected comparison domain, or the hard rejection requirement, respectively. Such a representation reconstructs the relevant structure rather than eliminating it; structural loss occurs if that structure is discarded, not merely because a faithful reconstruction uses a fixed encoding.
