# Final proof-adversarial recheck: boundary positivity obstruction for composite SEA

**Source SHA-256 (as supplied):** `54818f5de35272b76c84e661a2eba0da0767e36b9162cee6b953fe44188eb91a`. I did not recompute this hash because the brief prohibits commands. It identifies the inline packet I reviewed. Primary-source checks rely only on the supplied extracted text of Ray–Beretta pp. 6, 7, 9, 12, 15, 16 and 18. I did not open the publisher PDF (`b120925d…`).

**Verdict: GO-WITH-NOTES.** Every critical formula reproduces exactly. E1 and E2 are resolved, and I found no new theorem-level overclaim. One minor hypothesis omission (F1) should be fixed. Everything else is optional.

---

## 1. Recomputation of the critical formulas

Basis order is 00, 01, 10, 11, with ℓ = ln 3 and k_J = 8ℓ/(27τ_J).

| Item | Location | Result |
|---|---|---|
| Marginals a = b = diag(2/3, 1/3) | eq. (9) | ✔ |
| S(ρ\*) = ℓ·diag(1,1,1,0), using Bln(0)=0 | eq. (10) | ✔ |
| S^A₀₀ = b₀ℓ + b₁ℓ = ℓ; S^A₁₁ = b₀ℓ + b₁·0 = 2ℓ/3; B is symmetric | eq. (11) | ✔ |
| tr(aS^A) = 2ℓ/3 + 2ℓ/9 = 8ℓ/9 | eq. (12) | ✔ |
| ΔS^J = ℓ·diag(1/9, −2/9) | eq. (13) | ✔ |
| H^A = X + I·tr(bX) = X, because b is diagonal. (H,H)^J = tr(aX²) = 1. (H,S)^J = 0, because {X, diagonal} is off-diagonal | Thm 2 proof | ✔ |
| G_J = (4/τ_J)·ΔS^J·a = k_J·diag(1, −1) | eq. (14) | ✔ |
| ⟨11\|F\|11⟩ = −k_A/3 − k_B/3 = −(8ℓ/81)(τ_A⁻¹ + τ_B⁻¹) | eq. (8) | ✔ |
| ⟨11\|[H,ρ\*]\|11⟩ = 0, since ρ\*\|11⟩ = 0 | Thm 2 proof | ✔ |
| Equal-τ dissipative part: diag(4k/3, −k/3, −k/3, −2k/3) = (ℓ/81τ)·diag(32, −8, −8, −16) | eq. (15) | ✔ (trace 0) |
| Spectrum of H is {−2, 0, 0, 2}; a shift by 2I leaves Δ terms and the commutator unchanged | §2 | ✔ |
| tr(G_A H^A) = k·tr(diag(1,−1)X) = 0 | §2 | ✔ |
| C = ρ\* − a⊗b = diag(3,3,3,0)/9 − diag(4,2,2,1)/9 = diag(−1,1,1,−1)/9 | §3 | ✔ |
| Prop. 3: tr_B gives ȧ = −i[H_A,a] + G_A. The cross terms in d(a⊗b) match −i[H, a⊗b], so Ċ = −i[H,C] | eq. (16) | ✔ |
| Pinching: \|r_i\| ≤ Σ_j \|λ_j\|·\|⟨i\|u_j⟩\|², and summing over i gives ‖R‖₁ | eq. (20) | ✔ |
| Zero partial traces force diag(R) = (r, −r, −r, r) | Prop. 4 | ✔ |
| ½‖R₀‖₁ = c and ½‖R₁‖₁ = 2c. R₁ has both partial traces zero, and tr(HR₁) = 0 | eq. (21) | ✔ |
| Sharpness: σ(t) = ρ\* + t(F_diss + R) is diagonal, has a zero kernel entry and is positive for small t. Conjugating by e^{−itH} supplies the commutator term | Prop. 4 proof | ✔ |
| Full-rank family: a = diag(2u, v), with 2u + v = 1 | §5 | ✔ |
| S^J₁₁ − S^J₀₀ = vL_δ − (1−2u)L_u = v·ln(u/δ). ΔS^J₁₁ = 2u(S₁₁ − S₀₀) = 2uv·ln(u/δ) | eq. (23) | ✔ |
| (G_J)₁₁ = (4/τ_J)·2uv²·ln(u/δ). The joint 11 entry is 8uv³(Σ τ⁻¹)·ln(u/δ) | eq. (24) | ✔ |
| δ < u ⇔ δ < 1/4. Prefactor → 8/81 and the log term → +∞ | §5 | ✔ |

**Independent consistency check (not in the manuscript).** I compared the source's entropy-production formula, eq. (63), with the trace computed directly from the vector field.

- (S,S)^J = ℓ²(2/3·1/81 + 1/3·4/81) = 2ℓ²/81, so Σ_J (4/τ)(S,S)^J = 16ℓ²/(81τ).
- Directly, tr(F_diss·S) = (ℓ²/81τ)(32 − 8 − 8) = 16ℓ²/(81τ).

The two agree. This supports the claim that the specialization matches source eqs. (59)–(63), including the factor 2.

---

## 2. Status of earlier findings

**E1 (domain citations): resolved.**
- §1 now cites p. 7, which says P_HG is "all possible density operators ρ, idempotent and not". That matches the supplied text.
- It cites p. 6 (final paragraph of §4) for the ontic status of mixed states. This also matches.
- Section 11, p. 18, is cited for the treatment of pure states (Bln(ρ) = 0). This matches.
- The source's statement on nonnegativity after eq. (62), p. 16, is cited correctly.
- One small uncertainty: the "4." heading does not appear in the supplied extract. I infer the §4 attribution from the §5 heading that follows. This is low risk.

**E2 (abstract scope): resolved.** The abstract now says "For noninteracting Hamiltonians we derive the unitary evolution of the connected-correlation operator." That matches the hypothesis of Prop. 3.

---

## 3. Findings

**F1 — Minor (recommended correction). Prop. 4 statement, before eq. (18).** The statement reads "the resulting vector is the initial derivative of a positive semidefinite curve." It does not say the curve starts at ρ\*. Without that hypothesis, R₁₁,₁₁ ≥ c does not follow, because Lemma 1 needs ρ(0) = ρ\* and |11⟩ in its kernel. The fix is one phrase: "…of a positive semidefinite curve ρ(t) with ρ(0) = ρ\*, right differentiable at 0." The proof is otherwise correct.

**F2 — Optional. Prop. 3 hypotheses, eq. (16).** The proof uses tr b = tr a = 1 along the solution. This is automatic when the initial state has trace one, because traceless G_J preserve the trace. CLAIMS.md C6 lists "trace-one marginals", but the manuscript statement does not. Suggested wording: "along any differentiable trace-one solution."

**F3 — Optional (scope wording). §6, final sentence.** "A correction must change the boundary or domain interpretation, or address the incompatibility…" is broader than the paper shows. Other untested routes also escape the theorem's hypotheses: a non-uniform metric L_J ≠ I (source p. 15), additional conserved charges C_k, or the state-dependent τ already named in §5. The final disjunct is broad enough that the sentence is not false, but "must" reads as a classification result. Consider "Any correction must alter at least one hypothesis of Theorem 2 (e.g., …)".

**F4 — Optional (exposition). Abstract.** "Nonzero energy covariance denominators" and the "sharp … bounds on repairs" depend on the specific H = X⊗I + I⊗X and hold only at this witness. Adding "for a noninteracting Hamiltonian" to the witness sentence and "at the witness" to the repair sentence would make the abstract self-contained. The body already scopes both correctly, so this is not an overclaim.

**F5 — Optional (strengthens the domain argument). §1 or §2.** The witness belongs to the source's own Section 11 example class, eq. (71). It corresponds to a = b = (0, 0, 1/3), c = (0, 0, −1/3), with h_A = h_B = x̂ and ω_J = 1 in eq. (73). Check: 1 − a_z − b_z + c_z = 0, and the other three diagonal entries equal 4/3.

Eq. (73) then gives (H,H)^J = 1 − (h·a)² = 1 directly. Stating this would show that the witness lies inside a family the source itself evolves numerically. That is stronger than an appeal to the domain definition alone.

**F6 — Optional. eq. (3).** The manuscript defines Bln only on [0,1], while the source's eq. (19) sets Bln = 0 "otherwise". The two agree on density-operator spectra. A footnote "restricted to spec ρ ⊂ [0,1]" would remove any appearance of divergence from the source.

**F7 — Optional (exposition). After eq. (16) or in §6.** The p. 16 sentence the manuscript cites says the SEA direction is "compatible with … non-negativity of the overall density operator". Theorem 2 contradicts this pointwise at ρ\*. A plausible mechanism is the γ_J parametrization in the source's eq. (42), which enforces only local positivity of ρ_J, and the witness marginals are full rank so that constraint is inactive. The manuscript's §3 makes this point implicitly. Stating it explicitly, and attributing the mechanism cautiously, would sharpen the contribution without widening the claim.

**No new overclaim found.** I checked the abstract, Theorem 2, the scope of Props. 3 and 4, §5, §6, the disclosure, README.md, CLAIMS.md, SOURCES.md, .zenodo.json and CITATION.cff. None asserts human peer review, Lean acceptance, novelty or priority, a global no-go, or signaling. The attribution "formalizes the source's stated aim" (p. 12) matches the source text, which mentions protection against "build-up of correlations between non-interacting subsystems". The CLAIMS.md equation ranges (D1: 1–5, C3: 9–14, C8: 20) match my count of the numbered equations.

---

## 4. Attempted falsifiers

1. **Text extraction dropped the overbars in source eqs. (14) and (39).** I read the source as (X)^J = Tr_J̄[(I_J ⊗ ρ_J̄)X] and {D_J, ρ_J} ⊗ ρ_J̄. That is the only reading consistent in dimension with "operators on H_J", with eq. (17), and with eq. (73), where (H)^A = H_A + I·ω_B h_B·b. **Survives**, with extraction uncertainty that the stated visual inspection should cover.

2. **The embedded-anticommutator reading {D_A ⊗ I, ρ}.** Under this reading the kernel entry is 2(D_A)₁₁·ρ₁₁,₁₁ = 0, so **the theorem would not hold**. Both readings reproduce source eq. (41) after the partial trace, so eq. (41) cannot tell them apart. The obstruction therefore depends on the eq. (39) form. The manuscript states this explicitly (§1, "would define a different equation"). This is the main source-interpretation dependency, and it is correctly disclosed.

3. **Taking a limit instead of using the kernel convention.** Eq. (24) gives +∞, not a negative value. The manuscript correctly separates the two (§5). **Survives as scoped.**

4. **Degenerate denominator or β.** (H,H)^J = 1 and β = 0, both verified. **Survives.**

5. **Violated constraints.** Trace, local perceived energy, and global energy (via the eq. (17)-type identity tr[(G_A⊗b)H] = tr(G_A H^A)) are all preserved. **Survives.**

6. **Unequal τ.** The kernel entry is linear in τ_J⁻¹ with both coefficients negative. **Survives.**

7. **The pure-state exception.** Rank 3 means Bln(ρ\*) ≠ 0. **Survives.**

8. **Sharpness curve.** It has trace one, is PSD for small t, and with conjugation its derivative is the full corrected vector. **Survives.**

---

## 5. Essential versus optional

- **Essential before release:** F1, a one-phrase hypothesis fix.
- **Optional:** F2–F7.

This is an AI review of the supplied material only. It is not human peer review, not formal or kernel certification, and not a novelty assessment.
