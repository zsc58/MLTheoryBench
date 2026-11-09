# Problem

## Setup

Fix a follow-up time `t`. Let `(X_0,X_t,Z)` be centered random variables with `X_0,X_t in R^d`, `Z in R^q`, finite second moments, and i.i.d. observations from this distribution. Assume

`X_t = m_t(X_0,Z) + epsilon_t`, where `m_t(X_0,Z)=E[X_t|X_0,Z]` and `E[epsilon_t|X_0,Z]=0`.

Define the population reconstruction matrix

`B_t = argmin_{B in R^{dxd}} E[||X_0-X_t B||_2^2]`,

and assume that `B_t` is invertible. Assume also that `Cov(m_t(X_0,Z))` is invertible. Define

`h_t(X_0,Z)=E[X_t B_t|X_0,Z]`.

A preprocess-then-linear pair consists of a measurable `g:R^{d+q}->R^d` and a matrix `beta in R^{dxd}`; its prediction is `g(X_0,Z) beta`. Call such a pair Bayes-optimal if its squared-error risk equals the Bayes risk `E[||X_t-m_t(X_0,Z)||_2^2]`.

## Task

Prove the following theorem: among all Bayes-optimal preprocess-then-linear pairs satisfying the item-coordinate anchoring condition

`B_t beta=I_d`,

the unique pair (up to almost-sure equality of the preprocessor) is

`beta=B_t^{-1}` and `g(X_0,Z)=h_t(X_0,Z)=E[X_tB_t|X_0,Z]` almost surely.
