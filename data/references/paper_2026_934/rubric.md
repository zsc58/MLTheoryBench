# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Derives the environment-wise squared-error decomposition into an environment-invariant structural term \(R_0(\beta)\) and \(\beta^\top M_e\beta\), justifying invariance of the structural law and cancellation of the cross term by independence and centering.
- **2 points:** Averages the risk decomposition over the labeled subset \(\mathcal L\), obtaining \(R_0(\beta)+\beta^\top\bar M\beta\), and separately identifies the feature-mean covariance \(H\) with the perturbation-mean covariance \(V\) using all \(p\) training environments.
- **3 points:** Establishes the exact supremum over the uncertainty class. This includes explaining why the environment family realizes the needed positive-semidefinite second moment, proving the quadratic upper bound for \(0\preceq A\preceq\gamma V\), and attaining it with \(A=\gamma V\). Realizing only this endpoint suffices; proving the full moment-image equality is not mandatory.
- **2 points:** Combines the preceding steps into the stated pointwise objective identity and concludes minimax optimality of every specified minimizer.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The decomposition, correct distinction between labeled and all-training averages, exact PSD supremum, and pointwise objective identity are theorem-critical; merely naming a robustness or regularization principle is insufficient.

The source of moment attainability is the stipulated availability of every finite-second-moment perturbation law. An explicit finite-support construction, a centered Gaussian with the prescribed covariance, or an equivalent justified realization is acceptable. Do not demand a particular distributional construction.

Do not accept a proof only for \(\mathcal L=\mathcal E^{\mathrm{tr}}\). The loss and baseline moment use \(\mathcal L\), while \(H\) and \(V\) use all training environments. Do not assume that perturbations have zero mean, or that \(H\), \(V\), or the objective Hessian is invertible.

A general argument that includes \(\gamma=0\), \(p=1\), singleton labeled subsets, and singular or zero covariance needs no separate case enumeration. The minimax consequence concerns every minimizer, not a unique coefficient. An additional existence proof is welcome but is not required when the solver correctly proves the requested consequence for every specified minimizer; the reference proof verifies existence without a nonsingularity assumption.
