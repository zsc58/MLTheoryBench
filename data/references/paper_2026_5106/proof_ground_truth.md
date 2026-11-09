# Reference Proof

## Proof obligations and source corrections

The proof below closes the following obligations: normalization and well-definedness; local mixture bounds; optimizer relations, including zero and boundary cases; all four finite-time estimates with their stated constants; the uniform conditional estimate; and the bounded-wealth asymptotic conclusions. The only probabilistic result invoked is Ville's inequality, stated and applied below. All analytic estimates are derived here or are explicitly stated elementary calculus inequalities.

The source's auxiliary zero-optimizer restrictions are retained. Its boundary-prior equality with denominator 4 is used only as a lower bound; the actual denominator is 2. The quadratic argument is written for both signs and includes the moderate-regime endpoint. The high-regime contradiction is taken along the actual branch indices, without an incorrect equivalence involving strict limsup inequalities. The smooth public iterated logarithms make the all-time conditional statement meaningful at every variance. Finally, the large-regime constant is kept at the correct logarithm levels.

## 1. Normalization, domains, and notation

Put C=6.6e, k=ln C, and L=ln k. Thus L=ln ln(6.6e), while ln L=ln ln ln(6.6e).

On either side of zero, use the radial coordinate t=|lambda| and let A be the corresponding endpoint parameter: A=1-p on the positive side and A=p on the negative side. The radial density is

q_A(t)=L/[2t u(ln u)^2],  u=ln(C/(At)),  0<t<=1/A.

Its cumulative integral from zero to t is L/[2ln ln(C/(At))]. Consequently each side has mass 1/2, and q has total mass one. The value assigned to the density at the single point zero does not affect any integral.

The derivative of ln q_A(t) with respect to ln t is

-1+1/u+2/(u ln u).

Here u>=k, the last two terms decrease with u, and (k-1)ln k>2. The latter follows, for example, from k>2.887 and ln k>1.06. Hence the density is radially decreasing. At the endpoint,

q_A(1/A)=A/(2kL),

so throughout I minus {0}, q(lambda)>=b/(2kL).

For every finite n, F_n(lambda) is a continuous nonnegative polynomial on compact I and F_n(0)=1. Thus a maximizer exists and F_n^*>=1. The mixture is finite and strictly positive, since the integrand is strictly positive in the interior. Therefore its logarithm and the regret are finite. If V_n=0, every Y_i with i<=n is zero, so F_n(lambda)=F_n=F_n^*=1 and r_n=0.

Fix n with v=V_n>0. Write S=S_n, s=|S|, a=lambda_n^*, d=|a|, and f(lambda)=ln F_n(lambda), using the extended value minus infinity at a zero of the wealth. The optimizer has positive wealth, so all factors there are positive. On the segment joining zero to a,

f'(lambda)=-sum_i Y_i/(1-lambda Y_i),

f''(lambda)=-sum_i Y_i^2/(1-lambda Y_i)^2<0.

When a is nonzero, put A=1-p and B=p if a>0, and A=p and B=1-p if a<0. Thus A+B=1 and b<=A,B<=c. For the zero-optimizer subcase of the small-interior argument only, use A=1-p and B=p.

## 2. Local mixture bounds and optimizer relations

For a nonzero optimizer, log-concavity gives F_n(ta)>=(F_n^*)^t for 0<=t<=1. Radial monotonicity then gives

F_n>=q(a)d int_0^1 (F_n^*)^t dt>=q(a)d sqrt(F_n^*).

For the last inequality, pair t with 1-t and apply the arithmetic-geometric mean inequality. This also handles F_n^*=1 without a division by zero. Hence

r_n<=0.5 f(a)-ln(q(a)d).                                      (1)

If a is interior and nonzero, integrate instead over the segment of length min{rho,d} from a toward zero. On this segment f'(a)=0 and every denominator in the second derivative is at least 1-Ad. Taylor's theorem and radial monotonicity yield, for every rho>0,

r_n<=rho^2 v/[2(1-Ad)^2]-ln(min{rho,d}q(a)).                   (2)

For an interior optimizer, Taylor's theorem applied to f' gives

0=-S-a sum_i Y_i^2/(1-xi Y_i)^2

for some xi between zero and a. Thus aS<=0, with opposite nonzero signs when a is nonzero. Bounding the denominators between 1-Ad and 1+Bd gives

(s/v)(1-Ad)^2<=d<=(s/v)(1+Bd)^2.

Using (1-Ad)^2>=1-2Ad in the first inequality gives

d>=s/(v+2As).                                                (3)

If the interior optimizer is zero, f'(0)=0 implies S=0.

For a boundary optimizer, d=1/A and sign(a)f'(a)>=0. The same Taylor identity, now with the appropriate one-sided derivative inequality, gives s>=d sum_i Y_i^2/(1-xi Y_i)^2 and the opposite-sign relation. Since each denominator is at most 1+B/A=1/A,

s>=Av,  v/s<=d=1/A<=1/b.                                    (4)

All ratios in this paragraph are used only for v>0; in particular a boundary optimizer then has s>0.

## 3. Small deviation with an interior optimizer

Suppose s<sqrt(2v) and a is interior. If a is nonzero, ln(1-z)<=-z and the optimizer upper bound give

f(a)<=ds<=s^2(1+Bd)^2/v<=s^2/(A^2v)<2/A^2<=2/b^2.

If a=0, f(a)=0, so the same final upper bound holds.

Set rho=1/[2c sqrt(1+v)]. Choose J=[rho/2,rho] when S<=0 and J=[-rho,-rho/2] when S>0. This interval lies inside I, has length rho/2, and satisfies -lambda S>=0 and |lambda Y_i|<=1/2. The elementary inequality ln(1-z)>=-z-z^2 for |z|<=1/2 therefore gives

f(lambda)>=-lambda S-lambda^2v>=-rho^2v>=-1

on J, using c>=1/2. Let A correspond to the chosen side. Radial monotonicity gives

F_n>=e^(-1)L/[4u(ln u)^2],  u=ln(C/(A rho)).

Since C/(A rho)=13.2ec sqrt(1+v)/A<=(14ec/b)sqrt(1+v), we may enlarge the denominator and also weaken 4 to 8. Combining with f(a)<=2/b^2 proves exactly the first public bound, including the zero-optimizer case.

## 4. Small deviation with a boundary optimizer

Suppose s<sqrt(2v) and a is a boundary optimizer. From (4), Av<=s<sqrt(2v), so v<2/A^2. Also f(a)<=ds. Consequently

0.5 f(a)<=0.5 s/A<=1/A^2<=1/b^2.

At the endpoint the exact prior value is

q(a)d=L/(2kL^2)>=L/(4kL^2).

Substitute this lower bound into (1). The result is

r_n<=1/b^2-ln(L/[4kL^2]),

which is the second public bound. The inequality, rather than equality, in the displayed prior comparison is the local correction to the source.

## 5. Moderate deviation

Suppose sqrt(2v)<=s<=bv/5. Then v>=50/b^2, and in particular v>=1. A boundary optimizer would satisfy s>=Av>=bv by (4), a contradiction. Thus the optimizer is interior and nonzero.

Put t=s/v. We first justify the optimizer bound needed for the curvature estimate. Let

g(z)=t(1+Bz)^2-z.

The optimizer relation says g(d)>=0. We have t<=b/5<=A/5, Bt<=1/5, and

g(0)=t>0,

g(1/A)=(t-A)/A^2<0,

g(2t)=t[(1+2Bt)^2-2]<0.

As g is an upward-opening quadratic, its larger root exceeds 1/A. Since d<1/A and g(d)>=0, d is at most the smaller root, which is less than 2t. This argument covers both optimizer signs and equality s=bv/5. It also recovers the source's sharper auxiliary estimate:

d<=t(1+Bd)^2<=t(1+2Bt)^2<=t+5Bt^2.

Choose

rho=min{d,(1-Ad)/sqrt(1+v)}.

Equation (2) gives

r_n<=1/2+ln(d/rho)+ln(2/L)+ln ln(C/(Ad))+2ln ln ln(C/(Ad)).      (5)

From (3) and s>=sqrt(2v),

Ad>=A/[2A+v/s]>=A/[2(1+sqrt(v))].

Therefore C/(Ad)<=(14e/A)(1+sqrt(v))<=(14e/b)(1+sqrt(v)).

Set

x=s/sqrt(4s/3+2v).

Since t<=1/5 and s^2>=2v, x^2>=15/17. Moreover d<=2t<=2/5, so

d/(1-Ad)<=10t/3.

It follows that

d/rho=max{1,d sqrt(1+v)/(1-Ad)}

<=max{1,(10/3)x sqrt(2+4t/3)sqrt(1+1/v)}

<=(20/3)x sqrt(1+1/v).

The last expression exceeds one, and ln(1+1/v)<=1. Thus

ln(d/rho)<=ln((20/3)x)+1/2.

Substituting into (5), replacing ln(2/L) by the larger ln(4/L), and using the bound on C/(Ad), proves exactly the third public bound.

## 6. Large deviation

Suppose s>=sqrt(2v) and s>bv/5. Define

D=2c+5/b,

A_4=ln4+ln k+ln L+2ln D.

Notice that ln k=L. In the public notation, A_4 is exactly ln4+ln ln(6.6e)+ln ln ln(6.6e)+2ln(2c+5/b); it is not ln4+ln L+ln ln L+2ln D.

For an interior optimizer, (3) gives d>1/(2A+5/b)>=1/D. For a boundary optimizer, d=1/A>=1/D as well. Since q(a)>=b/(2kL),

-ln(q(a)d)<=ln(2kLD/b)<=ln2+ln k+ln L+2ln D<=A_4,

where D>=1/b was used. Equation (1) now yields

r_n<=0.5 ln F_n^*+A_4,

which is the fourth public bound. The four branches exhaust all v>0.

## 7. A hindsight-wealth lower bound

For |lambda|<1 and |y|<=1, expanding the logarithm and bounding each term of degree at least two by y^2|lambda|^j gives

ln(1-lambda y)>=-lambda y+y^2[ln(1-|lambda|)+|lambda|].

Summing over the observations and choosing lambda=-S/(v+s), which belongs to (-1,1) and hence to I, gives

ln F_n^*>=s-v ln(1+s/v).

For z>=0, the function z(6+z)/(6+4z)-ln(1+z) vanishes at zero and has derivative

4z^3/[(6+4z)^2(1+z)]>=0.

Consequently

ln F_n^*>=s^2/(4s/3+2v).                                    (6)

When v=0, define the right-hand side of (6) as zero; the corresponding assertion was already proved directly.

## 8. Uniform conditional bound

For compact notation define

T_1(v)=(14ec/b)sqrt(1+v),

T_2(v)=(14e/b)(1+sqrt(v)),

H_j(v)=ln ln T_j(v)+2ln ln ln T_j(v),  j=1,2,

A_1=2/b^2+1+ln(8/L),

A_2=1/b^2-ln(L/[4kL^2]),

A_3=1+ln(4/L)+ln(20/3).

The first three bounds read r_n<=A_1+H_1(v), r_n<=A_2, and r_n<=A_3+H_2(v)+ln x, respectively. All these functions are defined for v>=0.

On E_alpha, put h=ln(1/alpha), so ln F_n<=h. In the moderate branch, (6) and ln F_n^*=ln F_n+r_n give

x^2<=h+A_3+H_2(v)+ln x.

The elementary inequality ln x<=x^2/4 holds for every x>0: the maximum of ln x-x^2/4 occurs at sqrt(2) and is negative. Thus

x^2<=(4/3)(h+A_3+H_2(v)),

r_n<=h/3+(4/3)(A_3+H_2(v)).                                 (7)

In the large branch, substituting ln F_n^*=ln F_n+r_n into its regret bound gives

r_n<=h+2A_4.                                                (8)

It remains to compare the finite logarithmic functions with the public regularizations uniformly down to v=0. Put D_0=28e/b, kappa=1+ln(D_0)/e, and

h_p=ln kappa+2ln(1+ln kappa).

For j=1,2 and v>=0,

T_j(v)<=D_0(e^e+v),

ln ln T_j(v)<=ln kappa+Lambda_2(v).

Since Lambda_2(v)>=1 and ln Lambda_2(v)<=Lambda_3(v), it follows that

H_j(v)<=h_p+Lambda_2(v)+2Lambda_3(v).                         (9)

Combining (7)-(9) with the small-deviation bounds proves the required uniform statement. For example, take C_1=4/3, C_2=8/3, and any positive K_alpha at least

max{A_1+h_p, A_2, h/3+(4/3)(A_3+h_p), h+2A_4, 1}.

These constants depend only on p and alpha, not on the path or n. The v=0 indices have r_n=0 and cause no exception.

Ville's inequality states that for a nonnegative supermartingale M indexed from zero with M_0=1,

P(sup_{n>=0}M_n>=u)<=1/u,  u>0.

The public stochastic assumption supplies adaptedness, integrability, and the supermartingale inequalities including the first transition; the verified prior normalization supplies F_0=1. Apply Ville with u=1/alpha. Since the complement of E_alpha is contained in {sup_n F_n>=1/alpha}, P(E_alpha)>=1-alpha.

## 9. Bounded wealth and diverging variance

Fix a path in tilde E. Each F_n is finite, and its limsup is finite, so there is a finite constant M>=0 with ln F_n<=M for every n. Also v=V_n tends to infinity.

On a large-branch index, (6) and the fourth regret bound imply

ln F_n>=0.5 s^2/(4s/3+2v)-A_4

=(v/2)(s/v)^2/[2+4(s/v)/3]-A_4.

The function t^2/(2+4t/3) is increasing for t>=0. Since s/v>b/5 in this branch,

ln F_n>=v b^2/[50(2+4b/15)]-A_4.

If there were infinitely many such indices, v would tend to infinity along those indices and contradict ln F_n<=M. Therefore the large branch occurs only finitely often. This argument also covers ratios approaching b/5 from above.

Write ell=ln ln v, which is positive and tends to infinity eventually. Directly from the definitions,

H_j(v)=ell+2ln ell+O_p(1)=ell(1+o(1)),  j=1,2.               (10)

At a remaining small-deviation index, s<sqrt(2v), so s/v tends to zero and s/sqrt(2v ell) is at most 1/sqrt(ell), which tends to zero.

At a remaining moderate index, combine (6) with the third regret bound to obtain

ln F_n>=x^2-ln x-A_3-H_2(v).

Using ln x<=x-1 and completing the square gives

(x-1/2)^2<=M+A_3-3/4+H_2(v).

Together with (10), this implies

x<=1/2+sqrt(ell(1+o(1))),  x^2<=ell(1+o(1)).                 (11)

In this branch t=s/v<=b/5 and x^2=vt^2/(2+4t/3). Thus (11) first gives t->0. It then gives

s^2/(2v ell)=(x^2/ell)(1+2t/3)<=1+o(1).

Combining the small and moderate indices proves S_n/V_n->0 and

limsup_n |S_n|/sqrt(2V_n ln ln V_n)<=1.

For regret, the small-interior bound and (10) give r_n<=ell+o(ell); the small-boundary bound is constant. In the moderate branch, (11) gives ln x<=0.5ln ell+O(1)=o(ell), so the third bound again yields r_n<=ell+o(ell). Since the large branch has disappeared, this proves the eventual regret assertion on the entire path.

Finally, Ville's inequality gives P(sup_n F_n>=m)<=1/m for positive integers m, and hence sup_n F_n<infinity almost surely. Under the additional assumption V_n->infinity almost surely, tilde E therefore has probability one, and all three pathwise conclusions hold almost surely.
