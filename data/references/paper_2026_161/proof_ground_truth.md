# Reference Proof

## Proof Structure

1. Expand the convolutional composition and identify its effective-filter polynomial as a product of stride-dilated layer polynomials.
2. Use loss decrease, explicit residual bounds for all four losses, and full row rank of the input matrix to bound the effective filter.
3. Derive the conserved layer-norm differences. Prove the bounded linear-factor estimate, retain the scalar units in the layer factorization, and cancel them only in the product of squared layer norms. A monic polynomial and its elementary root bound then bound all layers. Include zero, constant, and lower-degree effective polynomials.
4. Verify analyticity, use local ODE existence and continuation to obtain a global bounded solution, and apply the standard Lojasiewicz bounded-gradient-flow convergence theorem.

## Complete Proof

All architectures, training data, and loss parameters below are fixed. The gradient and parameter norms are Euclidean. For a polynomial, its coefficient 1- or 2-norm includes all coefficients, with zero coefficients inserted when necessary. For a matrix, its 1-norm below is the entrywise sum of absolute values.

### 1. Convolution and polynomial representation

Write W_i for the ith layer matrix and V=W_N...W_1. Set S_i=product_{h<i}s_h, where S_1=1, and define

q_i(x)=sum_{j=0}^{k_i-1} w_{j+1}^{(i)} x^{jS_i}.

The coefficient norms of q_i equal the corresponding norms of w^(i). These polynomials can have smaller degree than (k_i-1)S_i or can vanish identically.

To verify the effective-filter representation, suppose the first i-1 layers have filter a and stride S_i. Applying layer i gives terms

w_n^(i) a_l x_{(j-1)s_i S_i+(n-1)S_i+l}.

Grouping terms with equal (n-1)S_i+l produces a convolution of stride s_i S_i and filter width k_a+(k_i-1)S_i. Its coefficient polynomial is the product of the previous coefficient polynomial and q_i. Induction, starting with the first layer, proves

s_v=product_i s_i,

k_v=k_1+sum_{i=2}^N(k_i-1)S_i,

P(x):=sum_{j=0}^{k_v-1}v_{j+1}x^j=product_{i=1}^N q_i(x).

Every row of V contains exactly the entries of v, shifted and padded by zeros. Consequently ||V||_1=d_N||v||_1.

### 2. Local existence and the effective-filter bound

The power loss is polynomial because p is even. The pseudo-Huber square-root argument is everywhere positive. The generalized-Huber logarithm argument is at least 2+beta>0, and cosh is everywhere positive for the log-cosh loss. Thus each listed loss is real analytic on its entire real input domain. Since the network output is polynomial in the parameters, L is real analytic on R^{sum_i k_i}. In particular, its gradient is locally Lipschitz.

The standard Picard-Lindelof theorem states that a locally Lipschitz vector field on an open subset of finite-dimensional Euclidean space has a unique local solution from each initial point and a unique maximal continuation. Apply it to -gradient L, and let [0,b) be the forward part of the maximal interval.

On this interval,

dL(w(t))/dt=-||gradient L(w(t))||_2^2<=0.

We give explicit scalar residual estimates. Write r for a residual coordinate and f(r) for its scalar loss contribution.

* Power loss: for u>=0, u^p/p-u has its minimum at u=1, so |r|<=|r|^p/p+(p-1)/p.
* Pseudo-Huber: |r|<=delta sqrt(1+r^2/delta^2).
* Generalized-Huber with beta>=0: e^{alpha|r|}<=e^{alpha r}+e^{-alpha r}+beta, so |r|<=f(r).
* Generalized-Huber with -2<beta<0: put A=e^{alpha r}+e^{-alpha r}>=2. Then

  log A=log(A+beta)+log(1-beta/(A+beta))

  <=log(A+beta)+log(2/(2+beta)).

  Hence |r|<=f(r)+alpha^{-1}log(2/(2+beta)).
* Log-cosh: e^{alpha|r|}<=2cosh(alpha r), hence |r|<=f(r)+alpha^{-1}log 2. Equivalently, the generalized-Huber loss at beta=0 equals the log-cosh loss plus log(2)/alpha per coordinate.

Let c be, respectively, (p-1)/p, 0, 0, alpha^{-1}log(2/(2+beta)), or alpha^{-1}log 2 in these cases. With Y=[y_1 ... y_m] and K=md_N c, summing over all residual coordinates gives

||VX-Y||_1<=L(w)+K.

This estimate does not presume that the generalized-Huber loss is nonnegative. For a globally positive nondecreasing function on R one may take h(t)=1+max{0,t+K}; it satisfies ||VX-Y||_1<=h(L(w)).

Set B_X=X^T(XX^T)^{-1}, so XB_X is the identity. Entrywise matrix 1-norms are submultiplicative: this follows by expanding (AB)_{ij}, applying the triangle inequality, and summing. Therefore

||v||_1=(1/d_N)||V||_1

<=(||B_X||_1/d_N)(||VX-Y||_1+||Y||_1)

<=(||B_X||_1/d_N)(h(L(w))+||Y||_1).

The right side defines a nonnegative nondecreasing function g on all of R. Loss decrease gives the uniform bound

||v(t)||_1<=g(L(w_0))=:T

for every 0<=t<b. This bound depends only on the fixed architecture, data, loss parameters, and initial loss.

### 3. Balancedness

Scaling one layer by a positive scalar a and another by a^{-1} leaves the network output and L unchanged. Differentiation at a=1 yields

<w^(i),gradient_i L>=<w^(j),gradient_j L>.

Thus

d/dt (||w^(i)||_2^2-||w^(j)||_2^2)=0.

For i<N define the conserved quantities

Delta_i=||w^(i+1)(0)||_2^2-||w^(i)(0)||_2^2.

Set beta_i(t)=||w^(i)(t)||_2^2, b_1=0, and b_i=sum_{h<i}Delta_h. Then beta_i=beta_1+b_i throughout the interval. Let D=max_{1<=i<=N}|b_i|. These definitions also apply to N=1, with no differences and D=0.

### 4. A bounded linear-factor estimate

We derive the auxiliary factorization rather than assuming it. Let p(x)=a_n x^n+...+a_0 have actual degree n>=1 and let U=max{||p||_1,1}. Define sign(a_n)=a_n/|a_n|. We prove that

p=sign(a_n) product_{j=1}^n u_j,

where every u_j is linear and ||u_j||_1<=6nU.

For n=1, take u_1=p/sign(a_1). Suppose n>=2 and use the fundamental theorem of algebra to write p=a_n product_j(x-z_j).

If every |z_j|<=1, set u_j=|a_n|^{1/n}(x-z_j). Their product has leading coefficient |a_n| and the required roots. Moreover ||u_j||_1<=2|a_n|^{1/n}<=2U.

Otherwise, order the roots so that |z_j|>=1 for j<=r and |z_j|<1 for j>r, with r>=1. Set B=max_{0<=j<=n}|a_j|/|a_n|>=1. Let e_j be the elementary symmetric functions of all n roots, with e_0=1; the coefficient identities imply |e_j|<=B.

For the small roots define h_0=1 and, for k>=1, let h_k be the sum of products z_{i_1}...z_{i_k} over nondecreasing indices r<i_1<=...<=i_k<=n. If there are no small roots, set h_k=0 for k>=1. Geometric-series multiplication, or just comparison of coefficients through degree r, gives

(product_{j>r}(1+z_j t))^{-1}=sum_{k>=0}(-1)^k h_k t^k.

There are at most n^k terms in h_k and each has modulus at most one, so |h_k|<=n^k. Comparing coefficients of t^r in

product_{j<=r}(1+z_j t)=product_{j=1}^n(1+z_j t) / product_{j>r}(1+z_j t)

gives

|z_1...z_r|<=sum_{k=0}^r |e_{r-k}||h_k|

<=B sum_{k=0}^r n^k<=3Bn^r.

This is the symmetric-coefficient estimate used in the source's root-splitting argument.

Put A=|a_n z_1...z_r|^{1/r}. For j<=r take u_j=A(x-z_j)/|z_j|, and for j>r take u_j=x-z_j. The leading coefficients of these factors multiply to |a_n|, so their product is p/sign(a_n). For j<=r,

||u_j||_1=A(1+1/|z_j|)<=2A

<=2(3|a_n|Bn^r)^{1/r}<=6nU.

For j>r, ||u_j||_1=1+|z_j|<=2<=6nU. This proves the estimate, including its normalization.

We will also use coefficient-norm submultiplicativity. For polynomials a and b, expansion of their coefficients gives

||ab||_1<=sum_{i,j}|a_i||b_j|=||a||_1||b||_1.

### 5. Boundedness of every layer, including degenerate cases

Fix any time in [0,b). Write P=product_i q_i for the effective polynomial and set T_*=max{T,1} and H=(6T_*k_v)^{2k_v}.

If P is zero, the polynomial ring has no zero divisors, so q_j is zero for some layer j. Thus beta_j=0 and beta_i=b_i-b_j<=2D for all i. This handles a zero layer at any index, including the last, and also handles N=1.

Suppose P is a nonzero constant. Since degrees of nonzero polynomial products add, every q_i is constant. Therefore

C:=product_i beta_i=|P|^2<=T^2<=H.

Otherwise let l be the actual degree of P, so 1<=l<=k_v-1. Apply the preceding factorization with U=max{||P||_1,1}<=T_* to obtain linear factors u_1,...,u_l, each of norm at most 6lT_*. Unique factorization assigns the roots with multiplicity to disjoint sets M_1,...,M_N partitioning {1,...,l}, and gives nonzero scalar units kappa_i such that

q_i=kappa_i product_{j in M_i}u_j.

Empty products equal the constant polynomial one. Comparison with P=sign(a_l)product_j u_j gives product_i kappa_i=sign(a_l), hence |product_i kappa_i|=1. Individual kappa_i need not be bounded. It is their cancellation in the following product that matters:

C:=product_i beta_i

=product_i |kappa_i|^2 product_i ||product_{j in M_i}u_j||_2^2

=product_i ||product_{j in M_i}u_j||_2^2

<=product_i ||product_{j in M_i}u_j||_1^2

<=product_{j=1}^l ||u_j||_1^2

<=(6T_*k_v)^{2k_v}=H.

Thus in either nonzero case, beta_1 is a root of the monic polynomial

Q(z)=product_{i=1}^N(z+b_i)-C.

Because b_1=0, its constant coefficient is -C. Every other coefficient has modulus at most product_i(1+|b_i|)<=(1+D)^N. Set M=max{H,(1+D)^N}; then all coefficients, including the leading coefficient, have modulus at most M, uniformly in time.

For completeness, if a monic degree-N polynomial has all coefficients of modulus at most M>=1, a root cannot satisfy |z|>NM. Indeed, after division by z^N, the sum of the magnitudes of its N lower terms is at most sum_{j=1}^N M/|z|^j<=NM/|z|<1, which cannot cancel the leading term one. Therefore beta_1<=NM and beta_i<=NM+D.

Combining the zero and nonzero cases gives a uniform finite bound on all layer squared norms for 0<=t<b. It also covers k_v=1, when only the zero and constant cases occur, and leading coefficients that vanish at intermediate times. No continuous choice of factors or roots along the trajectory is needed.

### 6. Global continuation and convergence

The parameter trajectory lies in a fixed compact ball. If b were finite, continuity of gradient L would bound its norm on that ball, so w(t) would be Lipschitz in time and have a limit as t approaches b from below. Local existence at this limiting point would extend the solution past b, contradicting maximality. Hence b=infinity, and the solution is globally defined and bounded.

We use the following two standard independent analytic-gradient facts stated in the source. A real-analytic function on a finite-dimensional real open set satisfies the Lojasiewicz gradient inequality locally at each point: for suitable C>0 and theta<1, |f(y)-f(a)|^theta<=C||gradient f(y)|| near a. Also, a C^2 function satisfying this inequality at every point has the property that every bounded solution of its negative-gradient ODE on [0,infinity) converges to a critical point.

Here L is real analytic on the whole parameter space, as verified in Section 2. The solution is defined on [0,infinity) and bounded, as just proved. All hypotheses of these standard results are satisfied. Consequently w(t) converges to a point w_infinity with gradient L(w_infinity)=0.

All theorem-critical obligations are closed. No nonstandard external theorem or unresolved private proof step is being assumed.
