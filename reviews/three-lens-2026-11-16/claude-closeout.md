**Source SHA-256 (as supplied, not recomputed):** `8176c99fff1fdb723493452a36eef09f25144987dddebbc1f3b81978572c6ee5`

**Lens:** Proof-adversarial final recheck. I read only the supplied packet and ran no tools. This is an AI review, not human peer review, formal or kernel certification, or a novelty search.

## Recomputed critical formulas (all confirmed)

| Item | Recomputation | Result |
|---|---|---|
| Marginals, Thm 2 eq (9) | a₀ = ρ₀₀+ρ₀₁ = 2/3, a₁ = 1/3; b by symmetry | ✓ |
| S^J, eqs (10)–(13) | S^A₀₀ = (2/3+1/3)ℓ = ℓ; S^A₁₁ = (2/3)ℓ + (1/3)·0; mean = 8ℓ/9; ΔS = ℓ·diag(1/9, −2/9) | ✓ |
| H^J, (H,H)^J, β_J | Tr(bX) = 0 so H^A = X; ½Tr(a{X,X}) = Tr a = 1; {X, diagonal} is off-diagonal, so covariance 0 and β = 0 | ✓ |
| G_J, eq (14) | G = (2/τ){ΔS, a} = (4ℓ/τ)·diag(2/27, −2/27) = (8ℓ/27τ)·diag(1, −1) | ✓ |
| Kernel entry, eq (8) | G_A,₁₁·b₁ + a₁·G_B,₁₁ = −(8ℓ/81)(τ_A⁻¹ + τ_B⁻¹) | ✓ |
| Equal-τ diagonal, eq (15) | entries 00: 32, 01: 8(1−2) = −8, 10: −8, 11: −16 (units ℓ/81τ) | ✓ |
| Commutator, kernel entry | ρ\*\|11⟩ = 0, so the 11 diagonal entry vanishes | ✓ |
| Prop 3, eq (16) | Tr_B(a⊗G_B) = a·Tr G_B = 0; the remainder is −i[H, ρ − a⊗b] for additive H | ✓ |
| C at witness | diag(3,3,3,0)/9 − diag(4,2,2,1)/9 = diag(−1,1,1,−1)/9 | ✓ |
| Prop 4 partial traces | r₀₀ = −r₀₁ = −r₁₀ = r₁₁, giving Σ\|r\| = 4r | ✓ |
| Sharpness | F_diss + R_{0,1} is diagonal, traceless, and 0 on the kernel. A linear step conjugated by e^{−itH} has the correct derivative. Tr(HR₁) = 0 since H is off-diagonal. | ✓ |
| Full-rank family, eq (21) | S₁₁ − S₀₀ = vL_δ − (1−2u)L_u = v·ln(u/δ), using 1−2u = v. ΔS₁₁ = 2uv·ln(u/δ). Joint 11 entry = 8uv³(Στ⁻¹)·ln(u/δ). δ < 1/4 ⇔ u > δ. Prefactor → 8/81. | ✓ |
| CLAIMS equation ranges | D1 (1)–(5), C3 (9)–(14), C8 (20) match the LaTeX numbering | ✓ |

## Prior-item resolution

- **E1 (domain citations): Resolved.** The cited pages contain what the manuscript attributes to them:
  - p.6: pure and mixed density operators both have ontic status.
  - p.7: P_HG is all density operators, idempotent and not.
  - p.18: pure states give Bln = 0 and form unitary limit cycles.
  - p.16 (after eq 62): "unit-trace and non-negativity of the overall density operator."
- **E2 (abstract scope): Resolved.** The correlation claim is now restricted to noninteracting Hamiltonians. The negation is limited to this witness.
- **Final F1–F3: Resolved.**
  - The repair curve starts at ρ\* with a right derivative at 0.
  - Prop 3 states the trace-one requirement.
  - The conclusion explicitly declines to classify all repairs.

## Attempted falsifiers (none succeeded)

1. **Mismatch with source eqs (59)–(62).** Checked the sign of β, the factor 2, and the centered Δ. Source eq (61) gives −{D,ρ_J} = (2/τ){Δ(M), ρ_J} with M = S − ϑ₂H, which matches eq (4). Source eq (63)'s 4/τ factor is consistent.
2. **Singular denominators or degenerate marginals.** Excluded: both denominators are 1 and both marginals are full rank.
3. **Hamiltonian term rescuing the kernel entry.** Excluded: the commutator's diagonal is zero on ker ρ\*.
4. **Bln domain.** Source eq (19) sets the value to 0 "otherwise," including x > 1. This is irrelevant here because all eigenvalues are ≤ 1.
5. **Sharpness relying on a non-PSD curve.** Excluded: the positive entries dominate for small t, and unitary conjugation preserves PSD.

## Findings

**Essential corrections: none.**

**Minor (optional exposition):**

- **[MINOR] §3, paragraph after Prop 3.** Prop 3 is stated "along any differentiable trace-one solution," but Theorem 2 shows no such solution exists from ρ\*. The witness-time use is valid because the cancellation is an algebraic identity of the vector field itself. A half-sentence saying so would close a pedantic gap.
- **[MINOR] Abstract, "unitary evolution of the connected-correlation operator."** This is accurate as Ċ = −i[H, C] along solutions. "Purely Hamiltonian" or "dissipation-free" would avoid implying a solution exists from the witness.
- **[NOTE] eq (3).** The manuscript defines Bln only at x = 0, while the source uses "otherwise." These are equivalent on density operators, so no change is needed.

**New overclaims:** None found. The abstract, the §6 scope paragraph, README, CLAIMS, SOURCES, .zenodo.json and CITATION.cff all disclaim:
- a general SEA no-go,
- signaling,
- a global repair,
- certification,
- novelty or priority.

**Extraction uncertainty:** The supplied source text loses some notation, such as the J/J̄ (complement) distinction in eqs (14) and (65). My correspondence check assumes the standard reading, where ρ_J̄ is the complementary marginal. That reading is consistent with eq (17).

## Verdict: **GO-WITH-NOTES**

The two notes are optional wording changes. No essential correction remains.
