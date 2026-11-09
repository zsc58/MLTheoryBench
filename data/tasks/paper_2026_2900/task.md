# Problem

## Setup

Let D be a positive integer and let 0<epsilon<=T<infinity. For each t in [epsilon,T], let p_t be a positive C^1 probability density on R^D, with score s_t=grad log p_t. Let v_t:R^D->R^D be C^1 in its spatial variable and be a probability-flow field: the ODE dx_t/dt=v_t(x_t) transports the densities p_t.

Let Y be an R^D-valued random vector with the target law, and let Z be a standard Gaussian vector independent of Y. Assume one of the following settings, where the displayed random vectors specify the marginal densities p_t.

- **(D) Diffusion:** p_t is the density of nu_t Y+eta_t Z, where nu_t is a finite real scalar and eta_t>0. The probability-flow field is v_t=f_t-(g_t^2/2)s_t, where g_t is a finite nonnegative scalar and either f_t(x)=-beta_t x/2, with finite real beta_t, or f_t(x)=0.
- **(F) Flow:** p_t is the density of alpha_t Y+sigma_t Z, where alpha_t is a finite real scalar and sigma_t>0.

Let H be a class of C^1 scalar functions on R^D. There is a nonnegative integer q such that, for each delta in H, a finite constant C_delta satisfies

\[
 |\delta(x)|+\|\nabla\delta(x)\|\le C_\delta(1+\|x\|)^q
 \qquad(x\in\mathbb R^D).
\]

For each t there are a nonnegative integer m_t and a finite constant C_t such that

\[
 \|v_t(x)\|\le C_t(1+\|x\|)^{m_t}
 \qquad(x\in\mathbb R^D),
 \qquad
 E[(1+\|Y\|)^{D-1+q+m_t}]<\infty.
\]

Define

\[
 A_{p_t}v_t=\operatorname{div}v_t+\langle v_t,s_t\rangle,
 \qquad b_t=-\langle v_t,s_t\rangle,
 \qquad r_t=A_{p_t}v_t.
\]

Thus div v_t=b_t+r_t. Assume r_t belongs to L^2(p_t) and H is contained in L^2(p_t) for every t, where L^2(p_t) consists of functions with finite integral of their square against p_t.

## Task

Prove that, for every t in [epsilon,T] and every delta in H,

\[
 E_{p_t}[\delta(X)r_t(X)]
 =-E_{p_t}[\langle\nabla\delta(X),v_t(X)\rangle].
\]

Consequently, prove that the computable functional

\[
 L_t(\delta)=E_{p_t}[\delta(X)^2+2\langle\nabla\delta(X),v_t(X)\rangle]
\]

differs from the residual-regression risk E_{p_t}[(delta-r_t)^2] only by the delta-independent constant E_{p_t}[r_t^2]. Here E_{p_t} means expectation under X with density p_t.

Show that these two objectives have the same population minimizers over H, whenever minimizers exist. If r_t belongs to H, show that a minimizer exists, that every minimizer delta_t^* recovers r_t in L^2(p_t), and that

\[
 b_t+\delta_t^*=\operatorname{div}v_t
 \quad p_t\text{-almost surely}.
\]

The conclusions must hold in both settings (D) and (F).
