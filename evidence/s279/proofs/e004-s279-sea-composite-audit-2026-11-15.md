# Entropy-gradient amplification: preparation boundary and a composite positivity obstruction

S279 / E004, 2026-11-15. Full goal `prove nonlinear quantum computing` remains active. Internal analytic source audit and a scoped counterexample, not proof of a physical nonlinear computer, an impossibility theorem for all nonlinear physics, or a publication/novelty claim. Base `7de732fba8a93f68b99dc4acdcb46b8a57b5a2c6`. Apply the [shared protocol including S3173](https://github.com/Quantyra/quantyra-planning/blob/main/docs/research-investigation-protocol.md). Prior jobs, inputs, ownership, stops, S277/S278 evidence and PaperMill remain unchanged.

## 1. Candidate, source and decision gate

Primary source: Rohit Kishan Ray and Gian Paolo Beretta, [arXiv:2301.11548v5](https://arxiv.org/html/2301.11548v5), 29 September 2025; published [Entropy 27(10), 1018](https://doi.org/10.3390/e27101018), 28 September 2025. The authors describe a phenomenological entropy-gradient model, not an experimentally established fundamental departure from quantum mechanics. Its explicit composite law and constrained dissipator make it a concrete alternative to adding another S277 energy carrier.

Named transfer questions: does its local nonlinear entropy flow act on a circuit-prepared output when the full preparation is included, and is its composite law positive on the stated density-operator domain? Inspect v5 equations 14-20, 39, 59-62 and Section 11. The PDF text on pages 12 and 15 independently matches the signs, tensor factors and factor 2 in the HTML equations. An attempted web PDF screenshot timed out; no successful visual rendering is claimed. A publisher version-notes request returned HTTP 429. The arXiv abstract identifies v5 as the latest listed version. Limited correction/positivity searches found no inspected replacement law; this is not exhaustive novelty clearance.

First falsifiers fixed before the exact diagnostic: the actual joint preparation has zero nonlinear evolution, or the published generator gives a negative population derivative at a zero eigenvalue. Stop this transfer at either supported failure; do not optimize its gain or silently substitute a new composite equation. One fixed exact arithmetic diagnostic is recorded separately; no trajectory simulation, physical trial, cloud/Lean job or independent review.

## 2. Reconstruct the published composite law

Set hbar=k_B=1. For two declared subsystems A,B and a joint density operator rho, write a=Tr_B rho and b=Tr_A rho. The published local-perception operation is

    F^A = Tr_B[(I tensor b)F],
    F^B = Tr_A[(a tensor I)F].                             (1)

The entropy operator is S=-Bln(rho), where Bln(x)=ln(x) for x>0 and Bln(0)=0 (source equations 18-20). Define

    Delta F^J = F^J - I Tr(rho_J F^J),
    (F,G)^J = Tr[rho_J {Delta F^J,Delta G^J}]/2,
    beta_J = (H,S)^J/(H,H)^J.

For the uniform metric with normalization and mean energy constraints, equations 59-62 give

    D_J = -(2/tau_J)[Delta S^J-beta_J Delta H^J],
    G_J = -{D_J,rho_J}.

Equation 39 is the GLOBAL equation

    dot rho = -i[H,rho] + G_A tensor b + a tensor G_B.      (2)

It is not an anticommutator of an embedded local operator with the joint rho. Replacing (2) by that different law would change the source being audited. The parameter tau_J is positive; the finite constant choices used below are sufficient. All covariance denominators in the counterexample equal 1, so no division by zero or redundant energy constraint is involved.

## 3. A boundary state makes the global generator nonpositive

In computational basis order 00,01,10,11, choose

    rho_* = diag(1,1,1,0)/3,
    H = X tensor I + I tensor X,
    tau_A=tau_B=tau>0.                                   (3)

This is a positive trace-one, rank-three separable state. The theory explicitly allows mixed density operators as homogeneous ontic states; (3) is tested in that declared mathematical domain. An epistemic mixture of three pure preparations is a different object under the source's ensemble interpretation and is not being silently identified with an available laboratory preparation. Both local states are full rank:

    a=b=diag(2/3,1/3).

The Hamiltonian is bounded below by -2; adding 2I makes it nonnegative and changes none of the centered quantities or dynamics. With ell=ln(3)>0, the exact entropy operator, including its prescribed value on the kernel, is

    S=ell diag(1,1,1,0),
    S^A=S^B=ell diag(1,2/3),
    Tr(a S^A)=8ell/9,
    Delta S^A=Delta S^B=ell diag(1/9,-2/9).               (4)

The perceived energy is H^A=H^B=X, its mean is zero and its variance is 1. Its covariance with the diagonal (4) is zero. Therefore beta_A=beta_B=0 and

    G_A=G_B=(8ell/(27tau)) diag(1,-1).                    (5)

Direct substitution into the full equation gives

    dot rho_diss = ell/(81tau) diag(32,-8,-8,-16).         (6)

The Hamiltonian commutator has zero 11,11 entry because rho_*|11>=0. Consequently

    <11|dot rho|11> = -16 ln(3)/(81tau) < 0.              (7)

Any differentiable positive-state trajectory starting at rho_* must instead satisfy <v|dot rho(0)|v> >= 0 for every vector v in its kernel: the scalar <v|rho(t)|v> is nonnegative for t>=0 and initially zero. Equation (7) violates this necessary tangent condition. Equivalently, a differentiable solution of the displayed initial-value law would have

    Pr(11 at t) = -16 ln(3)t/(81tau) + o(t),

which is negative for sufficiently small positive t. Thus the stated global generator does not define a positive differentiable evolution on its entire declared density-operator domain. This is an exact boundary obstruction, not a finite-step numerical integration artifact.

Unequal positive finite times do not remove it:

    <11|dot rho|11> = -(8ln(3)/81)(1/tau_A+1/tau_B).       (8)

Both local derivatives in (5) have zero trace, obey the energy constraint and preserve local positivity for sufficiently small times. This illustrates the specific proof gap: parametrizing the LOCAL square roots in source equation 42 does not establish positivity of the reconstructed GLOBAL state in (2). Norm and energy checks alone pass this counterexample.

### Scope and the discontinuous boundary prescription

The conclusion concerns equations (2)-(3) as a pointwise differentiable initial-value law, with the stated Bln(0)=0 convention and finite positive tau. It does not assert that all full-rank trajectories become negative, that every SEA equation is invalid, or that the source's every numerical example is wrong. It does not adjudicate the complete no-signaling claim. A proposed weak or non-differentiable boundary solution could evade this tangent test, but then the displayed finite right-hand side is not its initial infinitesimal generator; its existence, selection rule and computational error/time contract would need separate justification.

Indeed, for rho_delta=diag(u,u,u,delta), u=(1-delta)/3 and 0<delta<1/4, the same diagonal entropy calculation gives a positive kernel-cell population derivative proportional to ln(u/delta). It diverges positively as delta tends to zero if tau stays fixed. At delta=0 the published Bln convention produces (7) instead. Therefore taking a full-rank limiting law would be a different boundary prescription; it cannot be claimed to agree with the pointwise generator. Restricting to full rank would also require reassessing algorithms whose zero-versus-positive acceptance promise uses the boundary.

## 4. What any positivity repair must change

For equal tau let c=16ln(3)/(81tau), the magnitude in (7). If a proposed differentiable positive generator replaces F(rho_*) by F(rho_*)+R, then

    R_11,11 >= c.

For a Hermitian trace-preserving correction, Tr R=0, this forces ||R||_1/2 >= c. This follows by applying the two-outcome measurement {|11><11|, I-|11><11|} to the positive and negative parts, or by diagonal pinching.

If the repair also preserves BOTH local marginal derivatives, Tr_A R=Tr_B R=0, its diagonal entries must be (r,-r,-r,r), with r>=c. Pinching then strengthens the requirement to

    ||R||_1/2 >= 2c = 32ln(3)/(81tau).                    (9)

The diagonal matrix R=c diag(1,-1,-1,1) attains the norm lower bound and cancels the offending kernel block at this point while preserving both marginals and mean energy. This is only an instantaneous tangent correction, not a positive flow, no-signaling dynamics, entropy theorem or physical realization.

The structural reason is visible without logarithms. Under the dissipative part of (2), the connected correlation operator C=rho-a tensor b has dot C=0. With local noninteracting Hamiltonians, its remaining derivative is simply -i[H,C]. The model changes local states while retaining that connected operator up to local rotations. For (3), C=diag(-1,1,1,-1)/9, so decreasing both local populations a_1,b_1 from 1/3 immediately makes their implied joint 11 probability a_1 b_1-1/9 negative. A repair must allow a compensating change of correlations or otherwise constrain the local flow. Merely rechecking the two marginals does not escape the obstruction.

## 5. The apparent amplifier and its preparation cost

An isolated diagonal qubit with degenerate H and homogeneous state diag(1-p,p), treated as one unconstrained-normalization SEA system after removing the redundant energy constraint, obeys the scalar equation

    dot p = (4/tau) p(1-p) ln[(1-p)/p].                   (10)

For 0<p<1 its exact solution is

    p(t) = p(0)^alpha / [p(0)^alpha+(1-p(0))^alpha],
    alpha=exp(-4t/tau).                                  (11)

The endpoints are stationary under the source convention. At T=(tau/4)ln(n), n>=1, a promised p(0)=0 stays zero, whereas any p(0)>=2^-n gives p(T)>=1/3. Three independent fresh trials would then succeed with probability >=1-(2/3)^3>2/3. The isolated waiting time is O(tau log n), assuming a fixed or polynomially bounded relaxation time. This is an elementary conditional consequence of a postulated single-system law, not an efficient physical SAT algorithm or a novelty claim.

The missing input matters. A polynomial reversible circuit for a predicate f produces the GLOBAL pure state

    |Psi_f> = 2^(-n/2) sum_x |x>|f(x)>,

whose output marginal has p=m/2^n. For the actual joint projector |Psi_f><Psi_f|, Bln(rho)=0 everywhere, so S=0, all entropy gradients vanish, and the published composite dynamics reduces to ordinary unitary dynamics. This agrees with the source's explicit Section 11 pure-state statement. Ignoring or tracing out the first register does not physically turn this preparation into an uncorrelated homogeneous ontic mixed input for (10). An epistemic mixture of pure computational outputs also evolves componentwise with no entropy-gradient gain under the source's measure-of-preparations rule.

One must therefore construct and charge an allowed conversion to the required ontic mixed preparation, including the environment and references, rather than insert (11) after a formal partial trace. A nonlinear bath with separately supplied homogeneous resources might alter this conclusion, but its joint preparation and dynamics are not supplied here. This is the same preparation/composition obligation already recognized in S259/S260, not an additional independent general no-go. The new global-positivity witness is a distinct earlier failure of the displayed candidate law.

No complete resource theorem follows: the isolated formula charges three uses and its waiting time, but not the unavailable preparation conversion, physical tau, interaction/noise source, precision/robustness at p=0, apparatus energy/work, or causal all-history operation. The full goal requires these and a genuine computational guarantee, not just (11).

## 6. Verification, strategy and objective audit

The fixed exact Node diagnostic passes 244 rational matrix assertions, checking four declared positive time-scale pairs, nonzero covariance denominators, full/marginal derivatives, trace and energy, the kernel witness, a full-rank product control and a pure-state control. Script arithmetic time 0.1329645 seconds; the process finished within 1.7274783 seconds under the 60-second cap. Stdout contains PASS and stderr is empty. The PowerShell launcher failed to retain the child exit code (null in the preserved receipt); no exit-code-0 claim or rerun is substituted. No trajectory or parameter search was run. The analytic argument, not the assertion count, proves the scoped result.

Source correspondence is against both HTML and PDF text; it is not an independent review of the proof. The inspected primary source explicitly defines the null-eigenvalue convention and full mixed-state domain. The cited source is CC BY 4.0 and remains attributed; its equations are reconstructed here and the counterexample/correction bounds are our internal analysis. No exhaustive novelty or publication-worthiness determination has occurred.

Decision: PARK this displayed composite law as a general physical substrate. Physical-construction SELECTION NONE. Reopening requires a specified global positive update, a composition/causality audit and an affordable ontic-preparation mechanism. A local square-root parametrization or another isolated entropy curve does not qualify. A tangent-cone modification is a concrete mathematical escape, but (9) shows it cannot be a vanishing correction preserving the source's local flow at this witness; no full modified mechanism is selected automatically.

Full-objective audit: no physical nonlinear-computing theorem, experiment, native coupling or general BPP/BQP improvement. New auxiliary evidence: a global positivity counterexample and a necessary repair-size bound. External validation: attributed reconstruction of the known pure-global-state limit, with its explicit preparation consequence; not validation of the whole paper. Operational work: source custody and one exact arithmetic diagnostic, with the exit-code capture limitation preserved. S278's energy findings and all earlier valid results/counterexamples remain.

The protocol improved actual selection: the complete joint generator and a kernel probability were checked before pursuing the isolated logarithmic-time curve. Remaining to-do list: a qualifying positive, causal native interaction with operational energy/work and paid preparation; full goal active, no automatic successor. This changes the next research decision because this concrete candidate fails global probability positivity before it can supply a computational amplifier.
