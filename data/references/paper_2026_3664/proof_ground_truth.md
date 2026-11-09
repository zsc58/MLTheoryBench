# Reference Proof

For any countable-alphabet pmf p, write Z_i=hat p_i-p_i. Pointwise,

||hat p-p||_infty <= (sum_i Z_i^2)^(1/2).

Jensen's inequality and Tonelli's theorem give

Delta_n(p) <= (E_p sum_i Z_i^2)^(1/2)
           = ((sum_i p_i(1-p_i))/n)^(1/2)
           = ((1-sum_i p_i^2)/n)^(1/2)
           <= n^(-1/2).

The sums are well defined: their terms are nonnegative and sum_i p_i(1-p_i)<=1. Thus the upper bound holds uniformly over finite and infinite supports, including point masses.

For p*=(1/2,1/2,0,...), let epsilon_r=2 1{X_r=1}-1 and T=sum_{r=1}^n epsilon_r. These are independent Rademacher variables, and ||hat p-p*||_infty=|T|/(2n). Direct expansion gives E T^2=n and E T^4=3n^2-2n<=3n^2. Paley-Zygmund applied to T^2 yields

P(T^2>=n/2) >= (1/2)^2 (E T^2)^2/(E T^4) >= 1/12.

Consequently,

Delta_n(p*)=E|T|/(2n) >= sqrt(n/2)/(24n)=1/(24 sqrt(2n)).

Set c=1/(24 sqrt(2)), C=1, and n0=1. For every n>=n0 and every p, the uniform upper bound implies Delta_n(p*)>=c Delta_n(p). Since p* is among the distributions in the supremum,

c n^(-1/2) <= sup_p Delta_n(p) <= C n^(-1/2).

All theorem-critical steps are derived here. The nonstandard independent-Bernoulli characterization and maximal decoupling inequality cited in the source are not assumed or needed for this proof.
