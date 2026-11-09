# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Derive a simultaneous multi-task PAC-Bayes-Chernoff inequality, including fixed-parameter factorization over all independent observations, a justified exponential-moment estimate, change of measure for arbitrary data-dependent posteriors, and validity for a shared positive tuning parameter on one event. For the transform route, justify the passage from the gap tail bound to the transform tail and retain the initial 1 in the survival integral. Integrate the defining transform inequality, or correctly use expectation of a supremum; do not treat theta-dependent transforms as one fixed function in Jensen's inequality.
- **2 points:** Apply the CGF hypothesis and optimize to obtain the population-gradient bound M^{-1} sqrt(2KG), with G=sum_i m_i C_i E_rho E_{D_i}||nabla_x ell_i||^2. Use log(M/epsilon) at generic failure probability epsilon and epsilon=delta/2 to obtain the stated K. Include G=0 by a limiting argument or another valid treatment.
- **3 points:** Prove the empirical-to-population gradient-energy control using the weighted transformed losses C_i||nabla_x ell_i||^2 in [0,C_iL_i]. Justify their centered CGF bound lambda^2 C_i^2 L_i^2/8, apply the simultaneous bound at failure probability delta/2, identify their normalized gap as (G-Ghat)/M, and optimize K/lambda+lambda V/8 to obtain sqrt(VK/2), where V=sum_i m_i C_i^2L_i^2.
- **2 points:** Combine the two events by a union bound, obtain exactly the public inequality using L=sqrt(2V), and maintain posterior uniformity. Treat negative-infinite defined gaps and infinite-KL posteriors consistently with the public conventions; no finite posterior expectations of the two risks separately are required.

# Evaluator Notes

Accept a complete valid alternative proof, including a stronger bound that demonstrably implies the target. Do not require the reference proof's incidental presentation choices, a particular name for the change-of-measure argument, or explicit use of a generalized inverse.

A correct standard variational inequality or bounded-variable exponential-moment theorem may be cited with its applicable statement and verified hypotheses. Merely naming a specialized PAC-Bayes-Chernoff or Pareto argument without establishing the required moment estimate is not a completed proof step. Likewise, obtaining an inequality for each fixed tuning parameter on possibly different events does not justify sample-dependent optimization over that parameter.

The change-of-measure event must support arbitrary sample-dependent posteriors. Independence is needed for transformed observations only with the parameter fixed, not after choosing a posterior from the data. A union bound over the two final events does not require those events to be independent.

Treat omission of the uniform change-of-measure mechanism or empirical gradient-concentration step as theorem-critical. Routine omissions concerning a limiting zero-energy case, when readily repairable and not concealing another error, fit the 8-9 range rather than automatic rejection. Do not require bounded responses, uniform input distributions, finite KL for every posterior, or other assumptions absent from the public task.
