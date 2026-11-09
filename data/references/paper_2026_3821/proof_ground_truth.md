# Reference Proof

## Proof Structure

1. Introduce private auxiliary quantities from the public data and derive the exact deletion identity.
2. Rewrite the resulting fractional objective as additive size-k maximizations.
3. Construct the exact scalar procedure and prove finite noncycling termination, with an explicit update-counting convention.
4. Certify global optimality at zero residual.

## Complete Proof

### 1. Well-definedness and the exact deletion identity

Let [n]={1,...,n} and let C be the collection of all size-k subsets of [n]. Since 1<=k<n, C is finite and nonempty.

Define privately

q_i=b_i-theta a_i,  w_i=a_i q_i,  c_i=a_i^2,  T=sum_i c_i,

W(S)=sum_{i in S}w_i,  G(S)=sum_{i not in S}c_i=T-sum_{i in S}c_i.

All these quantities are obtained from the given pairs. The public assumptions give T>0 and G(S)>0 for every S in C, so all coefficients and ratios used below are finite and well-defined.

The full normal equation gives sum_i a_i b_i=theta T. For S in C,

G(S)theta_{-S}=sum_{i not in S}a_i b_i=theta T-sum_{i in S}a_i b_i.

Consequently,

theta-theta_{-S}
=[theta G(S)-theta T+sum_{i in S}a_i b_i]/G(S)
=sum_{i in S}a_i(b_i-theta a_i)/G(S)
=W(S)/G(S).

Write R(S)=W(S)/G(S). Thus Delta(S)=R(S) for every feasible set. In particular, the finite set V={R(S):S in C} has exactly M elements, and 1<=M<=|C|.

### 2. Exact additive top-k subproblems

For a real scalar eta, define

F_eta(S)=W(S)-eta G(S).

Expanding the denominator gives

F_eta(S)=-eta T+sum_{i in S}(w_i+eta c_i).

The term -eta T does not depend on S. Thus maximizing F_eta(S) over C is equivalent to maximizing the finite additive objective sum_{i in S}s_i(eta), where s_i(eta)=w_i+eta c_i. Equivalently, this is a linear maximization in membership variables x_i in {0,1}, subject to sum_i x_i=k.

Choose the k largest scores. If a proposed selection omits a strictly larger score than one it includes, exchanging those indices increases the sum; therefore selecting the k largest scores maximizes the objective. Ties may be resolved arbitrarily, or by a fixed index rule to make the procedure deterministic. Every such choice is an exact maximizer. No uniqueness assumption is needed.

### 3. Scalar procedure and finite termination

Because C is finite and nonempty, define

R_*=max_{S in C}R(S),  Z(eta)=max_{S in C}F_eta(S).

For every feasible S,

F_eta(S)=G(S)(R(S)-eta).

This identity proves the residual sign characterization directly. If eta<R_*, a maximizing-ratio set has positive residual, so Z(eta)>0. If eta=R_*, every residual is nonpositive and a maximizing-ratio set has residual zero, so Z(eta)=0. If eta>R_*, every residual is strictly negative; because the class is finite, their maximum is strictly negative. Hence Z(eta)<0.

Use the following exact procedure from any eta^(0) in R. On pass t:

1. Select S_t by an exact top-k maximization of the scores w_i+eta^(t)c_i.
2. Compute r_t=W(S_t)-eta^(t)G(S_t) and the trial ratio lambda_t=W(S_t)/G(S_t).
3. Assign eta^(t+1)=lambda_t. Count this as one ratio update, including an equal-value assignment on a terminal pass.
4. If r_t=0, return S_t; otherwise begin the next pass.

All arithmetic and comparisons are exact. The test r_t=0 is equivalent to lambda_t=eta^(t), since G(S_t)>0. The procedure does not require knowledge of M or R_*.

Exact subproblem optimization gives r_t=Z(eta^(t)), and

eta^(t+1)-eta^(t)=Z(eta^(t))/G(S_t).

Every assigned eta^(t+1) is a feasible ratio and therefore is at most R_*. In particular, an initial parameter above R_* moves into V at or below R_* in its very first update. There cannot be a prolonged decreasing phase above the optimum.

If eta^(t)<R_*, then the update is strictly increasing and satisfies

eta^(t)<eta^(t+1)<=R_*.

If eta^(t)=R_*, the residual is zero and that pass terminates. It follows that after the first assignment, all further nonterminal assignments strictly increase through feasible ratio values. The values produced by nonterminal assignments are distinct elements of V, regardless of whether the initial parameter was below, equal to, or above R_*.

There can therefore be at most M nonterminal assignments. If termination did not follow, another nonterminal assignment would produce an additional distinct element of V, a contradiction. After the last nonterminal assignment, at most one terminal pass is needed. With the stated convention of counting its equal-value assignment, the procedure makes at most M+1 ratio updates and at most M+1 top-k subproblem calls.

Equivalently, an implementation that tests the residual before making the terminal assignment uses at most M value-changing updates and at most M+1 subproblem calls. Either implementation satisfies the public M+1 update bound.

### 4. Global optimality of the returned set

On the terminal pass, r_t=Z(eta^(t))=0. The sign characterization forces eta^(t)=R_*. Since the selected set satisfies

0=F_{eta^(t)}(S_t)=G(S_t)(R(S_t)-eta^(t)),

and G(S_t)>0, it follows that R(S_t)=R_*. The deletion identity then gives Delta(S_t)=max_{S in C}Delta(S), so the returned size-k set is globally maximizing.

The argument covers M=1, zero residual scores, tied scores, multiple optimal subsets, zero individual a_i, and both boundary choices k=1 and k=n-1 whenever the stated retained-denominator condition holds. None of these cases requires an additional assumption.

## Private Source Reconciliation

The estimator-domain condition underlying theory_003 is already explicit in the public task and in the complete source contract. It is not an applied source repair.

The source-local repairs recorded for theory_005, theory_006, and theory_007 concern exact stopping and finite progression only. Global monotonicity from an arbitrary initial scalar is replaced by the source's own first-update-then-increasing argument. Exact stopping uses zero residual rather than an equivalence with consecutive-set equality. Counts distinguish value-changing assignments from the final certification assignment; the frozen M+1 target is unchanged.

All required finite-class fractional-programming facts have been derived above from positivity and exact maximization. No theorem-critical obligation is left to an unexpanded citation.
