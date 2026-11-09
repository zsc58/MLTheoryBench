# Reference Proof

## Proof Structure

Use the triangle inequality to separate the distance from the invariant law to the data law into a model-to-empirical term and the empirical sampling term. The invariant fixed-point identity and contraction of the transfer operator then turn the model-to-empirical term into a contraction multiple of itself plus the one-step empirical residual. Rearranging and substituting gives the claimed bound.

## Complete Proof

Fix n and theta, and write kappa = kappa_theta, pi = pi_theta, r = r_n(theta), and rho_hat = rho_n. Since pi is invariant, T_theta(pi) = pi. By the triangle inequality and then contractivity,

W2(pi, rho_hat)
  = W2(T_theta(pi), rho_hat)
  <= W2(T_theta(pi), T_theta(rho_hat)) + W2(T_theta(rho_hat), rho_hat)
  <= kappa W2(pi, rho_hat) + r.

Therefore (1-kappa) W2(pi, rho_hat) <= r. Because kappa < 1,

W2(pi, rho_hat) <= r/(1-kappa).

A second application of the triangle inequality gives

W2(pi, rho) <= W2(pi, rho_hat) + W2(rho_hat, rho)
             <= r_n(theta)/(1-kappa_theta) + s_n.

Using the definitions of the three errors, this is exactly

W2(pi_theta, rho) <= r_n(theta)/(1-kappa_theta) + s_n,

for every n and theta under the stated assumptions (and hence for every sample realization for which the empirical measure lies in P2(X)).
