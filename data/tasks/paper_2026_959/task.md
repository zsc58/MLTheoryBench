# Problem

## Setup

Let H be a class of hypotheses and let ell(h,.) be a measurable function taking finite values in [0,infinity) for each h in H. Let Z_1,...,Z_n be iid observations with the same law as Z, where n is a positive integer, and put X_h=ell(h,Z). Assume P X_h<infinity for every h. Write Pf=E[f(Z)] and P_n f=n^(-1)sum_{i=1}^n f(Z_i), and write (x)_+=max{x,0}. Fix alpha in (0,1). For t in R define T_h(t)=P(X_h>t) and T_{n,h}(t)=P_n(X_h>t).

Define the population Rockafellar-Uryasev value and an empirical value by

C(h)=inf_{t in R} {t+alpha^(-1)P[(X_h-t)_+]},

hat C_n(h)=hat theta_n(h)+alpha^(-1)P_n[(X_h-hat theta_n(h))_+],

where theta^star(h) in R is a population minimizer satisfying T_h(theta^star(h))=alpha and

hat theta_n(h)=inf{t in R:T_{n,h}(t)<=alpha}.

Assume there are finite constants kappa>=1, 0<c_-<=c_+, and u_0>0 such that, for every h and 0<u<=u_0,

alpha+c_-u^kappa <= T_h(theta^star(h)-u) <= alpha+c_+u^kappa,

alpha-c_+u^kappa <= T_h(theta^star(h)+u) <= alpha-c_-u^kappa.

Let epsilon_n,eta_n:(0,1)->(0,infinity) be deterministic functions. Assume that for every rho in (0,1), there is a measurable event of probability at least 1-rho on which

sup_h sup_t |T_{n,h}(t)-T_h(t)| <= epsilon_n(rho),

and there is a measurable event of probability at least 1-rho on which

sup_h |(P_n-P)[(X_h-theta^star(h))_+]| <= eta_n(rho).

All probabilities are under the joint law of the observations. For rho in (0,1), set

Delta_n(rho)=(2epsilon_n(rho)/c_-)^(1/kappa).

Fix delta in (0,1) such that epsilon_n(delta/2)<=(c_-/2)u_0^kappa.

## Task

Prove that there is a measurable event of probability at least 1-delta on which, uniformly for all h in H,

hat C_n(h)-C(h)
= alpha^(-1)(P_n-P)[(X_h-theta^star(h))_+]
 + alpha^(-1)(hat theta_n(h)-theta^star(h))(alpha-P(X_h>theta^star(h)))
 + R_n(h),

and

sup_h |R_n(h)| <= alpha^(-1)[epsilon_n(delta/2)Delta_n(delta/2) + c_+Delta_n(delta/2)^(kappa+1)/(kappa+1)].

In particular, on that event the first empirical-process term is uniformly bounded in absolute value by alpha^(-1)eta_n(delta/2), and the remainder is at most alpha^(-1)C_1 epsilon_n(delta/2)^((kappa+1)/kappa), where

C_1=(2/c_-)^(1/kappa)+(c_+/(kappa+1))(2/c_-)^((kappa+1)/kappa).
