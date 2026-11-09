# Reference Proof

## Proof Structure

Work under the conditional law given F=0 and retain the reference pool in the filtration. Prove rank calibration using order statistics and countably valued thresholds approaching the relevant order statistic from above. Then prove the predictable betting bound by a conditional finite-support layer-cake argument, verify adaptedness and integrability of the product, and apply Ville's inequality to an event containing finite-horizon release.

## Complete Proof

Write P_0=P(·|F=0) and E_0 for expectation under this law; when referring to the initial process value, write E_{t=0}=1. Fix t and let B=A_{t-1}. All conditional expectations in the proof are under P_0. Define N(s)=sum_{i=1}^n 1{R_i>=s}.

### 1. Conditional rank calibration

For every deterministic rational q, dominance gives

P_0(S_t>=q | B)<=N(q)/n.

These inequalities hold simultaneously outside one null set because the rational thresholds are countable. In particular, they extend to any B-measurable, countably valued rational threshold Q. Indeed, partitioning by its values and using conditional expectation gives

P_0(S_t>=Q | B)
= sum_{q in Q} 1{Q=q} P_0(S_t>=q | B)
<= sum_{q in Q} 1{Q=q} N(q)/n
= N(Q)/n,

where the sums range over the rational numbers. The identity follows first for finite partial sums and then by conditional monotone convergence.

Fix u in [0,1]. If u<1/(n+1), the event p_t<=u is empty. If u=1, the desired bound is immediate. Otherwise set

k=floor((n+1)u-1),

so 0<=k<=n-1. Order the reference scores as R_[1]>=...>=R_[n], retaining all multiplicities. These order statistics are B-measurable. On {p_t<=u}, the integer N(S_t) is at most k. If S_t<=R_[k+1], however, at least k+1 reference scores are at least S_t. Thus

{p_t<=u} is contained in {S_t>R_[k+1]}.

Put a=R_[k+1] and, for m>=1, define

Q_m=2^(-m)(floor(2^m a)+1).

Each Q_m is B-measurable and countably valued in the rationals. Moreover, Q_m>a and Q_m decreases to a. Since at most k reference scores can be at least Q_m, N(Q_m)<=k. The countably valued threshold argument therefore yields

P_0(S_t>=Q_m | B)<=k/n.

The events {S_t>=Q_m} increase to {S_t>a}. Conditional monotone convergence now gives

P_0(p_t<=u | B)<=P_0(S_t>a | B)<=k/n.

Finally,

k/n<=((n+1)u-1)/n=u+(u-1)/n<=u.

This proves the stated conditional super-uniformity, including all ties and endpoints. The same argument works for every t.

### 2. Predictable betting bound and measurability

Let v_j=j/(n+1), j=1,...,n+1. The statistic p_t is A_t-measurable and takes values in this finite set. Consequently,

f_t(p_t)=sum_{j=1}^{n+1} f_t(v_j) 1{p_t=v_j}

is A_t-measurable by the stated pointwise predictability. No additional joint measurability assumption on the whole random function is needed.

Let h_j=P_0(p_t=v_j | B). Choose versions simultaneously for these finitely many conditional probabilities. Outside one null set they are nonnegative, sum to one, and satisfy

sum_{i=1}^j h_i=P_0(p_t<=v_j | B)<=v_j

for every j. These inequalities follow from the rank-calibration result.

Fix an outcome outside this null set and one on which the betting normalization holds. For this paragraph write g(v)=f_t(v) for its realized nonincreasing function. For y>=0 let

a_y=Lebesgue measure of {v in [0,1]:g(v)>y}.

Every v with g(v)>y satisfies v<=a_y: monotonicity implies that the level set contains [0,v], whose length is v. Therefore

sum_{j=1}^{n+1} h_j 1{g(v_j)>y}
<=sum_{j:v_j<=a_y} h_j
<=a_y.

For the last inequality, if the sum is nonempty, let j_* be its largest index. Its value is at most v_{j_*} by the simultaneous finite-grid bounds, and v_{j_*}<=a_y. If the sum is empty, it is zero.

Integrating in y and using the layer-cake identity gives

sum_{j=1}^{n+1} h_j g(v_j)
<= integral_0^infinity a_y dy
= integral_0^1 g(v) dv
<=1.

The equality is Tonelli's theorem applied to the nonnegative measurable function 1{g(v)>y}; g is Borel measurable because it is monotone. All this integration is for a fixed realized g, so it does not presume unprovided joint measurability across outcomes.

Returning to conditional expectations, the finite-support expansion and B-measurability of each f_t(v_j) give

E_0[f_t(p_t) | B]=sum_{j=1}^{n+1} f_t(v_j)h_j<=1.

There is also a direct integrability check. For v>0, monotonicity and normalization imply

v f_t(v)<=integral_0^v f_t(w) dw<=1.

Since p_t>=1/(n+1), we have 0<=f_t(p_t)<=n+1 almost surely. Hence E_t is nonnegative, adapted, and bounded above by (n+1)^t almost surely for each fixed t; in particular, it is integrable.

### 3. Product supermartingale

Because E_{t-1} is A_{t-1}-measurable and nonnegative,

E_0[E_t | A_{t-1}]
=E_{t-1} E_0[f_t(p_t) | A_{t-1}]
<=E_{t-1}.

Together with the preceding adaptedness and integrability checks and E_{t=0}=1, this proves that (E_t) is a nonnegative supermartingale under P_0.

### 4. Release control

The crossing time is a stopping time because

{tau_alpha<=T}=union_{t=1}^T {E_t>=1/alpha}

belongs to A_T. By the definition of D,

{D=1}={tau_alpha<=T_max}
is contained in {tau_alpha<infinity},
which is contained in {sup_{t>=1} E_t>=1/alpha}.

Only containment is used: an infinite supremum need not be attained at a finite time.

The audited standard Ville inequality states that a nonnegative adapted supermartingale starting at one under a probability law satisfies

P(sup_{t>=1} E_t>=1/alpha)<=alpha

for alpha in (0,1). Every hypothesis has just been verified under P_0. Applying it yields

P(D=1 | F=0)=P_0(D=1)<=alpha.

The reference pool remains in the conditioning filtration throughout. P_0 already includes its randomness, so no additional independence assumption or conditioning theorem is needed.

## Obligation Closure and Source Note

The proof explicitly closes random-threshold calibration, ties and endpoint cases, evaluation measurability, the predictable betting expectation bound, adaptedness, integrability, initialization, and the release-event comparison. The only specialized named result used without derivation is the stated standard-independent Ville inequality, whose hypotheses are verified. No nonstandard dependency remains unresolved.

The source proof at L001189-L001191 incorrectly identifies finite-time threshold attainment with an infinite supremum event. The containment used above is the recorded local repair for theory_011. It changes neither the theorem nor its proof route.
