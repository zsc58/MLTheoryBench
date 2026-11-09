# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly sets up the finite categorical variables, coarsenings, conditional-probability matrices, and causal target, including consistency, positivity, exchangeability, and proxy independences. Uses Z_t=S_{t-1}, takes coarsenings of the two separate proxies, and works at a supported state with defined conditioning events.
- **4 points:** Derives the two latent-state factorizations of the observed action and proxy matrices and uses the square invertibility condition to eliminate the latent conditional matrix. Justifies the inherited conditional independences for deterministic coarsenings. Merely naming matrix inversion without deriving these factorizations is insufficient.
- **2 points:** Uses the marginal proxy factorization to replace the remaining latent factors and obtains the stated formula for the interventional action distribution. The proxy marginal is unconditional, with the coarsening map held fixed for the state under consideration.
- **2 points:** Connects the observational conditional law to the interventional law using consistency, positivity, and latent exchangeability, and concludes identification of the argmax policy, correctly handling ties.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the reference proof's notation or order. Treat failure to establish the proxy factorizations or the interventional bridge as theorem-critical gaps; propagate such failures to the final policy conclusion.

The claim is pointwise in the supported state and holds for every admissible pair of coarsenings at that state. Do not require one common pair of coarsenings to work for all states. No proof of an equivalence between raw-matrix rank and existence of coarsenings is required: existence of admissible coarsenings is explicitly assumed.

Do not accept replacing Z_t by (S_{t-1},W_{t-1}), or inferring independence of W'_{t-1} from a variable that may contain W'_{t-1}. Only positive-probability conditioning events are used; zero-weight terms in latent sums may be omitted. No strict positivity of every matrix entry is assumed. The argument must allow m=1, deterministic or latent-constant action laws, and ties, but separate case analyses are unnecessary when the general proof already covers them.
