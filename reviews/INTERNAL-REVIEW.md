# Internal preparation review and disposition

2026-11-16, S289. Reviewer: the same OpenAI Codex agent performing preparation. These are three internal perspectives, **not** independent agents, external providers, human peer review, or formal certification. No Claude/Grok/AGY acceptance is claimed. The final source/PDF hashes are in the build and package receipts.

| Perspective | Question / finding | Disposition |
|---|---|---|
| Source and domain | Journal HTML has updates after arXiv v5; do current equations differ? | Retrieved current version-of-record PDF, visually checked pp.9/12/15/16, recorded hashes and version-notes distinction. Targeted equation still agrees. External domain review remains. |
| Source and domain | Could singular local energy covariance invalidate the witness? | Both denominators computed as 1 using local X; beta=0. All marginals full rank. |
| Mathematical | Does a negative Euler step prove a true trajectory obstruction? | Replaced any numerical-integration inference by an explicit one-sided kernel tangent lemma. No ODE existence or uniform remainder estimate assumed. |
| Mathematical | Do repair matrices only attain an algebraic lower bound? | Supplied a positive trace-one short linear curve for the corrected diagonal dissipator, conjugated by exp(-itH), proving actual tangent attainment for the full derivative. No global repaired flow claimed. |
| Mathematical | Does diagonal arithmetic suffice for the norm bound against arbitrary repairs? | Wrote the Hermitian spectral decomposition proof of sum abs(diagonal)<=trace norm. Off-diagonal repairs included in the lower bound. |
| Mathematical | Can the Hamiltonian be dropped? | Only its diagonal/kernel expectation is zero. Kept the full commutator in the flow and in sharpness. |
| Adversarial scope | Does approaching the witness from full rank reproduce the sign? | Derived exact opposite-sign expression 8uv^3(sum inverse times) log(u/delta), positive and divergent. Section 5 makes the distinction explicit. |
| Adversarial scope | Does preserving connected correlation mean the operator or all correlation measures are constant? | Claimed only Cdot=-i[H,C] for local H; abstract explicitly says unitary evolution, not constant operator; no information-measure assertion. |
| Adversarial scope | Are other SEA formulations, pure states, physical nonlinear computing or signaling refuted? | Explicitly excluded those conclusions. Added the pure-projector control and restricted related-work comparison. |
| Reproducibility | Earlier S279 child exit code was absent | Original receipt imported unchanged. New independent Python implementation ran once, 122 exact checks, exit 0, 0.271 seconds wall, under the preregistered 60-second cap. This does not retrospectively fill the old receipt. |

The first document build exposed three layout warnings, which were repaired without changing the mathematics. Visual PDF inspection also found an orphaned bibliography continuation; the final five-page build/layout receipt records the corrected package. The package checker initially rejected the original receipt's UTF-8 byte-order mark; its reader was corrected without changing the archived bytes. These are operational corrections, not mathematical failures. Tectonic also emitted a Fontconfig environment message; all final pages rendered correctly, with no final TeX layout, missing-character or reference diagnostics.

Limits of the review: there is no independent confirmation of the source/domain reading, source-specific priority or full argument. Such review is recommended, not a new compulsory human gate. Technical proof obligations in the written draft have explicit proofs; this is an internal assessment, not a guarantee that reviewers cannot find an error. Formal debt is all of C1-C4 in [the Lean plan](../formal/CERTIFICATION-PLAN.md), including its applicable provider reviews. Funding/competing-interest declarations and the publication destination remain to be finalized for submission; publication itself is not authorized by preparation.

Decision: retain the scoped manuscript candidate and hand it to PaperMill; do not reopen the parked physical SEA-computation route or broaden to a general nonlinear impossibility paper.
