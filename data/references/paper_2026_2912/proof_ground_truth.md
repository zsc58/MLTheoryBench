# Reference Proof

## Proof Structure

Fix the conditional law at an aliased summary value. Establish the conditional KL decomposition, including the specified common smoothing convention and unsmoothed boundary forecasts. Minimize the resulting common-forecast term and prove its strict positivity. Then use the jointly realizable causal retrieval, gates, and transport to recover the regime-specific conditional mean. Finally construct finite-softmax approximations with a uniform positivity bound and prove convergence of conditional expected excess risk.

## Complete Proof

Fix a summary value g under the conditional law specified in the task. Put X=p_{t+1}, and write pi_z=Pr(Z=z|g) and u_z=E[X|Z=z,g]. All equalities concerning random quantities below hold almost surely under this conditional law.

### 1. Loss convention and finite oracle risk

Let S=S_epsilon be the task's normalized additive smoothing map, and set U_z=S(u_z). Directly from its definition, S is affine, so

E[S(X)|Z=z,g]=U_z,

and S(sum_z pi_z u_z)=sum_z pi_z U_z.

For epsilon>0, every coordinate of S(x), for x in the simplex, is at least gamma=epsilon/(1+D epsilon)>0. For epsilon=0, the assumed interior successors give m=min_{z,i}u_{z,i}>0 because D and K are finite. Consequently every U_z has strictly positive coordinates, in either convention.

The regime-aware Bayes risk

B_g=sum_z pi_z E[KL(S(X)||U_z)|Z=z,g]

is finite. Indeed, KL(y||U_z)<=-log(min_i U_{z,i}) for any probability vector y. The entropy terms are also bounded because x log x extends continuously to zero on [0,1]. Thus subtracting B_g from a possibly infinite forecast risk is well defined.

### 2. Conditional KL decomposition

For a fixed-summary forecast q, first suppose Q=S(q) has positive coordinates. Coordinatewise expansion gives

KL(S(X)||Q)-KL(S(X)||U_z)
=sum_i S(X)_i log(U_{z,i}/Q_i).

The logarithms are finite constants when conditioning on Z=z and g. Taking expectations and using E[S(X)_i|Z=z,g]=U_{z,i} gives

E[KL_epsilon(X||q)|Z=z,g]
=E[KL_epsilon(X||u_z)|Z=z,g]+KL(U_z||Q).

If Q has a zero coordinate, then necessarily epsilon=0. Since u_z is interior, E[X_i|Z=z,g]>0 at any such coordinate i. Hence Pr(X_i>0|Z=z,g)>0, the conditional expected loss to q is infinite, and KL(u_z||q)=infinity. The same equality therefore holds in the extended-real sense, without subtracting two infinite quantities.

Averaging over regimes and subtracting the finite B_g yields

E_g^epsilon(q)=sum_z pi_z KL_epsilon(u_z||q).

This derives the conditional KL/Bayes decomposition rather than merely invoking it.

### 3. Mixture minimization and strict positivity

Let bar_u=sum_z pi_z u_z and bar_U=S(bar_u)=sum_z pi_z U_z. Expanding the finite-coordinate expressions gives

sum_z pi_z KL(U_z||Q)
=sum_z pi_z KL(U_z||bar_U)+KL(bar_U||Q).

For a boundary Q in the unsmoothed case, both sides are infinite, so the identity remains valid.

For completeness, nonnegativity of KL and its equality condition follow from -log a>=1-a. Applied on the support of a probability vector v, this gives KL(v||w)>=0; equality requires w=v. Boundary support failures give infinite KL and cannot be equality cases. Here each U_z and bar_U is strictly positive, so equality in KL(bar_U||Q) occurs exactly when Q=bar_U.

Therefore

E_g^epsilon(q)>=sum_z pi_z KL(U_z||bar_U)
=JS_pi^epsilon(u_1,...,u_K),

with equality at q=bar_u. Since S_epsilon is injective for every finite epsilon>=0, this is also the unique fixed-summary minimizer.

Every summand in the Jensen-Shannon expression is nonnegative. With pi_z>0, its sum is zero exactly when every U_z=bar_U, equivalently when every u_z=bar_u. The aliasing assumption excludes this, proving strict positivity.

### 4. Exact causal realization

By assumption, the causal representation identifies Z, the strictly causal memory supplies causally available convex retrieval weights realizing s_Z, and the retrieval, gates, and transport head can jointly implement the required regime-dependent choices. Select r_t=s_Z, lambda_t=lambda_Z, rho_t=rho_Z, and T_t=T_Z.

The transport action is the source's mass-pushforward convention. Its nonnegative kernel has unit row sums, so it maps probability vectors to probability vectors. Together with lambda_Z in [0,1] and rho_Z in [0,rho_max], rho_max<=1, all stages remain simplex-valued. Every selected quantity uses only the permitted causal representation, observed history, and memory successors with s<t.

Substituting the choices gives

a_t=lambda_Z p_t+(1-lambda_Z)s_Z,

p_hat_{t+1}=(1-rho_Z)a_t+rho_Z T_Z a_t=u_Z

almost surely, by the regime-wise realization assumption. Its conditional expected loss is exactly B_g. Its oracle excess risk is therefore zero. This conclusion does not assert zero total target KL unless X=u_Z almost surely.

### 5. Finite-softmax realization and convergence of expected risk

The memory assumption makes the memory nonempty. At fixed t its size is N=t-1. Let w_s>=0, sum_{s<t}w_s=1, be the causally available convex retrieval weights for s_Z supplied by the retrieval realization assumption:

sum_{s<t}w_s p_{s+1}=s_Z.

The task uses the abstract causal convex-retrieval class, including its finite-softmax realization. For n>=1 define finite causal scores ell_s^(n)=log(w_s+1/n). Their normalized exponential weights are

w_s^(n)=(w_s+1/n)/(1+N/n).

They use exactly the same permitted causal information as w_s. This is a finite-softmax parameterization, not access to a future target. Define c_n=(1+N/n)^(-1) and b_t=N^(-1)sum_{s<t}p_{s+1}. The retrieved value is

r_t^(n)=c_n s_Z+(1-c_n)b_t.

Hold the jointly realizable gates and transport at their regime-specific values. The map from retrieval value to output is affine with nonnegative coefficients and a mass-preserving transport. Thus its output Q_n satisfies

Q_n=c_n u_Z+(1-c_n)v_t

for a simplex-valued causal vector v_t. In particular, Q_n>=c_n u_Z coordinatewise and ||Q_n-u_Z||_1<=2(1-c_n)<=2N/n. This proves convergence to u_Z uniformly over histories in the fixed conditional experiment.

For epsilon=0, let m=min_{z,i}u_{z,i}>0 and c_*=(1+N)^(-1). Then Q_{n,i}>=c_*m for all n and histories. The elementary inequality

|log a-log b|<=|a-b|/min(a,b)

therefore yields

|KL(X||Q_n)-KL(X||u_Z)|
=|sum_i X_i log(u_{Z,i}/Q_{n,i})|
<=||Q_n-u_Z||_1/(c_*m)
<=2N/(n c_*m).

For epsilon>0, S(Q_n) and S(u_Z) have the fixed lower bound gamma, and ||S(Q_n)-S(u_Z)||_1=||Q_n-u_Z||_1/(1+D epsilon). Applying the same logarithmic estimate to S(X) gives

|KL_epsilon(X||Q_n)-KL_epsilon(X||u_Z)|
<=2N/[n gamma(1+D epsilon)].

Taking conditional expectations proves that the conditional excess risk of these finite-softmax predictors converges to zero in either convention. This argument does not require conditional independence between Q_n and X and does not incorrectly replace a random history-dependent prediction by a constant in the decomposition from Step 2.

## Obligation Closure

All theorem-critical obligations are explicitly closed above. The proof uses only finite-dimensional expansions, convexity, nonnegative mass-preserving transport, and an elementary logarithmic inequality. There is no unresolved specialized or paper-specific external dependency.
