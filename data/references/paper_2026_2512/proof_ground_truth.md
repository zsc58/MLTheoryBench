# Reference Proof

## Proof Structure

Verify that the covariance powers and all traces are well defined. Express the conditional embedding discrepancy through Delta applied to the input feature vector and convert its expectation into a trace. Identify the joint embedding difference with cross-covariance operators and derive their factorization by conditional expectation. Finally compare arbitrary covariance powers using the Hilbert-Schmidt ideal inequality, handling equal exponents and zero covariance explicitly.

## Standard Operator Facts Used

The following are the relevant standard independent facts indexed by theory_022.

- If T is Hilbert-Schmidt, then T^*T is positive trace class and Tr(T^*T)=||T||_{HS}^2. If B is bounded, then TB is Hilbert-Schmidt and ||TB||_{HS}<=||T||_{HS}||B||_{op}.
- If S is trace class and B is bounded on the same Hilbert space, then SB and BS are trace class and Tr(SB)=Tr(BS).
- For a positive bounded operator C, the spectral calculus gives bounded powers C^a for a>=0, with C^0=I and C^a C^b=C^{a+b}. For a>0, ||C^a||_{op}=||C||_{op}^a. Positive trace-class operators are compact and their positive eigenvalues are summable.
- If A is bounded and B is trace class, then |Tr(AB)|<=||A||_{op}||B||_1. For positive trace-class B, ||B||_1=Tr(B).
- Douglas' range-factorization lemma: for bounded operators U:E->G and V:F->G, range(U) subset range(V) implies U=VB for a bounded B:E->F.

The proof below checks the hypotheses whenever these facts are used. No specialized external result is left as an unproved theorem-critical dependency.

## Well-Definedness and Source Regularity

Write C=C_XX and k_x=k(.,x). The covariance integrand is a positive rank-one operator with trace norm ||k_x||^2=k(x,x). Boundedness of k and the assumed Bochner measurability therefore make C positive trace class, with

Tr(C)=E_{X~R_X} k(X,X)<infinity.

The public setup supplies the bounded conditional mean operators and their representation through the distinguished conditional kernels. Their Hilbert-Schmidt regularity is also justified by the source smoothness condition, rather than by an estimation-rate citation. For either conditional mean operator T, let gamma>=1/2 be its specified exponent. The smoothness condition says range(T^*) subset range(C^gamma). Both operators are bounded, so Douglas' lemma yields T^*=C^gamma B for a bounded B. Hence T=B^*C^gamma. If C is nonzero, its positive eigenvalues satisfy

sum_i sigma_i^{2gamma} <= ||C||_{op}^{2gamma-1} sum_i sigma_i < infinity.

The kernel of C contributes zero because gamma>0. Thus

||T||_{HS}^2 <= ||B||_{op}^2 sum_i sigma_i^{2gamma}<infinity.

If C=0, the same factorization gives T=0. This verifies the internal support theory_009 for both conditional laws, including the degenerate case.

Consequently Delta is Hilbert-Schmidt, and D=Delta^*Delta is positive trace class. For every s>=0, C^{s/2} is bounded, so Delta C^{s/2} is Hilbert-Schmidt and all subsequent traces are finite. Trace cyclicity, applied with the trace-class factor D C^{s/2} and bounded factor C^{s/2}, gives

CMMD_s^2 = ||Delta C^{s/2}||_{HS}^2
= Tr(C^{s/2} D C^{s/2})
= Tr(D C^s).

This also covers s=0.

## Conditional Embedding Identification

By the conditional operator representation and the reproducing property,

mu_{Y|x}-mu_{Z|x}=Delta k_x.

For each x,

||Delta k_x||^2 = <D k_x,k_x> = <D,k_x tensor k_x>_{HS}.

Here D is trace class and therefore Hilbert-Schmidt. The random rank-one operator k_X tensor k_X is Bochner integrable in the Hilbert-Schmidt space, since its Hilbert-Schmidt norm is k(X,X), which is bounded. The Hilbert-Schmidt pairing with D is continuous, so expectation may pass through it. It follows that

E_{X~R_X} ||mu_{Y|X}-mu_{Z|X}||^2
= <D,C>_{HS}
= Tr(D C)
= CMMD_1^2.

The last equality is the already established level-s trace identity at s=1. This proves the conditional embedding identification and its trace representation without assuming that identification in the setup.

## Joint Embedding Identification

Under the two joint laws specified in the public task, define

C_YX = E[ell(.,Y) tensor k_X],
C_ZX = E[ell(.,Z) tensor k_X],

where a tensor u tensor v denotes the rank-one operator f -> u <v,f>. These Bochner expectations exist in the Hilbert-Schmidt space by the explicit joint integrability assumptions. Swapping the factors in the joint tensor embeddings and using the canonical tensor/Hilbert-Schmidt isometry gives

||mu_XY-mu_XZ||_{H_k tensor H_ell}^2 = ||C_YX-C_ZX||_{HS}^2.

We derive the kernel chain rule directly. For g in H_ell and f in H_k, reproducing properties and conditional expectation give

<g,C_YX f>
= E[g(Y) f(X)]
= E[(C_{Y|X}^*g)(X) f(X)]
= <C_{Y|X}^*g,C f>
= <g,C_{Y|X} C f>.

The scalar joint expectation is integrable: |g(Y)f(X)| is at most ||g||||f|| ||ell(.,Y)|| ||k_X||, whose expectation is finite by the public joint integrability condition. The conditional-expectation step is therefore legitimate. The covariance pairing is legitimate because H_k functions have bounded evaluations under bounded k. Since the displayed identity holds for every f and g, it proves

C_YX=C_{Y|X} C.

The same calculation under the other joint law proves C_ZX=C_{Z|X} C. In particular, the nonstandard citation indexed by theory_021 is not needed to close this obligation.

Therefore

||mu_XY-mu_XZ||^2
= ||Delta C||_{HS}^2
= CMMD_2^2
= Tr(C D C)
= Tr(D C^2).

All trace products are trace class because D is trace class and C is bounded; C is self-adjoint. This proves the joint embedding identification and the second trace representation.

## Eigenvalue-Controlled Hierarchy

Fix arbitrary real s>=s'>=0 and put r=s-s'. If r=0, the desired inequality is equality, using sigma_max^0=1, including when sigma_max=0.

Suppose r>0. Spectral multiplication gives

Delta C^{s/2} = (Delta C^{s'/2}) C^{r/2}.

The first factor is Hilbert-Schmidt and the second is bounded. Hence the Hilbert-Schmidt ideal inequality yields

CMMD_s^2 <= CMMD_{s'}^2 ||C^{r/2}||_{op}^2
= sigma_max^r CMMD_{s'}^2.

The spectral norm formula is used only at the positive exponent r/2. It remains valid for C=0, in which case both C^{r/2} and C^{s/2} are zero. Thus the proof covers zero covariance and the zero-dimensional input RKHS as well as all nondegenerate cases.

## Explicit Local Source-Proof Repair

The source's trace-based proof can equivalently be completed with the positive sandwich

B=C^{s'/2} D C^{s'/2}=(Delta C^{s'/2})^*(Delta C^{s'/2}).

For r>0, A=C^r is positive bounded and B is positive trace class. Trace cyclicity gives Tr(AB)=Tr(D C^s) and Tr(B)=CMMD_{s'}^2. The audited trace bound therefore gives

Tr(D C^s)=Tr(AB)<=||A||_{op}Tr(B)=sigma_max^r CMMD_{s'}^2.

The unsandwiched product D C^{s'} need not be positive and is not used as the positive factor in this argument. This closes the local proof defect recorded for theory_008 without changing its conclusion or assumptions.

## Obligation Closure

The proof explicitly establishes covariance and trace finiteness, source-grounded Hilbert-Schmidt regularity, the conditional embedding identification, both cross-covariance factorizations, the joint tensor identification, the trace formulas, and the hierarchy for every allowed pair of exponents. Only the stated standard independent operator facts are invoked without derivation. The inherited estimation-rate result theory_012 is unrelated to this population chain and is not used. There are no unresolved theorem-critical obligations.
