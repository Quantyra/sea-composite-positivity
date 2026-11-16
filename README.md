# Boundary positivity in composite steepest-entropy-ascent dynamics

Published preprint: **[DOI 10.5281/zenodo.24293863](https://doi.org/10.5281/zenodo.24293863)**. [GitHub release](https://github.com/Quantyra/sea-composite-positivity/releases/tag/v1.0.0) · [Archive verification](verification/publication-v1.0.0.json).

Preprint version 1.0.0, 2026-11-16, by Daniel Fredriksen, Quantyra Inc. Separate Claude, Grok and AGY AI reviews are complete on the corrected source; [reports and dispositions](reviews/three-lens-2026-11-16/DISPOSITION.md) retain their exact scope and failed attempts. Human peer review and Lean certification are not claimed.

The paper gives a rank-three, two-qubit counterexample to positivity of the pointwise composite equation in Ray and Beretta, *Entropy* 27, 1018 (2025), under its stated kernel-logarithm convention, uniform metric and normalization/mean-energy constraints. For arbitrary finite positive local relaxation times, the initially zero joint population has derivative

\[
-\frac{8\ln 3}{81}(\tau_A^{-1}+\tau_B^{-1})<0.
\]

The marginals are full rank and both energy covariance denominators are one. The paper also proves a connected-correlation identity, sharp instantaneous repair bounds, and an explicit divergent full-rank approach. These distinguish a pointwise boundary failure from other SEA equations or boundary completions. No physical nonlinear-computing, signaling, general simulation or complexity-class result follows.

## Read the package

- [Manuscript PDF](manuscript/main.pdf) and [LaTeX](manuscript/main.tex).
- [Claims and assumptions](CLAIMS.md), [primary-source correspondence and novelty limits](SOURCES.md).
- [Three-lens review summary](reviews/REVIEW-SUMMARY.json) and [dispositions](reviews/three-lens-2026-11-16/DISPOSITION.md).
- [Internal review and dispositions](reviews/INTERNAL-REVIEW.md): same-agent mathematical/source/adversarial review, not independent provider review.
- [Full-manuscript Lean certification plan](formal/CERTIFICATION-PLAN.md): planned modules and gates; no accepted declarations.
- [Exact-check receipt](verification/exact-check.json), [process receipt](verification/exact-process.json), [build receipt](verification/build.json).
- [Original S279 evidence](evidence/s279/proofs/e004-s279-sea-composite-audit-2026-11-15.md), imported byte-for-byte with [provenance](evidence/provenance.json). Its missing child exit code remains disclosed; the new Python check is separate evidence.

## Reproduce

Python 3.13.7 and Tectonic 0.17.0 were used; rendering uses PyMuPDF 1.28.2. The arithmetic check uses only the Python standard library. From the repository root:

```text
python -B tools/run_exact.py
python -B tools/build.py --tectonic /path/to/tectonic --render
python -B tools/verify_package.py
```

The first command runs a fixed <=4-by-4 rational diagnostic with a 60-second child-process cap. It checks substitutions, four time pairs and two controls; it is not the proof of the analytic statements. Running it again replaces its current receipts, so preserve the frozen commit when reproducing. Tectonic's initial bundle download may require Internet access. Build/render artifacts go under ignored `.build/`; the checked PDF is tracked.

Primary full-source snapshots are not redistributed in this repository. `tools/fetch_sources.py` retrieves the published PDF and arXiv HTML and records each response; a version-notes download returned HTTP 403 although browser inspection succeeded. See [source instructions](sources/README.md) and recorded hashes. `tools/import_evidence.py` is a provenance-import utility requiring the original technical checkout, not a requirement for reproducing the manuscript.

## Custody and next gates

Scientific custody: Quantyra Quantum S279/S289; requested review S290. Manuscript and certification planning: PaperMill P012/S025. This dedicated satellite holds the technical artifacts. Dan confirmed Zenodo enablement and explicitly authorized publication after both papers passed three-lens review. [Release preparation and exact source bindings](verification/release-preparation-v1.0.0.json). Publication does not start a proof job. Existing jobs, ownership, parked research and queue priorities remain intact.

Remaining work: PaperMill C1 dependency/type audit, then full C2-C4 formalization and R1-R4 reconciliation when admitted. Independent source/domain and mathematical review is recommended, not a newly imposed human-approval prerequisite. No claim of a novel first counterexample or globally repaired dynamics is made.

Manuscript and original project documentation: CC BY 4.0. New utility code: MIT. Imported evidence retains its original provenance; primary publications retain their own licenses. See [LICENSE](LICENSE).
