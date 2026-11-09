# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly identifies the pushforward and reference measures, forms the instability set, and partitions it into the positive and negative log-ratio regions.
- **3 points:** Correctly combines the two directional KL bounds into the symmetric integral \(\int(p-q)\log(p/q)\le 2\varepsilon\).
- **3 points:** Establishes valid pointwise lower bounds on both regions that control the integral from below by \(\delta(1-e^{-\delta})p\) and by the same multiple of \(q\), handling both signs of the log ratio.
- **2 points:** Integrates the bounds and concludes the stated simultaneous probability inequalities for the pushforward and target distributions for every \(\delta>0\).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The central requirement is a derived two-measure concentration bound with the stated constant; merely naming a divergence inequality without proving or correctly applying it is insufficient.
