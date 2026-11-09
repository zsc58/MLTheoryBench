# Reference Proof

Let `L_F=mL`, let `P_t(v)=a_t^(-1)[x_t-Pi_X(x_t-a_t v)]`, and write `p_t=a_{ceil(kappa t)}`. Thus `H_t=P_t(grad F(x_t))` and the update is `x_{t+1}=x_t-a_t P_t(v_t)`.

The projection facts used below are
`||P_t(v)||^2 <= <v,P_t(v)> <= ||v||^2` and
`||P_t(v)-P_t(w)|| <= ||v-w||`.
Since each `F_i` is L-smooth, `F=sum_i F_i` is `L_F=mL`-smooth.

For a stale sample, the explicit timing and independence assumptions in the task permit conditioning on its timestamp and then on the corresponding iterate. Hence
`E||v_t||^2 <= m sum_i E||G_i(x_{d_i(t)},xi_i(d_i(t)))||^2 <= m^2 G`.  (1)

Put `D_i(t)=t-d_i(t)`. For every index `s` between `d_i(t)` and `t-1`, scaled delay and monotonicity give `a_s<=p_t`. Projection nonexpansiveness and Cauchy-Schwarz give
`||x_t-x_{d_i(t)}||^2 <= D_i(t) sum_{s=d_i(t)}^{t-1} a_s^2 ||v_s||^2`.
Conditioning on the delay, using (1), and then using `E D_i(t)^2<=C` yields
`E||x_t-x_{d_i(t)}||^2 <= m^2 G C p_t^2`.  (2)
Consequently, for every i,
`E||bar G_i(t)-bar G_i(d_i(t))||^2 <= m^2 G C L^2 p_t^2`.  (3)
For completeness, aggregate smoothness gives the corrected auxiliary estimate
`E||grad F(x_t)-grad F(x_{d_i(t)})||^2 <= m^4 G C L^2 p_t^2`; it is not needed below.

Set
`A_t=sum_i bar G_i(d_i(t))`, `B_t=sum_i bar G_i(t)`, and `C_t=grad F(x_t)`.
The estimator assumptions and Jensen's inequality imply
`E||C_t||^2 <= 2m^2(b_t^2+G)`.  (4)
Also, projection Lipschitzness, (1), and conditional centering at each stale timestamp give
`E||P_t(v_t)-P_t(A_t)||^2 <= m^2G`.  (5)
By (3),
`E||P_t(A_t)-P_t(B_t)||^2 <= E||A_t-B_t||^2 <= m^4GCL^2p_t^2`,  (6)
and the bias bound gives
`E||P_t(B_t)-P_t(C_t)||^2 <= m^2b_t^2`.  (7)

Decompose
`-<C_t,P_t(v_t)>` into the three differences in (5)--(7), followed by `-<C_t,P_t(C_t)>`. Apply Young's inequality with parameter 1 to the first and third differences, parameter `p_t` to the second, and the projection inequality to the last. Taking expectations and using (4)--(7) gives
`E[-<C_t,P_t(v_t)>] <= -E||H_t||^2`
` + (5/2)m^2G + (5/2)m^2b_t^2`
` + [m^2G+(1/2)m^4GCL^2]p_t + m^2p_t b_t^2`.  (8)

Smoothness of `F`, the update formula, (1), and `||P_t(v_t)||<=||v_t||` yield
`E F(x_{t+1}) <= E F(x_t) - a_t E<C_t,P_t(v_t)> + (L_F/2)a_t^2m^2G`.
Combining this with (8), and setting constants that depend only on `m,L,G,C`, gives
`a_t E||H_t||^2 <= E[F(x_t)-F(x_{t+1})]`
` + c_1 a_t + c_2 a_t^2 + c_3 a_t p_t + c_4 a_t b_t^2 + c_5 a_t p_t b_t^2`.  (9)

The positive ratio limit implies a finite constant `R` such that `p_t<=R a_t` for every t (enlarge the eventual bound over the finitely many earlier indices). Since `a_t<=a_0`, the last two p-dependent terms in (9) are bounded by constant multiples of `a_t^2` and `a_t b_t^2`, respectively. Summing (9) from 0 through T and using `F>=F_*` gives, for a constant K independent of T,
`sum_{t=0}^T a_t E||H_t||^2 <= K sum_{t=0}^T [a_t+a_t^2+a_t b_t^2]`.
Here the fixed initial gap is absorbed into `K sum_{t=0}^T a_t`, which is positive and diverges.

Finally, monotonicity gives
`a_T sum_{t=0}^T E||H_t||^2 <= sum_{t=0}^T a_t E||H_t||^2`.
For `T>=1`, division by `(T+1)a_T` proves
`(1/(T+1))sum_{t=0}^T E||H_t||^2 = O((sum_{t=0}^T[a_t+a_t^2+a_t b_t^2])/(T a_T))`.

For `a_t=a_0/(t+1)^alpha`, `0<alpha<1`, one has `p_t/a_t -> kappa^(-alpha)`. Since `b_t` is nonnegative and nonincreasing, `a_t^2<=a_0a_t` and `a_tb_t^2<=b_0^2a_t`; moreover `sum_{t=0}^T a_t` and `T a_T` have the same order. The displayed bound is therefore `O(1)`.
