# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Defines the fixed-width multigrade ReLU residual-sum architecture and states the residual sequence with the required pointwise, finite-Lp, and uniform conclusions, correctly treating the first zero-output indexing grade.
2. **4 points:** Constructs the localized-grid cutoff operator, proves bounded overlap and the two positive-contraction inequalities using continuity, then symmetrizes the positive construction into a balanced signed contraction. Establishes pointwise residual domination for every individual signed cutoff update using domination of the full positive and negative sums. Proves strict finite-Lp decrease for each update on a positive-measure set where that cutoff is nonzero, including cubes touching the domain boundary.
3. **2 points:** Demonstrates realization by affine/ReLU maps of width at most 5d+1. For the reference route, gives explicit two-layer cutoff maps and a pipelined state carrying the input, the next cutoff's first-layer features, and the preceding completed cutoff. Shows that every grade after initialization emits a correction, including at block boundaries, without inserting inactive grades while the residual is nonzero.
4. **2 points:** Iterates the finite construction on successive residuals and proves geometric sup-norm decay at block endpoints, pointwise monotonicity at every grade, and strict finite-Lp decrease at every grade k>=2 unless both consecutive residuals vanish. Deduces uniform convergence for the entire sequence, and handles the zero target and continuation after a residual vanishes.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the reference proof's notation, grid choices, or ordering. The same sequence must work for every 1<=p<infinity.

Treat omission of the positive-measure strictness argument, the fixed-width realization, or the iteration-to-uniform-convergence step as theorem-critical gaps. Strict decrease only at contraction-block endpoints, or only at unspecified 'substantive' grades, does not establish the target. A construction that repeatedly inserts a zero-output initialization layer while the residual is nonzero also does not establish it.

Do not require an accumulator coordinate: in the source-grounded pipeline, the scalar state coordinate stores a completed cutoff and the external residual-sum outputs perform the accumulation.

A selected closed grid cube may meet a relatively open superlevel set only on a boundary face of D. Thus nonempty E intersect Q alone does not imply positive d-dimensional measure. Valid arguments include continuity of Gamma_Q at a selected point where Gamma_Q=1, or positivity on a sufficiently small dilation of Q intersected with D. The support lower bound from the continuity estimate ensures the required sign on selected dilated supports; that containment is not a source defect.
