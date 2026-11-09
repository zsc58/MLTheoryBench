# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Constructs one algorithm for all supplied nonempty indexed countable UUS classes using only queries `(i,x)->h_i(x)`. For the reference approach, correctly defines sure examples, the finite active set, finite-prefix criticality, protected witnesses, candidate selection restricted to active indices, and a defined fallback. Does not assume access to membership in the hidden target or to a full-support inclusion oracle.
- **2 points:** Establishes eventual criticality of the target's first index. For the reference approach, shows a distinguishing witness cannot be output while its earlier competing index remains active, uses complete enumeration to obtain a sure presentation and elimination, and treats the finite or empty collection of earlier competitors.
- **2 points:** Proves finite-round termination and eventual valid novel outputs. For the reference approach, establishes existence and stabilization of a critical index, bounds the excluded set uniformly over the searched prefix, and derives novelty relative to all observed inputs. Verifies finitely many permitted queries and operations per round.
- **1 point:** Verifies that the explicit padded class is UUS and uncountable and supplies an ordinary no-query limit generator. Correctness must include both integer families, the all-marker target, marker-index stabilization, and b=0. A specialized base generator must be justified rather than accepted solely by citation.
- **2 points:** Proves replay non-generation for the same class in the deterministic no-query model. For the reference approach, justifies the initial fresh marker, uses descending integer inputs, proves every phase terminates using a legal alternative-target replay enumeration, proves the selected outputs remain omitted, and identifies one fixed target with infinitely many invalid outputs.

# Evaluator Notes

Accept any correct alternative proof that meets the entire stated contract. The listed constructions describe the reference proof, not mandatory methods; allocate credit for corresponding mathematical obligations in an alternative argument.

A hidden-target membership oracle is not permitted in either clause. In clause 1, evaluating a specified indexed class member is permitted, but its target status is not known. In clause 2, generators have no oracle input and may otherwise be computationally unbounded.

The novelty requirement excludes previously observed inputs, not necessarily previous outputs. Do not penalize harmless repeated outputs that remain unseen as inputs.

In the reference ordinary generator, the branching test concerns whether the integer b has appeared, not whether the marker mu^b has appeared. Base-generator histories contain integers and their own virtual integer outputs, so marker symbols must not enter integer extrema. The no-marker case uses index zero and does not require a symbol mu^0.

In the reference lower bound, phase n begins with the integer z-n. The proof must respect a target fixed before interaction; deterministic dependence on the input history allows a target-stream pair to be constructed for each candidate generator. Merely changing targets during play is insufficient.

For termination of the positive search, saying that each excluded set is finite is not by itself sufficient when that set varies with the prefix. A uniform cardinality bound or another valid argument is required. Readily repairable omissions may receive 8-9 under the overall guide, but theorem-critical gaps are not completed proof steps.
