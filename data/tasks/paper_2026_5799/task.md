# Problem

## Setup

Consider a deterministic full-batch optimizer for an autonomous gradient-flow system, with parameter vectors in \(\mathbb R^d\), where \(d\ge1\) is a finite integer. Steps are indexed by \(t=0,1,2,\ldots\). The optimizer state includes the parameter vector \(\theta_t\) and all optimizer memory, including any moment estimates and cached gradients.

At step \(t\), with current state and step size \(h_t\), the optimizer's fixed deterministic stage routine supplies four finite stage gradient vectors \(k_{1,t},k_{2,t},k_{3,t},k_{4,t}\in\mathbb R^d\). Form the third-order and embedded second-order gradient combinations
\[
g_{3,t}=\tfrac29 k_{1,t}+\tfrac13 k_{2,t}+\tfrac49 k_{3,t},\qquad
g_{2,t}=\tfrac7{24}k_{1,t}+\tfrac14 k_{2,t}+\tfrac13 k_{3,t}+\tfrac18 k_{4,t}.
\]
Define the normalized error by
\[
e_t=\operatorname{RMS}_i\!\left(\frac{h_t(g_{3,t,i}-g_{2,t,i})}{\mathit{atol}+\rho\lvert\theta_{t,i}\rvert}\right),
\qquad
\operatorname{RMS}_i(x_i)=\left(\frac1d\sum_{i=1}^d x_i^2\right)^{1/2},
\]
where \(\mathit{atol}>0\) and \(\rho>0\) are finite real numbers. The controller uses
\[
\phi_t=\min\!\bigl(\max(0.9e_t^{-1/3},0.5),2.0\bigr),\qquad
h_{t+1}=\operatorname{clip}(h_t\phi_t,[\ell,h_{\max}]),
\]
where
\[
\operatorname{clip}(x,[a,b])=\min\{\max\{x,a\},b\},
\qquad 0<\ell\le h_0\le h_{\max}<\infty.
\]
At \(e_t=0\), interpret \(e_t^{-1/3}\) as \(+\infty\), so that the upper cap applies.

When comparing tolerances, all runs use the same initial optimizer state, initial step size, data, optimizer routine, and hyperparameters other than \(\rho\), and execute deterministically. Apart from its appearance in \(e_t\) and the controller, \(\rho\) does not enter the stage routine or the state/parameter update: conditional on the current state and step size, these are the same deterministic computations for every \(\rho\). Every step updates the state using its current step size \(h_t\); the controller specifies the next step size \(h_{t+1}\).

## Task

Prove the following theorem. If
\[
e_t\le(0.9/2)^3
\]
for every step \(t\), then \(\phi_t=2.0\) for every \(t\), the step sizes satisfy
\[
h_t=\min\{2^t h_0,h_{\max}\},
\]
and \(h_t=h_{\max}\) for all \(t\ge\lceil\log_2(h_{\max}/h_0)\rceil\). Moreover, any two tolerances \(\rho_1,\rho_2\) for which this same bound holds at every step produce identical (bit-for-bit under deterministic execution) parameter iterates.
