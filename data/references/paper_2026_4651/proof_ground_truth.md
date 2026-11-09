# Reference Proof

## Obligations and source corrections

The proof closes the following obligations explicitly: norm and gradient well-definedness; the cross-entropy proxy identities and comparisons; batch-gradient error and direction alignment; curvature control and descent; eventual low-loss entry; loss decay and unnormalized-margin growth; valid normalization with initialization accounted for; and the invariant counterexample. No specialized external theorem is used as a black box.

The cross-entropy proxy is H(W)=(1/n) sum_i [1-p_{i,y_i}(W)], not the exponential loss. The incorrect-class probabilities sum to 1-p_{i,y_i}, not to one. The needed batch estimate concerns a matrix gradient error, not a scalar proxy difference. In the source gradient formula the full softmax vector is required; the logarithm comparison uses log s<=s-1; and replacement of a dual norm by the entrywise sum norm is an inequality. The previously recorded normalization repair is retained below. We choose the low-loss starting index so the low-loss bound holds at that index as well as afterwards.

## step_001: Geometry, gradients, and the correct proxy

For c!=y_i set q_{ic}(W)=(e_{y_i}-e_c)^T W x_i, and let z(W)=min_{i,c!=y_i}q_{ic}(W). Define

u_i(W)=sum_{c!=y_i} exp(-q_{ic}(W)),
ell_i(W)=log(1+u_i(W)),
p_{ic}(W)=exp(e_c^T W x_i)/sum_j exp(e_j^T W x_i),
a_i(W)=1-p_{i,y_i}(W)=u_i(W)/(1+u_i(W)),
H(W)=(1/n) sum_i a_i(W).

All these quantities are finite for finite W. Since C>=2, every incorrect-class probability is positive, so ell_i>0, a_i>0, L>0, and H>0.

For either allowed norm, ||A||_max<=||A||. For an entrywise norm this follows directly from its definition. For a Schatten norm, |A_{cj}|=|e_c^T A e_j|<=sigma_max(A)<=||A||. Consequently

|(A x_i)_c|<=R||A||,
|q_{ic}(A)|<=2R||A||,
and ||M||_*<=||M||_sum,

where ||M||_sum is the sum of the absolute values of its entries. The last inequality follows by maximizing <M,A> over matrices with ||A||<=1, whose entries all have absolute value at most one.

The norm unit ball is compact, and the minimum of finitely many linear margins is continuous, so the maximum defining gamma is attained by a matrix U. Separability, after scaling a separating matrix into the unit ball, gives gamma>0. Thus q_{ic}(U)>=gamma for all incorrect classes.

Direct differentiation gives

g_i(W):=grad ell_i(W)=(p_i(W)-e_{y_i}) x_i^T,
g(W):=grad L(W)=(1/n) sum_i g_i(W),
-<g(W),A>=(1/n) sum_{i,c!=y_i} p_{ic}(W) q_{ic}(A).

In particular,

||g(W)||_*>=-<g(W),U>>=gamma H(W).

Also ||g_i(W)||_sum=2a_i(W)||x_i||_1<=2R a_i(W). Averaging yields

gamma H(W)<=||g(W)||_*<=||g(W)||_sum<=2R H(W)<=2R.

The same separator argument on any nonempty batch gives -<g_B(W),U>>=gamma (1/b)sum_{i in B}a_i(W)>0. Therefore every batch gradient used by this algorithm is nonzero. Any maximizing direction has norm one: a direction with norm strictly below one and positive optimal inner product could be rescaled to improve the objective. Thus the update is well-defined for endpoint norms and arbitrary choices among maximizers. Each finite iterate remains finite.

For u>=0, 1-e^{-u}<=u and

u-(1-e^{-u})=integral_0^u (1-e^{-v})dv<=u^2/2.

Applying these inequalities to ell_i and using sum_i ell_i^2<=(sum_i ell_i)^2 gives

L(W)>=H(W)>=L(W)-(n/2)L(W)^2,
1>=H(W)/L(W)>=1-nL(W)/2.

If H(W)<=1/(2n), then a_i<=nH<=1/2 for every i. The identity ell_i=-log(1-a_i)=integral_0^{a_i}(1-v)^{-1}dv gives ell_i<=2a_i, hence L<=2H. If instead L<=log(2)/n, the preceding ratio bound also gives H/L>=1-log(2)/2>1/2.

Finally, integrating the gradient along a line segment and using ||g||_*<=2R proves

|L(W')-L(W)|<=2R||W'-W||.

## step_002: Batch error, alignment, and descent

Fix a batch B of size b and write Xi=g_B(W)-g(W). If m=1, Xi=0. This case is handled before any use of a complementary-batch average. For m>=2, direct subtraction gives

Xi=((m-1)/n) sum_{i in B} g_i(W) -(1/n) sum_{i not in B} g_i(W).

Since m-1>=1,

||Xi||_sum<=((m-1)/n) sum_i ||g_i(W)||_sum<=2(m-1)R H(W).

This is the C.11 component of the existing aggregate indexed as theory_005. It is deterministic and holds for each batch and each current W; unbiasedness or independence of W and the current batch is not assumed.

Let Delta=phi(g_B(W)). Duality, the reverse triangle inequality, and ||Delta||<=1 give

<g(W),Delta>=||g_B(W)||_*-<Xi,Delta>
>=||g(W)||_*-2||Xi||_*
>=gamma H(W)-4(m-1)R H(W)=rho H(W).

For curvature, let p be a softmax probability vector, v=D x_i, and mu=sum_c p_c v_c. The Hessian quadratic form is

v^T(diag(p)-p p^T)v=sum_c p_c(v_c-mu)^2
<=sum_c p_c(v_c-v_{y_i})^2
<=4R^2||D||^2(1-p_{y_i}).

The first inequality follows because the difference between the two squared sums is (mu-v_{y_i})^2. The last uses |v_c-v_{y_i}|<=2R||D|| and the zero contribution of c=y_i.

If W is perturbed by D, each logit changes by at most h=R||D||. Writing these changes as delta_c, the exact ratio

p'_c/p_c=exp(delta_c)/(sum_j p_j exp(delta_j))

lies between exp(-2h) and exp(2h). Summing over incorrect classes and then examples yields H(W+D)<=exp(2R||D||)H(W).

Apply the integral form of Taylor's theorem to L(W-eta Delta). The Hessian bound along the segment and proxy stability bound its remainder by

eta^2 integral_0^1 (1-v) 4R^2 exp(2R eta) H(W) dv
=2R^2 eta^2 exp(2R eta)H(W).

Since eta_t<=eta_0, setting alpha=2R^2 exp(2R eta_0) gives the one-step inequality

L(W_{t+1})<=L(W_t)-eta_t(rho-alpha eta_t)H(W_t).

## step_003: Low-loss entry, margin growth, and normalization

Assume rho>0 and abbreviate L_t=L(W_t), H_t=H(W_t). Choose t_1>=1 so that alpha eta_t<=rho/2 and rho eta_t/4<1 for all t>=t_1. Such a choice exists because eta_t tends to zero. Then

L_{t+1}<=L_t-(rho/2)eta_t H_t,
(rho/2)sum_{s=t_1}^T eta_s H_s<=L_{t_1}.

The Lipschitz estimate and the update bound give

L_{t_1}<=M:=L_0+2R sum_{s=0}^{t_1-1}eta_s.

Let ell_bar=log(2)/n. The divergent stepsize sum permits an integer T>=t_1 with

sum_{s=t_1}^T eta_s>=4M/(rho ell_bar).

The weighted-average inequality then gives some s_* in [t_1,T] with H_{s_*}<=ell_bar/2<=1/(2n). The proxy comparison implies L_{s_*}<=ell_bar. Monotonicity from t_1 onward therefore gives L_t<=ell_bar for all t>=T. Set t_2=T, so t_2>=1 and the low-loss bound includes its starting index. This construction uses the fixed stepsize schedule but imposes no polynomial form or square-summability condition.

For t>=t_2, H_t/L_t>=1/2, hence

L_{t+1}<=L_t(1-rho eta_t/4).

Put A_s=sum_{tau=t_2}^{s-1}eta_tau. Iteration and 1-x<=exp(-x) yield

L_s<=ell_bar exp(-(rho/4)A_s),
H_s/L_s>=1-(log(2)/2)exp(-(rho/4)A_s)
>=1-exp(-(rho/4)A_s).

To obtain the sharper margin estimate, the original descent inequality and H_s/L_s<=1 give

L_{s+1}<=L_s exp(-rho eta_s H_s/L_s+alpha eta_s^2).

Thus

L_t<=L_{t_2} exp(-rho sum_{s=t_2}^{t-1}eta_s H_s/L_s+alpha sum_{s=t_2}^{t-1}eta_s^2).

For every t>=t_2, ell_i(W_t)<=nL_t<=log(2), so u_i(W_t)<=1 and all q_{ic}(W_t)>=0. In particular z_t:=z(W_t)>=0. Choosing a sample and class attaining z_t gives

nL_t>=log(1+exp(-z_t))>=log(2)exp(-z_t).

The last inequality follows from concavity of log(1+x) on [0,1], applied to x=exp(-z_t). Since nL_{t_2}<=log(2), combination with the preceding iterative loss bound yields

z_t>=rho sum_{s=t_2}^{t-1}eta_s H_s/L_s-alpha sum_{s=t_2}^{t-1}eta_s^2.

Define

S_t=sum_{s=0}^{t-1}eta_s,
P=sum_{s=0}^{t_2-1}eta_s,
Q_t=sum_{s=t_2}^{t-1}eta_s^2,
E_t=sum_{s=t_2}^{t-1}eta_s exp(-(rho/4)A_s).

The ratio estimate now gives

z_t>=rho S_t-rho P-rho E_t-alpha Q_t.                 (1)

Here S_t tends to infinity. Also Q_t=o(S_t): for every delta>0, the terms sufficiently far out satisfy eta_s^2<=delta eta_s, while the earlier sum is finite. Likewise E_t=o(S_t), because A_s tends to infinity, so its exponential factor is eventually at most any prescribed delta>0, and its finite initial contribution divided by S_t vanishes. Since P is fixed, (1) implies z_t>=rho S_t/2 for all sufficiently large t.

By the definition of gamma, z_t<=gamma||W_t|| whenever W_t!=0. Therefore

||W_t||>=rho S_t/(2gamma)

for all sufficiently large t. On the other hand, the update always gives

||W_t||<=||W_0||+S_t.

Using this upper bound in the numerator, and the established lower bound only in the denominator, gives

rho||W_t||-z_t<=rho||W_0||+rho P+rho E_t+alpha Q_t,

rho-z_t/||W_t||<=K(P+Q_t+E_t)/S_t

for all sufficiently large t. The fixed initialization term is absorbed legitimately because P>=eta_0>0. This is the retained normalization repair; an upper bound on ||W_t|| alone must not be substituted into the denominator of an arbitrary numerator bound.

The normalization is defined throughout the required range: class coverage implies n>=C>=2, while L(0)=log C>log(2)/n, so the low-loss condition excludes W_t=0 for all t>=t_2. Finitely many remaining indices t>t_2 are covered by increasing K. This can be done without dependence on the reshuffling or maximizing choices: |z_t|/||W_t||<=2R and (P+Q_t+E_t)/S_t>=P/S_t>0. Step_004 shows rho=gamma and hence nonnegativity of the gap, converting the one-sided bound into the stated O estimate under the usual absolute-value convention as well.

## step_004: Full-batch collapse

For every ||W||<=1, the norm dominance already proved gives

q_{ic}(W)<=(|e_{y_i}^T W x_i|+|e_c^T W x_i|)<=2R.

Taking the minimum over sample-class pairs and then the maximum gives gamma<=2R. If rho>0, then

m-1<gamma/(4R)<=1/2.

Because m is a positive integer, m=1 and rho=gamma. For nonzero W_t, the definition of gamma gives z_t/||W_t||<=gamma, so the gap in part (a) is nonnegative. Thus the rate established in step_003 is exactly the required one. All preceding estimates hold for each trajectory and every maximizing direction; no expectation or probability qualification is required.

## step_005: The batch-one counterexample

Fix 0<epsilon<1 and take the two examples in part (b). They satisfy the standing class-coverage and boundedness assumptions, with R=1+epsilon. Write the two rows of W as w_1^T and w_2^T, and set theta=w_1-w_2. Choosing theta=(1,1), for example with w_1=theta/2 and w_2=-theta/2, gives both correct-class margins equal to 1-epsilon>0. Thus the dataset is separable.

Let s=(1,-1). Both x_1 and x_2 have entrywise sign s. For sample 1, with a=p_2(Wx_1)>0, the two row gradients are -a x_1 and a x_1. Its SignSGD update consequently changes theta by +2 eta_t s. For sample 2, with a=p_1(Wx_2)>0, the row gradients are a x_2 and -a x_2, and its update changes theta by -2 eta_t s. All these gradient coordinates are nonzero because epsilon>0 and finite logits have strictly positive softmax probabilities.

Since theta_0=0, induction gives theta_t=c_t s for some real c_t at every iteration, for every sample order and every positive finite stepsize sequence. The two correct-class margins are therefore

q_{12}(W_t)=(1+epsilon)c_t,
q_{21}(W_t)=-(1+epsilon)c_t.

They cannot both be strictly positive, including when c_t=0. At least one binary cross-entropy term log(1+exp(-q)) is at least log(2), so L(W_t)>=log(2)/2 for every t. No decreasing-stepsize or divergent-sum assumption is used in this part.

All theorem-critical obligations are closed.
