# Reference Proof

## Proof Structure

Use the common initialization and the specified unit-noise dynamics to change measure on path space. Condition the path density on the terminal coordinate. Control its exponential Taylor remainder using bracket moments and exponential integrability, then transfer the conditional martingale signal through the observability coefficient. Treat zero energy separately and keep all constants uniform in the generation.

## Standard Results Used

Girsanov's theorem is used in the following form. If \(B\) is Brownian motion, \(h\) is predictable with finite integrated squared norm almost surely, and
\[
L_u=\exp\left(-\int_0^u h_v\cdot dB_v-\frac12\int_0^u\|h_v\|^2dv\right)
\]
is a true martingale starting at one, then \(dQ=L_LdP\) defines a probability measure and \(B_u+\int_0^u h_vdv\) is Brownian motion under \(Q\). The distribution on the initial sigma-field is unchanged. For an SDE with noise coefficient \(-I_d\), the drift consequently increases by \(h\). Uniqueness in law identifies the changed law with the specified learned diffusion law.

Ito isometry gives \(\mathbb E M_L=0\) and \(\mathbb E M_L^2=\mathbb E\langle M\rangle_L\) for a stochastic integral with a predictable square-integrable integrand. The BDG inequality supplies, for a continuous local martingale starting at zero,
\[
\mathbb E|M_L|^r\le B_r\mathbb E\langle M\rangle_L^{r/2},
\]
whenever the right-hand side is finite. The constants \(B_r\) depend only on \(r\). These standard independent results are the only stochastic-calculus inputs needed below.

## Complete Proof

Fix \(i\ge i_0\). Write \(L=T-t_0\), \(a=a_i\), \(\rho=\rho_i\), \(N=N_i\), \(A=A_i\), \(W=W_i\), and let all unqualified expectations be under \(P_i\). Set \(h_u=e_{i,T-u}(X_u)\).

### 1. Path density and terminal projection

Predictability and \(a^2<\infty\) imply that \(N_i(u)=-\int_0^u h_v\cdot dB_v\) is a square-integrable continuous martingale, with
\[
\langle N_i\rangle_L=\int_0^L\|h_u\|^2du=A,
\qquad \mathbb EA=a^2,
\qquad \mathbb EN=0,
\qquad \mathbb EN^2=a^2.
\]
By the true-martingale assumption, \(\mathcal E_i(L)=e^W\) has expectation one. Define \(Q\) by \(dQ=e^WdP_i\). Girsanov makes
\[
B_u^Q=B_u+\int_0^u h_vdv
\]
Brownian under \(Q\). Substitution into the ideal sampling-clock SDE gives
\[
dX_u=\left[\tfrac12X_u+s_i(X_u,T-u)+e_{i,T-u}(X_u)\right]du-dB_u^Q
=\left[\tfrac12X_u+\widehat s_i(X_u,T-u)\right]du-dB_u^Q.
\]
Moreover, the initial law remains \(\mathcal N(0,I_d)\), because \(\mathbb E[e^W\mid\mathcal F_0]=1\). The well-posed learned SDE therefore has law \(Q=\widehat P_i\), so
\[
\frac{d\widehat P_i}{dP_i}=e^W.
\]
There is no initialization-density factor: the initial laws are identical.

For every bounded measurable \(f\),
\[
\mathbb E_{\widehat P_i}f(X_L)
=\mathbb E[f(X_L)e^W]
=\mathbb E\left[f(X_L)\mathbb E[e^W\mid X_L]\right].
\]
Consequently \(\widehat p^{i+1}\ll q_i\), and its density ratio \(R\) satisfies
\[
R(X_L)=\mathbb E[e^W\mid X_L],\qquad
\chi^2(\widehat p^{i+1}\|q_i)=\mathbb E(R(X_L)-1)^2. \tag{1}
\]
Here \(X_L=Y_{t_0}\), so the conditioning variable agrees with the public observability definition.

### 2. Zero energy

If \(a=0\), nonnegativity and \(\mathbb EA=0\) give \(A=0\) almost surely. Ito isometry gives \(N=0\), hence \(W=0\). Equation (1) yields \(R=1\) and \(\chi^2=0\). Since \(\rho=0\) by definition, every claimed bound holds. The division-free bracket assumption is also well-defined in this case.

Henceforth suppose \(a>0\) and \(a^2\le1\). Conditional Jensen and Ito isometry give \(0\le\rho\le1\) and
\[
\mathbb E\bigl(\mathbb E[N\mid X_L]\bigr)^2=\rho a^2. \tag{2}
\]

### 3. Bracket and log-density moments

For every \(0<r\le2+\gamma\), Lyapunov's inequality and the bracket assumption give
\[
\mathbb EA^r\le K_\gamma^{r/(2+\gamma)}a^{2r}. \tag{3}
\]
Set \(k_2=K_\gamma^{2/(2+\gamma)}\) and \(k_4=K_\gamma^{4/(2+\gamma)}\). Then
\[
\mathbb EW^2\le2\mathbb EN^2+\tfrac12\mathbb EA^2
\le2a^2+\tfrac12k_2a^4. \tag{4}
\]
Because \(\gamma>2\), (3) applies at \(r=4\). BDG at exponent four gives
\[
\begin{aligned}
\mathbb EW^4
&\le8\mathbb E|N|^4+\tfrac12\mathbb EA^4\\
&\le8B_4k_2a^4+\tfrac12k_4a^8\\
&\le C_4a^4,
\end{aligned}\tag{5}
\]
where \(C_4=8B_4k_2+k_4/2\). This retains the BDG factor omitted in the source's intermediate fourth-moment display.

### 4. Exponential Taylor remainder

Let \(\psi(z)=e^z-1-z\). Taylor's integral formula gives
\[
0\le\psi(z)=z^2\int_0^1(1-v)e^{vz}dv\le\tfrac12z^2e^{z_+}.
\]
On \(W\le0\), this bounds \(\psi(W)^2\) by \(W^4/4\). On \(W>0\), nonnegativity of \(A\) gives \(0<W\le N\), so
\[
\psi(W)^2\mathbf1_{\{W>0\}}
\le\tfrac14N_+^4e^{2W}.
\]
Choose
\[
p=\frac{1+\delta}{2}>1,
\qquad p'=\frac{1+\delta}{\delta-1},
\qquad \frac1p+\frac1{p'}=1.
\]
The parameter hypothesis implies
\[
2p'=2+\frac4{\delta-1}<2+\gamma.
\]
Thus (3) and BDG at exponent \(4p'\) imply
\[
\mathbb E|N|^{4p'}
\le B_{4p'}\mathbb EA^{2p'}
\le B_{4p'}K_\gamma^{2p'/(2+\gamma)}a^{4p'}.
\]
Holder's inequality and exponential integrability now give
\[
\mathbb E[N_+^4e^{2W}]
\le C_\delta^{1/p}
\left(B_{4p'}K_\gamma^{2p'/(2+\gamma)}\right)^{1/p'}a^4.
\]
Together with (5), this proves
\[
\mathbb E\psi(W)^2\le C_\psi a^4, \tag{6}
\]
where an admissible constant is
\[
C_\psi=\frac14C_4+
\frac14C_\delta^{1/p}
\left(B_{4p'}K_\gamma^{2p'/(2+\gamma)}\right)^{1/p'}.
\]
All quantities used in this argument are integrable under the verified exponent conditions.

### 5. Observable lower bound

Define
\[
U=\mathbb E[W\mid X_L],\qquad
V=\mathbb E[\psi(W)\mid X_L].
\]
Equation (1) and the Taylor decomposition give \(R(X_L)-1=U+V\). Conditional Jensen and (6) give \(\mathbb EV^2\le C_\psi a^4\).

For \(0<\theta<1\), the elementary inequality
\[
(x-y)^2\ge(1-\theta)x^2-(\theta^{-1}-1)y^2
\]
applied to
\[
U=\mathbb E[N\mid X_L]-\tfrac12\mathbb E[A\mid X_L]
\]
yields, by (2), conditional Jensen, and (3),
\[
\mathbb EU^2\ge(1-\theta)\rho a^2
-\tfrac14(\theta^{-1}-1)k_2a^4. \tag{7}
\]
Taking \(\theta=1/2\) and then using \((U+V)^2\ge U^2/2-V^2\), we obtain
\[
\chi^2(\widehat p^{i+1}\|q_i)
\ge\tfrac14\rho a^2-\left(\tfrac18k_2+C_\psi\right)a^4. \tag{8}
\]
Choose \(C=1+k_2/8+C_\psi>0\). This depends only on the four permitted moment parameters. If \(a^2\le\rho/(8C)\), then \(Ca^4\le\rho a^2/8\), and (8) gives
\[
\chi^2(\widehat p^{i+1}\|q_i)\ge\tfrac18\rho a^2. \tag{9}
\]

### 6. Upper bound and uniform equivalence

Conditional Jensen, (4), and (6) give
\[
\begin{aligned}
\chi^2(\widehat p^{i+1}\|q_i)
&=\mathbb E(U+V)^2\\
&\le2\mathbb EU^2+2\mathbb EV^2\\
&\le2\mathbb EW^2+2\mathbb E\psi(W)^2\\
&\le4a^2+(k_2+2C_\psi)a^4.
\end{aligned}\tag{10}
\]
Take \(c=1+k_2+2C_\psi>0\). Equations (8)-(10), together with the zero-energy case, prove the full target with constants independent of the generation.

If \(\rho_i\ge\underline\rho>0\) and
\[
a_i^2\le\min\{1,\underline\rho/(8C)\}
\]
for the generations under consideration, then
\[
\frac{\underline\rho}{8}a_i^2
\le\chi^2(\widehat p^{i+1}\|q_i)
\le(4+c)a_i^2.
\]
This is the asserted uniform equivalence. Its comparison constants may depend on \(\underline\rho\) and the four moment parameters, but not on \(i\).

## Obligation Audit

The common-initial-law change of measure, terminal density projection, zero-energy case, bracket moments, both BDG applications, exponential remainder, observable lower bound, upper bound, and uniform comparison constants are explicitly established above. No nonstandard external result or unresolved private proof obligation is used.
