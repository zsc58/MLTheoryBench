# Problem

## Setup

The decision set is X=[-1,1]. At round t an algorithm chooses x_t in X and receives a differentiable loss f_t. Write g_t=f_t'(x_t). Define the projection P(z)=min(1,max(-1,z)). For a horizon T, define regret against the best fixed decision by
R_T = sum_{t=1}^T f_t(x_t) - min_{x in X} sum_{t=1}^T f_t(x).

Fix b,q in [0,1), epsilon>=0, an initial point x_1 in X, and positive step sizes alpha_t satisfying alpha_t->0, alpha_{t+1}/alpha_t->1, and sum_{t=1}^infinity alpha_t=infinity. Starting from m_0=v_0=0, projected Adam is defined by
m_t=b m_{t-1}+(1-b)g_t,
v_t=q v_{t-1}+(1-q)g_t^2,
h_t=m_t/(sqrt(v_t)+epsilon),
x_{t+1}=P(x_t-alpha_t h_t).

## Task

Prove that there exists a number delta in (0,1], depending only on b,q,epsilon, such that, with a=2+delta and the three-periodic linear losses
f_{3k+1}(x)=a x,   f_{3k+2}(x)=f_{3k+3}(x)=-x   (k=0,1,2,...),
the resulting iterates satisfy x_t->1 for every x_1 in X. Moreover, for every positive horizon T the best fixed comparator is x=-1, and
R_T/T -> 2delta/3 > 0.
