# Problem

## Setup

Let `Y` be a finite or countable action set and let `pi_k` be a probability mass function with `pi_k(y)>0` for every `y`. Fix a policy `rho` absolutely continuous with respect to `pi_k`. For an update fluctuation `v`, the resulting policy is `pi_new(y)=pi_k(y)(1+v(y))`.

Let `H=L^2(pi_k)` with inner product `<f,h>_{pi_k}=E_{pi_k}[fh]` and norm `||f||`. Let

`H0={f in H:E_{pi_k}[f]=0}`.

Let `A` be a real-valued advantage field and let `alpha` be fixed so that `(rho(y)/pi_k(y))^alpha` is defined for every `y`. Define the fixed escort field and driving field

`E_alpha(y)=(rho(y)/pi_k(y))^alpha`, `g_alpha(y)=E_alpha(y)A(y)`,

and assume `g_alpha in H`. Fix `mu>0`, put `u*=g_alpha/mu`, and define

`K={f in H0:f(y)>=-1 for every y}`.

## Task

Prove the following integrated theorem. The unique minimizer of `(mu/2)||v-u*||^2` over `H0` is

`v_perp(y)=(g_alpha(y)-E_{pi_k}[g_alpha])/mu`.

The unique minimizer over `K` is

`v_b(y)=max(-1,(g_alpha(y)-lambda*)/mu)`,

where `lambda*` is the unique real number satisfying

`E_{pi_k}[max(-1,(g_alpha-lambda*)/mu)]=0`.

Consequently the updated policy `pi_new(y)=pi_k(y)(1+v_b(y))` is a valid probability distribution, and every action with `g_alpha(y)<lambda*-mu` has `pi_new(y)=0`.
