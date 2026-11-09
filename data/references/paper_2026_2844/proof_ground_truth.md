# Reference Proof

## Proof Structure

First show that calibrating each group at its own quantile forces a positive expected-size gap relative to the reference group by monotonicity and the reference-group ordering assumption. Then show that any common expected size lying strictly between two distinct coverage-calibrated sizes moves the corresponding thresholds to opposite sides of their quantiles; local derivative and density bounds convert these threshold shifts into opposite-signed coverage errors.

## Complete Proof

By the finite-attainment assumption and continuity, F_{S|g}(q_g)=1-alpha for every group. Thus calibration at q_g has exact group coverage and expected size lambda_g=ell_g(q_g).

Let H_r={g:q_g>=q_r}. For every g in H_r\\{r}, monotonicity of ell_g gives ell_g(q_g)>=ell_g(q_r). By (A2), ell_g(q_r)-ell_r(q_r)>=c_g>0. Therefore lambda_g-lambda_r=ell_g(q_g)-ell_r(q_r)>=c_g>0. Exact group-wise coverage therefore cannot have equal expected set size. In particular, for D_r^2=sum_{g in H_r\\{r}} p_g(lambda_g-lambda_r)^2, D_r^2>=sum_{g in H_r\\{r}}p_gc_g^2>0, and the maximum pairwise size disparity is positive.

Now suppose thresholds tau_g attain one common expected size lambda, so ell_g(tau_g)=lambda. Choose groups g,h with lambda_g<lambda<lambda_h. Since each ell_j is nondecreasing, the strict inequalities imply tau_g>q_g and tau_h<q_h. On the segment from q_g to tau_g, absolute continuity and |ell'_g|<=V_g imply lambda-lambda_g<=V_g(tau_g-q_g), so tau_g-q_g>=(lambda-lambda_g)/V_g. Using absolute continuity of F_{S|g} and f_{S|g}>=m_g,

F_{S|g}(tau_g)-(1-alpha)=integral_{q_g}^{tau_g} f_{S|g}(t)dt>=m_g(tau_g-q_g)>=kappa_g(lambda-lambda_g).

For group h, the same argument on the segment from tau_h to q_h gives q_h-tau_h>=(lambda_h-lambda)/V_h and hence (1-alpha)-F_{S|h}(tau_h)>=kappa_h(lambda_h-lambda). The two groups have opposite-signed coverage deviations, whose absolute difference is at least kappa_g(lambda-lambda_g)+kappa_h(lambda_h-lambda)>0. Thus equalized expected size at a level strictly between two distinct calibrated sizes necessarily entails coverage disparity.
