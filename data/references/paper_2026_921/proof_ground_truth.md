# Reference Proof

All equalities between parameter functions are understood almost everywhere. Gradients and norms of parameter profiles use the product L2 Hilbert space. Write a_i=Q^i_{ii}, q_i=Q_{ii}, S=Q_sym, m_0=E[xi], and w_i=Var(xi^i)>0. Since S is positive semidefinite, q_i>=0.

## 1. The unilateral potential discrepancy

Deterministic distributed feedbacks and independent initial states and noises give independent state processes, including after a unilateral deviation. Consequently E[X^TQX]=sum_j Q_jj v^j+m^T S m, and the analogous identity holds for Q^i.

Put a_ij=Q^i_ij-Q^j_ji for i!=j and s_i=sum_{j!=i}a_ij. Holding the opponents fixed, the part of Phi-J^i that can change when player i changes policy is

R_i=(s_i/2) int_0^T(v^i+(m^i)^2)dt - sum_{j!=i} a_ij int_0^T m^i m^j dt.

All control and terminal terms cancel. For two policies in V_b^i, the absolute change in the variance term is at most M_b^v C_Q; the diagonal mean term contributes at most (M_b^m)^2 C_Q; and the interaction mean terms contribute at most 2(M_b^m)^2 C_Q by Cauchy-Schwarz. Thus

|[J^i(u)-J^i(tilde u^i,u^{-i})]-[Phi(u)-Phi(tilde u^i,u^{-i})]| <= alpha,

where alpha=(M_b^v+3(M_b^m)^2)C_Q. This calculation applies to nonlinear admissible deviations, not merely affine ones.

## 2. Decomposition and a global potential minimizer

For affine policies, taking expectations and applying Ito's formula gives

m_t^i=m_0^i+int_0^t G_s^i ds,

v_t^i=exp(2 int_0^t K_s^i ds)w_i+int_0^t exp(2 int_s^t K_r^i dr)(sigma_s^i)^2 ds.

In particular v_t^i>0 for every t and every L2 gain. The normalized gradients therefore require no zero-variance extension.

Expanding the quadratic costs gives exactly Phi(K,G)=Phi^1(K)+F(G), where

Phi^1(K)=sum_i[int_0^T((K_t^i)^2+q_i)v_t^i dt+gamma^i v_T^i],

F(G)=int_0^T(|G_t|^2+m_t^T S m_t)dt+(m_T-d)^T Lambda(m_T-d).

The individual costs split in the same way, with the player's own control energy and its matrix Q^i.

It is essential that the resulting minimum is global over V, not only over affine policies. Here is a direct verification. For any admissible distributed profile set g_t^i=E[u^i(t,X_t^i)], Y_t^i=X_t^i-E[X_t^i], and A_t^i=u^i(t,X_t^i)-g_t^i. Admissibility gives g in L2 and E int|A^i|^2<infinity. Independence gives

Phi(u)=F(g)+sum_i E[int_0^T(|A_t^i|^2+q_i|Y_t^i|^2)dt+gamma^i|Y_T^i|^2].

Let p_i solve p_i'=p_i^2-q_i, p_i(T)=gamma^i. Reversing time gives z'=q_i-z^2 with nonnegative initial value; scalar comparison keeps z between 0 and max(gamma^i,sqrt(q_i)), so the solution exists uniquely throughout the finite interval, including q_i=gamma^i=0. Ito's formula for p_i(t)|Y_t^i|^2 gives

E[int_0^T(|A_t^i|^2+q_i|Y_t^i|^2)dt+gamma^i|Y_T^i|^2]
= p_i(0)w_i+int_0^T p_i(t)(sigma_t^i)^2dt+E int_0^T|A_t^i+p_i(t)Y_t^i|^2dt.

The integrability in V justifies the expectation of the stochastic integral; alternatively localization followed by the stated square-integrability gives the same identity.

For completeness, define Gamma h(t)=int_0^t h_s ds and E_T h=int_0^T h_s ds. The Hessian of F is the bounded self-adjoint operator

H=2I+2Gamma^* S Gamma+2E_T^* Lambda E_T.

Cauchy-Schwarz and integration give ||Gamma||<=T/sqrt(2) and ||E_T||<=sqrt(T), hence

2I <= H <= L I,  L=2+T^2 lambda_max(S)+2T max_i gamma^i.

Writing F(G)=(1/2)<G,HG>+<b_0,G>+c, H is invertible: I-H/L has norm at most 1-2/L<1, so its geometric series gives the inverse. Therefore G*=-H^{-1}b_0 is the unique minimizer and grad F(G*)=0. In particular

||G-G*||_2^2 <= F(G)-F(G*) <= (L/2)||G-G*||_2^2.

Choosing K*=-p and G=G* makes every centered square vanish and attains the lower bound for Phi over all V. This affine policy is admissible because p is bounded and G* is square-integrable. Its intercept belongs to the projection ball by the radius assumption. No membership of this global minimizer in V_b is needed for the final comparison.

This verifies the required global optimizer directly. It does not invoke the specialized measure-space verification theorem. If the source's matrix-Riccati representation is used instead, its mean coefficient must be S, and the lifted HJB must have the corrected negative time derivative.

## 3. Gain evaluation, cost differences, and landscape

For a scalar coefficient c>=0 define P_c^K by

(P_c^K)'+2K P_c^K+K^2+c=0,  P_c^K(T)=gamma.

For L2 gains this linear equation has the explicit finite solution

P_c^K(t)=gamma exp(2 int_t^T K)+int_t^T exp(2 int_t^s K)(K_s^2+c)ds.

It is nonnegative. Integrating the derivative of P_c^K(t)v_t^{tilde K} and subtracting the corresponding identity with K gives

F_c(tilde K)-F_c(K)=int_0^T[2(P_c^K+K)(tilde K-K)+(tilde K-K)^2]v^{tilde K}dt,

where F_c(K)=int(K^2+c)v^K+gamma v_T^K. Differentiation, or passage to the first variation in this identity, yields grad_K F_c=2(P_c^K+K)v^K. The variance formula ensures its continuous dependence on L2 perturbations and justifies that passage.

Thus the individual normalized gain gradient is D_J^i=2(P_{a_i}^{K^i}+K^i), and the potential normalized gradient is D_Phi^i=2(P_{q_i}^{K^i}+K^i).

At K*=-p, P_q^{K*}=p, so the cost-difference identity gives

Phi^1(K)-Phi^1(K*)=sum_i int_0^T|K^i+p_i|^2v^{K,i}dt.

Strict positivity of the variance proves uniqueness of the gain minimizer in L2. Applying the cost-difference identity instead from K to K* and completing the square gives

0<=A(K):=Phi^1(K)-Phi^1(K*) <= (U_*/4)||D_Phi(K)||_2^2,

where U_*=max_i sup_t v_t^{K*,i}, a finite strictly positive number.

## 4. Uniform gain regularization and iterate membership

Let h=eta_K in (0,1/2). For one coordinate put P=P_a^K and K_+=K-2h(K+P). Subtracting the evaluation equations gives the pointwise identity

P_a^{K_+}(t)-P_a^K(t)
= -4h(1-h) int_t^T exp(2 int_t^s K_+(r)dr)|K_s+P_a^K(s)|^2 ds <=0.

Indeed, the inhomogeneous difference is (K_+-K)^2+2(K_+-K)(K+P)=-4h(1-h)(K+P)^2. Every evaluation solution is nonnegative. Induction therefore gives 0<=P_a^{K_n}<=P_a^{K_0}. Moreover

K_{n+1}=(1-2h)K_n+2h(-P_a^{K_n})

is a convex combination, so ||K_n^i||_infinity and ||P_{a_i}^{K_n^i}||_infinity are at most the B specified in the task. This proves the source's uniform bound without importing the cited single-agent proposition.

The variance formula now gives constants

l=(min_i w_i)exp(-2BT)>0,

U=(max_i w_i+T max_i||sigma^i||_infinity^2)exp(2BT)<infinity

such that l<=v_t^{K_n,i}<=U for every n,i,t. The intercept projection ensures ||G_n^i||_2<=Cbar_G. The moment-size assumptions on the whole bounded affine parameter classes therefore imply u_n in V_b for every n.

## 5. Gradient bias

For gains put Delta_i=P_{a_i}^{K^i}-P_{q_i}^{K^i}. Since a_i-q_i=-s_i/2, subtraction gives

Delta_i'=-2K^i Delta_i+s_i/2,  Delta_i(T)=0,

Delta_i(t)=-(s_i/2)int_t^T exp(2 int_t^s K_r^i dr)ds.

These are the corrected source signs. Since |s_i|<=C_Q and |K_n^i|<=B,

|Delta_i(t)| <= C_Q(exp(2B(T-t))-1)/(4B).

Here B>0 because a_i>0 and T>0. Squaring, integrating, and using D_J^i-D_Phi^i=2Delta_i gives

||D_J^i-D_Phi^i||_2 <= b_K C_Q,  b_K=exp(2BT)/(4B^(3/2)).

Consequently ||e_K||_2^2<=N b_K^2 C_Q^2 for the full gain bias e_K=D_J-D_Phi.

For intercepts, differentiating the mean costs gives

grad_{G^i}J^i(t)=2[G_t^i+int_t^T[Q^i m_s]_i ds+gamma^i(m_T^i-d^i)],

grad_i F(G)(t)=2[G_t^i+int_t^T[S m_s]_i ds+gamma^i(m_T^i-d^i)].

Let W_ii=s_i and W_ij=-a_ij for i!=j. Then 2[(Sm)_i-(Q^i m)_i]=(Wm)_i, so e_G=grad_G J-grad F=-Gamma^*(Wm).

Since a_ji=-a_ij, the absolute row sums and column sums of W are at most 2C_Q. Weighted Cauchy-Schwarz gives ||Wz||^2<=||W||_infinity||W||_1||z||^2, hence ||W||_2<=2C_Q. Also ||Gamma^*||<=T, and each iterate mean has L2 norm at most M_b^m. Therefore the full-vector bound is

||e_G||_2 <= E_G:=2T sqrt(N)M_b^m C_Q.

The two source notations Q^j_ij and Q^j_ji are equal because Q^j is symmetric; their interchange is not a source error.

## 6. Biased gain descent

Apply the cost-difference identity with K=K_n and tilde K=K_{n+1}. Writing D=D_Phi(K_n), e=e_K(K_n), the increment is -h(D+e), so

A_{n+1}-A_n=sum_i int[-hD_i(D_i+e_i)+h^2(D_i+e_i)^2]v^{K_{n+1},i}dt.

Expand the integrand. For h<=1/2, the coefficient of D_i e_i has absolute value h(1-2h). Using l<=v<=U and Young's inequality gives, for h<=l/(2U),

A_{n+1}-A_n <= -h(l/2-hU)||D||_2^2+h C_b||e||_2^2,

C_b=(U^2+l^2)/(2l).

For example, bound the cross term by h[l|D_i|^2/2+(1-2h)^2U^2|e_i|^2/(2l)], and use hU<=l/2 for the remaining bias-square term.

Choose h<min(1/2,l/(4U),U_*/(2l)). Gradient dominance then gives

A_{n+1} <= rho_K A_n+h C_b N b_K^2 C_Q^2,

rho_K=1-hl/U_* in (0,1).

Iterating,

A_n <= rho_K^n A_0+delta_1,

delta_1=(U_*/l)C_b N b_K^2 C_Q^2.

Thus one may take c_1=(U_*/l)C_b b_K^2. This is the common-gain-step specialization of the source residual.

## 7. Projected intercept descent

Put a=eta_G^min, b=eta_G^max and suppose b<1/L. Let D_eta be the diagonal operator with entries eta_G^i and S_eta=D_eta^(1/2). In the scaled coordinates, the Hessian is S_eta H S_eta, bounded between 2aI and LbI. Thus the unbiased gradient map has squared contraction factor at most 1-2a in scaled norm: its linear part is I-S_eta H S_eta, whose norm is at most 1-2a, and (1-2a)^2<=1-2a. Transforming back yields

||G-D_eta grad F(G)-G*||_2 <= r||G-G*||_2,

r=sqrt((b/a)(1-2a)).

The imposed step-ratio condition is precisely r<1, and b<1/L ensures r>0. Orthogonal projection onto each closed L2 ball is nonexpansive; summing the coordinate inequalities gives nonexpansiveness for the product projection. Since G* belongs to that product ball,

d_{n+1}:=||G_{n+1}-G*||_2 <= r d_n+bE_G.

Consequently

d_n<=r^n d_0+R,  R=bE_G/(1-r).

Smoothness and grad F(G*)=0 now give

F(G_n)-F(G*) <= (L/2)r^(2n)d_0^2+LRr^n d_0+delta_2,

delta_2=(L/2)R^2=2L[bT M_b^m/(1-r)]^2 N C_Q^2.

Take c_2=2L[bT M_b^m/(1-r)]^2. Retaining the cross term avoids the unjustified objective-gap recursion in the previous reference proof.

## 8. Accuracy, quantifiers, and Nash transfer

The constants used to bound gains and variances depend only on the fixed game data and initial gain bounds, not on the step sizes. Therefore a positive threshold smaller than

min(1/2,l/(4U),U_*/(2l),1/L)

is an admissible common upper threshold for the learning rates, subject also to the stated intercept step-ratio condition.

For fixed allowed steps let rho=max(rho_K,r) in (0,1) and

C=A_0+(L/2)d_0^2+LRd_0.

The preceding estimates imply

Phi(u_n)-inf_{u in V}Phi(u) <= C rho^n+delta_1+delta_2.

If C=0, take M=0. If C>0, take

M=max(0,ceil(log(C/epsilon)/(-log rho))).

Then the potential gap is at most epsilon+delta_1+delta_2 for every n>=M. This handles zero initial gaps, C_Q=0, and large epsilon without undefined logarithms or negative iteration counts. In all cases M=O(1+log_+(1/epsilon)), and hence O(log(1/epsilon)) as epsilon decreases to zero.

For every n>=M, player i, and tilde u^i in V_b^i, both profiles in the unilateral comparison belong to V_b. The alpha-potential inequality and global minimality over V give

J^i(u_n)-J^i(tilde u^i,u_n^{-i})
<=Phi(u_n)-Phi(tilde u^i,u_n^{-i})+alpha
<=Phi(u_n)-inf_{u in V}Phi(u)+alpha
<=epsilon+delta_1+delta_2+alpha.

The same M works for every player and every deviation. Both optimization residuals vanish when C_Q=0, as does alpha. The total residual contains the explicit linear alpha term and is not asserted to be purely quadratic in small C_Q.

## Proof-obligation closure

The unilateral discrepancy, exact affine gradients and decomposition, global optimality against nonlinear deviations, gain uniqueness and gradient dominance, uniform gain and variance bounds, full-vector bias estimates, both geometric estimates, and the uniform final transfer have all been derived above. The proof uses no unresolved paper-specific external theorem.
