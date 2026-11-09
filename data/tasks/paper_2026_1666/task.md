# Problem

## Setup

Consider a graph-based node-classification model. For each node, let H be its prediction representation and Y its label, taking values in a finite label set. The representation has latent components U (intra-class) and V (inter-class). Let Z be a graph-level, pre-treatment adjustment variable, for example a subgraph.

Let p_theta denote observational distributions and conditional kernels of an acyclic structural causal model, and let p_theta(y | do(H=h)) denote its label distribution under structural intervention on H. Assume Z satisfies the standard backdoor criterion for the effect of H on Y: Z contains no descendant of H, and every path from H to Y that begins with an arrow into H is blocked by Z.

All displayed probability kernels are measurable and normalized, with densities or mass functions relative to fixed dominating measures. The label kernels are probability mass functions. Fix versions of the observational conditional kernels. For observationally almost every (h,z), the latent model satisfies

p_theta(u,v | h,z) = p_theta(u | h)p_theta(v | h),

and the label distribution conditional on all the variables is

p_theta(y | h,u,v,z) = p_theta(y | h,u,z).

Let q_phi(z | h), q_phi(u | h), and q_phi(v | h) be measurable normalized posterior approximations, and set

q_phi(z,u,v | h) = q_phi(z | h)q_phi(u | h)q_phi(v | h).

Write P_theta^Z for the observational marginal law of Z and P_theta^{Z|h} for its observational conditional law given H=h. Call (theta, phi, h, y) admissible when:

- P_theta^Z is absolutely continuous with respect to P_theta^{Z|h};
- p_theta(y | h,u,z) is positive q_phi(z | h)q_phi(u | h)-almost everywhere;
- each of q_phi(z | h), q_phi(u | h), and q_phi(v | h) is absolutely continuous with respect to its corresponding model factor p_theta(z), p_theta(u | h), and p_theta(v | h);
- KL(q_phi(z | h) || p_theta(z)), KL(q_phi(u | h) || p_theta(u | h)), and KL(q_phi(v | h) || p_theta(v | h)) are finite; and
- p_theta(y | do(H=h)) > 0 and E_{q_phi(z | h)q_phi(u | h)}[|log p_theta(y | h,u,z)|] < infinity.

Here KL(Q || P) = integral log(dQ/dP) dQ when Q is absolutely continuous with respect to P, and is infinity otherwise. Products of distributions in expectations denote product measures.

## Task

Prove that the causal prediction objective is identifiable by adjustment and admits the following variational lower bound. For every theta, for p_theta(H)-almost every h, and for every phi and label y for which (theta, phi, h, y) is admissible,

p_theta(y | do(H=h)) = integral p_theta(y | h,z)p_theta(z) dz,

and, writing ell_theta(h,y) = log p_theta(y | do(H=h)),

ell_theta(h,y) >=
E_{q_phi(z | h)q_phi(u | h)}[log p_theta(y | h,u,z)]
- KL(q_phi(z | h) || p_theta(z))
- KL(q_phi(u | h) || p_theta(u | h))
- KL(q_phi(v | h) || p_theta(v | h)).

For discrete variables, replace integrals by the corresponding sums.
