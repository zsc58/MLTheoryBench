# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly express TSI and QSI as normalized sums of 0--1 ordinal-agreement indicators, with the appropriate ordered-tuple denominators.
2. **4 points:** Partition comparisons into tuples wholly contained in U and tuples touching V; count the former by \((|U|)_3\) or \((|U|)_4\), identify their restricted-similarity contribution, and bound the latter to derive the lower and upper interval bounds for the original and transformed similarities. Accept an equivalent direct affected-comparison argument.
3. **2 points:** Use the interval bounds and \(0\le S_r(X_U,Y_U)\le1\), or an equivalent argument, to prove the \(1-c_r\) outlier deviation bound for both indices.
4. **2 points:** Prove the corresponding corruption bound relative to \(S_r(X,Y)\) and correctly justify vanishing deviation as \(|V|/N\to0\) for fixed r. For example, counting tuples meeting V gives \(0\le1-c_r\le r|V|/N\); an equivalent justification is sufficient.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

The comparison functions are fixed real-valued functions on pairs, not necessarily metrics. A proof must cover the stated domain rather than assume metric axioms, absence of ties, distinct representation values, injectivity or continuity of T, or a sampling or independence model. The case \(V=\varnothing\) is included. A general argument that already covers these cases needs no separate case discussion.
