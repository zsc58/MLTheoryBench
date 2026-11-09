# Reference Proof

## Proof Structure

1. Obtain a bound uniform over the original trajectory and every warped trajectory.
2. Choose constant sigmoid gates and a linear candidate so the cell state exactly follows the original recursion.
3. Choose a finite output-gate bias giving the prescribed strict error bound, including zero-valued data.
4. Change only the forget- and input-gate biases; the same output gate then gives the same tolerance for every positive warp factor.

## Complete Proof

Let
\[
B=\max\{|z_0|,\max_{1\le s\le N}|X_s|\},
\qquad M_*>\max\{B,\epsilon\}.
\]
These quantities are finite, and \(M_*>\epsilon>0\). They are chosen independently of \(\gamma\).

For any \(r\in(0,1)\), define
\[
y_0=z_0,\qquad y_t=ry_{t-1}+(1-r)X_t,\quad 1\le t\le N.
\]
Its closed form is
\[
y_t=r^t z_0+(1-r)\sum_{k=0}^{t-1}r^kX_{t-k}.
\]
Indeed, the formula at \(t=1\) is the defining recurrence. If it holds at \(t-1\), substitution gives
\[
\begin{aligned}
y_t
&=r^t z_0+(1-r)\sum_{k=0}^{t-2}r^{k+1}X_{t-1-k}+(1-r)X_t\\
&=r^t z_0+(1-r)\sum_{k=0}^{t-1}r^kX_{t-k}.
\end{aligned}
\]
This proves the formula by induction. All its coefficients are nonnegative, and
\[
r^t+(1-r)\sum_{k=0}^{t-1}r^k
=r^t+(1-r^t)=1.
\]
Consequently,
\[
|y_t|\le r^t B+(1-r)\sum_{k=0}^{t-1}r^kB=B.
\]
The bound holds for every \(r\in(0,1)\) with the same \(B\). In particular, it bounds \(z_t\) when \(r=a\), and it bounds every \(\widetilde z_t\) when \(r=a^\gamma\). Here \(0<a^\gamma<1\) for every positive real \(\gamma\).

For \(v\in(0,1)\), substitution into the definitions gives \(\sigma(\operatorname{logit}(v))=v\), and \(\sigma\) is strictly increasing. Choose the base parameters
\[
W_f=U_f=0,\quad b_f=\operatorname{logit}(a),\qquad
W_i=U_i=0,\quad b_i=\operatorname{logit}(1-a),
\]
\[
W_g=1,\qquad U_g=b_g=0,
\]
and
\[
W_o=U_o=0,\qquad b_o>\operatorname{logit}(1-\epsilon/M_*).
\]
All biases are finite: \(a,1-a\in(0,1)\), and \(0<1-\epsilon/M_*<1\). Retain the prescribed initial cell state \(c_0=z_0\) and the given fixed initial hidden state \(h_0\). Every recurrent weight is zero, so that hidden initial value does not affect any subsequent gate or candidate.

The chosen parameters give
\[
f_t=a,\qquad i_t=1-a,\qquad g_t=X_t,\qquad o_t=o:=\sigma(b_o),
\]
where
\[
0<1-o<\epsilon/M_*.
\]
Thus
\[
c_t=ac_{t-1}+(1-a)X_t.
\]
Together with \(c_0=z_0\), induction shows \(c_t=z_t\) for every \(0\le t\le N\). For \(1\le t\le N\), the output equation gives \(h_t=oc_t\), and hence
\[
|z_t-h_t|=(1-o)|z_t|
\le(1-o)B
\le\frac{\epsilon B}{M_*}
<\epsilon.
\]
The last inequality follows from \(B<M_*\) and \(\epsilon>0\). The non-strict intermediate inequalities also hold when \(B=0\); in that case the error is exactly zero. Taking the maximum over the finite set of times proves the base approximation claim.

Now let \(\gamma>0\) be arbitrary. Replace only the two biases by
\[
\widetilde b_f=\operatorname{logit}(a^\gamma),\qquad
\widetilde b_i=\operatorname{logit}(1-a^\gamma).
\]
Both are finite because \(a^\gamma,1-a^\gamma\in(0,1)\). Leave every other parameter, \(c_0\), and \(h_0\) unchanged. The modified gates and candidate are
\[
\widetilde f_t=a^\gamma,\qquad
\widetilde i_t=1-a^\gamma,\qquad
\widetilde g_t=X_t,\qquad
\widetilde o_t=o.
\]
Therefore
\[
\widetilde c_t=a^\gamma\widetilde c_{t-1}+(1-a^\gamma)X_t,
\qquad \widetilde c_0=z_0=\widetilde z_0.
\]
Induction yields \(\widetilde c_t=\widetilde z_t\). Using the same bound and the unchanged output gate,
\[
|\widetilde z_t-h_t^{(\gamma)}|
=(1-o)|\widetilde z_t|
\le(1-o)B
\le\frac{\epsilon B}{M_*}
<\epsilon,
\qquad 1\le t\le N.
\]
Neither \(B\), \(M_*\), nor any base parameter depends on \(\gamma\). Thus a single base setting has the required property simultaneously for every \(\gamma>0\), with only the specified two biases replaced.

## Private Source-Alignment Notes

The source's global indexing convention at L000024 and accuracy definition at L000295-L000297 supply the finite horizon. A finite real input sequence automatically has a finite bound and can be extended by zeros if the bounded infinite-sequence setup at L000261 is used. No additional assumption on the public inputs is needed.

The source construction at L000413-L000432 chooses \(h_0=0\), but all recurrent weights vanish, so the same construction works for any fixed real \(h_0\). The source's intermediate maxima at L000436-L000441 incorrectly include time zero despite that initialization. The required conclusion at L000410 and L000443 concerns only times \(1,\ldots,N\); the proof above uses exactly that range for output-error estimates.

The common-bound and logit-domain repairs recorded for theory_009 and theory_010 are retained. The finite geometric calculation above explicitly closes the uniform-bound obligation for every warp factor, without invoking an unproved stability theorem or any nonstandard dependency.
