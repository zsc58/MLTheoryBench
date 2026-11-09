# Problem

## Setup

Let A>=1 and d_1,...,d_A>=1 be integers with d_1+...+d_A=d, and identify R^d with R^{d_1} x ... x R^{d_A}. Write z_alpha for the alpha-th block of z. For any dimension k, C0(R^k) denotes the continuous functions vanishing at infinity; Lebesgue and Sobolev spaces are taken with respect to Lebesgue measure.

For each block alpha, let kappa_alpha:R^{d_alpha} -> (0,infinity) be a kernel in C0 intersect L1 intersect Linfinity intersect W^{1,1}. Assume there are constants c_{1,alpha},c_{2,alpha},lambda_{0,alpha}>0 and lambda_{1,alpha}>=0 and a strictly positive eta_alpha in C2(R^{d_alpha}) such that eta_alpha and its gradient lie in C0 intersect L1 intersect Linfinity, its Hessian is bounded, and, for every z in R^{d_alpha},

grad eta_alpha(z)=-z kappa_alpha(z)/c_{1,alpha},

(lambda_{0,alpha}I-lambda_{1,alpha}Delta)eta_alpha(z)=c_{2,alpha}kappa_alpha(z).

Define kappa(z)=product_alpha kappa_alpha(z_alpha) and eta^[alpha](z)=eta_alpha(z_alpha) product_{beta ne alpha} kappa_beta(z_beta).

For a finite nonnegative Borel measure r on R^d define

u_r(x)=integral kappa(x-y)r(dy),

m_r(x)=integral y kappa(x-y)r(dy),

a_r(x)=m_r(x)/u_r(x) when u_r(x)>0.

For probability measures p and r define V_{p,r}(x)=a_p(x)-a_r(x). The companion-elliptic assumptions imply that these ratios are defined for every x and every probability measure. Let C0-vague convergence mean convergence against every f in C0(R^d), and let M_{<=1}(R^d) be the finite nonnegative Borel measures of total mass at most one. For a probability measure p and a finite nonnegative Borel measure r, set

Z_p(r)=integral u_p(x)r(dx).

## Task

Fix a Borel probability measure p on R^d and a sequence of Borel probability measures (q_n). Assume that V_{p,q_n}(x) tends to 0 for every x in R^d. Prove that every C0-vague subsequential limit mu of (q_n) belongs to M_{<=1}(R^d) and has the form

mu=c p for some c in [0,1].

Moreover, if

liminf_{n to infinity} Z_p(q_n) >= Z_p(p),

then q_n converges weakly to p on R^d.
