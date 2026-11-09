# Problem

## Setup

Let M be a compact, connected Riemannian manifold with Riemannian distance d_M, and let (N,d_N) be a metric space. Let f:M\to N be continuous. Say that f is **injective** if f(x)\ne f(y) for every pair of distinct points x,y\in M.

For delta,epsilon>0, say that f is **(delta,epsilon)-separated** if every x,y\in M satisfying d_M(x,y)\ge delta also satisfy
\[
\frac{d_N(f(x),f(y))}{d_M(x,y)}>\epsilon.
\]

## Task

Prove that f is injective if and only if, for every delta>0, there exists epsilon>0 such that f is (delta,epsilon)-separated.
