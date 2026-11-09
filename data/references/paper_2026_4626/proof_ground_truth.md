# Reference Proof

## Audit Status and Ambient Contract

This reference concerns a confidence-tuned strategy: T and δ are supplied before play. Its distributions must be chosen before the current loss is revealed. The adversary may adapt to the announced distribution and all previous observations, but not to the fresh current action draw. Loss revelation is full information, not bandit feedback. Neither smoothness nor any regularity of a loss's representing probability measure is assumed; atoms and endpoint masses are allowed.

The proof reconstructs the source's geometric, concentration, minimax, and implementation arguments, retaining the previously recorded local source repairs. It also supplies an explicit elementary constraint-weighting algorithm in Step 6. This algorithm replaces the reference's former reliance on an unproved specialized expert guarantee. Its guarantee is proved for the reward sequences produced by the LP construction, where weighted reward is nonpositive on every round. We neither assume nor claim to prove the stronger standalone MsMwC theorem for arbitrary reward sequences. No inference in this proof depends on that unproved general theorem.

Write A=ln T, L=ln(1/δ), and γ=sqrt(AL/T). Thus L≥A and Tγ=sqrt(TAL). For every realized interaction, 0≤SR_T≤T: the identity comparator gives zero, and Lipschitzness bounds each regret difference above by 1. If γ>1, any strategy already gives SR_T≤T<Tγ. The case T=2 is also covered by the deterministic bound after increasing the universal constant. The substantive construction can therefore be analyzed for T>2 and 0<γ≤1. All constants below are absolute.

## Step 1. Loss Representation and Comparator Semantics

For a convex 1-Lipschitz loss ℓ, choose its right-continuous, nondecreasing right derivative g on [0,1), with values in [-1,1], and set g(1)=1. This endpoint choice is a valid subgradient on the restricted domain. Set F(q)=(g(q)+1)/2 for q in [0,1], extend F by 0 below 0 and by 1 above 1, and let φ be the probability measure with this CDF. In particular, possible masses at 0 and 1 are retained. An arbitrary monotone subgradient without the right-continuity and endpoint specifications is not by itself a complete CDF construction.

Using bounded integrands and integrating the derivative gives

Eφ|p-v| = ∫_0^p F(q)dq + ∫_p^1(1-F(q))dq
         = ℓ(p)+(1-ℓ(0)-ℓ(1))/2.

Hence ℓ(p)=Eφ|p-v|+Cℓ, where Cℓ=(ℓ(0)+ℓ(1)-1)/2. All additive constants cancel from regret differences. When averaging random losses, first subtract each loss's own value at 0; the resulting functions are bounded by 1 in absolute value. No integrability assumption on random additive offsets is needed.

The source allows arbitrary comparator maps, whereas the task uses Borel-measurable maps. This does not change finite-horizon swap regret: any assignment on the finitely many distinct realized predictions extends to a Borel map. Continuity and compactness ensure that the optimal replacement for each such prediction exists. These observations also express swap regret through finitely many continuous minimizations, so the random quantity is measurable under the stated measurable strategies.

If predictions carry labels j=(r,b), several labels may have the same numerical prediction b. For n_j>0, let φhat_j be the average of the representing measures of the losses on rounds carrying label j, and let s_j be a median of φhat_j. Splitting an action group into separate labels relaxes the comparator constraint. Therefore

SR_T ≤ Σ_{j:n_j>0} n_j E_{φhat_j}[|b-v|-|s_j-v|].

This is an inequality when different labels share b. Empty groups contribute zero; no empirical probability measure or median is defined for an empty group.

## Step 2. Quantile Width and the Actual Grids

For z in [0,1], define Qφ(z)={q in [0,1]: φ([0,q))≤z≤φ([0,q])}. These are nonempty compact intervals, including the possible endpoint intervals at z=0 and z=1. For interior z, existence follows by taking the infimum of the points at which the CDF reaches z; continuity of probability from above and below verifies membership. The same continuity proves closedness. Monotonicity gives interval convexity. If z<z', every point of Qφ(z) is at most every point of Qφ(z'): otherwise φ([0,q))≥φ([0,q'])≥z'>z would contradict the lower-level quantile condition.

The endpoint identities are

max Qφ(z)=1 if z=1, and otherwise inf_{z'>z} min Qφ(z');
min Qφ(z)=0 if z=0, and otherwise sup_{z'<z} max Qφ(z').

For example, the decreasing limit of the minimum quantiles at levels z'>z belongs to Qφ(z), by continuity of probability, and is at least every element of Qφ(z) by the ordering just proved. This proves the maximum identity; the minimum identity is symmetric. These elementary derivations supply the proof of the quantile facts stated without a separate proof in the source.

For w in [γ,1], put S(w)=Qφ(1/2+γ/(2w))-Qφ(1/2-γ/(2w)), where the set difference means all differences of one element from each set. It is a nonempty compact interval contained in [0,1]. Its endpoint identities are

max S(γ)=1;
max S(w)=inf_{γ≤u<w} min S(u), for w>γ;
min S(w)=sup_{w<u≤1} max S(u), for w<1.

They follow by applying the preceding quantile identities to the two levels. Also, if u<w then min S(u)≥max S(w).

Let W={w in [γ,1]: w≤max S(w)}. It contains γ and is downward closed. Set w*=sup W. Taking a limit from W and using the left endpoint identity gives w*≤max S(w*); the endpoint case w*=γ is immediate. If w*<1, all w>w* satisfy w>max S(w), and the right endpoint identity gives w*≥min S(w*); if w*=1 this is immediate. Thus w* belongs to S(w*). If w<w*, then w<w*≤max S(w*)≤min S(w), so w is not in S(w). If w>w*, it is not in W and therefore not in S(w). This proves existence and uniqueness, including γ=1.

Use exactly the source grids

R={γ,2γ,4γ,...}∩[0,1],
B_r={0,r,2r,...}∩[0,1],
Θ={(r,b): r∈R, b∈B_r}, and B=∪_r B_r.

The spacing at scale r is r, not rγ/log T. There are O(log T) scales and N=|Θ|=O(1/γ)=O(sqrt T) labels, since γ≥ln(T)/sqrt(T).

For a measure φ, choose α and β from the two quantile sets at its γ-width w, with β-α=w. Choose the unique r∈R satisfying r≤w<2r, and a grid point b∈B_r∩[α,β]. Such a point exists because the interval has length at least r. Ties can be settled measurably, for example by taking the smallest permissible α and then the smallest permissible grid point. No additional randomized tie-handling construction is needed.

This pair satisfies all four inequalities

φ(v>b+2r) ≤ 1/2-γ/(4r),
φ(v<b-2r) ≤ 1/2-γ/(4r),
φ(v≥b) ≥ 1/2-γ/(2r),
φ(v≤b) ≥ 1/2-γ/(2r).

Indeed b+2r≥β and b-2r≤α. The outer-tail bounds follow from φ(v>β)≤1/2-γ/(2w) and φ(v<α)≤1/2-γ/(2w). For the central tails use φ(v≥b)≥φ(v≥β)≥1/2-γ/(2w) and φ(v≤b)≥φ(v≤α)≥1/2-γ/(2w). The weak inequalities at β and α are essential when φ has atoms.

## Step 3. Median Inequality and the Quantitative Heavy/Light Bound

If s is a median of φ and b>s, pointwise comparison at b gives

Eφ[|b-v|-|s-v|] ≤ (b-s)(1-2φ(v≥b)).

Pointwise comparison at s gives the lower bound (b-s)(2φ(v≤s)-1)≥0. The case b<s is symmetric, using φ(v≤b) for the upper bound; b=s is immediate. Thus

0≤Eφ[|b-v|-|s-v|]≤|b-s|(1-2φ(s<b≤v or v≤b<s)).

Suppose that, for each nonempty label j=(r,b), its empirical measure satisfies the four inequalities of Step 2 with an added error D sqrt(L/n_j): add this error to the two upper bounds and subtract it from the two lower bounds. Here D is an absolute constant.

Call j heavy when n_j≥KTr²/A, where K is a sufficiently large absolute constant. Since L=Tγ²/A,

sqrt(L/n_j)≤γ/(r sqrt K).

For K large enough, both outer tails are at most 1/2. Therefore an empirical median can be chosen within distance 2r of b, after clipping to [0,1]. Both central tails are at least 1/2-O(γ/r), not at most that quantity. The median inequality then gives empirical excess loss O(γ), and the label contributes O(γ n_j).

For a nonempty light label, γ/r≤sqrt K sqrt(L/n_j). Its central tails are consequently at least 1/2-O(sqrt(L/n_j)). An arbitrary empirical median is at distance at most 1, so its regret contribution is

O(sqrt(n_j L)) ≤ O(sqrt((Tr²/A)(Tγ²/A))) = O(Trγ/A).

This light-label estimate comes from central-tail control and the median inequality. It does not follow by multiplying the count by a purported bin width, since the comparator's optimal replacement need not lie in the prediction's grid cell.

Summing heavy contributions gives O(Tγ). Since |B_r|≤2/r, the light contributions at each scale sum to O(Tγ/A). There are O(A) scales, so the total is O(Tγ).

## Step 4. The Order-Reversed Experiment and Uniform Concentration

In this experiment the adversary first announces a conditional distribution π_t of losses. Apply Step 1 to each possible loss and let φbar_t be the mixture of its representing measures. The truthful rule of Step 2 chooses its label before the actual loss is sampled. After sampling the loss, denote its representing measure by φ_t. Conditional on the information available when the label was chosen, E[φ_t(H)]=φbar_t(H) for each of the four relevant half-interval events H.

There is no need to sample or observe a V-location v_t. The bounded observations in this argument are probabilities φ_t(H), obtained from the sampled loss, not indicators of an additional observed outcome.

For a fixed label j and one such event H, let I_t indicate selection of j and put D_t=φ_t(H)-φbar_t(H). Selection is predictable before the current loss is sampled, |D_t|≤1, and its conditional mean is zero. The elementary bounded-difference exponential estimate gives

E exp(λ Σ_t I_t D_t - (λ²/2) Σ_t I_t) ≤ 1.

For completeness, conditional convexity of the exponential bounds the moment of a mean-zero variable in [-1,1] by cosh λ≤exp(λ²/2); iteration gives the displayed inequality. For every fixed n=1,...,T, applying Markov's inequality with λ=sqrt(2q/n), and also with -λ, bounds the probability that Σ I_t=n and |Σ I_tD_t|>sqrt(2nq) by 2 exp(-q). Choose q=ln(8NT/δ) and union bound over the four events, the N labels, and all n. The joint failure probability is at most δ. Since N=O(sqrt T) and δ≤1/T, q=O(L).

Dividing by each positive count and using the truthful four inequalities yields precisely the empirical inequalities required in Step 3. This proves the O(Tγ) high-probability bound for random convex losses in the order-reversed game, including adaptively selected loss distributions and random label counts. The corresponding success probability is 1-δ, not 1-1/δ.

## Step 5. Finite Minimax and a Correct Adaptive Discretization

This step supplies the nonconstructive route; it does not establish efficient computation of a full-game strategy. The efficient original-order proof is given separately in Steps 6–7.

Normalize losses at 0 and let Λ be the resulting family of convex 1-Lipschitz functions. It has finite uniform ε-nets consisting of functions in Λ. One direct construction is to record values on a sufficiently fine finite grid, quantize the bounded recorded values, and choose one actual function from each nonempty quantization cell. Lipschitzness then bounds the uniform distance between functions in the same cell.

Fix such a finite net Λ_ε and the finite prediction set B. Pure predictor and adversary plans on histories in B^{t-1}×Λ_ε^{t-1} form finite sets. For any mixed adversary plan, its conditional distribution of the next loss at each history is an admissible order-reversed distribution. The deterministic truthful response therefore has the bound from Step 4.

The audited standard finite minimax theorem states that, for a real payoff matrix with finite row and column sets, minimizing over row distributions and maximizing over columns has the same value as maximizing over column distributions and minimizing over rows. Applying it to terminal swap regret, with the truthful rule tuned to δ=1/T and the bound SR_T≤T, gives the expected-regret transfer. Applying it instead to the bounded payoff 1{SR_T>K Tγ}, with K supplied by Step 4 at the requested confidence δ, gives a finite-game strategy whose failure probability is at most δ. A high-probability transfer does not follow merely by applying minimax to expected swap regret.

The behavioral realization can be made explicit. At a finite history h, condition the mixed predictor plan on its having prescribed the predictor actions already recorded in h, and use the resulting conditional distribution of its next action. If the conditioning event has zero mass, assign any action law there. For a fixed adversary pure plan consistent with h, the event that h occurs imposes exactly these restrictions on the predictor plan; thus this conditional law does not depend on which consistent adversary plan is used. It consequently realizes the mixed predictor against every adversary plan. Its conditional action law is determined by the finite history, so announcing it supplies no additional current random draw. Responses to that law are covered by the finite-history adversary strategies.

To handle actual losses, run this finite-game learner on a virtual transcript: after each true loss is revealed, feed the learner its chosen ε-net representative for use in subsequent rounds. For every realized interaction, compare the true and rounded losses along this same realized action sequence. For every comparator map the total difference is at most 2εT, hence

SR_T(true losses) ≤ SR_T(rounded losses)+2εT.

The rounded losses, conditional on the finite history, form an admissible adaptive stochastic adversary for the finite game, even if the original adversary also remembers unrounded losses. The learner uses only the rounded history and fresh action randomness, so the necessary conditional sampling law is preserved. A stochastic finite-history adversary is covered as a mixture of deterministic plans: one may sample its prescribed action at each of the finitely many histories in advance according to its conditional kernel.

It is incorrect to compare an arbitrary history-dependent predictor against two different feedback sequences while assuming its actions remain the same. The virtual-transcript construction is the required correction to the appendix's pointwise claim. Taking a fixed ε=1/T adds only 2 to the bound, which is absorbed into O(Tγ) for T≥2; no unproved limiting strategy argument is needed. We also hold the prediction alphabet fixed: arbitrary perturbations of predictions can change equality groups in swap regret and are not the basis of this continuity argument.

## Step 6. Efficient Original-Order Construction

### Constraint functions and the per-round LP

For j=(r,b), write a for a label in Θ. Define four functions, zero unless a=j, by

h_{j,+2}(a,v)=1{a=j}(1{v>b+2r}-(1/2-γ/(4r))),
h_{j,-2}(a,v)=1{a=j}(1{v<b-2r}-(1/2-γ/(4r))),
h_{j,+1}(a,v)=1{a=j}((1/2-γ/(2r))-1{v≥b}),
h_{j,-1}(a,v)=1{a=j}((1/2-γ/(2r))-1{v≤b}).

They lie in [-1,1]. Step 2 proves that, for every probability measure φ, some pure label a makes Eφ h_{j,ξ}(a,v)≤0 simultaneously for every constraint. Constraints belonging to other labels are identically zero.

For any nonnegative weights w_{j,ξ} summing to 1, put hbar=Σ w_{j,ξ}h_{j,ξ}. The functions depend only on finitely many comparisons with b and b±2r. To preserve both strict and weak comparisons, take V to contain every threshold in [0,1], the endpoints, and one representative from each nonempty open interval between consecutive thresholds. Then |V|=O(N), and each v∈[0,1] has the same entire vector of constraint values as some point of V. Keeping only threshold points without the intervening cells is not sufficient in general.

For every distribution on V a pure label has nonpositive expected hbar. Finite minimax yields a distribution κ on Θ such that E_{a∼κ}hbar(a,v)≤0 for every v∈V, and thus for every v∈[0,1]. It is exactly the feasibility LP with variables κ(a)≥0, Σ_a κ(a)=1, and constraints Σ_a κ(a)hbar(a,v)≤0 for v∈V. Its numbers of variables and constraints are O(N), giving the source's polynomial-size, polynomial-time LP computation under the same arithmetic and loss-evaluation convention as its computational claim. Fix a deterministic measurable choice among feasible LP solutions.

### Explicit constraint weighting and its proved guarantee

Index the M=4N constraints by i, each corresponding to one (j,ξ). Let J=1+ceil(log_2 T) and η_k=2^{-(k+1)} for k=0,...,J-1. Thus every η_k is at most 1/2 and the smallest is at most 1/(2T). Initialize positive weights

q_{i,k}^{(1)}=1/(MJ).

Before the current loss is revealed, compute

D_t=Σ_{i,k} η_k q_{i,k}^{(t)},
w_i^{(t)}=(Σ_k η_k q_{i,k}^{(t)})/D_t.

These w_i^{(t)} form a probability vector. Use them in the preceding LP to compute κ_t. Announce the marginal distribution of b as μ_t. The adversary then reveals ℓ_t; only after it has committed to that loss draw a_t=(r_t,b_t) from κ_t and play X_t=b_t. This is exactly the required original-game order.

Define φ_t from the revealed loss and set

u_i^{(t)}=E_{a∼κ_t}E_{v∼φ_t}h_i(a,v).

After this reward vector is available, update

q_{i,k}^{(t+1)}=q_{i,k}^{(t)}(1+η_k u_i^{(t)}).

The distribution in the reward expectation is κ_t, not an undefined τ_t. The reward vector depends on κ_t and the current loss, not on the sampled label. It may be computed after the action draw. The weighting update takes O(MJ) arithmetic operations per round.

Here is a complete proof of the required guarantee. Since |u_i^{(t)}|≤1 and η_k≤1/2, every update factor lies in [1/2,3/2]. All q remain positive and D_t>0. Let Z_t=Σ_{i,k}q_{i,k}^{(t)}. The LP gives

Σ_i w_i^{(t)}u_i^{(t)}
 = E_{a∼κ_t}E_{v∼φ_t}hbar_t(a,v) ≤ 0.

Consequently, pathwise,

Z_{t+1}=Z_t+D_t Σ_i w_i^{(t)}u_i^{(t)}≤Z_t.

Since Z_1=1, each q_{i,k}^{(T+1)}≤1. Put B_0=ln(MJ), S_i=Σ_t u_i^{(t)}, and V_i=Σ_t(u_i^{(t)})². For x∈[-1/2,1/2],

ln(1+x)≥x-x².

Indeed f(x)=ln(1+x)-x+x² satisfies f(0)=0 and f'(x)=x(1+2x)/(1+x), which is nonpositive to the left of zero and nonnegative to its right on this interval. Therefore

0 ≥ ln q_{i,k}^{(T+1)}
  = -B_0+Σ_t ln(1+η_k u_i^{(t)})
  ≥ -B_0+η_k S_i-η_k² V_i.

For every i and every available rate,

S_i≤B_0/η_k+η_k V_i.

If V_i≤4B_0, choosing η_k=1/2 gives S_i≤4B_0. If V_i>4B_0, let η*=sqrt(B_0/V_i)<1/2. Since V_i≤T, B_0≥1, and the smallest rate is at most 1/(2T), the grid contains a rate η_k satisfying η*/2<η_k≤η*. Choosing it gives S_i≤3sqrt(B_0 V_i). In all cases,

S_i≤4B_0+3sqrt(B_0 V_i).

Here M=O(sqrt T) and J=O(log T), so B_0=O(A). This proves the needed individual squared-reward control simultaneously for every constraint. The proof is deterministic and permits each reward vector to adapt to the current weights; its essential condition is the nonpositive weighted reward supplied by the LP on that round. It is not a proof of a standalone external-regret theorem for arbitrary reward vectors, and no such stronger theorem is needed.

### From expected constraints to realized constraints

Let p_{t,j}=κ_t(j), E_j=Σ_t p_{t,j}, I_{t,j}=1{a_t=j}, and n_j=Σ_t I_{t,j}. Put a_{t,j,ξ}=E_{φ_t}h_{j,ξ}(j,v). Then |a_{t,j,ξ}|≤1 and

u_{j,ξ}^{(t)}=p_{t,j}a_{t,j,ξ},
Σ_t(u_{j,ξ}^{(t)})²≤Σ_t p_{t,j}²≤E_j.

The proved potential bound therefore gives

Σ_t u_{j,ξ}^{(t)} ≤ C[A+sqrt(A E_j)].

This is a one-sided inequality on a signed quantity; no absolute-value bound is claimed or needed.

Condition immediately before each label draw, including the revealed loss. The quantities (I_{t,j}-p_{t,j})a_{t,j,ξ} and I_{t,j}-p_{t,j} have conditional mean zero, absolute value at most 1, and conditional second moment at most p_{t,j}. They are martingale differences for the filtration that includes the current loss before its corresponding draw.

The audited standard Freedman bound used here is: if |D_t|≤1, E[D_t|F_{t-1}]=0, and V=Σ_t E[D_t²|F_{t-1}], then with probability at least 1-η,

|Σ_t D_t|≤C[sqrt(V ln(T/η))+ln(T/η)].

Apply it to all constraint and count processes and union bound. Because their number is polynomial in T and δ≤1/T, all logarithms are O(L). With probability at least 1-δ, simultaneously,

H_{j,ξ}:=Σ_t I_{t,j}a_{t,j,ξ} ≤ C[L+sqrt(E_j L)],
|n_j-E_j| ≤ C[L+sqrt(E_j L)].

The additive L in the count bound must be retained. Dropping it is unjustified for small E_j.

### Heavy and light labels in the original game

Call a label heavy when E_j≥KTr²/A, with K a sufficiently large absolute constant. Since r≥γ, this implies E_j≥K L. The count bound then gives E_j/2≤n_j≤2E_j. The constraint bound gives H_{j,ξ}/n_j≤C sqrt(L/n_j), and n_j≥KTr²/(2A). Expanding the four definitions of H yields the empirical tail inequalities used in Step 3, with sufficiently small outer-tail error relative to γ/r. The median argument gives regret contribution O(γ n_j).

For a light label, E_j<KTr²/A. Using L=Tγ²/A and r≥γ gives

sqrt(E_j L)≤C_1 Trγ/A,
L≤Trγ/A,
n_j≤E_j+C sqrt(E_jL)+CL≤C_2 Tr²/A,

where C_1 and C_2 are absolute once K is fixed. If n_j>0, the central constraints give the exact identities followed by one-sided bounds

n_j(1/2-φhat_j(v≥b)) = (γ/(2r))n_j+H_{j,+1} ≤ C_3 Trγ/A,
n_j(1/2-φhat_j(v≤b)) = (γ/(2r))n_j+H_{j,-1} ≤ C_3 Trγ/A.

These are upper bounds on signed deficits, not assertions that their absolute values are small. The median inequality and distance bound 1 give regret contribution at most 2C_3 Trγ/A. If n_j=0, the contribution is zero without defining φhat_j.

Summing as in Step 3 now proves SR_T=O(Tγ) on the joint event. This is a direct efficient construction in the original game. It does not require the nonconstructive full-game transfer of Step 5 or the unproved standalone MsMwC guarantee. Its necessary per-round feasibility, weighting, concentration, and heavy/light obligations have all been established.

## Step 7. Computing Updates from Loss Evaluations

Exact one-sided derivatives of an arbitrary revealed loss are not necessary for the computational claim. A routine approximation closes this implementation detail without strengthening the observation model.

Set m=T² and evaluate each revealed loss at x_k=k/m for k=0,...,m. Let ℓtilde be the piecewise-linear interpolant. Convexity makes its consecutive secant slopes d_1,...,d_m nondecreasing, and Lipschitzness puts every slope in [-1,1]. Thus ℓtilde is convex and 1-Lipschitz. The Lipschitz bound gives ||ℓtilde-ℓ||_∞≤1/m.

Its representing measure is explicitly finite: assign mass (1+d_1)/2 to 0, mass (d_{k+1}-d_k)/2 to x_k for k=1,...,m-1, and mass (1-d_m)/2 to 1. These masses are nonnegative and sum to 1. Their CDF gives the interpolant's slopes exactly, so Step 1 proves the required representation up to its additive constant. Every constraint reward can now be computed from finitely many known masses.

Run the efficient construction using these interpolated losses for its updates. Interpolation occurs only after the learner has committed to its current distribution, so the transformed losses remain an admissible adaptive loss sequence with the same information timing. Along the same realized predictions, for every comparator, replacing the true losses by the interpolants changes regret by at most 2T/m. Hence

SR_T(true losses)≤SR_T(interpolated losses)+2/T.

The extra term is absorbed into the stated rate. There are T(m+1) loss evaluations, polynomially many finite sums, O(sqrt T) label variables, polynomial-size LPs, and O(MJ)=O(sqrt T log T) product-weight operations per round. Thus the total implementation has the required polynomial running time in the source's arithmetic and loss-evaluation model. This argument does not assume access to an exact derivative or CDF oracle for the original losses. In particular, the weighting routine is now explicit rather than conditional on the efficiency of an unspecified expert algorithm.

## Step 8. Expected Regret and Proof Closure

Run the confidence-tuned algorithm at δ=1/T. Its high-probability threshold is O(sqrt T ln T). Since 0≤SR_T≤T, the failure event contributes at most 1 to expectation. Thus E[SR_T]=O(sqrt T ln T), with an absolute constant covering T=2 and the trivial parameter regime.

The formerly unresolved obligation is closed by the directly proved constraint-specific weighting procedure in Step 6. Its hypothesis of nonpositive weighted reward follows from the already-established LP for every realized loss, so it is not a new restriction on the adversary. The general MsMwC statement remains a source quotation rather than an independently proved theorem, but is no longer a premise of this reference proof. All theorem-critical obligations for the public task are now derived or supplied by the audited standard finite minimax and martingale concentration results with their hypotheses checked.
