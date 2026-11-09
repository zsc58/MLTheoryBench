# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **4 points:** Correctly differentiates local invariance along arbitrary augmentation curves and derives \(V_{\mathrm{aug}}(z)\subseteq\ker J_h\). It must justify the chain-rule step and passage to the tangent span, or give an equivalent derivative-based argument, rather than merely assert that invariance causes singularity.
- **2 points:** Correctly concludes that \(G=J_h^\top J_h\) vanishes on augmentation tangent directions and is singular whenever that tangent space is nonzero. It must not infer unconditional global singularity when the tangent space is zero.
- **2 points:** Identifies \(\operatorname{col}(S_z)=V_{\mathrm{aug}}(z)\) from the actual sensitivity definition, derives \(S_h=J_hS_z\) by the chain rule, and concludes \(S_h=0\). An equivalent direct differentiation of exact invariance to obtain \(S_h=0\) is acceptable.
- **2 points:** Applies the stipulated parameter-space Jacobian-Gram Fisher-information approximation and the identity \(\operatorname{rank}(S^\top S)=\operatorname{rank}(S)\) to obtain \(\operatorname{rank}(I_z)=\dim V_{\mathrm{aug}}(z)\), \(\operatorname{rank}(I_h)=0\), and the requested rank deficit.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Standard finite-dimensional chain-rule and Gram-rank facts may be used without reproducing every elementary detail. The Fisher-information conclusion requires use of the supplied normalized local Jacobian-Gram approximation and the actual augmentation-sensitivity definitions; an unsupported generic claim that invariance always lowers Fisher-information rank is not sufficient. Both Fisher matrices act on the continuous augmentation-parameter space. Using \(SS^\top\) only to establish an equivalent sensitivity-rank calculation is acceptable, but identifying it as the stipulated parameter-space Fisher matrix is a typing error. The information claim is posed for a nontrivial augmentation-tangent space; the geometric inclusion remains valid when that space is zero.
