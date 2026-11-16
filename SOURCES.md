# Primary sources, correspondence and novelty audit

Audit date: 2026-11-16. Named questions: (1) Does the currently supplied publisher equation or domain remove the S279 witness? (2) Does the kernel prescription mean a limit from full rank? (3) Is the specific positivity issue already repaired or identified in inspected primary work? This is a bounded targeted audit, not an exhaustive priority search.

## Authoritative equation

Rohit Kishan Ray and Gian Paolo Beretta, [No-Signaling in Steepest Entropy Ascent: A Nonlinear, Non-Local, Non-Equilibrium Quantum Dynamics of Composite Systems Strongly Compatible with the Second Law](https://doi.org/10.3390/e27101018), *Entropy* 27(10), 1018, published 28 September 2025. [arXiv v5](https://arxiv.org/abs/2301.11548v5), 29 September 2025. Use the current publisher PDF for the manuscript claim; the original research record used arXiv v5.

| Source location (printed publisher pages) | Content checked | Manuscript correspondence / result |
|---|---|---|
| p.9, equations (18)-(20) | Spectral Bln, including value zero on the kernel; entropy and centered perceived operators | Section 1 preserves the kernel convention instead of replacing it by a divergent logarithm |
| p.12, equation (39) | Joint dissipator products with complementary marginals | Equation (5) uses GA tensor b + a tensor GB, not embedded local anticommutators with the correlated joint state |
| pp.15-16, equations (59)-(62) and adjacent text | Uniform metric, normalization/mean-energy projection, factor 2, covariance ratio and nonnegativity discussion | Equation (4) matches these local dissipators; the witness has denominators 1 and beta 0 |
| Section 4 p.6 final paragraph; Section 5 p.7 first paragraph; Section 11 p.18 first paragraph | The HG domain includes all density operators, idempotent and not; pure states have Bln=0 | The witness is one mixed homogeneous state. The pure-state special case does not remove rank-three inputs. Pages 7 and 18 additionally visually inspected for S290 |

Publisher PDF: [direct file](https://mdpi-res.com/d_attachment/entropy/entropy-27-01018/article_deploy/entropy-27-01018.pdf), HTTP 200, 7,406,633 bytes, SHA-256 `b120925da27bc6037527576aff66c7809216183fe53823dc9433ba808078c97c`, retrieved 2026-11-16T20:22:29Z. The source PDF has 29 pages. Pages 9, 12, 15 and 16 were visually inspected in addition to text extraction. [Receipt](verification/source-downloads.json); [page extraction/render receipt](verification/source-pages.json).

Original arXiv v5 PDF preserved by S279: SHA-256 `17a84abd01bdeb886c15a6764934cb071a6db8b48758cbce6cbd1c3094382e57`, 29 pages; [source provenance](evidence/provenance.json). The newly downloaded v5 HTML is separately hashed. No claim that the journal and arXiv PDFs are byte-identical is made; their targeted equations agree.

The [publisher version notes](https://www.mdpi.com/1099-4300/27/10/1018/notes) list a version-of-record PDF upload on 28 September 2025 and later **HTML** updates through 1 September 2026. The table does not establish mathematical changes. The current PDF still contains the audited prescription. A raw download of that notes page returned HTTP 403; a separate web-tool inspection succeeded and showed the table. This access failure is retained in the download receipt rather than replaced by a fictitious successful capture.

## Domain and alternative-interpretation tests

- A strictly positive-state restriction removes this particular initial state from the domain; the manuscript explicitly allows that narrower interpretation. It would change the all-density-operator pointwise claim tested here.
- Taking delta down to zero through full-rank states gives the positive divergent derivative in Section 5, not the negative value obtained by the source's pointwise Bln(0)=0 rule. One cannot substitute one interpretation for the other silently.
- Full-rank marginals, a separable state and nonzero covariance denominators exclude three elementary singularity explanations. Global rank deficiency remains the deliberate boundary hypothesis.
- A Hamiltonian bounded below is supplied; shifting its energy origin leaves every centered covariance and commutator unchanged.
- A boundary completion with no right derivative, modified relaxation time or different joint operator product needs its own analysis. No universal positivity or signaling conclusion is inferred.

## Adjacent primary work and priority limits

G. P. Beretta, R. K. Ray and M. R. von Spakovsky, [Evolution of Hypoequilibrium States in Steepest Entropy Ascent Models for Nonequilibrium Quantum Thermodynamics](https://doi.org/10.3390/e28070772), *Entropy* 28(7), 772, 7 July 2026. The inspected Section 4 CSHE1 construction takes noninteracting, uncorrelated product states; Appendix A restates the composite equation. Our correlated rank-three witness does not refute that product-family invariance result. The paper was not found to supply a demonstrated repair of this particular correlated boundary witness. This comparison does not evaluate all its other models or claims.

Targeted primary-source searches for the arXiv identifier with positivity/correction and the exact article title with comment, plus composite SEA boundary/correlation counterexamples, did not establish a matching published correction in the inspected material. **Absence from those results does not establish priority or novelty.** The draft makes no first-discovery claim. A final current-version/correction check belongs to publication readiness; independent domain-expert review is recommended, not imposed as a human-approval prerequisite by this audit. A 2019 SEA paper surfaced during search but was not used as an evidentiary premise for this manuscript.

The tangent test and Hermitian diagonal trace-norm inequality are elementary standard arguments, written out here. Claimed utility is the explicit source-specific failure, its nondegenerate constraint calculation and quantitative repair requirement, not invention of those general tools.
