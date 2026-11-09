# Reference Proof

Let the recurrent blocks and transient blocks be ordered as in the task. Since P is row-stochastic and gamma<1, I-gamma P is invertible by its Neumann series. Thus it suffices to show that the classwise constructions satisfy every block of the Bellman equation.

For a recurrent block, write P_k=P^(k), mu=mu^(k), and D=diag(mu). Stationarity gives (P_k)*1=D^{-1}P_k^T mu^T=1, so (P_k)* is stochastic. The restricted equation is v_k=gamma P_k v_k+r_k. Transposing and multiplying on the right by D gives

v_k^T D=gamma v_k^T D(P_k)*+r_k^T D.

If a_k=mu r_k>0, multiplication by (1-gamma)/a_k shows that w=(1-gamma)v_k^T D/a_k satisfies the specified PageRank equation. It is a probability row vector: v_k is nonnegative by the Neumann series, and multiplying the restricted Bellman equation by mu gives mu v_k=a_k/(1-gamma). PageRank uniqueness therefore identifies w with w_k and yields the stated coordinate formula. If r_k=0, invertibility gives v_k=0.

Now work backward through the transient blocks, so all downstream values of the current block are known. Its Bellman equation is

(I-gamma Q^(j))v^(j)=bvec^(j),  bvec^(j)=r^(j)+gamma sum_{d downstream}P_{T_j,d}v^(d).

The effective reward is nonnegative. If it is zero, invertibility gives v^(j)=0. If lambda_j=0, irreducibility of Q^(j) forces it to be a one-state zero matrix: a directed cycle would give positive spectral radius, while a one-state block without a self-transition has Q=[0]. Consequently the block equation gives v^(j)=bvec^(j), including its zero-reward case.

For lambda_j>0, abbreviate Q=Q^(j), lambda=lambda_j, nu=nu_j, D=diag(nu), b=bvec^(j), and B=lambda^{-1}D^{-1}Q^T D. Perron-Frobenius supplies a positive right eigenvector h with Qh=lambda h. With H=diag(h), the Doob transform lambda^{-1}H^{-1}QH is stochastic because Qh=lambda h. Its stationary probability law, after scaling h so nu h=1, is nu(s)h(s); direct substitution shows that its time reversal is B. Independently, B1=lambda^{-1}D^{-1}Q^T nu^T=1 by nu Q=lambda nu, so B is the stochastic kernel required for PageRank. These are algebraic consequences of the displayed eigenvector identities and require no separate specialized result.

Transposing the transient block equation and multiplying on the right by D yields

v^(j)^T D=gamma lambda v^(j)^T D B+b^T D.

Put b_j=nu b. Because nu is positive and b is nonnegative and nonzero, b_j>0. The Neumann series makes v^(j) nonnegative. Multiplication of the block equation by nu gives (1-gamma lambda)nu v^(j)=b_j. Hence w=(1-gamma lambda)v^(j)^T D/b_j is a probability row vector. The preceding matrix identity gives

w=gamma lambda wB+(1-gamma lambda)b^T D/b_j.

The restart row b^T D/b_j is the distribution specified in the task. PageRank uniqueness gives w=w_j and the claimed coordinate formula. Recursion through the finite downstream order constructs a vector satisfying every block equation; invertibility of I-gamma P makes it the unique global value.
