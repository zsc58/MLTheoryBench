# Reference Proof

## Proof Structure

1. Express the fixed noiseless projection as a weighted sum of independent standardized sources.
2. Establish nondegeneracy and variance normalization.
3. Expand the fourth moment, obtain the weighted kurtosis identity, and apply balance.
4. Verify the equality case and genuine order sharpness.
5. Identify the sampling bound as an explicit hypothesis, not a conclusion from moments alone.
6. Derive both necessary screening conditions, including their boundary cases.

## Complete Proof

### 1. Projection representation

Write b_j=a_j^T u. The assumed positivity of sum_j b_j^2 implies that J={j:b_j!=0} is nonempty, so q>=1. Since x=As, we have u^T x=sum_j b_j s_j.

### 2. Normalization and moments

Independence, zero means, and unit variances imply

Var(u^T x)=sum_j b_j^2>0.

Consequently y=sum_{j in J} alpha_j s_j, where alpha_j=b_j/(sum_l b_l^2)^{1/2}. In particular E[y]=0 and sum_{j in J} alpha_j^2=Var(y)=1. Its fourth moment is finite because it is a finite linear combination of variables with finite fourth moments. All subsequent sums are over J unless indicated otherwise.

### 3. Fourth-moment identity and balance

In the expansion of E[(sum_j alpha_j s_j)^4], any term with an index occurring exactly once vanishes by independence and the zero mean of that source. The remaining terms have either one index repeated four times or two distinct indices each repeated twice. Thus

E[y^4]=sum_j alpha_j^4 E[s_j^4]+6 sum_{i<j} alpha_i^2 alpha_j^2.

Also,

3=3(sum_j alpha_j^2)^2=3 sum_j alpha_j^4+6 sum_{i<j} alpha_i^2 alpha_j^2.

Subtracting gives

K(y)=sum_j alpha_j^4(E[s_j^4]-3)=sum_j alpha_j^4 K(s_j).

This derivation uses only the independence, centering, unit variances, and finite fourth moments already stated. It is also the fourth-cumulant identity for these centered standardized variables.

Taking absolute values yields

|K(y)|<=K_max sum_j |alpha_j|^4.

By normalization and balance,

sum_j |alpha_j|^4 <= (max_j |alpha_j|^2) sum_j |alpha_j|^2 <= beta/q.

Therefore |K(y)|<=beta K_max/q.

### 4. Equality and sharpness

If alpha_j^2=1/q and K(s_j)=K_0 for every active index, the identity above gives

K(y)=sum_j q^{-2}K_0=K_0/q.

For genuine nonzero order sharpness, for every positive integer q take independent sources with probabilities 1/2 at each of -1 and 1. They are centered, have unit variance, have moments of every order, and satisfy K(s_j)=1-3=-2. Taking A=I_q and u=(1,...,1)^T gives alpha_j=1/sqrt(q), balance with beta=1, and |K(y)|=2/q. Thus the 1/q dependence cannot be replaced by a smaller order uniformly over the admissible class, even with beta and K_max fixed. The equality formula also remains valid when K_0=0, although that case alone does not witness sharpness.

### 5. Sampling hypothesis

For the sampling comparison, finite eighth source moments imply E[|y|^8]<infinity. For example,

|sum_j alpha_j s_j|^8 <= q^7 sum_j |alpha_j s_j|^8,

whose expectation is finite. The statistic hat K_n=g_n(Y_1,...,Y_n) is measurable and square-integrable by hypothesis. Its bound std(hat K_n)<=tau/sqrt(n) is separately assumed. No finite-sample bound for an unspecified sample-kurtosis ratio, and no asymptotic-to-finite-sample inference, is needed or claimed.

### 6. Screening and boundary cases

If |K(y)|>tau/sqrt(n), the population bound implies

beta K_max/q >= |K(y)| > tau/sqrt(n).

Since q, tau, and n are positive, rearrangement gives

q < beta K_max sqrt(n)/tau.

If |K(y)|>=theta>0, then

beta K_max/q >= |K(y)| >= theta,

and hence q<=beta K_max/theta. This second implication requires only the population assumptions, not the sampling assumptions.

If K_max=0, the proved bound gives K(y)=0, so neither positive-contrast antecedent holds. No division by K_max is used. The argument includes q=1. Normalization implies max_j alpha_j^2>=1/q, so a projection satisfying the balance condition necessarily has beta>=1; beta<1 simply admits no balanced projection. Both screening inequalities are necessary conditions only. In particular, an upper bound on standard deviation is not a lower bound on actual estimation noise, and no statistical detection or algorithmic success guarantee follows.
