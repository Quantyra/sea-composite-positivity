# Separate three-lens review and disposition

2026-11-16. COMPLETE for the corrected scientific source bound by [REVIEW-SUMMARY.json](../REVIEW-SUMMARY.json). The selected final reports are [Claude](claude-closeout.md), [Grok](grok-closeout.md) and [AGY](agy-compact.md), all GO-WITH-NOTES with no essential finding left open. Each report names the same exact source hash. These are separate provider-native AI reviews, not independent human peer review, formal certification or exhaustive novelty clearance.

Claude used the configured `opus` alias and returned `claude-opus-5-5`. Grok used `grok-4.7`. AGY used installed `gemini-3.8-flash-high`; its returned JSON does not independently attest a serving model. The available informal AGY review is not represented as a different Gemini model or as satisfying a later formal-provider acceptance gate. Exact packets, binary/input/report hashes, effort, elapsed time and terminal exits are retained. Invocations had 1200-second caps. Initial proof/quantitative reviews used high effort, subsequent rechecks medium or low as recorded; AGY was high.

## Applied corrections

- Claude initial E1: supplied and cited the source's homogeneous all-density-operator domain (printed pp6-7) and pure-state treatment (p18); no unsupported source-domain attribution remains. Original PDF/formula inspection and source interpretation remain external evidence, not a Lean theorem.
- Claude initial E2 and overlapping Grok note: restricted the abstract's connected-correlation claim to noninteracting Hamiltonians. The abstract now states failure from the specific witness, avoiding a possible universal-negation reading.
- Clarified the divergent full-rank approach, positive-semidefinite tangent-curve terminology, natural-log notation and the claim-map equation range. Attributed correlation cancellation to the source's stated design aim.
- Claude recheck F1-F3: the repair curve explicitly starts at rho_star and is right differentiable at zero; the correlation proposition states trace-one; the conclusion does not classify all possible repairs. All three selected closeout reports accept this corrected source.

## Notes adjudicated without expanding the claim

Optional rank-stratum robustness and nondifferentiable-boundary constructions were not added without proofs. The Bln definitions agree on density spectra; the manuscript does not claim equality outside that domain. The correlation identity is conditional along solutions, and its witness-time cancellation is the same algebraic product-rule calculation; it does not assert a positive solution exists from the witness. Instantaneous sharp repairs remain distinct from a globally positive repaired flow.

Grok's closeout equation-number note is incorrect: the rendered PDF has G_J at (14) and the equal-time diagonal at (15); C3's (9)-(14) range is retained. AGY initial references to a Fisher--Rao metric and stronger priority/readiness conclusions were not adopted: the claim uses the stipulated uniform metric and retains priority uncertainty. No provider recommendation creates publication authority or a requirement for a formal journal submission before a separately authorized preprint release.

## Delivery failures and source limits

Two AGY rechecks returned empty responses after attempting commands outside their read-only prompt scope. A subsequent stdin attempt returned an explicit missing-packet response because that CLI invocation did not attach stdin to the prompt. None counts as completed review; terminal exit0 alone was insufficient. A bounded direct-argument retry supplied the entire manuscript and public claims without expanding tool permissions and returned the accepted review. It used a clearly labelled author-supplied source-correspondence paraphrase; it did not independently inspect the publisher PDF. Earlier complete reports and all attempt receipts remain preserved.

The 122-assertion diagnostic was not rerun for these wording/citation changes. The final PDF was rebuilt and its five pages/layout checked; the source/PDF/package hashes are separate operational evidence. Zenodo enablement was confirmed by Dan after the public visibility change. No release, DOI, external contact or proof job was performed.

Remaining to-do list: queued PaperMill full certification and a separate publication decision; independent specialist feedback remains useful but is not a newly imposed human approval gate.
