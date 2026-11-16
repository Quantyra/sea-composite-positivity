# Proof-adversarial review: SEA boundary-positivity manuscript (candidate 0.1.0)

**Source SHA-256 (as supplied, not recomputed):** `5ac0dd44c6dc2031576982eb7be2284214ec5a9bb43279a2a9ea985e1fcdd1fb`

**Basis:** Only the supplied packet was used: LaTeX, README, CLAIMS, SOURCES, .zenodo.json, CITATION.cff and publisher excerpts pp. 9, 12, 15, 16. No commands, files or external requests. I did not run the exact-rational diagnostic or render the PDF. Everything below was recomputed by hand. This is an AI review. It does not assert human review, kernel acceptance or novelty.

**Verdict: GO-WITH-NOTES.** Every load-bearing computation reproduces exactly, and no retained quantified claim was falsified. Two wording-level corrections are essential: E1 and E2 below. The rest is optional.

---

## 1. Recomputations (all reproduce)

Basis 00, 01, 10, 11; ℓ = ln 3; g_J = 8ℓ/(27τ_J).

| Item | Manuscript | Recomputed | Status |
|---|---|---|---|
| Marginals of ρ\* | a = b = diag(2/3, 1/3) | a₀ = ρ₀₀+ρ₀₁, a₁ = ρ₁₀+ρ₁₁; same for b | ✓ |
| S(ρ\*) with Bln(0)=0 | ℓ·diag(1,1,1,0) | −ln(1/3) on support, 0 on \|11⟩ | ✓ |
| S^A = Tr_B[(I⊗b)S] | ℓ·diag(1, 2/3) | S^A₀ = ℓ(b₀+b₁); S^A₁ = ℓ·b₀ | ✓ |
| Tr(aS^A) | 8ℓ/9 | 2ℓ/3 + 2ℓ/9 | ✓ |
| ΔS^J | ℓ·diag(1/9, −2/9) | ✓ | ✓ |
| H^J, (H,H)^J | X, 1 | Tr(bX) = 0 gives H^A = X; Tr(aX²) = 1 | ✓ |
| β_J | 0 | {X, diag(d₁,d₂)} = (d₁+d₂)X has zero trace against diagonal a | ✓ |
| G_J = (2/τ_J){ΔS^J, ρ_J} | (8ℓ/27τ_J)·diag(1,−1) | (4/τ)·ℓ·diag(2/27, −2/27) | ✓ |
| ⟨11\|F\|11⟩ | −(8ℓ/81)(τ_A⁻¹+τ_B⁻¹) | G_A,₁b₁ + a₁G_B,₁ = −g_A/3 − g_B/3 | ✓ |
| Equal-time F_diss | (ℓ/81τ)·diag(32,−8,−8,−16) | g·diag(4/3, −1/3, −1/3, −2/3) | ✓ |
| Commutator on kernel | 0 | ρ\*\|11⟩ = 0 and ⟨11\|ρ\* = 0; [H,ρ\*] is off-diagonal and nonzero | ✓ |
| spec H | bounded below by −2 | {2, 0, 0, −2}; shift cancels in every Δ and commutator | ✓ |
| C at witness | diag(−1,1,1,−1)/9 | ρ\* − diag(4,2,2,1)/9 | ✓ |
| Full-rank ΔS^J₁₁ | 2uv·ln(u/δ) | uses 1 − 2u = v; centering check 2u·ΔS₀₀ + v·ΔS₁₁ = 0 holds | ✓ |
| ⟨11\|F(ρ_δ)\|11⟩ | 8uv³(Σ τ⁻¹)·ln(u/δ) | G_J,₁ = 8uv²·ln(u/δ)/τ_J, times v from each side | ✓ |
| Prefactor as δ↓0 | 8/81 | u, v → 1/3 | ✓ |

**Normalization cross-check.** I tested whether the factor 2 is consistent with the source's entropy-production law (63). Tr(G_A S^A) = 8ℓ²/(81τ_A). (4/τ_A)(S,S)^A = (4/τ_A)·2ℓ²/81, which is the same value. The factor-2 and sign conventions of (59)/(61) are therefore internally consistent with (40) and (63).

**Equivalence of (59) with the centered form.** Solving (60) with C₁ = I (and (I)^J = I) gives ϑ₁ = ⟨S^J⟩ − ϑ₂⟨H^J⟩. Then S^J − ϑ₁ − ϑ₂H^J = ΔS^J − βΔH^J, which matches the manuscript's eq. (4).

---

## 2. Proof checks and attempted falsifiers

- **Lemma 1 (kernel tangent).** f(t)/t ≥ 0, and the limit exists by right-differentiability. Valid. *Falsifier attempted:* a curve with f′(0) < 0 that stays PSD is impossible. None exists.

- **Theorem 2.** Valid for every finite τ_A, τ_B > 0, including state-dependent τ that is finite and positive at ρ\*. *Falsifier attempted:* look for degeneracies the authors may have missed (a zero denominator, a redundant constraint ΔH ∝ I, a rank-deficient marginal, or a commutator contribution on the kernel). None is present. The kernel is exactly span{|11⟩}.

- **Proposition 3.** The partial trace of the commutator on the traced factor vanishes. [H_A⊗I + I⊗H_B, a⊗b] = [H_A,a]⊗b + a⊗[H_B,b]. This gives Ċ = −i[H,C]. *Falsifier attempted:* add an interaction V. The identity then fails because the extra terms −i[V,ρ] + i·Tr_B[V,ρ]⊗b + … appear. The proposition's hypotheses exclude this case, but the abstract does not (see E2). The identity also implicitly needs Tr a = Tr b = 1. That holds for trace-one ρ and is preserved because G_J is traceless.

- **Proposition 4.**
  - R₁₁,₁₁ ≥ c follows from the lemma.
  - The pinching inequality proof is correct for arbitrary Hermitian R, not only diagonal R.
  - With tr R = 0, Σ|r_i| ≥ 2r₁₁, so ½‖R‖₁ ≥ c.
  - Zero partial traces force the diagonal to be (r, −r, −r, r), so ½‖R‖₁ ≥ 2c.
  - Sharpness: I recomputed the unequal-τ dissipative diagonal as (⅔(g_A+g_B), g_A/3 − 2g_B/3, g_B/3 − 2g_A/3, −(g_A+g_B)/3). With R₀ or R₁ added, the 11 entry is 0, the trace is 0, and the other entries are finite against ρ\*-entries of 1/3. So ρ\* + tD is PSD for small t. Conjugating by e^{−itH} supplies −i[H,ρ\*].
  - Tr(HR₁) = 0 because H has zero diagonal in the product basis.
  - *Falsifier attempted:* use off-diagonal freedom to beat the bound. It cannot, because the bound depends only on the diagonal and is attained.

- **Section 5.** δ < 1/4 is equivalent to δ < u, so ln(u/δ) > 0. At δ = 1/4 the state is I/4 and the derivative is 0, as expected for the maximally mixed state. Divergence to +∞ is confirmed. G_J,₀ = −8uv²·ln(u/δ)/τ_J also diverges, to −∞.

---

## 3. Findings

### Essential (wording-level; required before GO)

**E1 — Moderate; source-correspondence uncertainty, not a demonstrated error.**
- **Locations:** §1 ("source's homogeneous-state domain", "treats pure states"), §6 ("The source's treatment of globally pure states"), and the SOURCES.md row "Homogeneous-state discussion and pure-state treatment".
- **Problem:** None of these appears in the supplied excerpts, and the SOURCES row is the only one without a printed page or equation.
- **What is supported:** The in-domain argument holds without them. (19) defines Bln at 0 ("0, otherwise"), and p. 16 refers to "non-negativity of the overall density operator, ρ."
- **Fix:** Give page and equation locations for the homogeneous-state and pure-state statements, or rephrase so they do not attribute content to the source.
- **Remaining uncertainty:** Unsupplied parts of the source could restrict the domain. I cannot exclude that from this packet.

**E2 — Minor; overbroad quantified claim.**
- **Location:** Abstract, "We derive the unitary evolution of the connected-correlation operator."
- **Problem:** As written this reads as general. It is false for interacting H. Proposition 3's hypotheses (local additive H, traceless G_J, trace-one ρ) should be reflected.
- **Fix:** Insert "for noninteracting Hamiltonians".
- **Recommended addition:** Relate Proposition 3 to the p. 12 sentence saying the structure protects against "the build-up of correlations between non-interacting subsystems." The identity formalizes that design property. The obstruction is precisely that frozen C combined with dissipating marginals violates joint positivity. Framed this way, the identity reads as the source's intended feature rather than an independent discovery.

### Optional (exposition and robustness)

**O1 — Minor.** Abstract ("the distinct full-rank boundary limit"), §5 title and §5 text ("inward full-rank limit") describe a divergence, not a limit value. The field is unbounded along ρ_δ, so F admits no continuous extension to ρ\*. Suggest "divergent full-rank approach."

It would also help to state the mechanism. Perception weights the kernel eigenvalue −ln δ of S by the marginal b₁ ≈ 1/3, not by the joint weight δ. So the usual δ·ln δ → 0 suppression is absent.

**O2 — Minor.** In Proposition 4, "If tr R = 0" is automatic when "positive-state curve" means trace-one. Either say it is automatic, or switch to "PSD curve." Without the trace condition, the sharp bound is ‖R‖₁ ≥ c, attained by c|11⟩⟨11|.

**O3 — Nit, source fidelity.** Eq. (3) gives "0, x = 0." Source (19) says "0, otherwise," which also covers x < 0 and x > 1. The two agree on density-operator spectra. The source's field is therefore literally defined beyond the PSD cone, which is relevant to "any differentiable solution" in Proposition 3. Optionally quote "otherwise."

**O4 — Optional, robustness.** Pre-empt a "fine-tuned symmetric witness (β = 0)" objection. On the rank-3 stratum near ρ\*, the support eigenvalues are bounded away from 0 and the spectral gap persists. So Bln(ρ), the marginals, the denominators and the kernel vector vary continuously, and ⟨v_ρ, F(ρ)v_ρ⟩ < 0 should persist on a neighborhood within the stratum, and for nearby H. I believe this follows from continuity, but the manuscript does not prove it and I have not written it out. Add it only with a proof.

**O5 — Optional, scope emphasis.** The full-rank data suggests a likely author response. Heuristically, in the diagonal reduction only (H couples off-diagonals, so this is not exact), δ̇ ≈ K·ln(1/(3δ)) gives δ(t) ~ K·t·ln(1/t). That is an inward, non-right-differentiable entry from the boundary. §5 and the abstract already exclude non-differentiable completions, so this is not an error. A sentence saying the result is specifically about the pointwise Bln(0) = 0 tangent would sharpen the scope.

**O6 — Nit, packet.** CLAIMS.md C3 cites "equations (9)–(15)". By my count of numbered environments, (14) is G_J and (15) is the equal-time formula, which belongs to C5. So C3 should probably read (9)–(14). This is unverified against the rendered PDF.

---

## 4. Source-interpretation checks against the excerpts

- **(14)/(17).** Extraction lost the overbars ("TrJ[(IJ⊗ρJ)X]"). The manuscript's reading F^A = Tr_B[(I⊗b)F] is the unique one satisfying identity (17), Tr(aF^A) = Tr((a⊗b)F). Resolved.
- **(39).** "{D,ρ_J}⊗ρ_J" lost its overbar. The complement-marginal reading is required for (41) to yield −{D,ρ_J}. The manuscript's warning against embedded anticommutators with the joint ρ is correct.
- **(61).** The determinant display is unreadable in extraction. The manuscript's ΔS − βΔH reading is consistent with (62), with the Gram-determinant remark in (63), and with the entropy-production cross-check in §1. Residual uncertainty about the exact display is low, and no alternative reading consistent with (62)/(63) changes the result.
- **p. 16 non-negativity sentence.** "Compatible with … non-negativity of the overall density operator" is ambiguous between a constraint and a theorem. The manuscript's neutral wording ("describes nonnegativity") is appropriate. The γ_J = √ρ_J·U construction on p. 12 preserves only marginal positivity, which is the distinction the manuscript exploits.
- **Equation and page citations.** (18)–(20) on p. 9, (39) on p. 12, and (59)–(62) on pp. 15–16 all match the excerpts.

**Not checked:** novelty and priority, the bibliography title and arXiv date beyond the excerpt header, the exact-rational diagnostic, the Lean plan, and the README process and custody statements.
