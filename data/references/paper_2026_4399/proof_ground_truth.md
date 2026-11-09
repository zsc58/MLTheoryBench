# Reference Proof

## Proof Structure

Compare the MDL optimizer with the uniform model before invoking pseudorandomness. This proves both existence of an optimizer and a polynomial bound on its description length. Its likelihood thresholds therefore give non-uniform polynomial-time tests. Normalization bounds their acceptance probabilities under uniform input, and security transfers those bounds to generator outputs. A real-valued shortfall estimate gives the entropy lower bound. The uniform-model comparison then gives epiplexity and the entropy-increase conclusion.

## Complete Proof

Fix the coding machine, the uniform implementation, and an admissible polynomial time bound T from the problem. Let c_U be the length of the uniform-model program. The dimension is auxiliary input and is not part of this program's description. At dimension m, its evaluator returns 2^{-m}, its sampler outputs m independent fair bits, and both run within the assumed time bound.

### 1. Uniform comparison and existence of optimizers

For every distribution Y on m-bit strings, the uniform model has objective value m+c_U. Every model's log-loss is nonnegative, allowing the value +infinity, so any program of length greater than m+c_U has objective greater than this benchmark. There are only finitely many binary programs of length at most m+c_U, and the uniform program is a feasible member of this finite set. Consequently the minimum exists, is finite, and satisfies

MDL_T(Y)<=m+c_U.

For every chosen optimizer P*_Y,

|P*_Y|<=m+c_U,

and its expected log-loss is finite. In particular, its probability is positive at every point of positive Y-probability. These observations justify the definitions even though arbitrary feasible models may assign zero probability to such points.

Write X_k=G(U_k), n=ell(k), and P*_k=P*_{X_k}. Then

|P*_k|<=n+c_U=poly(k).

No algorithm for finding this optimizer is needed: the security assumption permits non-uniform advice.

### 2. Threshold tests and simultaneous security transfer

For t in {1,...,n}, define

D_{k,t}(x)=1{P*_k(x)>=2^{-(n-t)}}.

The test simulates the model evaluator and compares finite binary probabilities exactly. It does not compute a logarithm. Evaluation takes at most T(n), and the comparison has polynomial cost because the output representation has length bounded by the evaluator's runtime. The advice consists of P*_k and the integer t, with total length polynomial in k. Since n is polynomially bounded in k and T is polynomial, this is a permitted non-uniform polynomial-time construction.

Let A_{k,t} be its acceptance set. Normalization gives

1>=sum_{x in A_{k,t}}P*_k(x)>=|A_{k,t}|2^{-(n-t)}.

Thus

Pr[D_{k,t}(U_n)=1]<=2^{-t}.

There is a quantifier issue to address: t ranges with k, and the security starting index may depend on a distinguisher family. For each k choose t_k maximizing

Delta_{k,t}=Pr[D_{k,t}(X_k)=1]-Pr[D_{k,t}(U_n)=1]

over t in {1,...,n}, breaking ties arbitrarily. Put t_k and P*_k in the advice of a single family D_k. This advice is still polynomially bounded, whether or not its selection is computable. The security assumption supplies one K such that, for every k>=K,

|Delta_{k,t_k}|<=epsilon(k).

By maximality, every Delta_{k,t}<=epsilon(k) at those same k. Hence, simultaneously for every t in {1,...,n},

Pr[D_{k,t}(X_k)=1]<=2^{-t}+epsilon(k).

### 3. Real-valued log-loss and the entropy lower bound

Fix k>=K and put L(x)=-log P*_k(x), interpreting -log 0 as +infinity. For any real l>=0,

(n-l)_+<=1+sum_{t=1}^n 1{l<=n-t}.

Indeed, when l<=n the sum counts the integers t with 1<=t<=n-l, and a nonnegative real number is at most one plus its integer part; when l>n the left side is zero. The same inequality holds for l=+infinity with left side zero. This is an inequality, not the integer-valued tail-sum identity.

Since the optimizer's expected log-loss is finite,

n-E[L(X_k)]<=E[(n-L(X_k))_+]
<=1+sum_{t=1}^n Pr[L(X_k)<=n-t]
<=1+sum_{t=1}^n(2^{-t}+epsilon(k))
=2-2^{-n}+n epsilon(k)
<=2+n epsilon(k).

By the definition of time-bounded entropy at the MDL optimizer,

H_T(X_k)>=n-2-n epsilon(k).

This does not identify H_T with the minimum of log-loss alone, and it does not require a security reduction for arbitrary super-polynomial-length model families.

### 4. Epiplexity and deterministic entropy increase

The uniform comparison at dimension n gives MDL_T(X_k)<=n+c_U. Therefore

S_T(X_k)=MDL_T(X_k)-H_T(X_k)<=c_U+2+n epsilon(k).

At the seed dimension, the same implementation and same time-bound function give

H_T(U_k)<=MDL_T(U_k)<=k+c_U,

because program lengths are nonnegative. Combining this with the output entropy lower bound yields

H_T(G(U_k))-H_T(U_k)
>=n-2-n epsilon(k)-(k+c_U)
=n-k-n epsilon(k)-(c_U+2).

Set c=c_U+2. This one constant proves both requested conclusions and depends only on the coding machine and uniform implementation, not on G, T, k, or the security starting index. All three conclusions hold for k>=K. Since n is polynomially bounded and epsilon is negligible, n epsilon(k) is negligible: if n<=C k^d eventually, apply negligibility of epsilon with an exponent greater than d plus any prescribed exponent.

## Security-Convention Audit

The public common eventual envelope is not a finite-size universal bound over all polynomial resource budgets. It is equivalent, as an existence condition, to ordinary non-uniform PRG security.

For completeness, enumerate all specifications consisting of a probabilistically clocked polynomial-time machine and a polynomial bound on its advice length. For specification j let a_j(k) be its largest absolute distinguishing advantage over allowed advice strings at length k. The maximum exists because there are finitely many such strings. If a_j were not negligible, a maximizing advice sequence would itself violate ordinary non-uniform security. Thus every a_j is negligible.

Choose strictly increasing integers K_j tending to infinity such that, for all k>=K_j and all i<=j, a_i(k)<=k^{-j}. For k>=K_1 let r(k)=max{j:K_j<=k}, and set epsilon_0(k)=k^{-r(k)}; set epsilon_0(k)=1 at the finitely many earlier lengths. Then epsilon_0 is negligible and eventually dominates each a_i. Conversely, an eventual negligible envelope immediately makes each individual distinguisher's advantage negligible. This explains why the public asymptotic clarification does not strengthen the source's security notion. The main proof works with any envelope epsilon supplied in the public setup.

## Obligation Closure

The proof explicitly establishes uniform-model feasibility, optimizer existence and finite loss, polynomial advice length, exact threshold computability, uniform counting, simultaneous security transfer, the real-valued shortfall estimate, both final comparisons, and constant dependencies. No external theorem or unresolved proof obligation is used.
