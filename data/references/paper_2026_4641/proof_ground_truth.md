# Reference Proof

## Contract and obligations

The task concerns exact finite-width trajectories from a duplicated initialization, not an infinite-width limit or a noisy mid-training intervention. The optimizer acts on one normalized variable A_W=W/n_in for each matrix, with all its forward and transpose occurrences sharing that variable. Vector and scalar optimizer variables are unnormalized. The only randomness relevant here is the shared realization of training data and losses.

We must establish: (1) forward replication for all three operations; (2) the reverse-mode normalization, including scalar dependencies and arbitrary OuterNonlin orders; (3) total parameter-gradient relations, including shared matrices used in both orientations and the loss chain rule; (4) both decay updates with the complete gradient history and auxiliary-parameter scaling; and (5) induction over every training step. All five obligations are derived below.

## 1. Forward replication

Write R_u for vector replication on width axis u and R_W for replication of a matrix's two axes. Suppose the raw parameters are related by replication, and evaluate the two programs on the same external input. Initial scalars agree and initial vectors and matrices are replicated.

For Avg on a width-d vector x with multiplier k,
\[
\frac1{kd}\sum_{i=1}^{d}\sum_{a=1}^{k}(R x)_{(i,a)}
=\frac1d\sum_{i=1}^{d}x_i.
\]

For z=Wh/b, where W has a rows and b columns, each output coordinate satisfies
\[
z^{\rm up}_{(i,c)}
=\frac1{k_{\rm in}b}\sum_{j=1}^{b}\sum_{e=1}^{k_{\rm in}}W_{ij}h_j
=z_i.
\]
For z=W^{\mathsf T}h/a, the analogous calculation sums k_out copies of each input coordinate and divides by k_out a, again giving the replicated base output. These calculations apply to every occurrence of a shared matrix.

For OuterNonlin on a width-d axis, each base r-tuple of averaged indices has exactly k^r widened copies. All arguments of psi at corresponding tuples agree by induction, including the scalar arguments. Consequently,
\[
z^{\rm up}_{(i,c)}
=\frac{k^r}{(kd)^r}\sum_{\beta_1,\ldots,\beta_r=1}^{d}
\psi(X_i;X_{\beta_1};\ldots;X_{\beta_r};c)
=z_i.
\]
For r=0 there is no averaged index and the same assertion follows directly from equality of the arguments.

Induction through the finite program proves equality of every scalar and replication of every vector. The final Avg therefore gives equal outputs for every external input whenever the raw parameters are replicated.

## 2. Normalized reverse-mode quantities

Fix one input and let F be its scalar model output. Include its final Avg as the last operation. For a vector v of dimension d_v, define its normalized reverse sensitivity
\[
a_v=d_v\frac{\partial F}{\partial v};
\]
for a scalar c, define
\[
b_c=\frac{\partial F}{\partial c}.
\]
These are computational-graph sensitivities: each node receives the sum of contributions through its uses. Seed the final scalar with sensitivity 1 and unused nodes with zero. The vector entering the terminal Avg therefore has a direct normalized contribution equal to the all-ones vector. Ordinary vector sensitivities are a_v/d_v; they are not themselves unscaled replicated vectors.

We derive every local reverse rule by the finite-dimensional chain rule.

**Avg.** For c=Avg(v), the contribution to a_v is b_c times the all-ones vector.

**Forward matrix multiplication.** For z=Wh/b with d_h=b and d_z=a,
\[
a_h\mathrel{+}=b\frac1b W^{\mathsf T}\frac{a_z}{a}
=\frac1a W^{\mathsf T}a_z.
\]
This is a scaled transpose MatMul.

**Transpose matrix multiplication.** For z=W^{\mathsf T}h/a with d_h=a and d_z=b,
\[
a_h\mathrel{+}=a\frac1a W\frac{a_z}{b}
=\frac1b Wa_z.
\]
This is a scaled forward MatMul.

**OuterNonlin.** Consider
\[
z_{\beta_0}=d^{-r}\sum_{\beta_1,\ldots,\beta_r}
\psi(X_{\beta_0};\ldots;X_{\beta_r};c).
\]
Let psi_{j,p} denote the derivative with respect to component p in vector slot j, where j=0,...,r, and let psi_{c_l} denote the derivative with respect to scalar c_l. The contribution to the normalized sensitivity of the p-th input vector at coordinate alpha is
\[
(a_{x^p})_\alpha\mathrel{+}=
\sum_{j=0}^{r}\frac1{d^r}
\sum_{\substack{\beta_i\in[d]\ (i\ne j)\\ \beta_j=\alpha}}
(a_z)_{\beta_0}\,
\psi_{j,p}(X_{\beta_0};\ldots;X_{\beta_r};c).
\]
The scalar contribution is
\[
b_{c_l}\mathrel{+}=\frac1{d^{r+1}}
\sum_{\beta_0,\ldots,\beta_r=1}^{d}
(a_z)_{\beta_0}\,
\psi_{c_l}(X_{\beta_0};\ldots;X_{\beta_r};c).
\]
The first formula sums over r free indices in each slot contribution; the second sums over r+1 free indices. They follow by substituting partial F/partial z_beta0=(a_z)_beta0/d into the ordinary chain rule and, for the vector input, multiplying by d. When several slots involve the same coordinate, their derivative contributions must all be included; the displayed sum does so. The formulas also cover r=0 and empty scalar or vector argument lists.

We now induct backward. The seeds agree or are replicated. The Avg rule preserves this property. The two matrix reverse rules preserve it by the scaled MatMul calculation in Section 1. In an OuterNonlin vector contribution, every free-index tuple has k^r copies, canceled by the widened denominator (kd)^r. In a scalar contribution the count is k^(r+1), canceled by (kd)^(r+1). Derivatives of psi at corresponding argument tuples agree because the same differentiable function is evaluated at equal arguments. Finally, summing contributions over uses preserves equality and replication. Thus
\[
a_v^{\rm up}=R_v a_v,
\qquad b_c^{\rm up}=b_c.
\]
This explicitly proves the reverse-mode property; no external automatic-backpropagation theorem is needed.

## 3. Parameter gradients and loss composition

For one model output F, consider a raw matrix W with a=n_out and b=n_in. Its complete raw derivative is
\[
\frac{\partial F}{\partial W}
=\frac1{ab}\left(
\sum_{z=Wh/b}a_z h^{\mathsf T}
+\sum_{z=W^{\mathsf T}h/a}h a_z^{\mathsf T}
\right).
\]
Both sums range over all occurrences of this same matrix in the program. For the first kind of occurrence, the factor is (1/b)(1/a); for the second it is (1/a)(1/b). The earlier reverse sensitivities already include all downstream paths, so this formula also covers repeated and tied use.

The corresponding raw vector and scalar derivatives are
\[
\frac{\partial F}{\partial u}=\frac{a_u}{n_u},
\qquad
\frac{\partial F}{\partial c}=b_c.
\]
The forward and reverse replication results imply
\[
\left(\frac{\partial F}{\partial W}\right)^{\rm up}
=\frac1{k_{\rm out}k_{\rm in}}R_W\left(\frac{\partial F}{\partial W}\right),
\quad
\left(\frac{\partial F}{\partial u}\right)^{\rm up}
=\frac1{k_u}R_u\left(\frac{\partial F}{\partial u}\right),
\quad
\left(\frac{\partial F}{\partial c}\right)^{\rm up}
=\frac{\partial F}{\partial c}.
\]

For a training batch, put F_b=f_n(xi_{t,b};Theta_t) and eta_b=partial_b ell_t(F_1,...,F_B). Equal forward outputs and a common loss imply equal eta_b in the two runs. For every raw parameter P,
\[
H_{P,t}:=\nabla_P\mathcal L_{n,t}
=\sum_{b=1}^{B_t}\eta_b\nabla_P F_b.
\]
In particular, the scalar gradient is the loss-weighted sum of its output sensitivities, not the unweighted sum. The same gradient replication relations therefore hold for H:
\[
H_{W,t}^{\rm up}=\frac1{k_{\rm out}k_{\rm in}}R_W H_{W,t},
\qquad H_{u,t}^{\rm up}=\frac1{k_u}R_u H_{u,t},
\qquad H_{c,t}^{\rm up}=H_{c,t}.
\]

For the actual matrix optimizer variable A_W=W/b, the chain rule gives
\[
G_{A_W,t}=bH_{W,t}.
\]
This differentiates every use of W, including its transpose. Consequently,
\[
A_W^{\rm up}=\frac1{k_{\rm in}}R_W A_W,
\qquad
G_{A_W,t}^{\rm up}=\frac1{k_{\rm out}}R_W G_{A_W,t}.
\]
The product-of-two-widths normalization belongs to the raw gradient H_W, not to G_{A_W}.

## 4. Optimizer updates

Fix a tensor and suppress its tensor-specific base-constant subscripts. All applications of homogeneity below use positive widths and scale the auxiliary vector together with the whole gradient history.

### Matrix parameters

Write a=n_out and b=n_in. In the coupled convention, applying the optimizer to A_W=W/b and multiplying the update by b gives
\[
W_{t+1}
=W_t-a^m\bar\gamma\,
Q_t\big((bH_{W,j}+a^{-1}\bar\lambda W_j)_{j=0}^{t};a^{-1}\bar\epsilon\big).
\]
Every argument inside Q_t is a^(-1) times the corresponding argument in the following expression, so joint homogeneity yields
\[
W_{t+1}
=W_t-\bar\gamma\,
Q_t\big((abH_{W,j}+\bar\lambda W_j)_{j=0}^{t};\bar\epsilon\big).
\tag{M-C}
\]
This uses decay on W_j/b before conversion to raw coordinates.

For decoupled decay,
\[
\gamma\lambda
=(a^m b^{-1}\bar\gamma)(ba^{-m}\bar\lambda)
=\bar\gamma\bar\lambda.
\]
The same homogeneity calculation, now without decay inside Q_t, gives
\[
W_{t+1}
=(1-\bar\gamma\bar\lambda)W_t
-\bar\gamma Q_t\big((abH_{W,j})_{j=0}^{t};\bar\epsilon\big).
\tag{M-D}
\]
Multiplicative decay acts only on W_t, not on the filtered-gradient term.

At widened dimensions A=k_out a and B=k_in b, the identical formulas hold with ABH_W^up in place of abH_W. Section 3 gives ABH_W,j^up=R_W(abH_W,j). If all raw weights through step t are replicated, every argument of each entrywise filter in (M-C) or (M-D) is therefore identical at corresponding entries. The widened raw matrix update is the replication of the base update.

### Vector parameters

For a vector u of width d, direct substitution gives in the coupled convention
\[
u_{t+1}
=u_t-d^m\bar\gamma Q_t\big((H_{u,j}+d^{-1}\bar\lambda u_j)_{j=0}^{t};d^{-1}\bar\epsilon\big)
=u_t-\bar\gamma Q_t\big((dH_{u,j}+\bar\lambda u_j)_{j=0}^{t};\bar\epsilon\big).
\tag{V-C}
\]
For decoupled decay it gives
\[
u_{t+1}
=(1-\bar\gamma\bar\lambda)u_t
-\bar\gamma Q_t\big((dH_{u,j})_{j=0}^{t};\bar\epsilon\big).
\tag{V-D}
\]
Because D H_u,j^up=R_u(dH_u,j) at D=k_u d, both vector updates preserve replication of the whole history.

### Scalar parameters

For a scalar c the updates are
\[
c_{t+1}=c_t-\bar\gamma Q_t\big((H_{c,j}+\bar\lambda c_j)_{j=0}^{t};\bar\epsilon\big)
\]
for coupled decay, and
\[
c_{t+1}=(1-\bar\gamma\bar\lambda)c_t
-\bar\gamma Q_t\big((H_{c,j})_{j=0}^{t};\bar\epsilon\big)
\]
for decoupled decay. Equal scalar parameters and loss gradients give equal scalar updates.

## 5. Training-time induction and boundary cases

At step zero the raw parameter relation holds by construction. Suppose it holds at every step j<=t. Applying Sections 1-3 at each of those steps gives the required relations for every stored gradient. Section 4 then gives the raw parameter relation at t+1 in either decay convention. Strong induction establishes it for every nonnegative training step.

Applying Section 1 to these parameters at any external input xi proves
\[
f_n(\xi;\Theta_t)=f_N(\xi;\Theta_t^{\rm up})
\]
for every t and xi.

No step divides by a learning rate, decay coefficient, gradient, or optimizer output. Thus zero gradients, zero learning rates or decay, unit widths, unit widening factors, unused parameters, and missing parameter classes cause no exception. Widths are strictly positive, so all width normalizations and real powers used in the proof are defined. Empty auxiliary vectors and r=0 are covered by their stated conventions. Every theorem-critical obligation has been discharged by finite sums, the chain rule, homogeneity, and induction.

## Source-local corrections incorporated

The normalized reverse rules above implement the dimension ratios required by L000414; L000497 already gives the correct scaled MatMul rule. The scalar loss derivative missing at L000547 is restored in the loss-composition formula. The vector multiplier at L000549 is k_u, and every unscaled vector-gradient history entry before the homogeneity step is du_j, correcting L000565-L000566. Raw and normalized matrix gradients are distinguished exactly as required by L000539 and L000551. The homogeneity law is read with positive scale factors, consistently with the positive-epsilon adaptive example and all width rescalings. These local corrections require no new proof mechanism and leave no unresolved reference-proof obligation.
