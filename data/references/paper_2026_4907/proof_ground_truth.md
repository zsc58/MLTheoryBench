# Reference Proof

## Proof Obligations

1. Verify the finite metric and its sectionwise equivalence relation, and verify that the discounted visitation formula defines a measurable probability kernel.
2. Establish joint measurability, normalization, finite supremum L_n norm, and representative independence for the density formulas.
3. Prove the gamma-contraction inequality with the stated supremum over every conditioning pair.
4. Derive the one-step visitation recursion from the discounted series and the transition-policy dynamics.
5. Verify directly that the specified q^pi is a fixed point in Q.
6. Derive uniqueness and the exact geometric error bound for every initial class in Q, including gamma=0.
7. Verify representative independence of the intrinsic reward without asserting continuity or finiteness of KL.

## Standard Background Used

For a probability measure nu and finite n>=1, Jensen's inequality gives |integral u dnu|^n <= integral |u|^n dnu whenever the right side is finite. It also gives ((1-gamma)a+gamma b)^n <= (1-gamma)a^n+gamma b^n for nonnegative a,b. The usual L_n triangle inequality applies to measurable functions with finite L_n norm.

Tonelli's theorem permits interchanging integration of a nonnegative jointly measurable function against a probability measure and the sigma-finite measure mu. Monotone convergence permits interchange with nonnegative series. Integration of a jointly measurable nonnegative function against a measurable probability kernel gives a measurable function of the remaining parameters; this follows first for measurable rectangles and then by nonnegative measurable approximation. These statements apply to the kernels and densities below. No specialized external theorem or paper-specific cited construction is left as an unproved obligation.

## Complete Proof

### 1. Metric, visitation kernel, and admissibility of q^pi

Write X=S x A and x=(s,a). For a conditional density f, set

M(f) = sup_x (integral |f(z|x)|^n mu(dz))^(1/n).

The L_n triangle inequality gives bar L_n([f],[g]) <= M(f)+M(g)<infinity. Symmetry and the triangle inequality follow sectionwise and then by taking suprema. Distance zero means precisely that f(.|x)=g(.|x) mu-almost everywhere for every x. Thus the displayed expression is a metric on the stated quotient. The class [h] belongs to Q, so Q is nonempty.

Define the transition-policy probability kernel

K(x,dy)=p(ds'|s,a)pi(da'|s'), where y=(s',a').

Let K^Delta be its Delta-fold composition. Starting with the fixed initial action a, the state marginal after Delta transitions is p_Delta^pi, and the action at that future state is sampled from pi. Consequently

K^Delta(x,d sbar d abar)=p_Delta^pi(d sbar|s,a)pi(d abar|sbar).

For brevity, write D_x=d^pi,gamma(.|x). Then

D_x=(1-gamma) sum_(Delta>=1) gamma^(Delta-1) K^Delta(x,.).

Each summand is a measurable probability kernel, all coefficients are nonnegative, and their sum is one. At gamma=0 the only nonzero coefficient is that of Delta=1. Therefore D is a measurable probability kernel.

Kernel integration shows that q^pi(z|x)=integral h(z|y)D_x(dy) is jointly measurable and nonnegative. Tonelli gives, for every x,

integral q^pi(z|x) mu(dz)
= integral [integral h(z|y) mu(dz)] D_x(dy)
= 1.

Jensen and Tonelli give

integral |q^pi(z|x)|^n mu(dz)
<= integral [integral |h(z|y)|^n mu(dz)] D_x(dy)
<= H^n.

Thus M(q^pi)<=H, and [q^pi] belongs to Q. In particular, its density is finite mu-almost everywhere in each section. If finite-valued representatives are desired, the jointly measurable set on which a displayed density is infinite can be assigned value zero; that set has measure zero in every section and does not change its class.

### 2. The operator and contraction

First apply the operator formula to representatives. Kernel integration gives joint measurability and nonnegativity of P^pi f. Tonelli and normalization of h and f give

integral (P^pi f)(z|x) mu(dz)
= integral [(1-gamma) integral h(z|y) mu(dz) + gamma integral f(z|y) mu(dz)] K(x,dy)
= 1.

Using Jensen for K(x,.) and convexity for the two mixture weights,

integral |(P^pi f)(z|x)|^n mu(dz)
<= integral [(1-gamma) integral |h(z|y)|^n mu(dz) + gamma integral |f(z|y)|^n mu(dz)] K(x,dy)
<= (1-gamma)H^n + gamma M(f)^n.

Hence P^pi f is a conditional probability density with finite supremum L_n norm.

Let f,g represent elements of Q, and put B=bar L_n([f],[g]). For each x, Tonelli gives

integral [integral |f(z|y)-g(z|y)|^n K(x,dy)] mu(dz)
= integral [integral |f(z|y)-g(z|y)|^n mu(dz)] K(x,dy)
<= B^n.

Thus the inner nth moment is finite for mu-almost every z, so the signed expectation and Jensen step used next are legitimate there. The one-step h terms cancel, giving

(P^pi f)(z|x)-(P^pi g)(z|x)
= gamma integral [f(z|y)-g(z|y)] K(x,dy)

mu-almost everywhere in each section. Therefore

integral |(P^pi f-P^pi g)(z|x)|^n mu(dz)
<= gamma^n integral [integral |f(z|y)-g(z|y)|^n mu(dz)] K(x,dy)
<= gamma^n B^n.

Taking nth roots and the supremum over all x yields

bar L_n([P^pi f],[P^pi g]) <= gamma bar L_n([f],[g]).

In particular, equivalent representatives have equivalent images. The operator therefore descends to a well-defined map Q to Q and is a gamma-contraction. This argument uses sectionwise null sets and does not assume the existence of one exceptional feature null set common to all conditioning pairs.

### 3. Discounted visitation recursion

For every measurable B subset of X, monotone convergence and kernel composition give

integral D_y(B) K(x,dy)
= (1-gamma) sum_(m>=1) gamma^(m-1) K^(m+1)(x,B).

Multiplying by gamma and adjoining the first summand of D_x(B) proves the measure identity

D_x = (1-gamma)K(x,.) + gamma integral D_y K(x,dy).

No division by gamma occurs, so the identity also holds at gamma=0.

### 4. Direct existence and identification of the fixed point

Integrate the nonnegative feature density against the preceding measure identity. Interchanging the probability-kernel integrations gives

q^pi(z|x)
= (1-gamma) integral h(z|y) K(x,dy)
  + gamma integral [integral h(z|u) D_y(du)] K(x,dy)
= integral [(1-gamma)h(z|y) + gamma q^pi(z|y)] K(x,dy)
= (P^pi q^pi)(z|x).

These identities determine the same conditional density class. Since membership [q^pi] in Q was already established, this proves existence of the claimed fixed point directly.

### 5. Uniqueness, convergence, and intrinsic reward

If [f] is another fixed point in Q, its distance B from [q^pi] is finite and satisfies

B=bar L_n(P^pi[f],P^pi[q^pi]) <= gamma B.

Because gamma<1, this forces B=0, proving uniqueness.

For any [f_0] in Q, invariance makes every iterate well-defined. Applying contraction to [f_k] and [q^pi] and using induction gives

bar L_n([f_k],[q^pi]) <= gamma^k bar L_n([f_0],[q^pi])

for all integers k>=0. The initial distance is finite and gamma^k tends to zero. At gamma=0 the first iterate already equals [q^pi], while the k=0 estimate uses gamma^0=1. This proves the claimed convergence and all endpoint cases without any completeness assumption.

For each x, equivalent densities define the same probability measure on Z. Relative entropy against the probability measure with density q* depends only on those measures, not on their density representatives. It is defined as an extended nonnegative value, with +infinity when appropriate; hence the negated intrinsic reward is also representative-independent. No convergence claim for the numerical KL values of arbitrary iterates follows or is required.

## Completeness Audit

Banach's theorem gives abstract existence for a contraction on a nonempty complete metric space, but completeness of Q is neither assumed in the repaired task nor needed here. It must not be inferred merely from completeness of L_n: normalized probability densities need not be closed in L_n when n>1 and mu has infinite mass. For example, m^(-1)1_[0,m] converges in L_n to zero. The source's explicit fixed-point calculation closes existence, and the elementary metric estimates above close uniqueness and convergence. All listed proof obligations are resolved.
