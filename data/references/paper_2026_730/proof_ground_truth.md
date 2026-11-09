# Reference Proof

## Proof Structure

Compute the population least-squares slope, show that the resulting fitted line is increasing and therefore selects the boundary treatment, and evaluate the resulting optimism. Then specialize the peak location to `t_0=1-epsilon` and integrate the squared approximation error to show that historical-distribution MSE tends to zero while the optimism remains controlled below only by the peak scale.

## Complete Proof

Let `t` be uniform on `[0,1]`, let `y=f^*(t)` noiselessly, and fit the restricted population model `f_beta(t)=beta t` by least squares. For `0<t_0<1` and `y_max>0`, define

`f^*(t) = (y_max/t_0)t` for `0<=t<=t_0`, and `f^*(t)=y_max(1-t)/(1-t_0)` for `t_0<t<=1`.

The population slope is

`beta = E[t f^*(t)]/E[t^2]`.

Since `E[t^2]=1/3`, splitting the numerator at `t_0` gives

`E[t f^*(t)] = integral_0^{t_0} (y_max/t_0)t^2 dt + integral_{t_0}^1 y_max t(1-t)/(1-t_0) dt = (1+t_0)y_max/6`.

Hence `beta=(1+t_0)y_max/2`. This is positive, so `f_beta` is increasing on `[0,1]`; the model-based optimizer therefore chooses `hat t=1`. The fitted value there is `f_beta(1)=beta`, whereas `f^*(1)=0`. Thus the optimism is

`O = f_beta(hat t)-f^*(hat t) = (1+t_0)y_max/2`.

For `t_0>=1/2`, `O>=y_max/2`, so the optimism can be made arbitrarily large by increasing `y_max`.

It remains to show that this can coexist with arbitrarily small historical MSE. Set `t_0=1-epsilon` with `0<epsilon<=1/2`, so `beta=(2-epsilon)y_max/2`. Directly splitting the integral at `1-epsilon` gives

`MSE = integral_0^{1-epsilon} y_max^2 t^2 ((2-epsilon)/2 - 1/(1-epsilon))^2 dt`

`     + integral_{1-epsilon}^1 y_max^2 ((2-epsilon)t/2 - (1-t)/epsilon)^2 dt`

and elementary evaluation (equivalently, the change of variable `u=1-t` in the second integral) yields

`MSE <= 2 epsilon y_max^2 + (epsilon^2 y_max^2)/3`.

Therefore, for every fixed positive `y_max`, `MSE -> 0` as `epsilon -> 0`, while `O=(2-epsilon)y_max/2` remains at least `y_max/2`. Given any requested optimism level `B>0` and MSE tolerance `eta>0`, choose `y_max>=2B` and then choose sufficiently small `epsilon` (also at most `1/2`) so that the displayed MSE bound is at most `eta`. The resulting randomized, noiseless, infinite-data population evaluator consequently reports optimism at least `B` despite MSE at most `eta`.
