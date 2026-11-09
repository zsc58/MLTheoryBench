# Reference Proof

## Proof Structure

1. Distinguish a change of coordinates in an existing predictor from a raw-output rescaling followed by restandardization. Verify predictor and marginal-likelihood invariance for a genuine coordinate reparameterization.
2. Derive the standardized coordinates induced by each allowed raw-output rescaling and identify their residual sign transformation.
3. Prove conditional and marginal likelihood invariance for the actual standardized model, including its random intercept.
4. Prove invariance of the magnitudes, defined shares, and their posterior ordering probabilities, and demonstrate raw-sign non-identifiability.

## Complete Proof

All encoder outputs and empirical normalization statistics are held fixed when defining the conditional posterior. Write q_ij=(1,z_ij,1,...,z_ij,K)^T for the augmented standardized design vector, and index theta and v_i by 0,...,K.

First consider a coordinate reparameterization of an existing latent predictor, without subsequently restandardizing that predictor. For B=diag(1,b_1,...,b_K) with every b_k nonzero, define auxiliary quantities

q_bar_ij=B q_ij,
theta_bar=B^{-T}theta,
v_bar_i=B^{-T}v_i,
V_bar=B^{-T}V B^{-1}.

Then

q_bar_ij^T(theta_bar+v_bar_i)=q_ij^T(theta+v_i).

The structured term is unchanged. Also v_bar_i has Gaussian law N(0,V_bar), the pushforward of N(0,V) under v -> B^{-T}v. Thus integration of the equal conditional likelihoods against these corresponding laws gives equal marginal likelihoods. This is a coordinate identity for the existing predictor. The auxiliary q_bar need not satisfy the normalization convention, and theta_bar is not asserted to be the parameter transformation induced by rescaling raw encoder outputs and then standardizing them.

For the actual procedure, let A=diag(a_1,...,a_K) act on raw outputs r_ij, with every a_k nonzero. Let mu_k and s_k>0 denote the empirical mean and standard deviation used to normalize coordinate k. The same empirical normalization sample and convention are used in the transformed representation. Its mean and standard deviation are therefore

mu'_k=a_k mu_k,
s'_k=|a_k|s_k.

Consequently

z'_ij,k=(a_k r_ij,k-a_k mu_k)/(|a_k|s_k)
=sign(a_k) z_ij,k.

Put epsilon_k=sign(a_k) and S=diag(1,epsilon_1,...,epsilon_K). Then q'_ij=S q_ij. Conversely, every such sign pattern is attained by choosing the raw rescaling factors to have those signs. Thus the residual ambiguity within the allowed rescaling family is exactly coordinatewise sign reversal of the learned coordinates, with the intercept fixed.

The corresponding parameters of the actual standardized model are

theta'=S theta,
v'_i=S v_i,
V'=S V S,
b'=b.

Since S^T S=I,

c_ij^T b'+q'_ij^T(theta'+v'_i)
=c_ij^T b+q_ij^T(theta+v_i).

Every conditional success probability is therefore unchanged. Conditional independence makes the subject likelihood the product of the Bernoulli probabilities, so each subject's entire conditional likelihood is unchanged as well.

To verify the transformed random-effect law also for singular V, its characteristic function at t is

E[exp(i t^T S v_i)]=exp(-t^T S V S t/2),

which is the characteristic function of N(0,V'). Independence between subjects is preserved by the separate deterministic transformations. If ell_i(v;b,theta,q) denotes the conditional subject likelihood, then

m_i(b,theta,V;q)
=E_{v~N(0,V)}[ell_i(v;b,theta,q)]
=E_{v~N(0,V)}[ell_i(Sv;b,S theta,Sq)]
=E_{v'~N(0,SVS)}[ell_i(v';b,S theta,Sq)]
=m_i(b',theta',V';q').

These are expectations of bounded functions, so they are well-defined for every Gaussian covariance matrix, including V=0. This pushforward change of variables needs no Gaussian density. When densities exist it is equivalent to the usual density/Jacobian argument. Multiplying over subjects proves invariance of the full marginal likelihood.

For k=1,...,K,

|theta'_k|=|epsilon_k theta_k|=|theta_k|

and

V'_kk=epsilon_k^2 V_kk=V_kk.

Thus d_k^pop and d_k^het are invariant. Define T_pop=sum_{l=1}^K |theta_l| and T_het=sum_{l=1}^K sqrt(V_ll). Both totals are invariant and nonnegative. Their positive domains are preserved by the transformation. Wherever the relevant total is positive, each corresponding share rho_k^pop or rho_k^het is unchanged. If a total is zero, its shares are undefined and no share assertion is made there.

Let Pi be any posterior covered by the setup, and let Pi' be its transported posterior under F_S(b,theta,V)=(b,S theta,SVS). On the domain where a family of shares is defined, every ordering event E for that family satisfies F_S^{-1}(E')=E, where E' is the same comparison in the primed representation. The setup requires this domain to have posterior probability one when the ordering probability is used. Therefore

Pi'(E')=Pi(F_S^{-1}(E'))=Pi(E).

This proves representation independence of posterior ordering probabilities, including comparisons with equal shares or repeated indices. It uses transported posteriors, not an assertion that every unchanged coordinate-specific prior is invariant.

Finally, for any k in {1,...,K} with theta_k nonzero, choose epsilon_k=-1 and every other epsilon_l=+1. This preserves the intercept, model assumptions, and marginal likelihood, but replaces theta_k by -theta_k. Its raw sign is therefore not identifiable within the specified ambiguity without an additional orientation convention. Magnitudes and defined shares are identifiable within that ambiguity in the stated sense of being constant on its equivalence classes. No full statistical identifiability beyond this equivalence relation is asserted.
