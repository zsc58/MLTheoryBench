# Problem

## Setup

Let D be a positive integer, M a nonnegative integer, and y_1,...,y_M observations in R^D at a fixed time. Consider one newly introduced component b in a Poisson-mixture measurement model with constant clutter intensity λ_c>0. Its state X lies in R^N, and H is a D-by-N observation matrix. Conditional on X and its latent positive-definite precision P, its positional likelihood is N(y;HX,P^{-1}).

The component has independent birth priors: a Gaussian state prior N(μ',Σ'), a Gamma rate prior with shape η'>0 and scale ρ'>0, and a Wishart precision prior with degrees of freedom φ'>D-1 and positive-definite scale Φ'. The birth existence weight is π_e∈(0,1), and its detectability weight is π_d=1. Define the fixed updated Gamma scale by

ρ=ρ'/(1+π_eπ_dρ').

The observations, birth parameters, weights, H, and λ_c are fixed across the iterations under consideration. Write ψ for the digamma function and define ψ_D(a)=sum_{i=1}^D ψ(a+(1-i)/2), for a>(D-1)/2. Determinants and traces are denoted by |·| and Tr(·).

Assume a diffuse observation-space birth prior: for finite τ>0, Σ' is positive definite and HΣ'H^T=τI_D, and the state update is interpreted in the limit τ→∞ with μ' fixed. This is an observation-space limiting convention, not a Gaussian probability distribution with an infinite covariance matrix. At each state update the limit is taken with that round's incoming association weights and updated rate and precision factors held fixed. Only the projected state moments Hμ and HΣH^T enter the scores and the next round.

A round starts with incoming association weights r_j∈[0,1] and mass β=sum_j r_j>0, together with finite incoming Gaussian observation-space mean m^-∈R^D and positive-definite covariance S^-. Update the precision factor first, then the rate factor, then the state factor, and finally the associations. Specifically, define

G=sum_{j=1}^M r_j[(y_j-m^-)(y_j-m^-)^T+S^-],

φ=φ'+β,   Φ^{-1}=(Φ')^{-1}+G,   η=η'+β.

The state update, written before taking the observation-space limit, is

Σ=(Σ'^{-1}+βH^TφΦH)^{-1},

μ=Σ(Σ'^{-1}μ'+H^TφΦ sum_j r_j y_j).

Here φΦ is the updated variational expected precision. The updated unnormalized score for y_j is

u_j=π_eπ_d ρ exp(ψ(η)) exp((ψ_D(φ/2)+log|Φ|-D log π)/2)
     · exp(-((y_j-Hμ)^TφΦ(y_j-Hμ)+Tr(φΦHΣH^T))/2).

Its next association weight is

r_j^+=u_j/(λ_c+u_j+c_j),

where c_j is the finite nonnegative combined score of the competing components in that round. The next round uses r_j^+ as its incoming weights and the just-updated projected state moments as m^- and S^-. These rounds are repeated with component b retained.

Fix s>0. Define

C_s=exp((ψ_D((φ'+s)/2)+log|Φ'|-D log π)/2)
    ·(π_eπ_d ρ/λ_c)·exp(ψ(η'+s)),

T_s=C_s exp(-D/(2s)).

After the precision, rate, and state updates of a round with 0<β<s, define

d_j=exp((y_j-Hμ)^TφΦ(y_j-Hμ)/2),

Δ=sum_{j=1}^M (1+T_s)/(d_j+T_s).

A fixed finite number B>0 is called admissible if Δ≤B for every incoming configuration consisting of weights r_j∈[0,1] with 0<sum_j r_j<s and Gaussian observation-space moments m^-∈R^D and positive-definite S^-. For M>0, B=M is admissible because d_j≥1. If M=0, any B>0 is admissible and the positive-mass premise below is impossible. No diffuse Gaussian state update at zero mass is part of the definition.

For an admissible B, set

A=(C_sB/(D/2))exp(-(D/2)/B).

If A<e, define L=s. If A≥e, define

V=[1/B-(1/(D/2))W_{-1}(-(D/2)/(C_sB)·exp((D/2)/B))]^{-1},

L=min{s,V}.

Here W_{-1}:[-1/e,0)→(-∞,-1] is the lower real branch of the Lambert W function, characterized by W_{-1}(z)exp(W_{-1}(z))=z. V is evaluated only in the case A≥e. The choices s and B, and hence L, remain fixed across subsequent rounds.

## Task

Prove that if at some iteration the association mass β of component b satisfies 0<β<L, then every subsequent round has positive incoming and outgoing masses and satisfies

β_new/β_old<Δ/B≤1,

where Δ is evaluated using that round's updated parameters. In particular, the masses remain below L, decrease strictly, and converge to zero. Thus, if retained and updated as specified, a component meeting the threshold has no nonvanishing limiting association mass.
