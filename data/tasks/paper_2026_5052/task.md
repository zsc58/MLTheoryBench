# Problem

## Setup

There are an integer number $Q\ge1$ of units. Unit $q$ has a fixed weight $w_q>0$ and a fixed human-label cost $c_q>0$. Write
\[
c_{\min}=\min_{1\le q\le Q}c_q,\qquad c_{\max}=\max_{1\le q\le Q}c_q.
\]
For each unit, $(Y_{q,i},Z_{q,i})_{i\ge1}$ is an iid sequence of paired human/AI observations with a fixed joint distribution. The sequences for different units are independent. Sampling unit $q$ reveals its next unobserved pair. All selection and tie-breaking decisions are measurable functions of observations already collected, the specified deterministic inputs, and, if used, auxiliary randomization independent of the observation sequences.

The AI-only population has the same marginal law for $Z_q$ as the paired population. Work in the synthetic-rich setting in which its mean $\mu_{Z,q}=\mathbb E[Z_q]$ is available exactly. Assume finite bounds $R_Y,R_Z$ and constants $A_{\min},V_{\min}>0$ such that, almost surely,
\[
|Y_q|\le R_Y,\qquad |Z_q|\le R_Z,
\]
\[
\operatorname{Var}(Z_q)\ge V_{\min},\qquad
A_q:=\operatorname{Var}(Y_q-\lambda_q^*Z_q)\ge A_{\min},
\]
where
\[
\Pi_{[0,1]}(x)=\min\{1,\max\{0,x\}\},\qquad
\lambda_q^*=\Pi_{[0,1]}\!\left(\frac{\operatorname{Cov}(Y_q,Z_q)}{\operatorname{Var}(Z_q)}\right).
\]

For an integer $s\ge2$, define
\[
\bar Y_{q,s}=\frac1s\sum_{i=1}^sY_{q,i},\qquad
\bar Z_{q,s}=\frac1s\sum_{i=1}^sZ_{q,i},
\]
\[
\widehat a_{q,s}=\frac1s\sum_{i=1}^s(Y_{q,i}-\bar Y_{q,s})(Z_{q,i}-\bar Z_{q,s}),\qquad
\widehat b_{q,s}=\frac1s\sum_{i=1}^s(Z_{q,i}-\bar Z_{q,s})^2.
\]
Set $\widetilde\lambda_{q,s}=\Pi_{[0,1]}(\widehat a_{q,s}/\widehat b_{q,s})$ if $\widehat b_{q,s}>0$, and set it to $0$ otherwise. Define
\[
\widehat\theta_{q,s}=\bar Y_{q,s}+\widetilde\lambda_{q,s}(\mu_{Z,q}-\bar Z_{q,s}),
\]
\[
\bar R_{q,s}=\frac1s\sum_{i=1}^s(Y_{q,i}-\widetilde\lambda_{q,s}Z_{q,i}),\qquad
\widehat A_{q,s}=\frac1{s-1}\sum_{i=1}^s\big(Y_{q,i}-\widetilde\lambda_{q,s}Z_{q,i}-\bar R_{q,s}\big)^2.
\]

For a budget $B\ge c_{\min}$, let
\[
\Lambda=\sum_{j=1}^Q\sqrt{w_jA_jc_j},\qquad
n_q^*=B\frac{\sqrt{w_qA_q/c_q}}{\Lambda}.
\]
For terminal counts $n_{q,B}$, define
\[
R(B)=\mathbb E\!\left[\sum_{q=1}^Q\frac{w_qA_q}{n_{q,B}}\right]-\sum_{q=1}^Q\frac{w_qA_q}{n_q^*},
\]
where the expectation includes the observations and any auxiliary policy randomization.

## Allocation Policy

The policy has a deterministic calibration parameter $K_0\ge2$. Given $0<\delta<1/2$, set
\[
T_{\max}=\left\lfloor\frac{B}{c_{\min}}\right\rfloor,\qquad
K=\left\lceil K_0\log(QT_{\max}/\delta)\right\rceil.
\]
Only budgets satisfying $B\ge K\sum_{q=1}^Qc_q$ are considered. Initialize with $K$ paired observations per unit.

For integers $s\ge2$, set
\[
g_s=\sqrt{\frac{\log(16QT_{\max}/\delta)}{2s}}
\]
and define the deterministic radius
\[
\begin{aligned}
\rho_{q,s}={}&2(R_Y+R_Z)\sqrt{\frac{2\log\!\big(4QT_{\max}(T_{\max}+1)/\delta\big)}{s-1}}
+\frac{2\sqrt2\,R_Z}{T_{\max}}\\
&+R_Z\left[
\frac{2}{V_{\min}}\big(6R_YR_Zg_s+4R_YR_Zg_s^2\big)
+\frac{4R_YR_Z}{V_{\min}^2}\big(5R_Z^2g_s+4R_Z^2g_s^2\big)
\right].
\end{aligned}
\]
At a decision time $t$, let $n_{q,t}$ denote the number of observations already collected for unit $q$, and let the remaining budget be $B-\sum_qc_qn_{q,t}$. If the remaining budget is less than $c_{\max}$, stop. Otherwise form
\[
A^{\mathrm{UCB}}_{q,n_{q,t}}=\big(\sqrt{\widehat A_{q,n_{q,t}}}+\rho_{q,n_{q,t}}\big)^2,\qquad
I_{q,t}=\frac{w_qA^{\mathrm{UCB}}_{q,n_{q,t}}}{c_qn_{q,t}^{\,2}}.
\]
Select any maximizer of $I_{q,t}$ over all units, collect its next paired observation, and update its count and statistics. Denote the resulting terminal counts by $n_{q,B}$.

## Task

Prove that $K_0$ can be chosen depending only on $R_Y,R_Z,A_{\min},V_{\min}$ so that there exist constants $C_1>0$, $C_2\ge1$, and $B_0\ge c_{\min}$, depending only on these bounds, $Q$, and the fixed weights and costs, for which the following holds simultaneously for every $0<\delta<1/2$ and every $B\ge B_0$ satisfying
\[
B\ge K\sum_{q=1}^Qc_q:
\]
\[
R(B)\le C_1\frac{\log(C_2QT_{\max}/\delta)}{B^2}+\delta V_{\max},\qquad
V_{\max}=\sum_{q=1}^Q\frac{w_qA_q}{K}.
\]
The choices of $K_0,C_1,C_2,B_0$ must be independent of $B$ and $\delta$. Consequently, prove that for $\delta=B^{-2}$ and all sufficiently large $B$, initialization is feasible and
\[
R(B)=O(\log B/B^2)
\]
relative to the continuous Neyman oracle.
