# Reference Proof

## Contract and obligations

Queries return the raw deterministic value F_z(x). The strictly increasing functions g_z are not supplied to the learner. Write Y_z(x)=g_z(F_z(x)) only in the analysis. At a fixed fidelity, raw and calibrated rankings coincide, and |Y_z(x)-F(x)|<=zeta(z).

The parameters q,v,r,d,C and the chosen fidelity-regime parameters are fixed. Constants and sufficiently-large-budget thresholds below depend only on these parameters, not on the policy, budget, objective, or admissible cost/fidelity instance. Lower bounds have quantifier order: for every sufficiently large B and every policy, there exists a hard admissible instance. Upper bounds hold for every admissible instance.

We close the following obligations: construction with an attained maximum; near-optimal-cell and fidelity admissibility; width and depth information limitations; inversion in all five regimes; complete algorithmic cost accounting; the same-fidelity ranking induction and validation comparison; and all upper-rate substitutions. The only external analytic fact used is the elementary positive-branch Lambert-W inequality proved below.

## 1. Admissible hard instances

Use the common known cost function ell(z)=1/(1-z) for 0<=z<1 and ell(1)=+infinity. For c>=1 set z_c=1-1/c. Thus all paid queries cost at least one, and the selection mechanism is the same on every hard instance.

Choose an envelope Psi on [1,infinity): A c^{-alpha} in the polynomial case, B0 exp(-c^beta/sigma) in the exponential case, and v for 1<=c<a and zero for c>=a in the threshold case. Set zeta(z)=Psi(ell(z)) for z<1 and zeta(1)=0.

Let T be a retained subtree with the root, between one and floor(r^{-dk}) retained cells at depth k, and containing the full partition path of an actual point x*. Write T^k for the union of its retained depth-k cells and define

F_T(x)=sup{-v r^k : k>=0 and x belongs to T^k}.

Then -v<=F_T<=0 and F_T(x*)=0. Every point in the optimal depth-k cell has value at least -v r^k, proving local smoothness.

Put L=log(1/r) and k0=floor(log 3/L). For k<=k0, q^k<=C_min r^{-dk}, because r^{-d}<=q. For k>k0, a depth-k cell not descending from a retained depth-(k-k0) cell has supremum at most -v r^{k-k0-1}<-3v r^k. Consequently the number of near-optimal cells is at most

q^{k0} floor(r^{-d(k-k0)}) <= C_min r^{-dk} <= C r^{-dk}.

Define raw fidelities by F_z(x)=min(F_T(x),-zeta(z)), with F_1=F_T and g_z the identity. Since F_T<=0, clipping changes its value by at most zeta(z). This verifies the entire fidelity contract.

It is essential not to infer existence of x* from the mere existence of an infinite retained branch. In each construction below we specify only a finite adversarial prefix, choose a point in its final retained cell, and continue along that point's cells. Every such cell is nonempty by the partition definition. The continuation gives an attained maximum and changes none of the finite-prefix information arguments.

## 2. Information accounting and coupling

For an integer h>=1 let

c_h=inf{c>=1: Psi(c)<=v r^h},    N_h=floor(B/c_h)+1.

The chosen envelopes attain these thresholds. A query with zeta(z)<=v r^h costs at least c_h. Include the policy's output as one additional free accurate probe, without giving feedback from that probe to the policy. There are at most N_h accurate probes, including this last probe.

Couple runs by using the same internal policy randomness. If a retained tree is cut below depth h, its observations and those of any continuation agree until an accurate probe enters the part continued below depth h. Outside that part the targets agree. Inside it, a query with zeta(z)>v r^h returns the common clipped value -zeta(z). This is a first-hit coupling, not a claim of unconditional equality after the first distinguishing observation.

The finite cut tree may be used as a comparison transcript even though it is not itself in the objective class. Budget stopping is enforced by the known costs, and every first-hit event under comparison is coupled to the corresponding admissible continuation.

## 3. Width limitation

Suppose r^{-dh}c_h>=qB. Choose an integer s>=0 with

B/c_h<q^s<=r^{-dh}.

Such s exists by taking the least integer with q^s>B/c_h; the displayed assumption provides the upper bound. Also s<=h because r^{-d}<=q.

Construct a single retained spine to depth h-s, followed by all descendants for s levels through depth h. At intermediate depth k between h-s and h, its width q^{k-(h-s)} is at most r^{-dk}: this follows from q^s<=r^{-dh} and r^{-d}<=q. Earlier widths are one.

There are q^{s+1} children below the retained depth-h cells. For each such child, retain that child alone below depth h and complete along a selected point inside it. Every resulting instance satisfies Section 1.

Under the cut-tree transcript, the expected number of these children hit by accurate probes is at most N_h<=q^s. First-hit coupling identifies each child's hit probability with its hit probability on the corresponding continued instance. Therefore some child has hit probability at most 1/q<=1/2. If that child is never hit, the output is outside it and has gap at least v r^h. Thus

r^{-dh}c_h>=qB  implies  R_B(pi)>=v r^h/2

for some admissible instance.

## 4. Depth limitation

Suppose h>=N_h. Start with one retained spine through depth h. Recursively, for k=h+1,...,4h, consider the cut tree ending at the current depth-(k-1) cell. For each of its q children, consider the probability that the first accurate probe entering the parent lands in that child. These disjoint probabilities sum to at most one, so select a child whose probability is at most 1/q<=1/2. After the choice at depth 4h, complete along a point in the selected cell.

On the final instance let E_k be the event that the first accurate probe into the selected depth-(k-1) parent already lies in its selected depth-k child. First-hit coupling with the cut tree gives P(E_k)<=1/2. Hence, for M=sum_{k=h+1}^{4h} 1_{E_k},

E[M]<=3h/2,    P(M>=2h)<=3/4.

To verify the pathwise implication, list the t<=N_h<=h accurate probes, including the output. Let a_0=h and let a_s be the deepest selected cell through depth 4h visited by one of the first s probes, or h if none has been visited. If a probe raises the deepest visited depth from a_s to a_{s+1}, every edge with child depth in {a_s+2,...,a_{s+1}} contributes to M: that probe is the first accurate entry into the corresponding parent. These intervals are disjoint. Consequently a_t<=h+t+M<=2h+M. Reaching depth 4h therefore requires M>=2h.

With probability at least 1/4 no accurate probe, including the output, enters the retained depth-4h cell. Outside that cell the regret is at least v r^{4h}. Thus

h>=floor(B/c_h)+1  implies  R_B(pi)>=v r^{4h}/4

for some admissible instance. This uses only a finite adversarial prefix, so the completion in Section 1 applies.

## 5. The five lower rates

Polynomial bias gives c_h=max{1,(A/(v r^h))^{1/alpha}}. For all large h, r^{-dh}c_h is a fixed positive constant times exp((d+1/alpha)Lh). Choose the least sufficiently large integer h making this quantity at least qB. Then h<=log B/((d+1/alpha)L)+O(1), and the width bound yields a positive constant times B^{-1/(d+1/alpha)}.

For exponential bias, c_h=max{1,[sigma log(B0/(v r^h))]_+^{1/beta}}, so c_h is bounded above and below by positive constant multiples of h^{1/beta} for large h. If d=0, choose h=ceil(K B^{beta/(1+beta)}) with a sufficiently large fixed K. Then h>=floor(B/c_h)+1 for all large B. The depth bound gives a positive constant times exp(-k B^{beta/(1+beta)}). If d>0, choose h=ceil(log(qB)/(dL)). Since c_h>=1, the width condition holds, giving a positive constant times B^{-1/d}.

For threshold bias, c_h=a for every h>=1, including a=1. If d=0 take h=floor(B/a)+1, obtaining a positive constant times exp(-kB) from the depth bound. If d>0 use the preceding width choice and c_h>=1, obtaining a positive constant times B^{-1/d}.

These constructions have fixed common cost and selection maps and identity calibrations. They therefore prove the bounds in the raw-observation experiment, even if the policy is told the fixed class parameters. An easier exact or free instance elsewhere in the class does not change this existential worst-case result.

## 6. Algorithmic cost

Let n=B' and kappa=qe/(e-1). For n=0 the algorithm makes no queries and has regret at most v by root smoothness.

Suppose n>=1. Opening at level j costs at most q sum_{u=0}^j e^u<=kappa e^j. Caching or skipping can only reduce cost. Exploration therefore costs at most

kappa n sum_{h=1}^n (1/h) sum_{m=1}^{floor(n/h)} (1/m)
<=kappa n(1+log n)^2<=B/2.

Initialization costs at most kappa n. There are floor(log n)+1 validation queries, each costing at most n, so initialization plus validation costs at most n[kappa+1+log n].

The definition of n and n>=1 imply B>=2kappa(1+log B)^2 and hence log B>=1. Also n<=B. For t=log B>=1,

kappa+1+log n<=kappa+1+t<=kappa(1+t)^2.

Thus initialization plus validation also costs at most B/2. The total is at most B. This includes the root's entire geometric collection of child evaluations and the j=0 validation candidate.

## 7. Generic depth/fidelity guarantee

Let Psi be a nonincreasing upper envelope of Phi. Suppose H>0 and an integer j>=0 satisfy

Psi(e^j)<=v r^H,    n/(4H e^j)>=C r^{-dH}.

Then

R_B(A)<=(3v/r)r^H+2Psi(n).

For H<1, the right side exceeds v, so root smoothness suffices. Assume H>=1 and put h=floor(H). The second condition implies e^j<=n, so this level is initialized.

Induct over k=1,...,h. The root is opened through all available levels. If the optimal depth-(k-1) cell was opened at level at least j, its optimal child has an observed level-j value. At depth k, the number of scheduled operations using exactly level j is

floor(n/(ke^j))-floor(n/(ke^{j+1}))
>=n/(2ke^j)-1>=n/(4ke^j)>=C r^{-dk}.

The middle inequality uses n/(2ke^j)>=2, a consequence of the assumed condition and C>1.

If the optimal cell was already opened at a higher level, the induction is complete. Otherwise, until it is selected it remains eligible throughout these level-j operations, so none of those operations is skipped. Every selected competitor has raw level-j value at least that of the optimal representative. Apply the same strictly increasing g_{z_{e^j}} to this comparison. The bias bound and smoothness give

F(x_competitor)>=F(x*)-v r^k-2Psi(e^j)>=F(x*)-3v r^k.

If the optimal cell were still unselected afterward, these distinct competitors together with the optimal cell would exceed the allowed number of near-optimal depth-k cells. Thus it is opened at level at least j, completing the induction. A cell opened at a higher level already had an observation at that level and, by the opening rules, at level j as well.

The optimal depth-h representative is consequently among the evaluated level-j cells. The level-j candidate maximizes raw observations over all such cells. The same calibrated comparison gives

F(x_j^c)>=F(x*)-v r^h-2Psi(e^j)>=F(x*)-3v r^h.

Validation compares all candidates at the single fidelity z_n. Applying its increasing calibration gives a loss of at most another 2Psi(n). Finally r^h<=r^{H-1}, proving the claim. Calibrations are used only in this analysis, never as algorithm inputs.

## 8. Parameter choices and low-budget cases

Throughout this section n>=1 and L=log(1/r).

### Polynomial bias

Set s=d+1/alpha. Let H1>0 solve

H1 exp(s L H1)=n v^{1/alpha}/(4Ce A^{1/alpha}),

and let H2>0 solve H2 exp(d L H2)=n/(4C).

If v r^{H1}<=e^alpha A, set j=floor(log(e(A/(v r^{H1}))^{1/alpha})). Then j>=0 and

(A/(v r^{H1}))^{1/alpha}<e^j<=e(A/(v r^{H1}))^{1/alpha}.

The two generic conditions follow from these bounds and the equation for H1. Therefore R_B(A)<=(3v/r)r^{H1}+2A n^{-alpha}.

Otherwise H1 exp(dLH1)>n/(4C)=H2 exp(dLH2), so H1>H2 and A<v r^{H2}. Set j=0. Both generic conditions hold at H2, yielding R_B(A)<=(3v/r)r^{H2}+2A n^{-alpha}. This includes the source's polynomial low-budget case.

### Exponential bias

Let b=max{1/(2sigma),log(B0/v)} and p=1+1/beta. Let H1 solve

H1^p exp(d L H1)=n/[4Ce(2sigma L)^{1/beta}],

and H2 solve

H2 exp(d L H2)=n/[4Ce(2sigma b)^{1/beta}].

If H1>=b/L, choose j=floor(log(2sigma L H1)/beta)+1. Then j>=1,

e^{beta j}>=2sigma L H1>=sigma(LH1+log(B0/v)),

and e^j<=e(2sigma L H1)^{1/beta}. These inequalities verify both generic conditions at H1. Hence R_B(A)<=(3v/r)r^{H1}+2B0 exp(-n^beta/sigma).

If H1<b/L, monotonicity of H exp(dLH) and the two equations imply H2<=H1. Choose j=floor(log(2sigma b)/beta)+1. Then e^{beta j}>=2sigma b>=sigma(LH2+log(B0/v)) and e^j<=e(2sigma b)^{1/beta}. Both conditions hold at H2, giving the analogous low-budget bound.

### Threshold bias

Let H solve H exp(dLH)=n/(4Cae). If n>=a, use j=floor(log(ea)); then a<=e^j<=ea. Take Psi(c)=+infinity for c<a and zero for c>=a. Both generic conditions hold and Psi(n)=0, giving R_B(A)<=(3v/r)r^H. If n<a, then H<1 and the root bound R_B(A)<=v suffices. One may sharpen the factor 3 when the relevant evaluations are exact, but that refinement is not needed for the target.

## 9. Rate simplification

For x>0 let W(x)>0 solve W(x)e^{W(x)}=x. If x>=e, then W(x)>=1 and W(x)<=log x; using W(x)=log x-log W(x) gives W(x)>=log x-log log x. For 0<x<=e, W(x)<=1 and x=W(x)e^{W(x)}<=eW(x), so W(x)>=x/e. Thus all Lambert-W facts needed here follow directly from its defining equation.

As B tends to infinity, n=Theta(B/(log B)^2). For fixed parameters, H1 tends to infinity in the polynomial and exponential cases, so their high-budget branches eventually apply.

In the polynomial case H1=W(k n)/(sL) for a fixed k>0. Therefore r^{H1}=O((log n/n)^{1/s}). Since 1/s<=alpha, the residual n^{-alpha} is no larger asymptotically. This yields

R_B(A)=O((B/(log B)^3)^{-1/(d+1/alpha)}).

For exponential bias with d=0, H1 is a fixed positive multiple of n^{beta/(1+beta)}. The residual exp(-n^beta/sigma) decreases faster. Thus

R_B(A)<=U exp(-k(B/(log B)^2)^{beta/(1+beta)})

for positive fixed U,k and all large B.

For exponential bias with d>0, put p=1+1/beta. The defining equation gives H1=(p/(dL))W(k n^{1/p}) for a fixed k>0. Hence r^{H1}=O(((log n)^p/n)^{1/d}), and the residual is negligible. Therefore

R_B(A)=O((B/(log B)^{3+1/beta})^{-1/d}).

For threshold bias with d=0, H=n/(4Cae), giving R_B(A)<=U exp(-kB/(log B)^2). With d>0, H=W(k n)/(dL), giving R_B(A)=O((B/(log B)^3)^{-1/d}).

All comparisons and loop indices of the algorithm use only its budget, partition, representatives, known cost/selection mechanism, and raw observations. None uses v,r,d,C, a calibration, the bias function, or a fidelity-regime parameter. The upper and lower rates therefore establish the claimed adaptive matching up to logarithmic factors. Their positive exponential constants are independent constants, not asserted to coincide.
