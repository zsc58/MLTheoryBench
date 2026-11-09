# Problem

## Classification and training experiment

Let \(\mathcal X\subseteq\mathbb R^p\) be a measurable feature space with its Euclidean distance. Conditional on \(Y=i\), let \(X\sim P_i\), where \(P_i\) has density \(p_i\) with respect to a common dominating measure. The priors satisfy \(\pi_i>0\) and \(\pi_0+\pi_1=1\). Assume \(P_1\ll P_0\), and define, up to null sets,
\[
L=\frac{dP_1}{dP_0},\qquad \Lambda=\frac{L}{1+L}.
\]
For a measurable real-valued score s, define
\[
\operatorname{AUC}(s)=P(s(X_1)>s(X_0))+\tfrac12P(s(X_1)=s(X_0)),
\]
where \(X_1\sim P_1\) and \(X_0\sim P_0\) are independent. Evaluation always uses these original class distributions, not the synthetic distribution.

Fix integers \(n_0>n_1\ge1\) and \(\tilde n\ge0\), and write \(n=n_0+n_1\), \(N=n+\tilde n\). Observe mutually independent samples
\[
X_j^{(i)}\sim P_i\quad(1\le j\le n_i),\qquad
\widetilde X_j\sim P_{\rm syn}\quad(1\le j\le\tilde n).
\]
The distribution \(P_{\rm syn}\) is fixed for this experiment and does not depend on the classifier-training observations.

Let \(\Theta\subseteq\mathbb R^d\) be convex and \(s_\theta\) a jointly measurable score family. Write \(\ell(\theta;x,y)=\ell(s_\theta(x),y)\). The loss is defined on all score values used here and is strictly proper on probability-valued scores: for every \(\eta\in[0,1]\), the function \(u\mapsto\eta\ell(u,1)+(1-\eta)\ell(u,0)\) on \([0,1]\) is uniquely minimized at \(u=\eta\).

Define
\[
R_\alpha(\theta)=(1-\alpha)E_{P_0}\ell(\theta;X,0)+\alpha E_{P_1}\ell(\theta;X,1),\qquad0<\alpha<1,
\]
\[
\alpha_{\rm raw}=\frac{n_1}{n},\qquad
\alpha_{\rm aug}=\frac{n_1+\tilde n}{N},\qquad
R_{\rm raw}=R_{\alpha_{\rm raw}},
\]
and
\[
R_{\rm aug}(\theta)=\frac{n_0}{N}E_{P_0}\ell(\theta;X,0)+\frac{n_1}{N}E_{P_1}\ell(\theta;X,1)+\frac{\tilde n}{N}E_{P_{\rm syn}}\ell(\theta;X,1).
\]
The ideal augmented risk is \(R_{\alpha_{\rm aug}}\), which uses the true positive distribution throughout. Let \(\theta_\alpha^*\) minimize \(R_\alpha\), let \(\theta_{\rm raw}^*=\theta_{\alpha_{\rm raw}}^*\), and let \(\theta_{\rm aug}^*\) minimize the actual risk \(R_{\rm aug}\).

The empirical risks are
\[
\widehat R_{\rm raw}(\theta)=\frac1n\left[\sum_{j=1}^{n_0}\ell(\theta;X_j^{(0)},0)+\sum_{j=1}^{n_1}\ell(\theta;X_j^{(1)},1)\right],
\]
\[
\widehat R_{\rm aug}(\theta)=\frac1N\left[\sum_{j=1}^{n_0}\ell(\theta;X_j^{(0)},0)+\sum_{j=1}^{n_1}\ell(\theta;X_j^{(1)},1)+\sum_{j=1}^{\tilde n}\ell(\theta;\widetilde X_j,1)\right].
\]
Let \(\widehat\theta_{\rm raw}\) and \(\widehat\theta_{\rm aug}\) be measurable global minimizers over \(\Theta\). All stated minimizers exist, and the population risks and expectations defining their gradients and Hessians are finite where used. An empty synthetic sum is zero.

## Upper-bound assumptions

All constants below are fixed regularity constants for the experiments under consideration. Vector norms are Euclidean, \(\|\cdot\|_{\rm op}\) is operator norm, and gradients and Hessians are with respect to \(\theta\).

1. **Population alignment and score regularity.** For every \(\alpha\in(0,1)\),
\[
s_{\theta_\alpha^*}=g_\alpha\circ\Lambda\quad(P_0+P_1)\text{-almost everywhere}
\]
for a strictly increasing function \(g_\alpha\). For all \(\theta,\theta'\in\Theta\) and x,
\[
|s_\theta(x)-s_{\theta'}(x)|\le L_s\|\theta-\theta'\|.
\]
There are \(C_{ac},t_0>0\) such that, for the raw, actual augmented, and ideal augmented population scores, and almost surely for the two empirical scores, there are no cross-class ties and
\[
P(|s(X_1)-s(X_0)|\le t)\le C_{ac}t,\qquad0\le t\le t_0.
\]
For an empirical score this probability is over independent evaluation observations conditional on its training data, with the same constants.

2. **Convexity and local empirical-risk regularity.** For every \((x,y)\), \(\theta\mapsto\ell(\theta;x,y)\) is convex and twice continuously differentiable. There are \(\lambda,r,L_H,B_H,B>0\) such that the closed radius-r balls around \(\theta_{\rm raw}^*\) and \(\theta_{\rm aug}^*\) lie in \(\operatorname{int}\Theta\), \(L_Hr\le\lambda/4\), and
\[
\nabla^2R_{\rm raw}(\theta_{\rm raw}^*)\succeq\lambda I,
\qquad
\nabla^2R_{\rm aug}(\theta_{\rm aug}^*)\succeq\lambda I.
\]
At either center, each coordinate of \(\nabla\ell(\theta_*;X,i)\) is bounded in absolute value by B for \(X\sim P_i\), \(i=0,1\). This also holds at \(\theta_{\rm aug}^*\) for \(X\sim P_{\rm syn}\), \(y=1\).

For either center \(\theta_*\) and \(\|\theta-\theta_*\|\le r\),
\[
\|\nabla^2\ell(\theta;x,y)-\nabla^2\ell(\theta_*;x,y)\|_{\rm op}
\le L_H\|\theta-\theta_*\|
\]
almost surely under \((P_0,0)\), \((P_1,1)\), and \((P_{\rm syn},1)\). At either center and for \(i=0,1\),
\[
\|\nabla^2\ell(\theta_*;X,i)-E_{P_i}\nabla^2\ell(\theta_*;X,i)\|_{\rm op}\le B_H
\quad P_i\text{-almost surely}.
\]
The corresponding centered-Hessian bound holds at \(\theta_{\rm aug}^*\) under \(P_{\rm syn}\) with label 1.

3. **Synthetic discrepancy and ideal-risk curvature.** Define
\[
W_1(P,Q)=\inf_{\Gamma\in\Pi(P,Q)}\int\|x-z\|\,d\Gamma(x,z),
\]
where \(\Pi(P,Q)\) is the set of probability couplings. Assume
\[
W_1(P_{\rm syn},P_1)\le\varepsilon_{\rm syn},\qquad\varepsilon_{\rm syn}\ge0,
\]
and \(x\mapsto\nabla\ell(\theta_{\rm aug}^*;x,1)\) is \(L_g\)-Lipschitz in Euclidean norm. Put \(F=R_{\alpha_{\rm aug}}\) and \(\theta_I=\theta_{\alpha_{\rm aug}}^*\). There are \(L_\alpha,\mu>0\) and a neighborhood of \(\theta_I\) containing \(\theta_{\rm aug}^*\) on which
\[
F(\theta)-F(\theta_I)\ge L_\alpha\|\theta-\theta_I\|^2,
\]
\[
F(\theta_I)\ge F(\theta)+\nabla F(\theta)^T(\theta_I-\theta)+\frac\mu2\|\theta_I-\theta\|^2.
\]

## Local family for the lower bound

Consider a family \(\{(P_{0,\eta},P_{1,\eta}):\eta\in\mathcal H\}\), where \(\mathcal H\subseteq\mathbb R^d\). Its unknown data-generating parameter \(\eta\) is distinct from the fitted score parameter \(\theta\). There are \(\eta_0\in\mathcal H\) and \(r_0>0\) such that
\[
U=\{\eta:\|\eta-\eta_0\|<r_0\}\subseteq\mathcal H.
\]
The class densities \(p_{y,\eta}\) are with respect to a common measure \(\nu\), are jointly measurable, and for every x are continuously differentiable in \(\eta\) on U. Assume \(P_{1,\eta}\ll P_{0,\eta}\), and write
\[
L_\eta=\frac{dP_{1,\eta}}{dP_{0,\eta}},\qquad
\Lambda_\eta=\frac{L_\eta}{1+L_\eta},\qquad
S_y(x;\eta)=\nabla_\eta\log p_{y,\eta}(x)
\]
on positive-density sets. Values on null sets do not affect the definitions.

There are finite constants \(I_0,I_1\ge0\) and \(B_{lr}\ge1\) such that
\[
\sup_{\eta\in U}E_{P_{y,\eta}}\|S_y(X;\eta)\|^2\le I_y,\qquad y=0,1,
\]
and, for all \(\eta,\eta'\in U\), \(t\in[0,1]\), and \(\eta_t=\eta'+t(\eta-\eta')\),
\[
p_{y,\eta_t}(x)\le B_{lr}p_{y,\eta'}(x)\quad\nu\text{-almost everywhere},\qquad y=0,1.
\]

Define
\[
\Delta_\eta(x,z)=L_\eta(x)-L_\eta(z),\qquad
Q_\eta=P_{0,\eta}\otimes P_{0,\eta},\qquad Q_0=Q_{\eta_0}.
\]
Assume \(Q_\eta\ge c_QQ_0\) as measures on \(\mathcal X^2\) for every \(\eta\in U\), with \(c_Q>0\). There are \(\gamma\in(0,1)\), \(c_{rk}>0\), and \(h_0>0\) such that for every \(0<h\le h_0\) with \(h<r_0\), and every \(u,u'\in\mathbb S^{d-1}\) satisfying \(\|u-u'\|\ge\gamma\), the set
\[
\mathcal R_h(u,u')=\{(x,z):\Delta_{\eta_0+hu}(x,z)\Delta_{\eta_0+hu'}(x,z)<0\}
\]
satisfies
\[
\int_{\mathcal R_h(u,u')}\min\{|\Delta_{\eta_0+hu}(x,z)|,|\Delta_{\eta_0+hu'}(x,z)|\}\,dQ_0(x,z)\ge c_{rk}h.
\]

For this family, \(\operatorname{AUC}_\eta\) uses independent evaluation observations from \(P_{1,\eta}\) and \(P_{0,\eta}\). An estimator in the lower bound observes only the class-stratified training sample with law
\[
\mathbb P_\eta^{(n)}=P_{0,\eta}^{\otimes n_0}\otimes P_{1,\eta}^{\otimes n_1}.
\]
It outputs a jointly measurable real-valued score and may use auxiliary randomness independent of the data and the unknown parameter. The expectation \(E_\eta\) includes training and auxiliary randomness. No synthetic observations are supplied in this lower-bound experiment.

## Task

Prove that there is \(C>0\), depending only on \(C_{ac}\) and \(t_0\) apart from numerical factors, with the following property. For every \(\delta\in(0,1)\), there is a finite sample-size threshold depending only on \(d,\delta,B,B_H,\lambda,r,L_H\) such that, when \(n_0,n_1\) exceed this threshold and the upper-bound assumptions hold, the following inequalities hold simultaneously with probability at least \(1-\delta\):
\[
\operatorname{AUC}(\Lambda)-\operatorname{AUC}(s_{\widehat\theta_{\rm raw}})
\le C\frac{L_sB}{\lambda}\sqrt{\frac{d\log(6d/\delta)}n},
\]
\[
\operatorname{AUC}(\Lambda)-\operatorname{AUC}(s_{\widehat\theta_{\rm aug}})
\le C\frac{L_sB}{\lambda}\sqrt{\frac{d\log(6d/\delta)}N}
+C\frac{L_sL_g}{\sqrt{\mu L_\alpha}}\frac{\tilde n}{N}\varepsilon_{\rm syn}.
\]

Also prove that the local-family assumptions imply the existence of constants \(a,c>0\) and a dimension threshold \(d_0\), depending only on the stated family regularity and separation constants, such that for \(d\ge d_0\) and sample sizes satisfying
\[
a\sqrt{d/n}\le h_0,\qquad a\sqrt{d/n}<r_0,
\]
every estimator in the specified stratified experiment satisfies
\[
\sup_{\eta\in\mathcal H}E_\eta\left[\operatorname{AUC}_\eta(\Lambda_\eta)-\operatorname{AUC}_\eta(\widehat s)\right]\ge c\sqrt{d/n}.
\]
The constants are independent of the sample sizes and the estimator. No dimension-uniform control of family regularity constants is assumed. Interpret the augmentation variance–bias tradeoff and the matching \(n^{-1/2}\) dependence at fixed dimension, retaining the displayed dimension factors. A uniform comparison of the upper and lower bounds on the local family is understood only where the upper-bound assumptions also hold uniformly on that family.
