# Problem

## Setup

Fix an input \(x\), and let an embedding model produce \(z_t(x)=f(x;\theta_t)\in\mathbb R^d\) after optimizer step \(t\). Let \(S_t\) denote the full current training state, including \(\theta_t\) and any optimizer state. Assume this state process has a stationary law \(\pi\), and work under that law. Write \(R_t=\|z_t(x)\|\), assume \(R_t>0\) almost surely, and set \(\hat z_t=z_t(x)/R_t\).

At each step, with the current training state fixed, draw a fresh minibatch \(B_t\) of \(N\geq1\) i.i.d. pairs from a distribution \(P_{\rm data}\). Training uses a contrastive loss \(L\) satisfying:

1. **Scale invariance:** multiplying any individual embedding by any factor \(\alpha>0\) leaves \(L\) unchanged.
2. **Per-sample decomposition:** \(L=(1/N)\sum_{k=1}^N L_k\), where each \(L_k\) may depend on other batch members through shared minibatch similarities.

Embeddings used in normalized similarities are nonzero. Use a decoupled update with learning rate \(\eta>0\):
\[
\theta_t^+=\theta_t+U_t,\qquad
\theta_{t+1}=\theta_t^++\Delta\theta_{\rm wd}.
\]
Here \(U_t\) is the task update computed from the current state and minibatch. Define
\[
z_t^+(x)=f(x;\theta_t^+),\qquad
\Delta z_{\rm task}=z_t^+(x)-z_t(x),\qquad
\Delta z_{\rm wd}=z_{t+1}(x)-z_t^+(x).
\]
Assume these random variables are measurable and
\[
\mathbb E_\pi[R_t^2]<\infty,\qquad
\mathbb E_{\pi,B_t}[\|\Delta z_{\rm task}\|^2]<\infty.
\]

First define moments conditional on the full current state:
\[
\mu_t=\mathbb E[R_t\Delta z_{\rm task}\mid S_t],\qquad
C_t=\operatorname{Cov}(R_t\Delta z_{\rm task}\mid S_t).
\]
At each fixed state used below, these local moments are computed by integrating the prescribed fresh-minibatch law with the update functions evaluated at that state.

Let \(Q_R\) be a fixed version of the conditional distribution of the stationary training state given \(R_t=R\). All radius-conditioned evaluations use the joint experiment that draws a state from \(Q_R\), draws a fresh minibatch from the prescribed distribution, and applies the specified update. Only use radii \(R>0\) for which
\[
Q_R\bigl(\{s:\|f(x;\theta(s))\|=R\}\bigr)=1,
\]
where \(\theta(s)\) is the parameter component of state \(s\), and for which this joint experiment satisfies
\[
\mathbb E[\|\Delta z_{\rm task}\|^2+R_{t+1}^2\mid R_t=R]<\infty.
\]
These requirements apply in particular at the equilibrium radius selected below, even if that radius has probability zero under the stationary radius law.

For these radii, define the stationary radius-conditioned quantities by
\[
\widetilde D_R=\mathbb E[\hat z_t^\top\mu_t\mid R_t=R],\qquad
\widetilde V_R^2=\mathbb E[\operatorname{tr}C_t\mid R_t=R],
\]
\[
M_R^2=\mathbb E[\|\mu_t\|^2\mid R_t=R],\qquad
\Sigma_R^2=M_R^2+\widetilde V_R^2.
\]
The latter expectations average over the stationary training state, rather than fixing the embedding direction.

Define the effective radial damping \(\bar\lambda_{\rm rad}(R)\) by
\[
\mathbb E[\|z_{t+1}(x)\|^2-\|z_t^+(x)\|^2\mid R_t=R]
=-2\eta\bar\lambda_{\rm rad}(R)R^2.
\]
Thus it measures the actual post-task decay contribution, including its interaction with the task update, after stationary radius conditioning.

Select an equilibrium radius \(R_{\rm eq}>0\) in the stated evaluation domain at which the stated conditional moments are finite and
\[
\mathbb E[R_{t+1}^2-R_t^2\mid R_t=R_{\rm eq}]=0.
\]
Assume \(\bar\lambda_{\rm rad}(R)>0\) for the radii under consideration near \(R_{\rm eq}\). Define
\[
D_*:=\frac{\widetilde D_{R_{\rm eq}}}{\eta\bar\lambda_{\rm rad}(R_{\rm eq})},\qquad
V_*^2:=\frac{\Sigma_{R_{\rm eq}}^2}{\eta\bar\lambda_{\rm rad}(R_{\rm eq})}.
\]

## Task

Prove that the equilibrium norm obeys
\[
2R_{\rm eq}^4-2D_*R_{\rm eq}^2-V_*^2=0,
\]
and hence
\[
R_{\rm eq}^2=\frac{D_*+\sqrt{D_*^2+2V_*^2}}{2}.
\]
With \(D_*\) and \(V_*^2\) evaluated at the selected radius and held fixed, show that the displayed value is the unique nonnegative solution of the quadratic in \(R_{\rm eq}^2\), and is strictly positive when \(V_*^2>0\). This asks for algebraic uniqueness with these evaluated coefficients, not uniqueness of the selected radius among zeros of a radius-dependent conditional drift.

Establish the following limiting interpretations along families satisfying the setup, writing \(V_*:=\sqrt{V_*^2}\):

- If \(D_*\) remains bounded and \(V_*\to\infty\), then \(R_{\rm eq}^2\sim V_*/\sqrt2\).
- If \(D_*>0\) and \(V_*^2/D_*^2\to0\), then \(R_{\rm eq}^2=D_*+O(V_*^2/D_*)\).
- If \(D_*<0\) and \(V_*^2/|D_*|^2\to0\), then \(R_{\rm eq}^2\sim V_*^2/(2|D_*|)\).
