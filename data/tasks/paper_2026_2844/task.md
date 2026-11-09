# Problem

## Setup

Let X be a covariate, Y a label, and G=G(X) in {1,...,K} a prespecified finite group label with masses p_g=P(G=g)>0 and sum_g p_g=1. Let S=S(X,Y) be a score with continuous conditional CDFs F_{S|g}(t):=P(S<=t|G=g). For each threshold t define C_t(X):={y:S(X,y)<=t}, and set ell_g(t):=E[|C_t(X)| | G=g], the expected prediction-set size at threshold t. Fix alpha in (0,1), and assume the quantile infima below are finite (hence attained by continuity). Define

q_g:=inf{t:F_{S|g}(t)>=1-alpha},   lambda_g:=ell_g(q_g).

Fix a reference group r, let H_r:={g:q_g>=q_r}, and assume H_r\\{r} is nonempty. For each g in H_r\\{r}, there is c_g>0 such that

ell_g(q_r)-ell_r(q_r)>=c_g. (A2)

Whenever a segment joining q_g and a threshold tau_g is considered, assume F_{S|g} and ell_g are absolutely continuous there, F_{S|g} has density f_{S|g}(t)>=m_g>0, and |ell'_g(t)|<=V_g almost everywhere, with 0<V_g<infinity. Set kappa_g:=m_g/V_g.

## Task

Prove the following integrated theorem.

1. Exact group-wise coverage forces size disparity. Calibrating each group at q_g gives F_{S|g}(q_g)=1-alpha. Under (A2), lambda_g-lambda_r>=c_g>0 for every g in H_r\\{r}. Consequently expected set sizes cannot all be equal, and D_r^2:=sum_{g in H_r\\{r}}p_g(lambda_g-lambda_r)^2>=sum_{g in H_r\\{r}}p_gc_g^2>0.

2. Equalized expected size forces coverage disparity. Let tau_g satisfy ell_g(tau_g)=lambda for every group. If lambda_g<lambda<lambda_h for some groups g,h, prove

F_{S|g}(tau_g)-(1-alpha)>=kappa_g(lambda-lambda_g),

(1-alpha)-F_{S|h}(tau_h)>=kappa_h(lambda_h-lambda),

and hence the cross-group coverage disparity is at least kappa_g(lambda-lambda_g)+kappa_h(lambda_h-lambda)>0. Thus a common size strictly between two distinct calibrated sizes is incompatible with exact group-wise coverage.

The statement is conditional on the existence of thresholds tau_g satisfying the displayed equal-size equations; no existence or uniqueness of such thresholds is asserted beyond that condition.
