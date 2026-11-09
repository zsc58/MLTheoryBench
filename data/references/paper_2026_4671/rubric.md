# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Concentration and feasible optimistic spaces (2 points).** Establish one simultaneous coordinatewise constraint concentration event with the stated radii. Derive empirical-prefix, empirical-to-fixed-vector, and empirical-to-horizon-average comparisons as needed. Show that the strictly feasible strategy belongs to every projection set on that same event, so the fallback is not used there. Keep the public pre-round indexing consistent with the source's post-observation updates.

2. **Corruption-adaptive comparators and exact accounting (3 points).** Relate the hindsight optimum to the optimistic constraints, construct feasible mixtures with the strictly feasible strategy, and verify membership throughout each phase. Correctly count all phases, including the final partial phase. Prove the claimed `(2C/rho) log_2 T` contribution rather than merely an asymptotic bound. One valid route uses the sharper slack `C/T+C/s`, phases starting at powers of two, and the bound `(C/rho)(1+S)` for `T>=4`. Other valid constructions are acceptable.

3. **Fixed-share regret and loss conversion (3 points).** Analyze the actual update: entropic projection using the played iterate as prior, followed by fixed sharing. Derive the projection/Bregman inequality, account for share costs and phase boundaries, and verify the exact `4 log_2(T) sqrt(T ln(KT))` constant. One sufficient estimate is `S ln(KT)/eta+2/eta+eta T/2`. Work with observed losses in the deterministic OMD argument and then justify the two loss deviations. In particular, handle the hindsight optimizer using a uniform coordinatewise loss event or another valid argument, not an unjustified predictable-comparator martingale claim. Obtain the stated probability `1-3delta`.

4. **Positive constraint violation (2 points).** Distinguish the played fixed-share mixture from its projected point, accounting for at most one unit of total share violation and at most one unit from the initial round. Use optimistic feasibility and the empirical-to-fixed-vector bound, retaining the instantaneous corruption deviations and summing them to at most `C`. Sum the harmonic and inverse-square-root terms and obtain `V_T <= 2+2C+C ln T+16 sqrt(T ln(TKm/delta))` simultaneously over constraints on an event of probability at least `1-delta`.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat omission of the switching/moving-space argument or of either final guarantee as theorem-critical.

Do not accept `S=log_2 T` as the literal number of phases starting at `1,2,4,...` without correct endpoint accounting. Do not accept the original per-round claim that arbitrary current mean constraints differ from the fixed reference by `C/T`; only the horizon-average comparison has that normalization. Do not apply observed-loss mirror-descent regret directly to conditional mean losses without a valid additional argument.

The public algorithm shares after projection; a proof for sharing before projection does not automatically establish the requested result. Played iterates need not themselves lie in the optimistic sets.

A fully correct solution must address small horizons, `C=0`, and the unused zero learning rate when `K=T=1`. Direct bounds `R_T<=T` and `V_T<=T` suffice for the small-horizon cases. A missing small-horizon check is readily repairable only when the main proof is otherwise valid and does not rely on a false all-horizon inequality.

The reference proof has no unresolved theorem-critical dependency.
