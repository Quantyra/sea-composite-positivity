# Full manuscript claim inventory

Frozen candidate: `manuscript/main.tex`; build and package receipts bind the exact bytes. All entries below have written arguments. None has a Lean certificate or independent review acceptance.

| ID | Claim | Essential assumptions / limits | Manuscript location | Formal target |
|---|---|---|---|---|
| D1 | Perceived operators, centered covariance, spectral Bln, local dissipators and joint vector field match the tested equation | Two finite subsystems; Bln(0)=0; uniform metric; normalization and mean energy; nonzero energy variance; hbar=kB=1 | Section 1, equations (1)-(5) | SourceDefinitions / SourceBridge |
| C1 | A positive curve has a nonnegative kernel quadratic-form right derivative | Positivity for t>=0 near zero; actual right derivative, kernel vector | Lemma 1 | KernelTangent |
| C2 | The witness is separable, PSD, trace one, rank three; both marginals are diag(2/3,1/3) | Basis 00,01,10,11; complex matrices even though entries are real | Theorem 2 | Witness |
| C3 | Perceived entropy and Hamiltonian, covariance denominators and generator evaluate as displayed | Natural log; Bln kernel value; covariance denominators exactly 1, not assumed away | Theorem 2 proof, equations (9)-(15) | Witness / SourceBridge |
| C4 | The kernel derivative is -8 log(3)/81 times the sum of inverse times, strictly negative; no positive right-differentiable initial trajectory obeys it | Every finite positive tauA,tauB; full Hamiltonian commutator included | Theorem 2 | NoPositiveInitialFlow |
| C5 | Trace and local mean-energy constraints hold; equal-time diagonal formula; H>=-2I and identity shifts leave the field unchanged | Centered perceived covariance; local X Hamiltonian; does not say the whole commutator vanishes | Section 2 | WitnessAuxiliary |
| C6 | Connected correlation obeys Cdot=-i[H,C] | Local additive H; trace-one marginals; traceless GJ; any differentiable solution; GJ may depend on the global state | Proposition 3 | Correlation |
| C7 | Witness connected correlation is diag(-1,1,1,-1)/9 and dissipative marginal drift produces the kernel violation | Instantaneous statement; C may rotate under local H | Section 3 | Correlation |
| C8 | Sum of absolute diagonal entries of Hermitian R is at most its genuine trace norm | Arbitrary Hermitian 4-by-4 complex matrix, not assumed diagonal | Equation (20) and proof | TraceNorm |
| C9 | Positive tangent correction requires R11,11>=c; trace preserving correction has half trace norm>=c | R Hermitian, tr R=0, corrected field is derivative of a PSD curve | Proposition 4 | RepairBounds |
| C10 | Both marginal derivatives preserved implies half trace norm>=2c | Both partial traces zero, including off-diagonal constraints | Proposition 4 | RepairBounds |
| C11 | Both bounds are attained as actual positive trace-one curve derivatives; R1 also preserves both marginal derivatives and mean energy at time zero | R0 and R1 as given; short linear dissipative curve conjugated by exp(-itH) | Proposition 4 proof | RepairSharpness |
| C12 | Full-rank family has positive kernel-population derivative 8uv^3(sum inverse times) log(u/delta), diverging to +infinity | 0<delta<1/4; u=(1-delta)/3; v=u+delta; fixed positive times | Section 5 | FullRankLimit |
| C13 | Pure projector has Bln=0; uniform product control has zero dissipative drift | Specified spectral convention; arithmetic controls support special substitutions only | Section 6 / diagnostic | BoundaryControls |

The proposition numbers in the rendered PDF are 1-4 across theorem environments; claim IDs remain stable across editing. Definitions and unnumbered subsidiary claims are part of the certification target, including logarithm identities, Hamiltonian shifts, trace-norm semantics and the one-sided limiting statement.

Excluded conclusions: positivity failure of every full-rank solution; a no-go for all SEA models; superluminal signaling; a globally positive repaired flow; an experimentally realizable nonlinear gate; BPP/BQP progress. Source correspondence is a documented external interpretation in addition to the formally checkable mathematical definition. It must remain reviewable even after Lean checks succeed.
