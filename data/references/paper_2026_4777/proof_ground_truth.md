# Reference Proof

## Proof Structure

1. Minimize the scalar function in the latent variable for each fixed coordinate.
2. Verify that the latent minimum is attained for every nonnegative TV budget.
3. For sufficiently large TV budget, the coordinatewise minimizers are feasible, giving the fine-partition limit.
4. At zero TV budget, all latent variables coincide; minimize the resulting one-variable objective to obtain the single-partition expression.
5. Use compactness of a common objective sublevel to prove convergence to the zero-budget value as the budget decreases to zero.

## Complete Proof

For fixed x and epsilon, set z_n=(|x_n|/epsilon+1)^2, so z_n>=1. For tau>=1,

f_e(x_n,tau)=z_n/(2 tau)+(1/2)log tau-1/2.

Its derivative is (tau-z_n)/(2 tau^2). Hence it decreases on [1,z_n] and increases on [z_n,infinity), with the unique minimizer tau=z_n. This includes z_n=1, when the minimum is at the left endpoint. Substitution gives

f_e(x_n,z_n)=z_n/(2z_n)+(1/2)log z_n-1/2=log(|x_n|/epsilon+1).

Every summand is therefore nonnegative, and the unconstrained minimum of the sum over sigma is Omega_epsilon(x)=sum_n log(|x_n|/epsilon+1).

We first verify that the minimum defining Psi_{alpha,epsilon}(x) exists for every alpha>=0. Write H(sigma)=sum_n f_e(x_n,sigma_n). The constant vector with entries 1 has zero total variation and finite objective. Thus the infimum is finite and nonnegative, and any minimizing sequence can be chosen with H(sigma)<=C for some fixed finite C>=0. Finite objective requires sigma_n>=1. Since the summands are nonnegative, each is at most C. Also,

f_e(x_n,sigma_n)>=(1/2)log sigma_n-1/2,

so every coordinate satisfies 1<=sigma_n<=exp(2C+1). A bounded sequence in this finite-dimensional box has a convergent subsequence. The TV constraint and the coordinate constraints are closed, and H is continuous on [1,infinity)^N. The subsequential limit is therefore feasible and attains the infimum. The same reasoning shows that every finite sublevel of H in [1,infinity)^N is compact.

Let sigma^*_n=z_n. Its total variation A=||D sigma^*||_1 is finite. If alpha>=A, sigma^* is feasible, so Psi_{alpha,epsilon}(x)<=Omega_epsilon(x). Conversely, every feasible sigma has each summand at least its scalar minimum, so Psi_{alpha,epsilon}(x)>=Omega_epsilon(x). Therefore equality holds for all alpha>=A, and consequently

lim_{alpha->infinity} Psi_{alpha,epsilon}(x)=Omega_epsilon(x).

If alpha=0, ||D sigma||_1=0 forces sigma_1=...=sigma_N=tau (for N=1 this is automatic). A finite objective requires tau>=1. The objective becomes

F(tau)=(sum_n z_n)/(2 tau)+(N/2)log tau-N/2.

Writing bar z=(1/N)sum_n z_n>=1, its derivative is N(tau-bar z)/(2 tau^2), so its unique minimum on [1,infinity) is attained at tau=bar z. Evaluating there gives

Psi_{0,epsilon}(x)=N/2 log bar z=N log sqrt((1/N)sum_n (|x_n|/epsilon+1)^2).

It remains to prove the limit at zero, rather than only the value at zero. Let alpha_k>0 be any sequence tending to zero, and choose an attained minimizer sigma^k for each alpha_k. The constant vector with entries bar z is feasible for every budget. Hence, with C=Psi_{0,epsilon}(x),

0<=H(sigma^k)=Psi_{alpha_k,epsilon}(x)<=C.

All sigma^k therefore belong to the same compact sublevel established above. The sequence of objective values is bounded, so choose a subsequence along which it converges to its liminf, and then a further subsequence along which sigma^k converges to a vector sigma^0. The coordinate constraints persist in the limit, and continuity of D gives

||D sigma^0||_1=lim_k ||D sigma^k||_1=0,

because ||D sigma^k||_1<=alpha_k->0. Thus sigma^0 is feasible at budget zero. By continuity of H on [1,infinity)^N,

liminf_k Psi_{alpha_k,epsilon}(x)=H(sigma^0)>=Psi_{0,epsilon}(x).

The opposite upper bound Psi_{alpha_k,epsilon}(x)<=Psi_{0,epsilon}(x) already holds for every k, so the entire sequence of values converges to Psi_{0,epsilon}(x). Since the positive sequence alpha_k tending to zero was arbitrary,

lim_{alpha->0+} Psi_{alpha,epsilon}(x)=Psi_{0,epsilon}(x).

Combining this with the evaluated zero-budget minimum proves the second endpoint assertion. No step requires a nonzero coordinate or N>1; in particular, if x=0 then bar z=1 and both endpoint values are zero.
