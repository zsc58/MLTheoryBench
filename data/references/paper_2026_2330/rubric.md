# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Proves safe elimination from the two optimistic inequalities: for an unqueried implementation, a failed resource test implies the true resource is already in the current upper closure, and a failed functionality test excludes target feasibility.
- **3 points:** Gives the exhaustive, mutually exclusive queried/eliminated/persistently-admissible classification and proves coverage in the first two cases. Justifies almost-sure termination of all rounds and obtains the classification for all optimal witnesses on a common full-probability execution event, without an unjustified uncountable intersection of probability-one events.
- **3 points:** For an uncovered optimal resource, proves that its entire positive-measure witness set remains admissible, derives a uniform positive conditional probability of selecting a witness, and correctly rules out perpetual noncoverage. Accept either an elementary conditional survival recursion or a conditional Borel-Cantelli argument with an appropriate filtration and adapted events.
- **2 points:** Establishes persistence of coverage from monotonicity of finite-history upper closures, uses finiteness of the optimal antichain to obtain one measurable finite random time, and proves both upper-closure inclusions needed for eventual equality.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or require use of conditional Borel-Cantelli. A mere assertion that sampling eventually finds witnesses, without deriving a uniform positive conditional probability while the resource is uncovered, does not earn the third step. A conditional Borel-Cantelli proof must distinguish the event of perpetual noncoverage from current-history conditioning; adapted stopped events are one valid formulation. Failure to prove either inclusion in the final equality is theorem-critical.

The Borel acceptance-graph assumption supplies measurable adaptive acceptance; do not demand a topology or sigma-field on the arbitrary functionality and resource posets. For a fixed optimal resource with Borel witness set, coverage is measurable because minimality makes coverage equivalent to having queried a witness. This observation, or an equivalent justification, suffices for random coverage times. The finite-set upper-closure identity and its monotonicity may be established briefly as elementary order facts. The common full-probability witness statement may be obtained pathwise once all rounds terminate; no enumeration of the optimal witnesses is necessary.

The source's strict positive-measure admissibility assumption applies to every finite valid history. Do not silently replace the procedure by a sampler that stops upon exhaustion. Histories are sets, so no evaluator dependence on query order is authorized.
