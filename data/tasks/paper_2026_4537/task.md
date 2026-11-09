# Problem

## Setup

Let d, m, and K be positive integers, x in R^d, y in {1,...,K}, and epsilon be a nonnegative real number. Define C_epsilon(x)={x' in R^d: ||x'-x||_infinity <= epsilon}. A student has the form f=g composed with h, where h:R^d->R^m and g:R^m->R^K. A teacher has feature map h^t:R^d->R^m; the teacher feature used below is h^t(x). Fix x_adv in C_epsilon(x). Let 1^K denote the vector of K ones, and define z_f(u,y)=f(u)_y 1^K-f(u) for u in R^d.

Assume there are sound coordinatewise bounds underline h, overline h in R^m such that underline h_i <= h_i(x') <= overline h_i for every x' in C_epsilon(x) and i=1,...,m. For alpha in [0,1], define

ell_i^alpha=(1-alpha)h_i(x_adv)+alpha underline h_i,

nu_i^alpha=(1-alpha)h_i(x_adv)+alpha overline h_i,

R_mix(alpha)=sum_{i=1}^m max{(ell_i^alpha-h_i^t(x))^2,(nu_i^alpha-h_i^t(x))^2},

R_adv=||h(x_adv)-h^t(x)||_2^2,

and

overline R=sum_{i=1}^m max{(underline h_i-h_i^t(x))^2,(overline h_i-h_i^t(x))^2}.

If the student head g is affine, define the feature-space logit-difference map by

zeta(a,y):=g(a)_y 1^K-g(a)=tilde W a+tilde b, for a in R^m,

where tilde W is in R^{K by m} and tilde b is in R^K. Define the signed matrix parts entrywise by ([tilde W]_+)_{ji}=max{tilde W_{ji},0} and ([tilde W]_-)_{ji}=min{tilde W_{ji},0}. Define the sound lower logit bound

underline z=[tilde W]_+ underline h+[tilde W]_- overline h+tilde b,

the adversarial vector z_adv=zeta(h(x_adv),y), and

z_mix^alpha=(1-alpha)z_adv+alpha underline z.

## Task

Prove that R_mix is continuous and monotonically nondecreasing on [0,1], that R_mix(0)=R_adv, R_mix(1)=overline R, and that R_adv<=R_mix(alpha)<=overline R for every alpha in [0,1]. In the affine-head case, prove the coupled representation z_mix^alpha=[tilde W]_+ell^alpha+[tilde W]_-nu^alpha+tilde b for every alpha in [0,1], where ell^alpha,nu^alpha are the vectors of the coordinates defined above.
