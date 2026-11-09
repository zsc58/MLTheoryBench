# Problem

## Setup

Let N, M, and K be positive integers, and let V ∈ R_+^{N×M}, E ∈ R_+^{N×K}, and D ∈ R_+^{K×N}, where R_+ denotes the nonnegative real numbers. The reconstruction is the M×N matrix

X = VᵀED.

Fix a dispersion parameter alpha > 0. For v ≥ 0 and x > 0, define

d_alpha(v || x) = v log(v/x) - (alpha+v) log((alpha+v)/(alpha+x)),

with the first term equal to zero when v=0. Extend this function to x=0 by

d_alpha(0 || 0)=0,   d_alpha(v || 0)=+infinity for v>0.

Set

F(E,D) = sum_{m=1}^M sum_{n=1}^N d_alpha((Vᵀ)_{mn} || (VᵀED)_{mn}).

At each fixed-factor update, take a current nonnegative pair with F(E,D)<infinity. Minimization of an auxiliary is over all nonnegative values of the factor being updated, including boundary values, and auxiliary functions may take the value +infinity.

Products denoted by ⊙ and all displayed quotients are elementwise; other matrix products are ordinary matrix products. Scalar addition to a matrix is entrywise. In the inner data/reconstruction quotient Vᵀ/X, define an entry 0/0 to be zero. In the outer quotient multiplying a factor, define 0/0 to be 1, so that the corresponding factor coordinate remains unchanged. As usual, zero divided by a positive number is zero.

## Task

Construct tight MM auxiliary functions for the two fixed-factor objectives and prove that alternating minimization of these auxiliaries yields

E^{t+1} = E^t ⊙ [ V ( Vᵀ/(VᵀE^tD) ) Dᵀ ] / [ V ( (alpha+Vᵀ)/(alpha+VᵀE^tD) ) Dᵀ ],

and, with E fixed,

D^{t+1} = D^t ⊙ [ (VᵀE)ᵀ ( Vᵀ/(VᵀED^t) ) ] / [ (VᵀE)ᵀ ( (alpha+Vᵀ)/(alpha+VᵀED^t) ) ].

Specifically, show that each auxiliary globally majorizes its fixed-factor divergence on the nonnegative domain, is tangent in the sense of equality at the current iterate, and has the displayed update as a coordinatewise minimizer, with the stated quotient conventions. Establish that the updates are well-defined, have finite objective, and give nonincreasing F under alternation. In alternation, each factor update uses the most recently updated value of the other factor.
