# Problem

## Setup

Let y in R^n be the vector of sample responses and let each prediction vector be f in R^n. A prediction-dependent weak-learner class is represented by B(f) in R^{n x p}. Define the orthogonal projector A(f):=B(f)B(f)^+, where B(f)^+ is the Moore–Penrose pseudoinverse. Throughout, vector norms are Euclidean and matrix norms are the induced operator norms.

Consider the following two regimes, each with its own stepsize assumptions.

### General inexact regime

Let ell:R^2->R be a loss function and define the finite objective V(f):=sum_{i=1}^n ell(y_i,f_i)>=0. Fix constants m>0 and L>0. Starting from f_0, for every integer t>=0 choose theta_t in R^p, set h_t=B(f_t)theta_t, and update
\[
f_{t+1}=f_t+\eta h_t,
\qquad 0\le\eta\le\min\{1,m/(2L)\},
\]
with a fixed stepsize eta.

Assume V is differentiable on the segments used below, is L-smooth on the segment from f_t to f_{t+1}, and is m-strongly convex on {f_t+tau h_t:0<=tau<=1}, for every t. Assume also that the following minimum exists and that
\[
V(f_t+h_t)\le\min_{\theta\in\mathbb R^p}V(f_t+B(f_t)\theta)+\varepsilon_t,
\qquad 0\le\varepsilon_t<\infty.
\]
The constants m and L are the same for all rounds.

### Exact squared-loss regime

Separately, take V(f)=1/2||y-f||^2 and an exact oracle, so epsilon_t=0, and use the update
\[
f_{t+1}=f_t+\eta A(f_t)(y-f_t),\qquad 0<\eta\le1,
\]
with fixed eta. Assume that, for some fixed L_A>=0,
\[
\|A(f)-A(g)\|\le L_A\|f-g\|
\]
for all f and g belonging to the trajectory {f_t:t>=0}.

## Task

In the general inexact regime, prove that for every integer T>=1,
\[
\min_{0\le t<T}\|f_{t+1}-f_t\|
\le\frac1T\sum_{t=0}^{T-1}\|f_{t+1}-f_t\|
\le\sqrt{\frac{4\eta}{mT}\left(V(f_0)+\eta\sum_{t=0}^{T-1}\varepsilon_t\right)}.
\]
If sum_{t=0}^infinity epsilon_t<infinity, prove that the displayed average and minimum are O(T^{-1/2}) and that the individual gaps ||f_{t+1}-f_t|| tend to zero.

In the exact squared-loss regime, define
\[
\kappa:=1-\eta+\eta L_A\|y-f_0\|.
\]
Prove that
\[
\|f_{t+1}-f_t\|\le\kappa\|f_t-f_{t-1}\|\qquad(t\ge1),
\]
and hence that, when kappa<1, the successive gaps decay geometrically and the prediction sequence converges at a geometric rate.
