# Problem

## Setup

Let `𝒯` be a measurable treatment space, `𝒳` a confounder space, and `𝒜` a measurable space of treatment attributes. On an observational population probability space `(Ω,𝓕,P)`, let `T` take values in `𝒯`, let `X` take values in `𝒳`, and let `{Y(t): t ∈ 𝒯}` be real-valued potential outcomes. Assume that `(ω,t) ↦ Y(t,ω)` is measurable with respect to the product of `𝓕` and the treatment σ-field, and that `E_P[|Y(t)|] < ∞` for every `t ∈ 𝒯`. Binary potential outcomes are included.

The observed outcome is `Y=Y(T)`. Assume the stable unit treatment value assumption: there is no interference between units and no treatment variation left unspecified by `t`. Assume strong ignorability, `{Y(t)}_{t∈𝒯} independent of T given X`. Also assume the observational positivity condition `0 < e(t,x) < 1` for `t ∈ 𝒯` and `x ∈ 𝒳`, where `e(t,x)` is a specified conditional probability mass function or density of `T` given `X=x`, relative to a fixed reference measure on `𝒯`. Define

`g(t)=E_P[Y(t)]`.

Write `p_T` for the marginal treatment law under `P`, and let `K(t,·)` be a known probability kernel from `𝒯` to `𝒜`. Define the randomized experiment on `Ω×𝒯×𝒜`, equipped with its product σ-field, by the probability law

`P*(dω,dt,du)=P(dω) p_T(dt) K(t,du)`.

In this experiment, `T` and `T'` denote the treatment and attribute coordinate maps, respectively. The population variables `X` and each `Y(s)` are pulled back from the coordinate `ω`, and the realized outcome at `(ω,t,u)` is `Y(t,ω)`. Attribute generation uses `K(T,·)` and is conditionally independent of `(X,{Y(s)}_{s∈𝒯})` given the randomized assignment `T`.

The induced attribute law is defined, for every measurable `B ⊆ 𝒜`, by

`p_{T'}(B)=∫_𝒯 K(t,B) p_T(dt)`.

A deterministic measurable attribute `T'=h(T)` is included by taking `K(t,·)` to be the point mass at `h(t)`.

Assume that under `P*` there exist regular conditional laws `R_{t'}(dy)` of `Y` given `T'=t'` and `Q_{t'}(dt)` of `T` given `T'=t'`, and fix versions of them. Define the finite-mean domain

`D={t' ∈ 𝒜 : ∫_ℝ |y| R_{t'}(dy) < ∞}`.

For `t' ∈ D`, the attribute-level average potential outcome is the mean under the randomized experiment conditioned on that attribute:

`g'(t')=∫_ℝ y R_{t'}(dy)`.

The notation `E*_{T | T'=t'}[·]` refers to integration against `Q_{t'}`. Let `ĝ:𝒯→ℝ` denote a measurable fitted estimate of `g`, with predictions evaluated as a function of the supplied treatment.

## Task

Prove that, for `p_{T'}`-almost every `t' ∈ D`,

`g'(t') = E*_{T | T'=t'}[g(T)]`.

In addition, suppose `T'` is discrete and fix `t' ∈ D` with `p_{T'}({t'})>0`. For i.i.d. pairs `(T_i,T'_i)` drawn from the randomized assignment law specified by `p_T` and `K`, show that the plug-in Monte Carlo estimator of this conditional average is

`ĝ'_n(t') = [Σ_{i=1}^n 1{T'_i=t'} ĝ(T_i)] / [Σ_{i=1}^n 1{T'_i=t'}]`,

defined on samples with a positive denominator. When `ĝ=g`, establish convergence to `g'(t')` in probability, or more strongly almost surely, as `n→∞`, accounting for the possibility of a zero denominator at finite sample sizes.
