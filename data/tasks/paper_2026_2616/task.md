# Problem

## Setup

Let X be a nontrivial separable real Hilbert space (X != {0}). For p >= 1, let P_p(X) denote the Borel probability measures P with finite p-th moment, and let W_p be the p-Wasserstein distance. For m in X and a self-adjoint positive trace-class operator K on X, N(m,K) denotes the corresponding Gaussian measure; require K != 0. A finite Gaussian mixture is a law Q = sum_{j=1}^m pi_j N(m_j,K_j), where pi_j >= 0, sum_j pi_j = 1, and every K_j is self-adjoint, positive, trace class, and nonzero.

Let kappa : X x X -> R be a continuous positive-definite kernel with sup_x kappa(x,x) <= 1. Let H_kappa be its RKHS, let mu_P = E_{X~P}[kappa(X,.)], and define MMD_kappa(P,Q) = ||mu_P - mu_Q||_{H_kappa} (equivalently by the usual three kernel-expectation terms).

## Task

Prove the following integrated theorem.

1. For every p >= 1, finite Gaussian mixtures with nonzero trace-class covariance operators are dense in P_p(X) under W_p: for every P in P_p(X) and every delta > 0, there is such a mixture Q with W_p(P,Q) < delta.

2. For every probability measure P on X and every integer K >= 1, there exists a Gaussian mixture Q_K with exactly K components, each covariance self-adjoint, positive, trace class, and nonzero, such that
   MMD_kappa(P,Q_K) <= 2/sqrt(K).
