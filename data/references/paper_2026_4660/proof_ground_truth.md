# Reference Proof

## Proof Structure

Follow the realized off-manifold trajectory, subtract its endpoint-specific constant displacement velocity, establish that the resulting deviation has zero temporal mean, and apply the Poincare-Wirtinger inequality to convert its energy excess into a lower bound on integrated squared acceleration.

## Complete Proof

Let gamma(t) = psi_t(x_0) and w(t) = v_t(gamma(t), tilde c). The flow equation gives gamma'(t) = w(t), gamma(0) = x_0, and gamma(1) = x_hat_1. Define the constant endpoint velocity u = x_hat_1 - x_0 and the deviation epsilon(t) = w(t) - u.

Since gamma(1) - gamma(0) = integral_0^1 gamma'(t) dt = integral_0^1 w(t) dt = u, we have integral_0^1 epsilon(t) dt = 0. By the assumed trajectory regularity, epsilon belongs to H^1([0,1]; R^d). The endpoint-relative excess assumption is

integral_0^1 ||epsilon(t)||_2^2 dt >= Delta_local > 0.

The Poincare-Wirtinger inequality for zero-mean H^1 vector-valued functions on [0,1] gives

integral_0^1 ||epsilon(t)||_2^2 dt <= (1/pi^2) integral_0^1 ||epsilon'(t)||_2^2 dt.

Because u is constant, epsilon'(t) = w'(t) = d/dt v_t(gamma(t), tilde c). Therefore, with kappa = integral_0^1 ||d/dt v_t(psi_t(x_0), tilde c)||_2^2 dt, the preceding inequalities imply

Delta_local <= integral_0^1 ||epsilon(t)||_2^2 dt <= kappa/pi^2,

so kappa >= pi^2 Delta_local > 0. This proves the claimed quantitative nonzero integrated curvature for the realized off-manifold trajectory.
