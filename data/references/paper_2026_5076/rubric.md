# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Establishes the hard-family geometry: identifies the appropriate sign-testing events, proves that the central-game gap controls the absolute second-policy deviation, and proves the signed-game gap lower bound on the corresponding event.
- **3 points:** Carries out the attenuated-information argument. This includes a valid reduced-transcript KL calculation conditioned on the current first-player action, justified Bernoulli constants, the rate-to-deviation summation, and Pinsker/testing giving the stated constant or a stronger one. Preserves the public uniform limsup-sup quantifier order.
- **2 points:** Constructs a single game-independent uncoupled bandit procedure with a synchronized exploration schedule, proves its marginal and cumulative-count properties, and derives the mixture/output-gap inequality with valid conditioning. Establishes that the procedure also satisfies the reduced-transcript restriction, rather than merely assuming that an ordinary max-player bandit update does not use its sampled arm.
- **2 points:** Derives a sufficient output moment bound from the stated standard regret result or another valid argument, including the stochastic regret-to-gap correction where needed. Completes the schedule substitution and numerical estimates for the exact public upper bound, treating singleton action sets, the first rounds, and all p in (0,2].

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental choices of output constant, counterfactual representation, or randomization implementation.

The standard EXP3-IX regret theorem may be invoked without re-proving its internal algorithmic analysis, provided the relevant regret statement and information assumptions are stated and checked. A realized-regret theorem alone does not establish an almost-sure saddle-gap bound for averages of random mixed policies; the necessary conversion must be justified.

An unconditional output moment bound cannot simply be conditioned on an exploitation event. A valid solution may condition on an independent scheduling seed and verify the virtual learner's conditional law, or supply another correct argument.

The lower bound hides the actual sampled second-player action from both decision maps. Ordinary access to that action in a max-player importance-weighted update is not automatically compatible with this restriction. Accept any valid implementation showing compatibility; internal random selection followed by a pure exploration policy is one such implementation, but is not required.

Do not require the incorrect intermediate constants or exploration-count inequality appearing in the original source. Any rigorously established intermediate estimates yielding the public constant 17 and displayed logarithm are acceptable.

A proof that merely invokes a specialized conversion result, or merely names an information-theoretic method without deriving the transcript-KL/testing argument, does not earn the corresponding core-step credit. All core steps in the replacement reference proof are closed; there is no unresolved GT obligation to treat as an established scoring premise.
