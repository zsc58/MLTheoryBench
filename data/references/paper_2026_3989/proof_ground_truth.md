# Reference Proof

## Proof Structure

Verify that the empirical means belong to the generator's domain and agree with the minimizing representatives used in the source. Derive the Bregman three-point identity directly from the definition, apply it in each child, and cancel centered residuals. Normalize to obtain the exact gain decomposition without strong convexity. Under the additional strong-convexity hypothesis, bound the two divergences and simplify using the weighted parent mean.

## Complete Proof

All observations lie in the convex set C, so each finite empirical mean mu_u belongs to C. All divergences used below are finite because psi is real-valued and differentiable on C.

First, subtraction of the defining formulas gives, for x,y,z in C,

D_psi(x,z)-D_psi(x,y)-D_psi(y,z)=<grad psi(y)-grad psi(z),x-y>.

Thus the three-point identity is

D_psi(x,z)=D_psi(x,y)+D_psi(y,z)+<x-y,grad psi(y)-grad psi(z)>.

For a finite nonempty node u and any z in C, apply this identity with x=y_i and y=mu_u and sum over i in u. Since sum_{i in u}(y_i-mu_u)=0,

sum_{i in u}D_psi(y_i,z)=sum_{i in u}D_psi(y_i,mu_u)+|u|D_psi(mu_u,z).

The first-order strict-convexity inequality gives D_psi(mu_u,z)>=0, with equality exactly when z=mu_u. Consequently, mu_u is the unique minimizer of the within-node divergence sum over C. This verifies the equivalence between the public empirical-mean definition and the source's minimizing representative.

Write p_L=|t_L|/|t| and p_R=|t_R|/|t|. Since the nonempty children partition the parent, p_L,p_R>0 and p_L+p_R=1. For c in {L,R}, apply the three-point identity to each observation in t_c:

D_psi(y_i,mu_t)=D_psi(y_i,mu_{t_c})+D_psi(mu_{t_c},mu_t)+<y_i-mu_{t_c},grad psi(mu_{t_c})-grad psi(mu_t)>.

Summing over i in t_c, the inner-product term vanishes because sum_{i in t_c}(y_i-mu_{t_c})=0. Hence

sum_{i in t_c}D_psi(y_i,mu_t)=sum_{i in t_c}D_psi(y_i,mu_{t_c})+|t_c|D_psi(mu_{t_c},mu_t).

Add the two child identities and divide by |t|. The definitions of impurity give

I_psi(t)=p_L I_psi(t_L)+p_R I_psi(t_R)+p_L D_psi(mu_{t_L},mu_t)+p_R D_psi(mu_{t_R},mu_t).

Subtracting the weighted child impurities yields

Delta_psi(t)=p_L D_psi(mu_{t_L},mu_t)+p_R D_psi(mu_{t_R},mu_t).

This establishes the exact decomposition without strong convexity.

Now additionally assume that psi is lambda-strongly convex for some lambda>0, meaning that D_psi(a,b)>=lambda||a-b||^2/2 for all a,b in C. Applying this inequality to both terms gives

Delta_psi(t)>=lambda/2 [p_L||mu_{t_L}-mu_t||^2+p_R||mu_{t_R}-mu_t||^2].

Because the children partition t,

mu_t=p_L mu_{t_L}+p_R mu_{t_R}.

Consequently,

mu_{t_L}-mu_t=p_R(mu_{t_L}-mu_{t_R}),

mu_{t_R}-mu_t=-p_L(mu_{t_L}-mu_{t_R}).

Therefore

p_L||mu_{t_L}-mu_t||^2+p_R||mu_{t_R}-mu_t||^2
=(p_L p_R^2+p_R p_L^2)||mu_{t_L}-mu_{t_R}||^2
=p_L p_R||mu_{t_L}-mu_{t_R}||^2.

Substitution proves

Delta_psi(t)>=(lambda/2)p_L p_R||mu_{t_L}-mu_{t_R}||^2.

No division by a mean difference occurs, so the argument includes coincident child means and singleton children.

## Source Repair Notes

The general three-point formula at L000046 reverses the gradient difference. The correct formula follows from the definition and agrees with L000204; this repair is recorded under theory_002. The existing theory_006 repair replaces global observation indexing and normalization by the parent-node index set and |t|. The existing theory_008 repair replaces the duplicated left-child weight by the product of the two child weights. All three repairs are reflected in this proof. There are no unresolved proof obligations.
