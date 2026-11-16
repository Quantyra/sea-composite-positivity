# Full-manuscript Lean certification plan

2026-11-16. PaperMill P012 / S025; Quantum scientific custody S279/S289. **PLAN ONLY; no Lean source, compiler run, accepted declaration or completed C1 audit.** The certification target is the entire candidate manuscript and [claim inventory](../CLAIMS.md), not only its negative rational coefficient. Exact source/PDF hashes are in `verification/build.json` and the frozen Git commit.

## Objective, operation and first decision gate

Input: the frozen manuscript, source correspondence, immutable S279 evidence, and one specifically pinned candidate Lean/mathlib dependency set. Output of C1: complete claim-to-type/dependency/axiom table, source-interpretation boundary, actual reusable declaration types, missing proofs, module graph, effort/routing estimate and an explicit proceed/hold decision. There is no approximation error in the target; all statements are exact over complex matrices and real logarithms. Source-to-equation interpretation additionally requires external review; a kernel cannot certify that a formula fairly represents a publication.

Quantitative payoff: certify the all-positive-time kernel derivative `-8*log(3)/81*(1/tauA+1/tauB)`, the `c` and `2c` half-trace-norm repair thresholds with attaining curves, and the explicit positive divergent full-rank expression. There is no general computational bound or physical realization payoff.

First falsifier: the formal source-derived generator fails to reduce to the claimed derivative under an admissible witness, or a supposed trace norm/tangent lemma actually proves a weaker surrogate. Stop and repair the written claim before moving downstream. The weakest expected formal bridge is not rational arithmetic: it is reconciling the finite spectral Bln convention, arbitrary Hermitian repair norm and actual one-sided trajectory semantics with library types.

Bounded next action when scheduled: one read-only C1 pass, proposed cap 90 minutes, with a single candidate dependency pin and no compilation/remote dispatch. Inspect the spectral/trace-norm/tangent bridges before estimating the easy matrix core. End with a missing-dependency list if the cap is reached; do not label that a complete audit or manufacture a proof campaign. Two substantive failures of one bridge trigger reassessment, not repeated equivalent encodings. This is queued work, not a job started by intake.

## Representation and non-negotiable semantics

Use `Qubit := Fin 2`, `Joint := Qubit × Qubit`, and complex matrices indexed by these types. Define density operators by genuine positive semidefiniteness and trace one. Prove the product-basis identification with the manuscript order; implement partial traces as finite sums and tensor product entries explicitly or through a library operation with proved correspondence. Real-only computations are useful lemmas, not a restriction on the ambient complex trajectories or repair matrices.

Define Bln through finite Hermitian spectral calculus, with zero mapped to zero and positive eigenvalues mapped to `Real.log`. Prove diagonal evaluation and its match to the source definition. The scalar function is discontinuous at zero, but a fixed finite spectrum supports its spectral evaluation; do not assume continuity through a varying zero eigenvalue. Mathlib's chosen scalar-log value at zero must be checked explicitly before using it as the same convention. Keep both finite positive relaxation times as quantified real parameters.

Use the actual Schatten-1 trace norm. If it is implemented as a sum of absolute Hermitian eigenvalues, prove equivalence to `Tr sqrt(R†R)` for this domain. Do not rename sum of absolute diagonal entries as the trace norm. Prove the scalar one-sided derivative assertion on `Ici 0` or a precisely specified right-neighborhood filter and transfer matrix derivatives through the quadratic form. An Euler-step calculation alone is not the trajectory theorem. Sharpness requires an actual positive trace-one curve with the advertised derivative, including the commutator.

## Proposed modules and acceptance statements

Names below are proposed module/lemma contracts, not existing declarations or Lean code.

| Module | Claims | Exact deliverable and dependencies |
|---|---|---|
| `SEA/FiniteMatrices` | D1, C2 | Finite complex tensor/partial-trace identities; Hermitian/PSD/density semantics; basis and marginal indexing; trace product and commutator laws |
| `SEA/SourceDefinitions` | D1 | Spectral Bln, entropy perception, centering, covariance, beta, local and joint fields; no assumption of their positivity |
| `SEA/SourceBridge` | D1, C3 | For the witness, spectral entropy equals diag(log3,log3,log3,0); all perceived/covariance expressions reduce from the source definitions; nonzero denominator facts derived |
| `SEA/KernelTangent` | C1 | Any right-differentiable PSD curve has nonnegative kernel quadratic-form derivative; correct one-sided filter and real-part semantics |
| `SEA/Witness` | C2-C5 | Density/separability/rank/marginal facts; denominators=1, beta=0, exact local and joint fields for arbitrary positive times; log3>0; trace and energy constraints; H bound/shift and equal-time corollary |
| `SEA/NoPositiveInitialFlow` | C4 | No positive right-differentiable curve from the witness has initial derivative equal to the defined field; compose SourceBridge, Witness, KernelTangent |
| `SEA/Correlation` | C6-C7 | Product derivative, partial traces of the local commutators, and Cdot identity under exact local-H/traceless-G assumptions; witness C entries |
| `SEA/TraceNorm` | C8 | Spectral definition bridge and `sum abs(diag R) <= traceNorm R` for all Hermitian R; diagonal norm evaluation |
| `SEA/RepairBounds` | C9-C10 | Any positive tangent correction has kernel entry>=c; trR=0 implies half norm>=c; both partial traces zero imply half norm>=2c; no diagonality hypothesis on R |
| `SEA/RepairSharpness` | C11 | R0/R1 attain bounds; construct short positive trace-one linear diagonal path; conjugate by the actual matrix exponential; prove derivative, unitary positivity, marginal and energy claims at zero |
| `SEA/FullRankLimit` | C12 | Density/full-rank/covariance hypotheses for 0<delta<1/4; exact formula 8uv^3*sumInvTau*log(u/delta); strict sign; right-limit=+infinity for fixed times |
| `SEA/BoundaryControls` | C13 | Spectral Bln of every pure projector is zero; the displayed uniform product witness has zero dissipative drift |
| `SEA/Checks` | All | Exported theorem list, full `#print` statements and transitive axiom audit; assumptions/coverage matrix and any justified exclusions |

Dependency order: finite semantics -> source definitions/bridge and tangent -> witness/no-flow; finite semantics -> correlation; trace norm plus tangent/witness -> repair bounds -> sharpness; source bridge and real-log analysis -> full-rank limit. The kernel counterexample can be checked early without waiting for all auxiliary modules, but cannot be called full-manuscript certification until every retained claim is covered.

## Read-only library reconnaissance, not C1 completion

Inspected local bare mathlib snapshot `c5ea00351c28e24afc9f0f84379aa41082b1188f`, whose `lean-toolchain` is `leanprover/lean4:v4.30.0`. This is a **candidate**, not a campaign pin or authorization to change any active toolchain. Current PaperMill projects may use other versions; do not transplant their declarations or trust their receipts without matching types and commits.

Source inspection found:

- `Mathlib/LinearAlgebra/Matrix/PosDef.lean`: `Matrix.PosSemidef`, `Matrix.posSemidef_diagonal_iff`, the finite dot-product characterization, and `PosSemidef.dotProduct_mulVec_nonneg`. Check namespace/typeclass instantiations for complex matrices during C1.
- `Mathlib/Analysis/Matrix/HermitianFunctionalCalculus.lean`: the Hermitian finite functional calculus and its `cfc_eq` bridge. Availability alone does not prove the discontinuous Bln evaluation.
- `Mathlib/Analysis/SpecialFunctions/Log/Basic.lean`: `Real.log_pos`, `Real.log_inv`, `Real.log_div`. The one-sided divergence theorem and composition must still be located and audited.
- Matrix Hermitian, trace and positive-matrix files exist. No reusable partial-trace, Schatten-1, matrix-exponential derivative, or one-sided kernel theorem has yet been accepted for this plan.

No imports were compiled and no transitive axioms were checked. These observations reduce discovery uncertainty, not mathematical or formal obligations. C1 must inspect actual reusable types rather than infer coverage from filenames.

## Execution, cost and review gates

1. **C1 — full dependency/type/cost audit.** Produce the complete map above against one pinned environment. Scientific value is a source-specific correctness test; formal leverage and effort remain UNKNOWN. The fixed matrix arithmetic is comparatively small; spectral semantics, norm equivalence and one-sided analysis may dominate. Do not assign a fabricated completion date or declaration count.
2. **C2 — author and compile when eligible.** PaperMill's existing tt-quietbox/OProver route authors candidates. Compilation uses independently admitted CPU01-CPU05 under current leases, source custody, resource guards and stop conditions. CPU06/webserver is retired from compute. No local Lean/Lake/LSP build, new host use, spend or preemption follows from this plan. Stop at missing admission, a guard event or an unapproved dependency/claim change.
3. **C3 — exact-source kernel/type/axiom acceptance.** Freeze the author inputs and candidate outputs; compile every module, audit the actual theorem types and all transitive axioms under PaperMill's allowed set; reject `sorry`, `admit`, `sorryAx`, axiomatized target claims or unchecked external arithmetic. Store real exit codes, warnings, logs and hashes. No numerical receipt substitutes for a proof.
4. **C4 — required three-lens formal review.** Follow the current shared formal review protocol and provider requirements on the frozen source and kernel evidence. Establish source semantics, mathematical scope and adversarial claim coverage. Internal review in this repository does not discharge this gate.
5. **R1-R4 — reconcile and release decision.** Reconcile every manuscript claim with final types, document all assumptions/dependencies and uncovered text, rebuild/review source and PDF, then obtain/use the separately applicable publication authority. Source/domain correspondence and novelty checks remain distinct from kernel acceptance; independent human peer review is recommended, not newly required by this plan. Archive and DOI/release are separate operations.

Charge author inference, rejected candidates, compilation, dependency setup, review and reconciliation separately. Existing PaperMill queues/jobs and scientific custody are preserved. The exact finite diagnostic is already paid preparation work (122 checks, one run); it is neither C2 nor C3 work.

Remaining to-do list: C1 first; then admitted full C2-C4 and R1-R4. This changes the next research decision because the candidate is ready for scoped assurance work while the parked physical SEA route remains parked; neither a rational-only proof nor this plan can masquerade as a full scientific resolution.
