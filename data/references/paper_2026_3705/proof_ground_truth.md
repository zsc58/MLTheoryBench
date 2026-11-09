# Reference Proof

## Proof Structure

First verify that the procedure and its logarithms are well-defined. Relate each group's wealth to its cumulative coverage error. Apply the quantitative two-asset Jeffreys-mixture comparison, and derive the weighted Bernoulli KL lower bound, including endpoint cases. Bound total wealth using nonnegativity and growth of the scores. Finally compare the bounds and solve the quadratic inequality.

## Complete Proof

Fix a horizon T at which every n_j is positive. All arguments are deterministic and apply to the realized stream. Write

I_t=1{s_t<=tau_t}, a_{t,j}=(I_t-(1-alpha))h_{t,j}, A_j=sum_{t=1}^T a_{t,j}, and n_j=sum_{t=1}^T h_{t,j}.

### 1. Well-definedness and the wealth identity

When I_t=0, the return pair for group j is

(p_{t,j,1},p_{t,j,2})=(1+(1-alpha)h_{t,j}/alpha, 1-h_{t,j}).

When I_t=1, it is

(p_{t,j,1},p_{t,j,2})=(1-h_{t,j}, 1+alpha h_{t,j}/(1-alpha)).

Thus both returns are finite and nonnegative and at least one is positive. For every u in (0,1), each fixed-portfolio return is strictly positive. At every finite time the past-return product is a bounded continuous function on [0,1], positive on (0,1). Its integral against the finite Jeffreys probability measure is finite and strictly positive. The prior-weighted mean lambda_{t,j} therefore lies strictly between zero and one. Induction gives finite, strictly positive V_{t,j}, finite theta_{t,j}, and a well-defined procedure, even when individual returns vanish or a group is absent in some rounds.

The definitions give

lambda_{t,j}p_{t,j,1}+(1-lambda_{t,j})p_{t,j,2}
=1-[(lambda_{t,j}-alpha)/(alpha(1-alpha))]a_{t,j}.

Consequently

V_{t,j}=V_{t-1,j}-theta_{t,j}a_{t,j},

V_{T,j}=1/k-sum_{t=1}^T theta_{t,j}a_{t,j},

and

sum_{j=1}^k V_{T,j}=1-sum_{t=1}^T <theta_t,a_t>.

### 2. The standard independent portfolio comparison

We use the following quantitative standard two-asset result. For any finite sequence of finite nonnegative return pairs (r_{t,1},r_{t,2}) with r_{t,1}+r_{t,2}>0, the portfolio defined as the past-wealth-weighted mean under the Beta(1/2,1/2) prior satisfies

log prod_{t=1}^T[lambda_t r_{t,1}+(1-lambda_t)r_{t,2}]
>= max_{u in [0,1]} log prod_{t=1}^T[u r_{t,1}+(1-u)r_{t,2}] - 0.5 log(pi(T+1)).

This is a deterministic comparison for every return sequence, not a probabilistic assertion requiring independent returns. A zero comparator product has logarithm minus infinity. The update in the task is exactly this portfolio, and Section 1 verifies its return hypotheses.

For completeness, its interpretation as a mixture has the correct normalization: if R_{t,j}(u)=prod_{i=1}^t[u p_{i,j,1}+(1-u)p_{i,j,2}] and M_{t,j}=integral R_{t,j}(u) mu(du), then M_{0,j}=1 and the update formula gives

M_{t,j}/M_{t-1,j}=lambda_{t,j}p_{t,j,1}+(1-lambda_{t,j})p_{t,j,2}.

Thus V_{T,j}=M_{T,j}/k. Applying the stated comparison gives

log V_{T,j} >= -log k + max_{u in [0,1]} log R_{T,j}(u) - 0.5 log(pi(T+1)).

### 3. Weighted outcome counts and the KL lower bound

Fix a group j and let

n_0=sum_{t=1}^T h_{t,j}1{I_t=0},
n_1=sum_{t=1}^T h_{t,j}1{I_t=1}.

Then n_0+n_1=n_j>0 and A_j=alpha n_j-n_0. For a comparator u in (0,1), its return is 1-h_{t,j}+h_{t,j}u/alpha when I_t=0 and 1-h_{t,j}+h_{t,j}(1-u)/(1-alpha) when I_t=1. Concavity of log therefore gives

log R_{T,j}(u) >= n_0 log(u/alpha)+n_1 log((1-u)/(1-alpha)).

Put p=n_0/n_j. If 0<p<1, choose u=p. If p=0 or p=1, take the corresponding limit from (0,1); the zero-weight terms contribute zero. Equivalently, maximize the continuous comparator product on [0,1] and take these limits in the lower bound. This proves

max_{u in [0,1]} log R_{T,j}(u) >= n_j K(p,alpha),

where

K(p,alpha)=p log(p/alpha)+(1-p)log((1-p)/(1-alpha)),

with 0 log 0=0. In particular K is finite for p in [0,1] because alpha is strictly interior.

The needed Bernoulli inequality is

K(p,alpha) >= (p-alpha)^2/[2alpha(1-alpha)+(2/3)|p-alpha|].

Here is an elementary verification. Let B have Bernoulli(alpha) law, put v=alpha(1-alpha)>0, and write psi(t)=log E exp(t(B-alpha)). For every integer m>=2, E|B-alpha|^m<=v. Also m!>=2*3^(m-2). Expanding the exponential and using log(1+x)<=x gives, for |t|<3,

psi(t) <= v t^2/[2(1-|t|/3)].

Exponential tilting of the Bernoulli law gives

K(p,alpha) >= t(p-alpha)-psi(t).

Indeed, with r=alpha exp(t)/(1-alpha+alpha exp(t)), the difference between the two sides is K(p,r)>=0. Nonnegativity follows from concavity of log, and the endpoint cases follow by continuity. If d=|p-alpha|>0, choose t with the sign of p-alpha and magnitude d/(v+d/3), which is strictly less than 3. Substitution yields

K(p,alpha) >= d^2/[2(v+d/3)].

If d=0, the claimed inequality is immediate. This proves the stated bound without a specialized external dependency.

Since p-alpha=-A_j/n_j, we conclude

max_{u in [0,1]} log R_{T,j}(u)
>= r_j := A_j^2/[2n_j alpha(1-alpha)+(2/3)|A_j|].

The denominator is positive, including when A_j=0. Consequently

V_{T,j} >= exp(r_j)/(k sqrt(pi(T+1))).

### 4. Upper bound on total wealth

Put b_t=<theta_t,h_t>=tau_t. Because a_t=(I_t-(1-alpha))h_t and s_t>=0, the following cases exhaust all possibilities:

- If b_t<0, then I_t=0 and -<theta_t,a_t>=(1-alpha)b_t<=0<=(1-alpha)s_t.
- If 0<=b_t<s_t, then I_t=0 and -<theta_t,a_t>=(1-alpha)b_t<=(1-alpha)s_t.
- If b_t>=s_t, then I_t=1 and -<theta_t,a_t>=-alpha b_t<=0<=(1-alpha)s_t.

The last case includes equality, including b_t=s_t=0. Hence the wealth identity gives

sum_{j=1}^k V_{T,j} <= 1+(1-alpha)sum_{t=1}^T s_t.

For q>=0, monotonicity of x^q on positive x gives

sum_{t=1}^T s_t <= D sum_{t=1}^T t^q
<= D integral_1^{T+1} x^q dx
<= D(T+1)^(q+1)/(q+1).

This also covers q=0. Therefore

sum_{j=1}^k V_{T,j} <= B_T := 1+(1-alpha)D(T+1)^(q+1)/(q+1).

### 5. Comparison and conclusion

Each V_{T,j} is positive, so it is at most the total wealth. Combining the bounds and taking logarithms yields

r_j <= log B_T+log k+0.5 log(pi(T+1))=U_T(k).

All logarithms have positive arguments and U_T(k)>0. With x=|A_j|, this implies

x^2-(2/3)U_T(k)x-2n_j alpha(1-alpha)U_T(k)<=0.

Since x>=0, the positive-root bound is

x <= U_T(k)/3 + sqrt(U_T(k)^2/9+2n_j alpha(1-alpha)U_T(k))
<= (2/3)U_T(k)+sqrt(2n_j alpha(1-alpha)U_T(k))
<= U_T(k)+sqrt(2n_j alpha(1-alpha)U_T(k)).

Divide by n_j>0 to obtain the required bound. The argument applies to every group and every horizon satisfying the stated positive-count condition, without any distributional assumptions.

## Obligation Closure

The procedure's well-definedness, positivity of wealth, wealth identity, weighted comparator reduction, endpoint cases, KL inequality, total-wealth estimate, growth summation, and quadratic inversion are derived above. The sole invoked quantitative external theorem is the standard independent two-asset portfolio comparison stated in Section 2, whose algorithm and return hypotheses are explicitly verified. No unresolved theorem-critical obligation remains.
