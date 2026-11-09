# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly expands the global expected likelihood through the environment-conditioned mixture and converts the resulting joint expectation to an average under \(\pi(de)p(dx,dy\mid e)\). The public joint integrability assumption justifies changing the order of integration.
- **3 points:** Establishes the posterior KL mixture identity at fixed \((x,y)\), either by its logarithmic mixture calculation or by a correctly stated and verified standard chain-rule application, and uses it with the correct sign to isolate the posterior cross-environment discrepancy. Changes of conditioning for the intermediate divergence must be justified in the common jointly measurable density setting.
- **3 points:** Establishes the label-marginal KL identity after averaging over \(p(dy\mid x,e)\), then correctly uses \(\pi(de)p(dx\mid e)=p(dx)p(de\mid x)\) to obtain the prior cross-environment discrepancy and the same integrated intermediate divergence.
- **2 points:** Combines the identities into exactly \(\mathcal L=\mathbb E_{\pi(e)}\mathcal L_e+R(q)\), with both residual terms, their signs, and their conditioning correct, without undefined infinite subtractions.

# Evaluator Notes

Accept a complete valid alternative proof and allocate the core-step credit to the corresponding mathematical accomplishments. Do not require the reference proof's ordering or incidental presentation choices. A combined logarithmic calculation or a conditional mutual-information argument can earn full credit without separately displaying the reference proof's two intermediate identities.

A standard KL chain rule or conditional mutual-information chain rule may be used when the relevant identity is stated and its distributions, conditioning, mixture relations, measurability, and finiteness hypotheses are correctly instantiated. It is not necessary to reprove such a standard result from first principles. Merely naming a method, or asserting the desired mixture identities without a calculation or justified theorem application, does not close the central obligations.

The common jointly measurable variational densities ensure that the mixture densities and all KL integrands used in the proof are measurable. A solver may invoke the standard parameter-integration fact for these densities and need not reproduce the reference proof's nonnegative KL-integrand representation. Mere kernel measurability on an unrestricted latent measurable space would not suffice, and finiteness of the four displayed divergences alone would not justify a conditioning-order change for another divergence.

The public assumptions provide the needed likelihood integrability and finite averaged divergences. A solver need not reproduce the reference proof's negative-log-part estimate, but must not rely on an unjustified cancellation of infinities. Interpret conditional statements almost everywhere. No additional proof is needed for null conditioning events or zero mixture weights when the argument is formulated through the stated kernels, densities, and integrals.

Incorrect conditioning, omission of the label average, or reversing either residual sign is theorem-critical unless independently corrected later. No result about parameter estimation, finite-sample prediction, Gaussian variational families, or the sign of \(R(q)\) is requested.
