# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Compression representation and stability (3 points).** Correctly represents the common-hidden-width network with its factor L+2 normalization, all bias blocks, and a linear output. Establishes bias stationarity for the induced input signal. Proves the cut-norm stability estimate on the relevant nonnegative unit-bounded initial signals, accounting for ReLU rather than dropping it. Handles equivariance, pointwise fixation of input/output/bias, and an infimum without assuming a minimizing relabeling.
2. **Width-independent regularity compression (2 points).** Justifies the quantitative regularity ingredient rather than merely naming an unproved nonstandard dependency. Preserves the feedforward block structure, equitizes the coarse approximating kernel, and controls the remainder. Derives an input-independent approximation in the one exact common-width architecture D(epsilon), with the stated numerical bound. The reference proof's energy-increment reconstruction and equitization argument are a complete route; an equally justified alternative is acceptable.
3. **Lipschitz approximation parameter lower bound (3 points).** Uses targets that are genuinely 1-Lipschitz for infinity norms, handles integer grid cardinalities for all relevant epsilon, and obtains the required shattering count. States and correctly applies the standard quadratic VC bound to a fixed architecture, yielding W >= c^(-1/2)(6epsilon)^(-d0/2). Embedding scalar targets into one output coordinate is sufficient.
4. **Parameter contradiction and conclusion (2 points).** Justifies the explicit W-tilde bound, including ceilings and the L=2 case, and applies the strict logarithmic comparison. Selects a hard target for the single architecture supplied by compression, not an unjustified union of architectures. Uses the eta+eta strict triangle inequality with eta=1/16 to contradict the epsilon0=1/8 lower bound.

# Evaluator Notes

Accept any complete valid alternative proof of the public target; the reference route is not mandatory. Do not require incidental notation or an exact reproduction of the reference proof.

The public model has a common hidden width, and both weights and biases enter with the explicitly stated normalization. Treat a proof for independently variable hidden widths or a different normalization as addressing a different class unless a valid inclusion or equivalence argument is supplied. Divisibility of the common width can be arranged by identical neuron replication without changing represented functions or parameter bounds.

Do not accept the source's unrestricted stability assertion for arbitrary computational signals: it is false without signal-amplitude control. The cube-induced signals needed here already take values in [0,1], and the replacement reference proof establishes that specialization. Likewise, bias stationarity requires the induced unit bias, not an arbitrary computational signal.

A weak-regularity citation or specialized compression claim is not by itself a completed theorem-critical derivation. The supplied standard independent VC bound may be used with its stated fixed-architecture hypotheses. The general approximation-complexity citation is not needed when the grid argument is given.

An exact common-width architecture has (L-2)D^2+(d0+dL+L-1)D+dL parameters. A larger expression may be used as an upper bound, but not asserted as an exact count. A fixed-architecture VC theorem does not automatically control a union of all low-parameter architectures. Bounded normalized networks of different widths also cannot simply be zero-padded while assuming their functions and parameter bounds are unchanged.

Treat omitted routine algebra as minor only when the numerical width, parameter bound, and dimension comparison are justified. Unsupported compression, an incorrect target norm, an unjustified architecture-union inference, or a non-strict final inequality that fails to yield a contradiction is a major gap unless the answer independently closes it.
