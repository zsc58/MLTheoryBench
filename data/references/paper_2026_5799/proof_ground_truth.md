# Reference Proof

## Proof Structure

Show that the assumed error bound makes the controller's upper growth cap active at every step. The step-size recursion therefore doubles until clipping at the upper limit, yielding finite-time fixation. Finally, use determinism and the fact that tolerance enters only through the error/controller to inductively establish identical trajectories for any two tolerances satisfying the bound.

## Complete Proof

Let \(e_t\) denote the normalized error at step \(t\). For \(e_t>0\), the hypothesis gives
\[
e_t\le (0.9/2)^3,
\]
so, because \(x\mapsto x^{-1/3}\) is decreasing on \((0,\infty)\),
\[
0.9\,e_t^{-1/3}\ge 0.9\,((0.9/2)^3)^{-1/3}=2.
\]
When \(e_t=0\), use the controller's stated extended-value convention \(0^{-1/3}=+\infty\), and the same conclusion holds. Hence
\[
\phi_t=\min\{\max\{0.9e_t^{-1/3},0.5\},2.0\}=2.0.
\]
Therefore
\[
h_{t+1}=\operatorname{clip}(2h_t,[\ell,h_{\max}]).
\]
Since \(h_t\ge\ell>0\), this is \(h_{t+1}=\min\{2h_t,h_{\max}\}\). Induction gives
\[
h_t=\min\{2^t h_0,h_{\max}\}\quad(t\ge0).
\]
Let \(N=\lceil\log_2(h_{\max}/h_0)\rceil\). Because \(h_0\le h_{\max}\), \(N\ge0\), and \(2^N h_0\ge h_{\max}\). Thus \(h_N=h_{\max}\), after which the recursion keeps \(h_t=h_{\max}\) for every \(t\ge N\).

Now take two tolerances \(\rho_1,\rho_2\) for which the error bound holds at every step. The preceding argument gives the same multiplier and step-size sequence in both runs. With common initial state, data, and hyperparameters, the deterministic state/parameter update is a function only of the current state and step size, while \(\rho\) enters only through the error/controller. Induction on \(t\) therefore gives equal states and parameters at every step; under deterministic execution these iterates are bit-identical.
