# Reference Proof

## Proof Structure

On the simultaneous tail event, bracket the empirical threshold using the two-sided local margin. Expand the empirical RU objective at the population threshold using a signed hinge-integral identity. Separate the population linear term, population curvature, and empirical coupling. Bound the last two terms on the localized interval, and intersect with the hinge-process event.

## Complete Proof

All population hinge expectations are finite because (X_h-t)_+ <= X_h+|t| and P X_h<infinity. Empirical hinge averages are finite because the losses are finite-valued and n>=1.

For a fixed h, the empirical tail is a nonincreasing right-continuous step function. It equals 1 below the smallest observed loss and 0 at and above the largest observed loss. Since 0<alpha<1, its level-crossing infimum q=hat theta_n(h) is finite and attained, T_{n,h}(q)<=alpha, and T_{n,h}(s)>alpha for s<q. These facts hold even with ties and even when n alpha is an integer. The threshold is an order statistic and is measurable for each fixed h.

For any finite real x,a,b, direct integration gives the signed identity

(x-a)_+-(x-b)_+ = - integral_b^a 1{x>s} ds.

Integrals are oriented: integral_b^a=-integral_a^b when a<b. Taking expectation or a finite sample average is legitimate because the increment is bounded in absolute value by |a-b|. In particular, for either population or empirical RU objective F with tail T,

F(a)-F(b)=alpha^(-1) integral_b^a (alpha-T(s)) ds.

For the empirical tail at q, the integrand is nonnegative to the right of q and negative to the left. Thus F(a)>=F(q) for every a; moreover, for a<q the inequality is strict. This verifies that q is the minimal empirical RU minimizer and that the public empirical value is the empirical RU infimum. No external representation theorem is needed, since the public values are defined through the RU objectives themselves.

The public population threshold is assumed to attain the population infimum. It also agrees with the source's minimal crossing: the left margin and monotonicity give T_h(t)>alpha for every t<theta^star(h), whereas T_h(theta^star(h))=alpha. The two-sided margins force the one-sided limits at this threshold to equal alpha, so there is no atom there. No continuity away from this threshold is needed.

Fix delta in (0,1) satisfying the stated smallness condition. Let E_T and E_H be the measurable tail and hinge events at confidence delta/2. Their intersection has probability at least 1-delta by the union bound; independence of the events is not required. Set

e=epsilon_n(delta/2)>0,
Delta=(2e/c_-)^(1/kappa).

The smallness condition gives 0<Delta<=u_0, including equality at u_0. On E_T, simultaneously for every h and t,

|T_{n,h}(t)-T_h(t)|<=e.

The margins at theta^star(h)+Delta and theta^star(h)-Delta imply

T_{n,h}(theta^star(h)+Delta)<=alpha-c_-Delta^kappa+e=alpha-e<alpha,

T_{n,h}(theta^star(h)-Delta)>=alpha+c_-Delta^kappa-e=alpha+e>alpha.

The upper endpoint belongs to the empirical crossing set, and no point below the lower endpoint belongs to that set. Therefore

|hat theta_n(h)-theta^star(h)|<=Delta

simultaneously for all h on E_T.

Fix any h on this event and abbreviate theta=theta^star(h), d=hat theta_n(h)-theta, T=T_h, and T_n=T_{n,h}. Let g_t(z)=(ell(h,z)-t)_+. Define the exact population and empirical increment remainders

Q_h(d)=- integral_theta^(theta+d) [T(s)-T(theta)] ds,

J_h(d)=- integral_theta^(theta+d) [T_n(s)-T(s)] ds.

The signed hinge identity gives

P(g_(theta+d)-g_theta)=-d T(theta)+Q_h(d),

(P_n-P)(g_(theta+d)-g_theta)=J_h(d).

These identities hold for every finite pair of endpoints, so they remain valid when the second endpoint is the observed threshold; no independence of that threshold and the sample is assumed.

Using C(h)=theta+alpha^(-1)P g_theta and the definition of hat C_n(h), we obtain

hat C_n(h)-C(h)
=alpha^(-1)(P_n-P)g_theta+d+alpha^(-1)P_n(g_(theta+d)-g_theta)
=alpha^(-1)(P_n-P)g_theta+alpha^(-1)d(alpha-T(theta))+R_n(h),

where

R_n(h)=alpha^(-1)[Q_h(d)+J_h(d)].

This fixes the remainder's signs exactly. In terms of objective increments, the telescoping identity being used is A+B=A+C+(B-C), where A=hat Phi(theta)-Phi(theta), B=hat Phi(theta+d)-hat Phi(theta), and C=Phi(theta+d)-Phi(theta).

To bound the integrals for either sign of d, integrate absolute values over [min(theta,theta+d),max(theta,theta+d)]. On E_T,

|J_h(d)|<=e|d|.

Since |d|<=Delta<=u_0 and T(theta)=alpha, the upper parts of the two margin bounds give

|T(s)-T(theta)|<=c_+|s-theta|^kappa

throughout this interval. Hence

|Q_h(d)|<=c_+ integral_0^|d| u^kappa du
=c_+|d|^(kappa+1)/(kappa+1).

The formulas also apply when d=0, when both integrals vanish. Consequently, simultaneously for every h on E_T,

|R_n(h)|<=alpha^(-1)[e|d|+c_+|d|^(kappa+1)/(kappa+1)]
<=alpha^(-1)[e Delta+c_+Delta^(kappa+1)/(kappa+1)].

On E_H, the leading term satisfies

sup_h |alpha^(-1)(P_n-P)[(X_h-theta^star(h))_+]|<=alpha^(-1)eta_n(delta/2).

The correction alpha^(-1)d(alpha-T_h(theta^star(h))) is zero under the assumed equality, but retaining it yields exactly the requested decomposition. All assertions therefore hold on E_T intersect E_H, of probability at least 1-delta. If H is empty, the simultaneous assertions are vacuous and the supremum inequalities hold with the usual empty-supremum convention.

Finally,

e Delta=(2/c_-)^(1/kappa)e^((kappa+1)/kappa),

Delta^(kappa+1)=(2/c_-)^((kappa+1)/kappa)e^((kappa+1)/kappa).

Substitution gives the stated bound with

C_1=(2/c_-)^(1/kappa)+(c_+/(kappa+1))(2/c_-)^((kappa+1)/kappa).

## Source Repair Note

The source's displayed decomposition (83), hinge-increment sign in (86), subsequent signs and coupling label in (87)-(90), and reversed-endpoint treatment in (91) and (93) contain local algebraic errors. The exact telescoping and signed integral identities above repair them without changing the target or its proof architecture. This repair is recorded under theory_007. All theorem-critical obligations are derived above; no private proof gap remains.
