# Problem

## Setup

Work on a discrete-time filtered probability space \((\Omega,\mathcal F,(\mathcal F_t)_{t\ge0},\Pr)\). Index all potential node-candidate tests by a fixed countable set \(I\). For each \(j\), let \(\sigma_j\in\{1,2,\ldots\}\cup\{\infty\}\) be its predictable first test-observation time, with \(\sigma_j=\infty\) if the test is never instantiated. Write \(J=\{j:\sigma_j<\infty\}\), and assume each finite-time history instantiates only finitely many tests.

Before the first observation of an instantiated test, choose whether it uses a strong-null betting test or a weak-null confidence-sequence test, and assign its level \(\alpha_j\in(0,1]\). Both choices are measurable with respect to \(\mathcal F_{\sigma_j-1}\). Put \(\alpha_j=0\) if \(j\) is not instantiated, and assume the pathwise allocation satisfies \(\sum_{j\in I}\alpha_j\le\alpha\), where \(0<\alpha<1\).

For an instantiated \(j\), the observations \(\Delta_{j,n}\in[-1,1]\), \(n\ge1\), are \(\mathcal F_{\sigma_j+n-1}\)-measurable. Define
\[
\delta_{j,n}=\mathbb E[\Delta_{j,n}\mid\mathcal F_{\sigma_j+n-2}],\qquad
\mu_{j,n}=\frac1n\sum_{r=1}^n\delta_{j,r}.
\]
The strong null is \(\delta_{j,n}\le0\) for every \(n\); the weak null is \(\mu_{j,n}\le0\) for every \(n\).

For a strong-null test choose \(\mathcal F_{\sigma_j+n-2}\)-measurable \(\beta_{j,n}\in[0,1]\), set \(W_{j,0}=1\), and update
\[
W_{j,n}=W_{j,n-1}(1+\beta_{j,n}\Delta_{j,n}).
\]
Its commitment time is \(\tau_j=\inf\{n\ge1:W_{j,n}\ge1/\alpha_j\}\).

For a weak-null test, use \(\mathcal F_{\sigma_j+n-1}\)-measurable bounds \(L_{j,n}\le U_{j,n}\) forming a confidence sequence for \(\mu_{j,n}\), with the conditional guarantee
\[
\Pr\{\mu_{j,n}\in[L_{j,n},U_{j,n}]\ \forall n\mid\mathcal F_{\sigma_j-1}\}\ge1-\alpha_j
\]
on the instantiation event. Choose a margin \(m_j\ge0\) measurable with respect to \(\mathcal F_{\sigma_j-1}\), and set \(\tau_j=\inf\{n\ge1:L_{j,n}>m_j\}\).

A test commits when \(\tau_j<\infty\); the procedure may continue growing the tree and may inspect tests at arbitrary data-dependent times.

## Task

Prove that
\[
\Pr\{\exists j\in J:\text{the tested null for }j\text{ is true and }\tau_j<\infty\}\le\alpha.
\]
Equivalently, with probability at least \(1-\alpha\), no false split commitment occurs at any time throughout the entire adaptive run, for either type of test above.
