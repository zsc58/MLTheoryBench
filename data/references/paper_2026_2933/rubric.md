# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly specifies the symmetric N-level uniform quantizer, relates endpoint clipping value and spacing by \(s=2C/(N-1)\), and identifies midpoint cells and saturation to the endpoint levels. Accept equivalent indexing and offsets.
- **3 points:** Correctly uses the stipulated additive error-power model, including \(E_s=s^2/12\) and the two endpoint-clipping tail integrals. Distinguishes this modeled objective from an unsupported exact deterministic-Gaussian MSE calculation.
- **3 points:** Evaluates the Gaussian tail integrals correctly to obtain \(E_c=2(\sigma^2+C^2)Q(C/\sigma)-2C\sigma\phi(C/\sigma)\), with justified Gaussian moment identities or a valid equivalent calculation.
- **2 points:** Combines the terms into \(E(C)\), forms \(\operatorname{SNR}(C)=\sigma^2/E(C)\), and correctly characterizes a global optimizer \(C^*\) and its resulting quantizer parameters for the modeled objective. The equivalence uses fixed positive input power and positive modeled error power.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

The uniform stepping law and its additive power contribution are stipulated modeling assumptions. They are not a conditional-uniform law given an unsaturated observation and are not inferred from an arbitrary Gaussian density. Do not require a factor \(\mathbb P(|X|\le C)\) in the stepping contribution; inserting such a factor changes the stated model. Arguments that claim the stipulated law follows exactly from deterministic Gaussian quantization should lose credit on the decomposition step.

Use the task's endpoint-clipping convention. Integrating over the full exterior decision cells beginning at their midpoint thresholds computes a different clipping quantity and does not establish the requested formula.

The quantizer symbol \(\mathsf q\) and Gaussian tail function \(Q\) are distinct. Equivalent unambiguous notation is acceptable.

Normal-optimality here means optimality within the symmetric uniform family for the modeled objective. Do not require optimization over arbitrary offsets, arbitrary nonuniform quantizers, or the exact deterministic quantizer MSE.

No specific numerical search algorithm, numerical value of the optimizer, convergence theorem for a numerical method, stationarity equation, or uniqueness proof is required. The target concerns a global optimizer in the stated argmax, not an arbitrary approximate numerical output. The reference proof's supplementary optimizer-existence argument is not an additional scoring requirement.
