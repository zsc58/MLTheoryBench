# Problem

## Setup

Let \(d\ge1\), let \(g\in\mathbb R^d\), and let \(c\in\mathbb R^d\) satisfy \(c_j>0\) for every coordinate. For a support \(S\subseteq\{1,\ldots,d\}\), write its mask as \(m\in\{0,1\}^d\), define the sparsified vector \(\Pi_S(g)=m\odot g\), and measure its energy by \(c^\top m\). Fix an energy budget \(E>0\).

Consider the continuous relaxation
\[
\max_{m\in[0,1]^d}\;\sum_{j=1}^d m_j|g_j|
\qquad\text{subject to}\qquad
\sum_{j=1}^d m_jc_j\le E.
\]
For each coordinate define its efficiency score \(s_j=|g_j|/c_j\).

## Task

Prove that an optimal relaxed mask can be obtained by ordering the coordinates so that
\[
s_{(1)}\ge s_{(2)}\ge\cdots\ge s_{(d)}
\]
and filling the available energy in that order. If \(E<\sum_j c_j\), select successive coordinates fully, take the fraction of the next coordinate needed to exhaust the remaining budget, and leave later coordinates unselected; the fraction may be zero. Coordinates tied at the boundary score may instead share the allocation arbitrarily within \([0,1]\), provided their total allocated energy is unchanged. If \(E\ge\sum_j c_j\), selecting every coordinate is an optimal choice.

Also establish the common-threshold characterization of all optimal masks: a feasible mask \(m\) is optimal if and only if there exists \(\tau\ge0\) such that
\[
s_j>\tau\ \Longrightarrow\ m_j=1,
\qquad
s_j<\tau\ \Longrightarrow\ m_j=0,
\]
and
\[
c^\top m=E\quad\text{or}\quad\tau=0.
\]
Coordinates with \(s_j=\tau\) may have any values in \([0,1]\) consistent with feasibility and this energy condition.
