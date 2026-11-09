# Reference Proof

## Source contract and scope

The source specifies measurable regime-local carriers, typed transports, evaluator families, a protected-core operator, protected equivalence, and measurable updates (L000043-L000079). Comparisons require a supplied order, preorder, or transported gauge; an arbitrary measurable evaluator codomain does not supply comparison by itself (L000069, L000084-L000094). Protected equivalence and its regularity discipline appear at L000127-L000136. Certification is extensional and can be memory-mediated; it certifies admissibility rather than promising a universally computable decision procedure (L000137-L000162).

The source's fixed tuple has experience E, task family T, and performance measure P, not a transition mechanism named T (L000015, L000163-L000172, L000271-L000274). Its sufficient-reduction discussion explicitly permits absorbing history into experience when history contains no irreducible admissibility information (L000279-L000293). Therefore an operationally passive memory need not have the same stored encoding as another memory. The relevant restriction is absence of its active protected gating role.

All four standing requirements were checked at L000199-L000246. Structural closure and evaluative invariance directly govern the selected reduction/obstruction branch, as the source's traceability paragraph records at L000209. Stability and capacity remain restrictions on source realizations; the present task is the semantic obstruction on their specified continuation and comparison data, not an assertion of stability, learnability, or membership in a quantitative theorem layer. It introduces no stochastic experiment, drift estimate, capacity estimate, or associated constants. No result from the separate stability, factorization, or composition theorem branches is required to prove the obstruction.

The complete obstruction discussion at L000298-L000312 restricts its argument to reductions that remove active boundary semantics. It expressly allows static constrained formulations and does not deny syntactic simulation in an enlarged state. Its scalar calculation uses the given local utility U and a finite violation penalty. The gain-over-penalty premise concerns that utility and that candidate reduction, not every real-valued function. The corrected public condition 3 makes the uniform non-compensability premise explicit for the fixed utility q. The proof must not infer that premise from hardness alone.

## Theorem-critical obligations

1. Identify the operational decision that a memory-passive reduction must give equally to the two configurations in condition 1, without assuming their stored experience codes coincide.
2. Show a mismatch of comparison domains under condition 2, including the case where scalar scores tie or records share an encoding.
3. For an arbitrary finite penalty in the specified scalarization class, derive the violating candidate's strict scalar advantage and connect it to the absence of a hard rejection gate. Do not claim existence of a global optimizer or that every optimizer violates the requirement.
4. Explain the boundary-reconstruction alternative without claiming that a faithful reconstruction itself loses semantics.

All four obligations are derived below. No external theorem or specialized method is used.

## Complete proof

### step_001 — Active retained memory

Assume condition 1. Let k and k' be its two reachable configurations, and let c be the common candidate continuation. Their non-memory local data agree, while

a(k,c)=1 and a(k',c)=0.

Consider a proposed faithful representation that eliminates the operational protected-memory gate in the stipulated manner. Its legality decision for c is unchanged between k and k'. Denote that common Boolean decision by L.

If L=0, it rejects the legal occurrence (k,c). If L=1, it accepts the illegal occurrence (k',c). Either choice contradicts exact preservation of legal continuations.

This argument does not require equality of stored experience descriptions. A representation can retain different histories as data. If it uses the retained protected commitments in those histories to produce different legality decisions here, it has retained the operational memory gate. That is the reconstruction alternative, not a memory-passive flattening.

### step_002 — Partial protected comparison

Assume condition 2. Choose u,v in J with (u,v) outside D. The protected comparison query for this pair is undefined.

In a representation replacing that query with ordinary comparison of a total real-valued P, both encoded records have real scores. The query whether P(u) <= P(v) has a definite truth value. It is true or false, never undefined. Hence its definedness differs from that of the protected query, independently of the order of the scores.

A tie does not fix this problem: equality still gives a defined scalar comparison. Identifying the two records in the encoding also gives equal scores and therefore a defined comparison. Nor does it help to preserve all truth values on D while assigning additional truth values outside D: faithfulness requires preservation of the domain as well as the values on that domain.

A representation may suppress the scalar answer for pairs outside D, but then it represents and uses the protected comparison domain. Because the source comparison data respect the certified protected identifications, preserving that domain and its values retains the relevant protected-quotient comparison semantics. This need not require a particular quotient data structure; it requires the semantic restriction that the scalar-only reduction discarded.

### step_003 — A hard requirement and a finite compensable penalty

Assume condition 3. Fix any proposed standard compensable scalar reduction in the stated class, and let its finite penalty be lambda > 0. The fixed utility is q. Write its score on an occurrence as

S_lambda(k,d) = q(k,d) - lambda(1-K(k,d)).

By condition 3, there are a reachable k and candidates c,c' available at k such that a(k,c)=1, K(k,c')=0, and q(k,c')-q(k,c)>lambda. Soundness of certification gives K(k,c)=1. Therefore

S_lambda(k,c') - S_lambda(k,c)
= q(k,c') - lambda - q(k,c)
> 0.

Thus the compensable score strictly favors the protected violation over an available legal alternative. A scalar-only treatment of the protected requirement cannot reject that strict improvement on protected grounds: the hard rejection mechanism was precisely what it removed. Consequently it does not preserve unconditional rejection of every occurrence with K=0.

This is a semantic and pairwise contradiction, not a theorem asserting that a global maximum exists or that every maximizing algorithm selects c'. An implementation that nevertheless excludes c' because it violates the protected requirement uses an additional rejection, feasibility, projection, or equivalent operational rule. Such an implementation retains the hard boundary and is outside the boundary-eliminating scalarization class. Assigning a singular infinite penalty is likewise outside the stipulated total real-valued, finite-penalty class.

The penalty was arbitrary, and condition 3 supplies a witness after each finite penalty is fixed. Hence no member of that class eliminates the hard boundary faithfully. No quantification over arbitrary utilities is used. In particular, constant or bounded alternative proxies cannot be substituted for the specified q to assert or refute this hypothesis.

### step_004 — Combining the cases and interpreting reconstruction

Each satisfied condition rules out elimination of its corresponding boundary. If at least one condition holds, a representation that purports to eliminate all applicable boundary objects fails at least one exact faithfulness requirement.

A faithful representation can avoid the relevant contradiction only by retaining the operational memory distinction, the domain of protected comparison, or the hard rejection requirement. These objects may be represented inside a larger fixed state, a restricted task family, or an update mechanism. Such a representation is a reconstruction of the pertinent boundary semantics, not their elimination.

The conclusion is therefore conditional and structural: discarding an active boundary loses semantics; retaining it can preserve semantics but is not the asserted flattening. Nothing in the proof rules out static constrained learning, arbitrary syntactic simulation, or representation classes outside the ones specified in the task.

## Completion check

The witnesses in conditions 1 and 3 supply nonempty relevant candidate sets, and condition 2 supplies a pair within the represented evaluation universe. Undefined comparisons are not treated as false. No injectivity of an encoding is assumed. The finite-penalty argument uses lambda > 0 as in the source and assumes neither a uniform utility bound nor an optimizer. The three alternatives need not hold simultaneously. All theorem-critical obligations are closed.
