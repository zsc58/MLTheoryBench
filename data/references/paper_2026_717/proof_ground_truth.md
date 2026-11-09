# Reference Proof

## Theorem-Critical Obligations

1. Establish feasibility, the nuclear-norm support identity, and the exact regret decomposition.
2. Control the Bregman sum with the correct updated-endpoint trace inequality, including singular cumulative Gram matrices and the initial-gradient subtraction.
3. Control the temporal and initial smoothing terms and obtain the general bound with the stated constants.
4. Verify convexity, positive-definite differentiability, feasibility including singular parameters, dominance, stability, and smoothness for the specified potential.
5. Derive the explicit update and final trace bound.

All five obligations are proved below. The only independent matrix-analysis background is stated explicitly in the next section; the paper-specific Hessian estimate is derived rather than assumed.

## Standard Matrix-Analysis Background

For symmetric positive semidefinite matrices, the principal square root is order preserving. Thus 0<=A<=B implies A^{1/2}<=B^{1/2}. For positive definite matrices, inverse square roots reverse order: 0<A<=B implies B^{-1/2}<=A^{-1/2}.

The function F(A)=Tr(A^{1/2}) is continuous and concave on the positive semidefinite cone. On the positive-definite cone it is twice continuously differentiable and, for symmetric K,

DF(A)[K]=(1/2)Tr(A^{-1/2}K).

Consequently, for positive definite A and B,

F(A)<=F(B)+(1/2)Tr(B^{-1/2}(A-B)),

and D^2F(A)[K,K]<=0. These are the standard independent facts indexed by theory_024. All derivative and inverse-power applications below have positive-definite arguments; positive semidefinite endpoints are handled explicitly by limits.

We also use the elementary fact that Tr(PQ)>=0 for PSD P,Q, which follows from Tr(PQ)=Tr(P^{1/2}QP^{1/2}).

## 1. Support Identity, Feasibility, and Regret Decomposition

For any rectangular matrix Y with singular value decomposition Y=sum_j sigma_j u_j v_j^T, every Z with ||Z||_op<=1 satisfies

<Z,Y>=sum_j sigma_j u_j^T Z v_j<=sum_j sigma_j=||Y||_*.

Equality is attained by Z=sum_j u_j v_j^T. Hence

max_{||Z||_op<=1}<Z,Y>=||Y||_*.

By symmetry, min_{||X||_op<=D}<S_T,X>=-D||S_T||_*. Thus the task's regret expression agrees with comparator regret on K.

Because G>0, L_t=(G^2 I_m+M_t)^{1/2} is positive definite for every t. Admissibility therefore supplies an ordinary gradient at every algorithmic evaluation and implies ||X_{t+1}||_op<=D. Also X_1=0 is feasible.

Write f_t(S)=Psi~(S;L_t/eta), Phi(S)=||S||_*, and S_0=0. For 1<=t<T, the update and the definition of Bregman divergence give

<G_{t+1},X_{t+1}>/D
= B_{f_t}(S_{t+1}||S_t)-f_t(S_{t+1})+f_t(S_t).

Adding and subtracting f_{t+1}(S_{t+1}), summing over t, and using <G_1,X_1>=0 yields

Reg_T/D
= Phi(S_T)-f_T(S_T)+f_1(G_1)
  +sum_{t=1}^{T-1}B_{f_t}(S_{t+1}||S_t)
  +sum_{t=1}^{T-1}[f_{t+1}(S_{t+1})-f_t(S_{t+1})].

This identity also holds when T=1, with both sums empty. Dominance makes Phi(S_T)-f_T(S_T)<=0.

## 2. Correct Endpoint Trace Estimate

Let H_{t+1}=G_{t+1}G_{t+1}^T and A_t=G^2 I_m+M_t=L_t^2. The gradient bound gives H_{t+1}<=G^2 I_m, and therefore

A_t>=M_t+H_{t+1}=M_{t+1}.

For epsilon>0, all matrices in the following inverse powers are positive definite. Inverse-square-root order and a PSD trace pairing give

Tr(H_{t+1}(A_t+epsilon I_m)^{-1/2})
<=Tr(H_{t+1}(M_{t+1}+epsilon I_m)^{-1/2}).

Apply the concavity tangent inequality for F at the updated endpoint M_{t+1}+epsilon I_m, with the other point M_t+epsilon I_m. Rearrangement gives

Tr(H_{t+1}(M_{t+1}+epsilon I_m)^{-1/2})
<=2[F(M_{t+1}+epsilon I_m)-F(M_t+epsilon I_m)].

Let epsilon decrease to zero. The left side involving A_t converges ordinarily because A_t is positive definite; F is continuous at both PSD endpoints. Thus

Tr(G_{t+1}^T L_t^{-1}G_{t+1})
<=2[Tr(M_{t+1}^{1/2})-Tr(M_t^{1/2})].

Summing from t=1 to T-1 gives

sum_{t=1}^{T-1}Tr(G_{t+1}^T L_t^{-1}G_{t+1})
<=2[Tr(M_T^{1/2})-Tr(M_1^{1/2})]
=2[Tr(M_T^{1/2})-||G_1||_*].

This proof does not assert a global Loewner comparison with a pseudoinverse. It handles arbitrary singular M_t, including M_t=0. For T=1 both sides of the summed inequality are zero.

Smoothness at parameter L_t/eta now gives

sum_{t=1}^{T-1}B_{f_t}(S_{t+1}||S_t)
<= (beta eta/2)sum_{t=1}^{T-1}Tr(G_{t+1}^T L_t^{-1}G_{t+1})
<= beta eta[Tr(M_T^{1/2})-||G_1||_*].

The endpoint placement is essential: the inequality with H paired against the inverse square root of the earlier endpoint and the same factor 2 is generally false.

## 3. Stability, Initialization, and the General Bound

Since M_t<=M_{t+1}, square-root monotonicity gives L_t<=L_{t+1}. Upper stability at the scaled parameters implies

f_{t+1}(S)-f_t(S)<=(alpha/eta)Tr(L_{t+1}-L_t)

for every S. Hence

sum_{t=1}^{T-1}[f_{t+1}(S_{t+1})-f_t(S_{t+1})]
<=(alpha/eta)[Tr L_T-Tr L_1].

The boundary value and upper stability from 0 to L_1/eta give

f_1(G_1)<=||G_1||_*+(alpha/eta)Tr L_1.

The temporal sum and the initial term therefore contribute at most

||G_1||_*+(alpha/eta)Tr L_T.

Combining these estimates with the decomposition yields

Reg_T/D
<= beta eta Tr(M_T^{1/2})+(alpha/eta)Tr L_T
   +(1-beta eta)||G_1||_*.

Since M_T<=G^2 I_m+M_T, square-root monotonicity gives Tr(M_T^{1/2})<=Tr L_T. Thus, for the chosen positive eta,

Reg_T
<=D[(beta eta+alpha/eta)Tr L_T+(1-beta eta)||G_1||_*].

Set eta=sqrt(alpha/beta), which balances the two terms in the leading coefficient. Then beta eta=alpha/eta=sqrt(alpha beta), and

Reg_T
<=2sqrt(alpha beta)D Tr(G^2 I_m+M_T)^{1/2}
 +(1-sqrt(alpha beta))D||G_1||_*.

No sign assumption on 1-sqrt(alpha beta) is used: its contribution is retained exactly throughout.

## 4. Admissibility of the Specified Potential

Let h_L(S)=Tr(SS^T+LL^T)^{1/2} for symmetric PSD L.

### Convexity and the singular boundary

For the augmented matrix Y=[S L], we have YY^T=SS^T+LL^T, and therefore

h_L(S)=||[S L]||_*.

The nuclear norm is convex, and S maps affinely to [S L], so h_L is finite and convex in S.

For any PSD L and any S, choose a maximizer W in

||[S L]||_*=max_{||W||_op<=1}<W,[S L]>.

A maximizer exists because the feasible set is compact in finite dimensions. Let Q be the first n columns of W. For every U,

h_L(U)>=<W,[U L]>
=h_L(S)+<Q,U-S>.

Thus Q is a subgradient of h_L at S. Since taking a column block cannot increase operator norm, ||Q||_op<=||W||_op<=1. This verifies feasibility even when L is singular, without claiming that an ordinary gradient exists there.

### Differentiability and gradient for positive definite L

Now let L be positive definite. Then A=SS^T+L^2 is positive definite for every S. Spectral differentiation gives, for every direction H,

Dh_L(S)[H]
=(1/2)Tr(A^{-1/2}(HS^T+SH^T))
=<A^{-1/2}S,H>.

Hence h_L is continuously differentiable and

nabla h_L(S)=A^{-1/2}S.

Moreover,

(nabla h_L(S))(nabla h_L(S))^T
=A^{-1/2}SS^T A^{-1/2}
<=A^{-1/2}AA^{-1/2}=I_m.

Thus ||nabla h_L(S)||_op<=1, consistently with the subgradient verification.

### Dominance and boundary value

Since SS^T+LL^T>=SS^T, square-root monotonicity and taking traces imply

h_L(S)>=Tr(SS^T)^{1/2}=||S||_*.

At L=0 there is equality.

### Upper stability

For 0<=L_1<=L_2, the nuclear-norm triangle inequality gives

h_{L_2}(S)-h_{L_1}(S)
=||[S L_2]||_*-||[S L_1]||_*
<=||[0 L_2-L_1]||_*
=||L_2-L_1||_*
=Tr(L_2-L_1).

The last equality holds because L_2-L_1 is symmetric PSD. Thus alpha=1.

### Hessian bound and smoothness

We derive the needed nuclear-norm Hessian estimate explicitly. Let Y be any full-row-rank matrix and let E be a direction of the same size. Put A=YY^T and F(A)=Tr(A^{1/2}). Along Y+uE,

A'(0)=EY^T+YE^T,
A''(0)=2EE^T.

The second-order chain rule gives

D^2||Y||_*[E,E]
=D^2F(A)[EY^T+YE^T,EY^T+YE^T]
 +DF(A)[2EE^T].

The first term is nonpositive by concavity of F, and the second equals Tr(E^T A^{-1/2}E). Therefore

D^2||Y||_*[E,E]<=Tr(E^T(YY^T)^{-1/2}E).

Apply this to Y=[S L] and E=[H 0]. Because L is positive definite, Y has full row rank for every S. Its number of columns is n+m>=m, so this application imposes no restriction on the relative sizes of the original m and n. We obtain

D^2h_L(S)[H,H]
<=Tr(H^T(SS^T+L^2)^{-1/2}H).

Since SS^T+L^2>=L^2>0, inverse-square-root order gives

(SS^T+L^2)^{-1/2}<=(L^2)^{-1/2}=L^{-1}.

Consequently,

D^2h_L(S)[H,H]<=Tr(H^T L^{-1}H).

For Delta=U-V, Taylor's formula along the segment V+uDelta gives

B_{h_L}(U||V)
=int_0^1(1-u)D^2h_L(V+uDelta)[Delta,Delta] du
<=(1/2)Tr(Delta^T L^{-1}Delta).

This proves beta=1. All admissibility requirements are now established, including the singular-parameter boundary convention.

## 5. Explicit Update and Final Bound

For this family alpha=beta=1 and eta=1. At the algorithmic parameter L_t,

SS^T+L_tL_t^T=S S^T+G^2 I_m+M_t.

The gradient formula therefore yields

X_{t+1}=-D(G^2 I_m+M_t+S_tS_t^T)^{-1/2}S_t.

The general result gives

Reg_T<=2D Tr(G^2 I_m+M_T)^{1/2}.

If lambda_1,...,lambda_m are the nonnegative eigenvalues of M_T, then sqrt(G^2+lambda_j)<=G+sqrt(lambda_j). Summing yields

Tr(G^2 I_m+M_T)^{1/2}<=mG+Tr(M_T^{1/2}),

and hence

Reg_T<=2D(Tr M_T^{1/2}+mG).

All arguments remain valid for zero gradient matrices, singular cumulative Gram matrices, T=1, and arbitrary positive m,n. No theorem-critical proof obligation remains unresolved.
