# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Finite-grid validity and normalization (2 points).** Uses the supplied uniform null law of P_n, proves the expectation inequality for nonincreasing functions of arbitrary grid p-variables, and uses grid normalization to obtain e-validity and exactness for P_n. An equivalent elementary stochastic-order argument is acceptable.
2. **General existence (3 points).** Establishes a finite positive strictly decreasing f on all of [0,1] satisfying the required normalization equation. One valid route is the augmented-grid decrement construction: verify the coefficient signs, justify existence of strictly positive coordinates, and interpolate, adding the endpoint 0 afterward. A complete logistic construction also earns these points when the answer verifies that it supplies such an f; no independent decrement construction is required. Other complete valid existence arguments are acceptable.
3. **Logistic normalization (2 points).** For every fixed admissible s, defines the logistic family and its finite-grid mean, proves continuity and limits strictly above and below one, and applies the intermediate value theorem on a finite interval to obtain a positive scale. An alternative complete proof of the required scale's existence is acceptable. The scale may depend on s as well as n and alpha.
4. **Calibrator properties and set preservation (2 points).** Verifies positivity, smooth strict decrease, invertibility onto the image, grid-calibrator validity, exactness for P_n, and the threshold equivalence preserving the conformal prediction set. An explicit inverse formula is sufficient but not mandatory when invertibility onto the image is otherwise justified. The answer must also establish the requested validity and set preservation of the general normalized map, either separately or through a construction satisfying both targets.
5. **Domination (1 point).** Proves pointwise domination of F_AoN on both p<=alpha and p>alpha, with the stated domain including its endpoints.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, a separate positive-decrement construction, a unique logistic scale, or a scale independent of s. The same verified logistic construction may establish both existence targets and receive credit for both fulfilled obligations.

The theorem-critical requirements are existence of a positive strictly decreasing normalized function, existence of the stated logistic calibrator for every admissible fixed s, validity for every grid p-variable, exactness for the uniform P_n, the requested regularity and invertibility, set preservation, and domination. A missing construction or normalization argument is a substantive gap unless another valid argument establishes that obligation. A bare citation to an unproved paper-specific internal lemma does not itself supply the missing existence argument; the elementary positive-coordinate construction or an equivalent justification suffices.

Distinguish grid p-to-e calibration from calibration of arbitrary nongrid p-variables. Do not demand exactness for every grid p-variable: only expectation at most one is required for that class, while exactness is required for P_n. Interpret invertibility as invertibility onto the image. Do not introduce cases excluded by alpha N>1 and nonintegrality, but the proof must cover all allowed cases, including n=1 and j=floor(alpha N)=N-1 when using the augmented-grid method.
