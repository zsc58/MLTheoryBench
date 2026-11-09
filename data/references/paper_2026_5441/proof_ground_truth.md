# Reference Proof

## Contract and notation

All geometric parameters and memories are fixed. Constants in large-beta O-estimates may depend on this fixed configuration but not on beta. A subscript beta on O_beta denotes an epsilon-asymptotic estimate whose constant may also depend on beta. Set gamma=1-c, h=exp(-beta), t=exp(-beta gamma), and D=d-1. Both gamma and D are positive. The assumed memory configuration is realizable; indeed its Gram matrix has rank N+1, so its existence already forces d>=N+1. No separate assumption about dimension growth is used.

The proof closes five obligations: the exact replay identity, averaged small-rotation response, localization and leakage estimates, the energy-rise comparison, and the five replay comparisons with their correct quantifiers.

## 1. Energy differentiation and exact replay identity [step_001]

Let Z_Y(xi)=sum_{y in Y} exp(beta y^T xi), counting multiplicities. Differentiation gives

grad E(xi | X)=xi-sum_j p_j(xi | X)x_j.

Thus the stated fixed-point equation is stationarity. Every such point is a convex combination of unit memories, so ||xi_k^*||<=1.

Since V is orthogonal,

E(xi | VX)=E(V^T xi | X).

The appended replay copy contributes an additional partition term, including when V=I_d. Hence

R_{r->k}(V) = beta^{-1} log(1+exp(beta x_r^T xi_k^*)/Z_{VX}(xi_k^*)).

The quadratic terms cancel in the energy difference, giving

exp(beta Delta E_k^fp(V))=Z_X(xi_k^*)/Z_{VX}(xi_k^*).

Consequently, writing p=p_{r|k} and delta=Delta E_k^fp(V),

R_{r->k}(V)=f_p(delta), where f_p(z)=beta^{-1}log(1+p exp(beta z)).

In particular R_{r->k}(I_d)=f_p(0)=beta^{-1}log(1+p). This is the retained-duplicate baseline, not zero.

## 2. Rotation expansion and legitimate averaging [step_002]

Write xi=xi_k^*, H=H_k=I-beta C_k, and

C_k=sum_j p_j^* x_j x_j^T-xi xi^T.

The matrix C_k is a covariance matrix. Let M=||Omega||_op. All moments of M are finite: M<=||Omega||_F, and Omega has finitely many Gaussian entries.

For any state, the covariance of unit memories has operator norm at most one. Thus the spatial Hessian has norm at most 1+beta. Stationarity and the integral Taylor remainder give

|delta| <= (1+beta)||V^T xi-xi||^2/2 <= (1+beta)epsilon^2 M^2/2.

Here ||exp(-epsilon Omega)-I||_op<=epsilon M follows by integrating its derivative and using orthogonality. Independently, the quadratic terms cancel along this rotation and log-sum-exp changes by at most the largest logit change. Therefore |delta|<=2.

For every fixed beta and Omega,

delta/epsilon^2 -> Q_k(Omega)=(1/2)(Omega xi)^T H(Omega xi).

These bounds justify dominated convergence for the moments used below. They also justify differentiation of the averaged rotation energy through order four: along the orthogonal orbit, the required derivatives are bounded by a beta-dependent constant times powers of M. The averaged energy is an even function of epsilon because Omega and -Omega have the same law. It follows that

Delta E_k^fp = epsilon^2 E[Q_k] + O_beta(epsilon^4).

Directly from independent standard-normal entries of W,

E[Omega_ab Omega_cd]=(1/2)(delta_ac delta_bd-delta_ad delta_bc),

and therefore

E[(Omega u)(Omega u)^T]=(1/2)(||u||^2 I-u u^T).

Taking the trace against H yields

Delta E_k^fp = (epsilon^2/4)S_k + O_beta(epsilon^4),

where S_k=||xi_k^*||^2 tr H_k-(xi_k^*)^T H_k xi_k^*.

For the replay response,

f_p'(0)=rho=p/(1+p),

f_p''(z)=beta p exp(beta z)/(1+p exp(beta z))^2.

Taylor's integral remainder, valid for either sign of delta, gives

|f_p(delta)-f_p(0)-rho delta| <= beta rho exp(beta max(delta,0)) delta^2,

because p<=2rho. For fixed beta, |delta|<=2 and the preceding quadratic bound supply an integrable dominating function after division by epsilon^4. Hence

lim_{epsilon->0+} E[exp(beta max(delta,0))delta^2]/epsilon^4 = E[Q_k^2].

This proves the fixed-beta fourth-order response estimate without assuming that the Gaussian generator is bounded. A constant independent of large beta will be obtained in Section 4.

## 3. Localized branches and explicit leakage estimates [step_003]

We first verify that the branch notation is legitimate, without invoking an external capacity theorem. Let T_beta(xi)=sum_j p_j(xi)x_j and put r_0=gamma/8. In the closed ball ||xi-x_k||<=r_0, every competing logit satisfies

(x_k-x_j)^T xi >= gamma-2r_0 = 3gamma/4.

Thus sum_{j!=k}p_j(xi)<=N exp(-3beta gamma/4), and

||T_beta(xi)-x_k||<=2N exp(-3beta gamma/4).

Moreover, D T_beta=beta Cov_p(x), and comparison with the second moment about x_k gives

||D T_beta||_op<=4beta N exp(-3beta gamma/4).

For sufficiently large beta, T_beta maps this ball to itself and has Lipschitz constant less than 1/2. Iteration from x_k is Cauchy by the geometric bound on successive differences, so it converges to a fixed point in the ball. The same Lipschitz inequality proves uniqueness there. Any branch converging to x_k eventually lies in this ball and therefore coincides with this branch. In particular beta times its total off-memory probability tends to zero. At these fixed points, 0<=D T_beta<I/2, so

(1/2)I <= H_k <= I.

Permutations of the cluster memories preserve their Gram matrix and therefore extend to orthogonal maps of the ambient space. Equivariance of T_beta and the local uniqueness just proved imply the symmetry reductions. At the outlier branch the weights are (u,...,u,v), with Nu+v=1. At the branch near x_1 they are (a,b,...,b,q), with a+(N-1)b+q=1. All cluster target branches have the same corresponding quantities.

Set A_0=1+(N-1)c. The outlier logit ratio gives the exact equation

u=(1-Nu)h exp(beta(A_0+N)u).

The already established beta u->0 first gives u/h->1. Substitution back into this equation then gives

u=h+O(beta h^2),

v=1-Nh+O(beta h^2).

For the cluster branch, its logits are z_1=a+(N-1)cb, z_-=ca+[1+(N-2)c]b, and z_o=q. Their ratios yield the exact equations

b=a t exp(beta gamma(Nb+q)),

q=a h exp(beta[gamma(N-1)b+2q]).

The preliminary localization bound makes both feedback exponents tend to zero. Consequently b/t->1 and q/h->1, and the same equations sharpen these to

b=t+O(beta t^2),

q=h+O(beta h t),

a=1-(N-1)t-h+O(beta t^2).

These estimates use beta times the leakage tending to zero, not merely convergence of the fixed point. Normalization also recovers the fixed-point vector expansions:

xi_o^*=x_o+h(sum_{i=1}^N x_i-Nx_o)+O(beta h^2),

xi_1^*=x_1+t(sum_{j=2}^N x_j-(N-1)x_1)+h(x_o-x_1)+O(beta t^2).

Next consider any localized branch with dominant memory x_k. Write eta_j=p_j^* for j!=k, eta=sum_{j!=k}eta_j, alpha_j=x_j^T x_k, and w=sum_{j!=k}eta_j(x_j-x_k). The following identities are exact:

xi=x_k+w,

C=sum_{j!=k}eta_j(x_j-x_k)(x_j-x_k)^T-w w^T.

In particular ||w||<=2eta. Using

S=(d-1)||xi||^2-beta(||xi||^2 tr C-xi^T C xi),

we obtain

||xi||^2=1-2sum_{j!=k}eta_j(1-alpha_j)+O(eta^2),

||xi||^2 tr C-xi^T C xi=sum_{j!=k}eta_j(1-alpha_j^2)+O(eta^2).

The second formula follows by replacing xi with x_k in terms already linear in eta and using ||x_j-x_k||^2=2(1-alpha_j) and [x_k^T(x_j-x_k)]^2=(1-alpha_j)^2. All discarded products contain at least two leakage factors. Therefore, with constants independent of beta,

S=D-sum_{j!=k}eta_j Lambda(alpha_j)+O((1+beta)eta^2),

Lambda(alpha)=2D(1-alpha)+beta(1-alpha^2).

This explicit remainder is the bound needed for the subsequent large-beta comparison; an unqualified O(eta^2) must not be assumed uniform in beta.

## 4. Energy-rise comparison and response constants [step_004]

Substituting the weight estimates into the leakage formula, and taking beta>=1, gives

S_o=D-Nh Lambda(0)+O(beta^2 h^2),

S_cl=D-(N-1)t Lambda(c)-h Lambda(0)+O(beta^2 t^2).

The extra beta factors account both for the Hessian's beta multiplier and for the errors in replacing exact weights by their leading exponentials. Thus

S_o-S_cl=(N-1)[t Lambda(c)-h Lambda(0)]+O(beta^2 t^2).

Since h/t=exp(-beta c)->0, beta t->0, and Lambda(c)/beta->1-c^2>0,

S_o-S_cl ~ (N-1)beta(1-c^2)t > 0.

Also S_o->D and S_cl->D, so S_o>S_cl>0 for all sufficiently large beta. The rotation expansion consequently proves Delta E_o^fp>Delta E_cl^fp>0 for each such fixed beta and all sufficiently small positive epsilon. In the stated iterated sense it also gives the inherited asymptotic difference

Delta E_o^fp-Delta E_cl^fp ~ (epsilon^2/4)(N-1)[t Lambda(c)-h Lambda(0)].

We now complete the claimed uniform response bound. Since ||xi_k^*||<=1 and ||H_k||_op<=1 for large beta,

|Q_k|<=(1/2)M^2,

so E[Q_k^2]<=E[M^4]/4 independently of beta and k. By the fixed-beta convergence established in Section 2, for every sufficiently large beta one can choose a positive epsilon threshold such that

E[exp(beta max(delta,0))delta^2] <= C epsilon^4

for every target k, where, for example, C=1+E[M^4] is independent of beta. There are finitely many target indices, so their thresholds can be minimized. Averaging the replay Taylor bound now yields

|Delta_{r->k}-rho_{r|k}Delta E_k^fp| <= C beta rho_{r|k}epsilon^4

for every replay index r as well. This is precisely the quantified factorization in the public task. No bound at fixed positive epsilon as beta tends to infinity has been asserted.

## 5. Susceptibilities, strict ordering, and iterated ratios [step_005]

The branch estimates give

rho(v)=1/2-Nh/4+O(beta h^2),

rho(a)=1/2-[(N-1)t+h]/4+O(beta t^2),

rho(b)=t(1+o(1)),

rho(u)=h(1+o(1)),

rho(q)=h(1+o(1)).

In particular rho(v)-rho(a)~(N-1)t/4>0.

For this private calculation define J_{r->k}=lim_{epsilon->0+}Delta_{r->k}/epsilon^2. The response and rotation expansions prove that this limit exists and equals rho_{r|k}S_k/4. Symmetry therefore gives

J_{o->o}=rho(v)S_o/4,

J_{cl1->cl1}=rho(a)S_cl/4,

J_{cl1->cl2}=rho(b)S_cl/4,

J_{cl1->o}=rho(u)S_o/4,

J_{o->cl1}=rho(q)S_cl/4.

All five coefficients are positive for sufficiently large beta. Moreover,

4(J_{o->o}-J_{cl1->cl1})=[rho(v)-rho(a)]S_cl+rho(v)(S_o-S_cl)>0.

For each fixed sufficiently large beta, the actual gains equal epsilon^2 times these coefficients plus O_beta(epsilon^4). Their positivity and the strict self-replay inequality therefore hold for all sufficiently small positive epsilon. This argument controls the strict difference itself; it does not infer its sign merely from the common leading term epsilon^2 D/8. The epsilon threshold may depend on beta, as the task allows.

Taking the epsilon limit first, the remaining gain ratios become ratios of the positive J coefficients. Their large-beta asymptotics are

J_{cl1->cl1}/J_{cl1->cl2}=rho(a)/rho(b) ~ (1/2)exp(beta(1-c)),

J_{cl1->cl2}/J_{cl1->o}=[rho(b)/rho(u)]S_cl/S_o ~ exp(beta c),

J_{cl1->cl2}/J_{o->cl1}=rho(b)/rho(q) ~ exp(beta c),

J_{cl1->o}/J_{o->cl1}=[rho(u)/rho(q)]S_o/S_cl -> 1.

The first three ratios diverge, and the last tends to one. Combining these with the strict self-replay comparison proves every requested assertion.

## Closure

All theorem-critical obligations are derived from the energy, fixed-point equations, finite-dimensional Gaussian moments, and elementary Taylor and contraction estimates. No specialized external result, unresolved paper-specific dependency, or unproved uniform remainder is used.
