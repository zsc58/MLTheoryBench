# Reference Proof

## Proof Structure and Obligation Closure

1. Derive the singular-value product bound, the two-factor and multilayer Schatten inequalities, and the fixed-product variational identity. Construct attaining factors with the prescribed widths and handle depth one separately.
2. Establish the two-way correspondence between factor minimizers and minimizers of the reduced matrix objective.
3. Apply the precise simultaneous-SVD equality form of von Neumann's inequality and derive the correctly normalized scalar objectives.
4. Prove the scalar threshold classification and monotonicity, then handle repeated positive and zero target singular values to establish matrix uniqueness.
5. Prove that the exceptional set is null.
6. Derive balancedness directly by a product-preserving first variation, then prove minimizer-independent layer norms.
7. Compute the diagonal Hessian blocks and prove the trace bound, including the zero-norm case.

The only specialized result accepted as standard independent is the von Neumann trace inequality with its simultaneous ordered SVD equality characterization, stated precisely below. Balancedness and the paper-specific variational reduction are derived, not accepted merely by citation. No theorem-critical obligation remains unresolved.

## Complete Proof

Write q=2/L and r=min(d_0,d_L). For a real matrix Z and p>0, use the notation ||Z||_{S^p}^p=sum_j sigma_j(Z)^p, with all singular values included. This is private proof notation. Since lambda>0,

F(W)>= (lambda/L)sum_i||W_i||_F^2.

Thus F is continuous and coercive on its finite-dimensional parameter space, so Omega is nonempty.

### 1. Product inequalities and the variational identity

We first derive the matrix inequality used by the source's variational argument. For conformable A,B, put R=min(rank(A),rank(B)). For every 1<=k<=R,

prod_{j=1}^k sigma_j(AB) <= prod_{j=1}^k sigma_j(A)sigma_j(B).

Indeed, the induced map on the kth exterior power of a Euclidean space has singular values equal to the k-fold products of distinct singular values of the original map: this follows by taking exterior powers of an SVD in the orthonormal exterior-product bases. Its operator norm is therefore the product of the k largest singular values. The identity wedge^k(AB)=(wedge^k A)(wedge^k B) and operator-norm submultiplicativity prove the display. If AB has rank below k, its left-hand side is zero and the conclusion is immediate.

Here is an explicit justification of the powered-sum consequence, avoiding any ambiguity about the quantifier in weak log-majorization. Let h=rank(AB). If h=0 there is nothing to prove. Otherwise, for 1<=j<=h, set

u_j=log sigma_j(AB),    v_j=log(sigma_j(A)sigma_j(B)).

Both vectors are nonincreasing and have finite entries, and the preceding product inequalities give sum_{j<=k}u_j<=sum_{j<=k}v_j for every k<=h. For every real t,

sum_j(u_j-t)_+ = max_{0<=k<=h}(sum_{j<=k}u_j-kt)
                  <= max_{0<=k<=h}(sum_{j<=k}v_j-kt)
                   = sum_j(v_j-t)_+.

For every p>0, the elementary integral identity

p^2 integral_{-infinity}^{infinity} exp(pt)(a-t)_+ dt = exp(pa)

therefore yields

sum_{j=1}^R sigma_j(AB)^p
 = sum_{j=1}^h sigma_j(AB)^p
 <= sum_{j=1}^h (sigma_j(A)sigma_j(B))^p
 <= sum_{j=1}^R (sigma_j(A)sigma_j(B))^p.

For positive a,b,c with 1/a+1/b=1/c, apply this inequality with power c and then scalar Holder with conjugate exponents a/c and b/c. It follows that

||AB||_{S^c}^c <= ||A||_{S^a}^c ||B||_{S^b}^c.

The exponents a/c and b/c exceed one because a,b are positive and finite. A zero factor gives the inequality immediately; no division by a vanishing norm is needed. Scalar Holder here is the ordinary nonnegative-sequence inequality. It follows, for example, by normalizing the two sequences and summing Young's inequality xy<=x^alpha/alpha+y^beta/beta for conjugate alpha,beta>1. Young's inequality itself follows from convexity of the exponential, with zero arguments obtained by continuity.

Apply the two-factor inequality inductively, using exponent 2 for each factor and exponent 2/k for the product of the first k factors. This gives

||W_L...W_1||_{S^{2/L}} <= prod_i||W_i||_F.

Consequently, for every factorization of Z,

||Z||_{S^q}^q <= (prod_i||W_i||_F^2)^{1/L}
                <= (1/L)sum_i||W_i||_F^2,

where the final inequality is AM-GM for nonnegative numbers.

For L>=2, write a thin SVD with r columns as Z=U D V^T, where D=diag(sigma_1(Z),...,sigma_r(Z)); zero singular values are allowed. Choose Q_i in R^{d_i x r} with orthonormal columns for each hidden layer, and put Q_0=V and Q_L=U. These choices are possible because d_i>=r. Set

W_i=Q_i D^{1/L}Q_{i-1}^T,    1<=i<=L.

The factors have exactly the prescribed dimensions, their product is Z, and

||W_i||_F^2=tr(D^{2/L})=||Z||_{S^q}^q

for every i. This attains the lower bound. If L=1, the only factor with product Z is W_1=Z, so the same identity is immediate. We have proved, with attainment,

min_{W_L...W_1=Z}(1/L)sum_i||W_i||_F^2=||Z||_{S^q}^q.

### 2. Reduction and minimizer correspondence

Define

G(Z)=||X-Z||_F^2+lambda||Z||_{S^q}^q.

For every factor tuple W, the identity just proved gives F(W)>=G(P(W)), and every Z has an attaining factorization with F(W)=G(Z). Hence min F=min G. More explicitly, if W minimizes F, then G(P(W)) cannot be smaller than F(W), since an attaining factorization of P(W) would contradict optimality; nor can P(W) fail to minimize G, since an attaining factorization of a better Z would contradict optimality. Conversely, an attaining factorization of any minimizer of G minimizes F. Thus the products of Omega are exactly the minimizers of G.

### 3. Singular coordinates and the precise equality condition

We use the following standard-independent von Neumann theorem. For real A,B of the same rectangular size,

tr(AB^T)<=sum_j sigma_j(A)sigma_j(B).

Equality holds if and only if there exist common left and right orthogonal matrices U,V such that A=U Sigma_A V^T and B=U Sigma_B V^T, with both rectangular diagonal matrices having nonnegative, nonincreasing diagonal entries. This is an existence statement about simultaneous ordered SVDs, not a claim that arbitrary preselected singular-vector bases agree. It includes repeated and zero singular values.

Let s_j=sigma_j(X). For any ordered singular values x_j=sigma_j(Z), expansion of the square and this theorem give

G(Z)>=sum_{j=1}^r [(s_j-x_j)^2+lambda x_j^q].

There is no additional ||X||_F^2 outside this sum. For every nonnegative ordered vector x, equality is attained by inserting x into an SVD of X. Equality for an arbitrary Z holds precisely when X and Z admit simultaneous ordered SVDs. The theorem's hypotheses hold because X and Z are real matrices of the same dimensions, and s,x are their ordered singular values.

### 4. Scalar minimizers, ordering, and uniqueness

For s>=0 consider phi_s(t)=(s-t)^2+lambda t^q on t>=0. Continuity and coercivity give a minimizer.

If L=1, q=2 and the unique minimizer is s/(1+lambda). If L=2, q=1 and the unique minimizer is max(s-lambda/2,0). These conclusions follow either by differentiation with the boundary constraint or by strict convexity.

Now suppose L>=3, so 0<q<1. For t>0,

phi_s(t)-phi_s(0)=t[t+lambda t^{q-1}-2s].

Set k(t)=(t+lambda t^{q-1})/2. Its derivative is

k'(t)=[1-lambda(1-q)t^{q-2}]/2.

It is negative below rho_0=(lambda(1-q))^{1/(2-q)} and positive above rho_0. Moreover k tends to infinity at both endpoints of (0,infinity). Its unique minimum is

k(rho_0)=(1-q/2)lambda^{1/(2-q)}(1-q)^{(q-1)/(2-q)}=tau.

It follows immediately that 0 is the unique minimizer if s<tau, and the minimizer set is exactly {0,rho_0} if s=tau. If s>tau, some positive t has phi_s(t)<phi_s(0), so every global minimizer is positive. There is at most one positive local minimum: on (0,infinity),

phi_s'(t)=2(t-s)+lambda q t^{q-1},
phi_s''(t)=2-lambda q(1-q)t^{q-2}.

The second derivative increases strictly from minus infinity to 2. Hence phi_s' first decreases and then increases, with limit plus infinity at both endpoints. It has at most two zeros; when two exist, only the larger can be a local minimum. A single tangency zero does not create a local minimum because the derivative does not change from negative to positive there. Thus for s>tau the positive global minimizer is unique. For signed scalar targets, comparison of t and -t forces any nonzero minimizing t to have the target's sign, so the symmetric exceptional value is -tau.

The ordering of the optimal coordinates also follows directly. If a minimizes phi_s and b minimizes phi_t, their two optimality inequalities give

phi_s(a)+phi_t(b)<=phi_s(b)+phi_t(a),

which simplifies to (s-t)(a-b)>=0. Therefore when s>t every choice of minimizers satisfies a>=b. At equal targets away from the tie threshold, scalar uniqueness makes their minimizers equal. Thus for X outside E the unique scalar minimizers x_j are automatically nonincreasing. The ordering constraint in the singular-value problem introduces no further coupling.

The matrix built from these x_j and any SVD of X attains the sum of the scalar minima. Conversely, every minimizer of G must attain both the trace-inequality bound and every scalar minimum, so it has these singular values and a simultaneous ordered SVD with X.

It remains to check that the permissible choices of SVD do not change the resulting matrix. On any positive singular-value block s of X, all optimal singular values equal the same scalar x(s). The corresponding block of the product is (x(s)/s) times the corresponding block of X; simultaneous rotations of its left and right bases therefore have no effect. On the zero singular-value subspaces, phi_0(t)=t^2+lambda t^q has the unique minimizer zero, so the product vanishes there regardless of the independent null-space basis choices. Signs also cancel between matching left and right vectors. Hence G has a unique matrix minimizer P*. By the minimizer correspondence,

{P(W): W in Omega}={P*}.

### 5. The exceptional set is null

For L<=2 the set is empty. For L>=3, tau>0. If sigma_j(X)=tau, then

p(X)=det(X^T X-tau^2 I_{d_0})=0.

This is a polynomial in the entries of X, is valid for either rectangular orientation, and is not identically zero because p(0)=(-tau^2)^{d_0} is nonzero.

For completeness, a nonzero polynomial in finitely many real variables has a null zero set. This follows by induction on the number of variables: write it as a polynomial in the last variable, choose one coefficient polynomial that is not identically zero, and apply the induction hypothesis to the set where all coefficient polynomials vanish. Outside that null set, each one-dimensional fiber has finitely many roots. Fubini on bounded boxes, followed by a countable union of boxes, proves the claim. Therefore each of the finitely many level sets defining E is null, and so is E.

### 6. Balancedness and invariant layer norms

We derive balancedness instead of relying on the quoted nonstandard external result. Fix W in Omega, an adjacent pair i,i+1, and a symmetric d_i-by-d_i matrix H. Modify only these two factors by

W_i(t)=exp(tH)W_i,    W_{i+1}(t)=W_{i+1}exp(-tH).

Their adjacent product, and hence the entire end-to-end product, is unchanged for every real t. Differentiating F along this feasible curve at its minimum t=0 gives

0=(2lambda/L)tr[H(W_iW_i^T-W_{i+1}^TW_{i+1})].

The matrix in parentheses is symmetric. Taking H equal to that matrix and using lambda>0 proves

W_iW_i^T=W_{i+1}^TW_{i+1}.

Taking traces gives ||W_i||_F=||W_{i+1}||_F. Thus all layer norms agree within every minimizing tuple. For L=1 this conclusion is automatic.

Now fix X outside E. The product is P* at every minimizer, so the data-fit term equals ||X-P*||_F^2 throughout Omega. The total objective value is also constant throughout Omega. Since lambda/L>0, the regularization sum sum_i||W_i||_F^2 is therefore constant. At every minimizer this sum is L times the common squared layer norm. Its nonnegative square root defines g* independent of both the minimizer and layer, as required.

### 7. Hessian trace

For each layer set

A_i=W_L...W_{i+1},    B_i=W_{i-1}...W_1,

with A_L=I_{d_L} and B_1=I_{d_0}. Holding the other factors fixed, the map W_i -> A_iW_iB_i is linear. Under column vectorization its matrix is K_i=B_i^T tensor A_i. Therefore the diagonal Hessian block is

2K_i^T K_i+(2lambda/L)I_{d_i d_{i-1}}.

Only the diagonal blocks contribute to the full trace. Summing them and using the entrywise identity ||B_i^T tensor A_i||_F^2=||B_i||_F^2||A_i||_F^2 gives, at every parameter tuple,

tr(nabla^2 F(W))=(2lambda/L)N+2sum_{i=1}^L||A_i||_F^2||B_i||_F^2.

At a minimizer, P*=A_iW_iB_i. Frobenius submultiplicativity follows from entrywise Cauchy-Schwarz: for conformable C,D,

sum_{a,b}|sum_k C_{ak}D_{kb}|^2
 <= sum_{a,b}(sum_k C_{ak}^2)(sum_k D_{kb}^2)
 = ||C||_F^2||D||_F^2.

Applying this twice yields ||P*||_F<=||A_i||_F||W_i||_F||B_i||_F. If g*>0, division and summation give

tr(nabla^2 F(W)) >= (2lambda/L)N+2L||P*||_F^2/(g*)^2.

If g*=0, all factors are zero and P*=0. No division is made: the exact trace identity gives tr(nabla^2 F(W))>=(2lambda/L)N because every summand is nonnegative. This is exactly the asserted bound with the task's zero-term convention. The same calculation includes L=1, for which both A_1 and B_1 are identity matrices. All conclusions follow.
