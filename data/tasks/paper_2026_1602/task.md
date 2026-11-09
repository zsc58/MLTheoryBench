# Problem

## Setup

Fix an integer k0>=1, constants gamma_0>0 and sigma_0>=0, a learning rate eta in (0,1), a constant c_t in (0,1], and constants 0<a_T<=b_T<infinity. All of these quantities are fixed independently of the sample and initialization. The target f* is also fixed independently of them: it is a spherical polynomial of degree at most k0 whose norm in the reproducing kernel Hilbert space H_K of the kernel defined below is at most gamma_0.

There are constants d_0,C_0,C_1,c>0 depending only on k0,gamma_0,sigma_0,eta,c_t,a_T,b_T for which the following assertion holds. Let d>=d_0 be an integer. Let x_1,...,x_n be i.i.d. uniform on S^{d-1}. Let xi_1,...,xi_n be i.i.d. mean-zero noises, independent of the covariates, satisfying

E[exp(lambda xi_i)]<=exp(lambda^2 sigma_0^2/2) for every real lambda.

Observe y_i=f*(x_i)+xi_i.

For u,v in S^{d-1}, define

K^(0)(u,v)=(pi-arccos(u^T v))/(2pi),

K^(1)(u,v)=(u^T v)K^(0)(u,v), and K=K^(0)+K^(1).

Let N(d,ell) be the dimension of the degree-ell spherical-harmonic space and set r0=sum_{ell=0}^{k0}N(d,ell).

Let m be a positive even integer. Independently of all observations, draw independent seeds g_1,...,g_{m/2} from N(0,I_d) and independent signs s_1,...,s_{m/2}, each uniform on {-1,1}; the seeds and signs are mutually independent. Set

w_{2j-1}(0)=w_{2j}(0)=g_j,

a_{2j-1}=s_j, and a_{2j}=-s_j.

The a_r remain fixed during training. Initialize b(0)=0 in R^m. Define the scalar initialization-gate feature F(W(0),x) in R^m by

[F(W(0),x)]_r=1{w_r(0)^T x>=0}.

For W=(w_1,...,w_m), with w_r in R^d, and b in R^m, consider

f(theta,x)=m^{-1/2}sum_{r=1}^m a_r ReLU(w_r^T x)+m^{-1/2}b^T F(W(0),x),

where ReLU(z)=max{z,0}, theta=(vec(W),b), and p=md+m. Paired initialization gives f(theta_0,x)=0.

For the updates, use the ReLU derivative convention ReLU'(z)=1{z>=0}. Specifically, let Z_t in R^{n x p} have first-layer blocks

[Z_t]_{i,(r)}=m^{-1/2}a_r 1{w_r(t)^T x_i>=0}x_i^T

and augmented block m^{-1/2}F(W(0),x_i)^T in row i. Thus Z_t is the full generalized Jacobian used by the procedure.

Set

K_n=n^{-1}[K(x_i,x_j)]_{i,j=1}^n,

and let P_{r0} be the orthogonal projector onto a leading r0-dimensional eigenspace of this exact kernel matrix. Use a fixed measurable eigenbasis selection rule if eigenvalues tie. Starting from theta_0, iterate

theta_{t+1}=theta_t-(eta/n)Z_t^T P_{r0}(f_t(S)-y),

where f_t(S)=(f(theta_t,x_i))_{i=1}^n and y=(y_i)_{i=1}^n.

Assume delta in (0,1/2), positive integers n,T satisfying

n>=C_0 log(4/delta)d^{2k0},

a_T n/d^{k0}<=T<=b_T n/d^{k0},

and write w=d^{k0}/n. Take

m>=C_0 max{n^{2/d},T^{5/3},T^{15/2}d^{5/2}w^{-5},T^{25/2}d^{5/2}},

m/log m>=C_0 d.

The constants are chosen so that these conditions imply r0<n and w<1. They do not depend on n,d,m,T,delta.

## Task

Prove that, with probability at least

1-delta-exp(-cn)-2exp(-cr0)-2/n

over the covariates, noise, seeds, and signs, simultaneously every integer iterate t with c_tT<=t<=T satisfies

E_{x~Unif(S^{d-1})}[(f(theta_t,x)-f*(x))^2]

<=C_1 log(4/delta)d^{k0}/n.

The expectation is over a fresh independent covariate, with the trained parameters held fixed.

Consequently, prove that for any epsilon>0 it suffices to choose

n>=C_2 max{log(4/delta)d^{2k0},log(1/delta)d^{k0}/epsilon}

for population risk at most epsilon with the same probability bound, provided the other width and horizon conditions above remain satisfied. Here C_2 may depend on the same fixed quantities as C_0 and C_1, but not on epsilon or n,d,m,T,delta.
