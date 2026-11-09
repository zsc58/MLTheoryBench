# Reference Proof

## Source Contract and Proof Obligations

The frozen target is the noiseless-density comparison. The source supplies its single-window estimate at L000262-L000266 and explicitly distinguishes noiseless and observed comparisons at L000294-L000296. The source's initial observed-density notation at L000270 also makes its citations to the observed-density theorem valid for that reading; adding a nonnegative noise term merely enlarges the radius. No source repair is needed to justify either reading when the density convention is kept consistent.

The proof must close the following obligations: the empirical matrices and stationary vectors are well defined; normalized pair and departure frequencies yield a uniform transition bound with the stated sample-size dependence; regularization converts transition error to stationary-vector error; the embedding and the three bias terms give the noiseless-density radius; and two event inclusions give the false-alarm and detection bounds. All of these obligations are derived below. The concentration inequality, partition approximation, and noise stability are explicit assumptions, not results that the solver must establish. No operator-perturbation theorem or specialized external method is used.

## 1. Stochasticity, Stationary Vectors, and the Embedding

For every observed departure from state i, exactly one transition from i is counted. Consequently, the positive-count rows of the empirical matrix sum to one and are nonnegative. The prescribed zero-count rows are probability vectors as well. This remains true when n=1 and every count is zero.

For any row-stochastic matrix R-tilde and signed row vector z,

||z R-tilde||_1 <= sum_j sum_i |z_i| R-tilde(i,j) = ||z||_1.

If R=(1-rho)R-tilde+rho J_N and z has coordinate sum zero, then z J_N=0, so

||zR||_1 <= (1-rho)||z||_1.

This also proves existence and uniqueness of a stationary probability vector without invoking an external theorem. Starting from a probability row v_0, put v_{k+1}=v_k R. Successive differences have zero sum, and their norms are bounded by (1-rho)^k ||v_1-v_0||_1. The geometric-series estimate makes (v_k) Cauchy. Its limit is a probability vector v satisfying vR=v. If v and w are stationary probability vectors, the same contraction gives ||v-w||_1 <= (1-rho)||v-w||_1, hence v=w. Apply this to both regularized matrices in each regime. For fixed sample size, the data take values in a finite set, so the matrices and their uniquely determined stationary vectors are measurable.

Because the partition cells are disjoint up to their assigned endpoints and have positive measure, for any u,v in R^N,

||E_Nu-E_Nv||_1 = sum_i integral_{I_i} |u_i-v_i|/m(I_i) dm = sum_i |u_i-v_i| = ||u-v||_1.

In particular, E_N maps probability vectors to probability densities. This is an established proof step, not an additional public assumption.

## 2. Uniform Empirical Transition Concentration

Fix a regime and suppress its label. Write p=pi_min,N. Since pi_N is a probability vector and pi_N(i)>=p, we have 0<p<=1. Define

c_0=c_*/32,    C_0=max{2C_*, exp(c_0)}.

These choices depend only on the given concentration constants and work for both regimes. Larger C_0 or smaller positive c_0 are also permissible.

First take n>=2 and put ell=n-1. Let

q_ij=pi_N(i)P_N(i,j),    q_i=pi_N(i),

q-hat_ij=C_ij/ell,    q-hat_i=C_i/ell.

Stationarity gives E q-hat_ij=q_ij and E q-hat_i=q_i. Fix epsilon in (0,1) and set a=p epsilon/4, which lies in (0,1). Let H be the event that all N^2 pair-frequency errors and all N departure-frequency errors are at most a. The assumed concentration inequality and a union bound give

P(H^c) <= (N^2+N) C_* exp(-c_* ell a^2)
         <= 2 C_* N^2 exp(-c_* n p^2 epsilon^2/32)
         <= C_0 N^2 exp(-c_0 n p^2 epsilon^2),

where ell=n-1>=n/2 was used.

On H,

q-hat_i >= pi_N(i)-a >= pi_N(i)/2 > 0.

Thus every empirical denominator is positive on H. Since q_ij=pi_N(i)P_N(i,j) and 0<=P_N(i,j)<=1,

|P-hat_n(i,j)-P_N(i,j)|
= |q-hat_ij-P_N(i,j)q-hat_i|/q-hat_i
<= (|q-hat_ij-q_ij|+P_N(i,j)|pi_N(i)-q-hat_i|)/q-hat_i
<= 4a/pi_N(i)
<= epsilon.

It follows that H is contained in G={||P-hat_n-P_N||_max<=epsilon}, and therefore P(G^c)<=B_s(epsilon). Here ||A||_max=max_{i,j}|A_ij|. Importantly, denominator control was proved on H; it is neither needed nor asserted on every outcome in G.

If n=1, the frequency-normalization argument is not used. Instead,

B_s(epsilon)=C_0 N^2 exp(-c_0 p^2 epsilon^2) >= C_0 exp(-c_0) >= 1.

Hence P(G^c)<=1<=B_s(epsilon) also in this case. This covers the empty transition counts without removing the one-observation case from the task.

For every sample outcome, the common regularization cancels in the difference:

P-hat_{n,rho}-P_{N,rho}=(1-rho)(P-hat_n-P_N).

Thus on G its max norm is at most (1-rho)epsilon, with the same failure bound.

## 3. Stationary-Distribution Perturbation

Let P=(1-rho)P-tilde+rho J_N and Q=(1-rho)Q-tilde+rho J_N, with stochastic tilde matrices, and let pi_P,pi_Q be their stationary probability row vectors. Set

x=pi_Q-pi_P,    e=pi_Q(Q-P).

Stationarity gives x=e+xP, and x has coordinate sum zero. The contraction proved in Section 1 therefore yields

||x||_1 <= ||e||_1+(1-rho)||x||_1,

so ||x||_1<=rho^{-1}||e||_1. Defining ||A||_{row,1}=max_i sum_j |A_ij|, we also have

||e||_1 <= sum_i pi_Q(i) sum_j |Q_ij-P_ij|
         <= ||Q-P||_{row,1}
         <= N||Q-P||_max.

Consequently,

||pi_Q-pi_P||_1 <= rho^{-1}||Q-P||_{row,1} <= (N/rho)||Q-P||_max.

Apply this with Q=P-hat_{n,rho} and P=P_{N,rho}. On G, the embedding identity from Section 1 gives

||E_N pi-hat_{n,rho}-E_N pi_{N,rho}||_1 <= N(1-rho)epsilon/rho.

## 4. Noiseless-Density Radius

Restore the regime label s. On G_s, insert the regularized population density, the partition density, and the observed density into the triangle inequality:

||E_N pi-hat_{n_s,rho}^{(s)}-h_s||_1
<= ||E_N pi-hat_{n_s,rho}^{(s)}-E_N pi_{N,rho}^{(s)}||_1
 + ||E_N pi_{N,rho}^{(s)}-h_{N,s}||_1
 + ||h_{N,s}-h_{delta,s}||_1
 + ||h_{delta,s}-h_s||_1
<= N(1-rho)epsilon/rho + zeta_{N,s}(rho) + C_A Delta_N^beta + eta(delta)
= r_s(epsilon).

The second term is the definition of zeta. The third uses the explicit identification h_{N,s}=Pi_N h_{delta,s} and the partition bound. The last uses noise stability. Thus

{||E_N pi-hat_{n_s,rho}^{(s)}-h_s||_1>r_s(epsilon)} is contained in G_s^c,

which proves the single-window probability bound, including n_s=1.

For completeness, the source's fixed-N regularization-bias limit requires no additional public hypothesis beyond the unique stationary distribution already assumed. If rho_j tends to zero, any convergent subsequence of pi_{N,rho_j} has a probability-vector limit v. Passing to the limit in pi_{N,rho_j}P_{N,rho_j}=pi_{N,rho_j} gives vP_N=v, so uniqueness implies v=pi_N. Compactness of the finite-dimensional probability simplex then implies pi_{N,rho}->pi_N, and the embedding identity gives zeta_N(rho)->0. This observation checks the inherited source assumption; it is not an additional target.

## 5. False Alarms and Detection

Let A_s be the event that the density-estimation error in regime s is at most r_s(epsilon). The previous section proves P(A_s^c)<=B_s(epsilon). No independence between the two segments is required.

The embedding identity gives

S_t=||E_N pi-hat_{n_t,rho}^{(t)}-E_N pi-hat_{n_0,rho}^{(0)}||_1.

If h_t=h_0, then on A_0 intersect A_t the triangle inequality implies

S_t <= ||E_N pi-hat_{n_t,rho}^{(t)}-h_t||_1
       + ||E_N pi-hat_{n_0,rho}^{(0)}-h_0||_1
    <= r_t(epsilon)+r_0(epsilon)=tau_t(epsilon).

Therefore {S_t>tau_t(epsilon)} is contained in A_0^c union A_t^c, and its probability is at most B_0(epsilon)+B_t(epsilon).

If ||h_t-h_0||_1>2tau_t(epsilon), then on A_0 intersect A_t the reverse triangle inequality gives

S_t >= ||h_t-h_0||_1-r_t(epsilon)-r_0(epsilon) > tau_t(epsilon).

Hence the detection event contains A_0 intersect A_t, and

P(S_t>tau_t(epsilon)) >= P(A_0 intersect A_t) >= 1-B_0(epsilon)-B_t(epsilon).

The strict separation assumption supplies the strict threshold crossing. Bounds above one or below zero are simply uninformative probability bounds. N=1 is covered throughout; no argument divides by N-1. The endpoints rho=0 and rho=1 are excluded by the task, and delta=0 introduces no division or exceptional step. All proof obligations are closed.
