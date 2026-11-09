# Problem

## Setup

Let $X=\mathbb R^{d_x}$ and $Y=\mathbb R^{d_y}$ with their Borel sigma-algebras. Let $\pi_x$ be a prior probability measure on $X$, let $\pi_y$ be an observation marginal on $Y$, and let $\pi_{y\mid x}(\,\cdot\mid x)$ be a likelihood kernel admitting a posterior disintegration $\pi_{x\mid y}(\,\cdot\mid y)$ such that the Bayesian joint law
\[
Q(dx,dy)=\pi_x(dx)\,\pi_{y\mid x}(dy\mid x)=\pi_{x\mid y}(dx\mid y)\,\pi_y(dy).
\]
Let $P=\pi_x\otimes\pi_y$ denote the independent coupling. Let $T:X\times Y\to X\times Y$ be measurable and block triangular:
\[
T(x,y)=(T_x(x,y),y).
\]
Let $k$ be a universal (hence characteristic) Gaussian kernel on $X\times Y$, and define
\[
\operatorname{MMD}_k(\mu,\nu)=\sup_{\|f\|_{\mathcal H_k}\le 1}\left|\int f\,d\mu-\int f\,d\nu\right|
\]
for probability measures $\mu,\nu$, where $\mathcal H_k$ is the RKHS of $k$. Assume
\[
\operatorname{MMD}_k(T\#P,Q)=0.
\]

## Task

Prove that
\[
T_x(\cdot,y)\#\pi_x=\pi_{x\mid y}(\cdot\mid y)
\quad\text{for }\pi_y\text{-almost every }y\in Y.
\]
Here $T_x(\cdot,y)\#\pi_x$ denotes the push-forward of the prior by the state component with the observation held fixed at $y$.
