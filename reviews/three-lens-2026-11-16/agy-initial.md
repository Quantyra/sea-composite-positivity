### Independent AI Review: Non-Claims and Attribution Lens

- **Source Packet SHA-256:** `5ac0dd44c6dc2031576982eb7be2284214ec5a9bb43279a2a9ea985e1fcdd1fb`
- **Primary Source Evaluated:** R. K. Ray and G. P. Beretta, *Entropy* **27**, 1018 (2025), DOI: [10.3390/e27101018](https://doi.org/10.3390/e27101018) (Publisher PDF SHA-256: `b120925da27bc6037527576aff66c7809216183fe53823dc9433ba808078c97c`).
- **Audit Target:** Manuscript candidate 0.1.0 (`manuscript/main.tex`), `README.md`, `CLAIMS.md`, `SOURCES.md`, `.zenodo.json`, and `CITATION.cff`.
- **Review Lens:** Non-claims / Attribution. Audit abstract, main claims, README, and metadata against the actual proofs and supplied primary excerpts. Verify fairness of equation criticism, boundary/domain qualifications, related literature and novelty limits, unitary correlation evolution, and public draft/review/formal labeling.

---

### 1. Executive Summary & Verdict

**Verdict: GO-WITH-NOTES**

The manuscript and accompanying repository files satisfy the highest standards of scientific fairness, rigorous qualification, and attribution integrity:
1. **Targeted Criticism is Fully Grounded:** The mathematical counterexample directly confronts the exact pointwise composite equation published by Ray and Beretta (*Entropy* 2025, **27**, 1018, Eqs. 39, 59–62) under their explicit spectral kernel convention $\operatorname{Bln}(0) = 0$ (Eqs. 18–20), uniform Fisher–Rao metric ($L_J = I_J$), and standard conservation constraints (normalization and mean energy).
2. **Exemplary Scoping & Non-Claims:** The draft scrupulously avoids overgeneralization. It explicitly disclaims refuting all steepest-entropy-ascent (SEA) models, disclaims establishing superluminal signaling or nonlinear computing power, disclaims global dynamics repairs, and disclaims priority or first-discovery honors.
3. **Domain & Boundary Nuances are Highlighted, Not Obscured:** The manuscript devotes an entire section (Section 5) to proving that the inward full-rank limit yields a positive divergent derivative ($+\infty$), contrasting it directly with the finite negative pointwise value ($-c < 0$) induced by the published $\operatorname{Bln}(0)=0$ convention.
4. **Metadata & Status Labeling are Completely Transparent:** Across `main.tex`, `README.md`, `CLAIMS.md`, `.zenodo.json`, and `CITATION.cff`, the work is consistently designated as an uncertified, unreviewed preparation-stage preprint candidate with clear AI assistance disclosures (OpenAI Codex) and explicit boundaries on arithmetic diagnostics vs. analytic proofs.

The single note recorded below is strictly expository regarding adjacent literature context in the LaTeX bibliography and does not impede public draft archiving or preprint deposition.

---

### 2. Detailed Audit against Primary Source & Proofs

#### A. Fairness and Specificity of Published-Equation Criticism
- **Primary Source Formulation:**
  - On page 9, Eqs. (14)–(16) define local perceptions $(X)^J_\rho$, deviations $\Delta(X)^J_\rho$, and covariances $(X,Y)^J_\rho$.
  - Eqs. (18)–(20) define the entropy operator $S(\rho) = -k_B \operatorname{Bln}(\rho)$ with the pointwise kernel convention $\operatorname{Bln}(x) = \ln x$ for $0 < x \le 1$ and $0$ otherwise.
  - On page 12, Eq. (39) specifies the joint dissipation vector field:
    $$\frac{d\rho}{dt} = -\frac{i}{\hbar}[H,\rho] - \sum_{J=1}^M \{D^J_\rho, \rho_J\} \otimes \rho_{\bar{J}}.$$
  - On pages 15–16, Section 10 specializes this to the uniform metric ($L_J = I_J$) with normalization and energy conservation, yielding Eqs. (59)–(62) where $- \{D^J_\rho, \rho_J\} = G_J$.
  - Critically, on page 16 (lines 665–666), Ray and Beretta explicitly claim that this dynamics is:
    > "...compatible with the conservation of the locally perceived overall composite-system energy and the conditions of unit-trace and non-negativity of the overall density operator, $\rho$."
- **Manuscript Correspondence:**
  - Manuscript Section 1, Eqs. (1)–(5), matches Ray and Beretta's specialized system point-for-point.
  - Theorem 2 demonstrates that for the valid bipartite separable rank-three state $\rho_* = \frac{1}{3}\operatorname{diag}(1,1,1,0)$ with $H = X \otimes I + I \otimes X$, both energy covariance denominators equal $1$, both cross-covariances $\beta_J$ vanish, and the instantaneous population rate along the null eigenvector $|11\rangle$ is strictly negative:
    $$\langle 11 | \mathcal{F}(\rho_*) | 11 \rangle = -\frac{8\ln 3}{81}\left(\frac{1}{\tau_A} + \frac{1}{\tau_B}\right) < 0.$$
  - Lemma 1 establishes that any right-differentiable curve in the positive semidefinite cone starting at $\rho_*$ must have $\langle 11 | \dot{\rho}(0) | 11 \rangle \ge 0$.
  - The criticism directly addresses Ray and Beretta's explicit claim of overall nonnegativity preservation without modifying their equations or inventing unstated assumptions.

#### B. Boundary, Domain, and Continuity Delimitation
- **Full-Rank Limit vs. Pointwise Evaluation:**
  - In Section 5 (Eqs. 21–23 / claim C12), the manuscript investigates the full-rank perturbation $\rho_\delta = \operatorname{diag}(u, u, u, \delta)$ with $u = (1-\delta)/3$.
  - It demonstrates that $\langle 11 | \mathcal{F}(\rho_\delta) | 11 \rangle = 8uv^3(\tau_A^{-1} + \tau_B^{-1})\ln(u/\delta) > 0$, which diverges to $+\infty$ as $\delta \downarrow 0$.
  - The manuscript explicitly cautions (lines 177–178):
    > "This inward full-rank limit does not equal the finite negative pointwise value (8). A restriction to full rank, a non-differentiable boundary trajectory, a different kernel convention, or state-dependent relaxation times vanishing or diverging at the boundary changes a hypothesis and requires its own existence and positivity analysis. The present result does not decide those alternatives."
  - This demonstrates remarkable fairness: it informs the reader that the obstruction arises specifically from the discontinuous pointwise convention $\operatorname{Bln}(0)=0$ combined with the marginal product structure, rather than an inescapable failure across the interior.

#### C. Unitary Connected-Correlation Evolution (Proposition 3)
- Proposition 3 establishes that for $H = H_A \otimes I + I \otimes H_B$ and traceless $G_A, G_B$, the connected correlation $C = \rho - a \otimes b$ satisfies $\dot{C} = -i[H, C]$.
- The dissipative contribution to $\dot{C}$ is identically zero.
- The attribution and analytical framing are exact: the manuscript attributes this identity as a structural consequence of Ray and Beretta's Eq. (39). Because Eq. (39) forms the joint dissipator by taking tensor products with complementary marginals ($G_A \otimes b + a \otimes G_B$), it dissipates only the uncorrelated product part $a \otimes b$, leaving connected correlations to evolve purely unitarily. At the witness $\rho_*$, this causes the marginal drift to push the $(1,1)$ population below zero without any correlation damping to compensate.

#### D. Novelty Limits and Prior Literature
- Neither the manuscript nor the metadata claims a "first discovery," a general no-go theorem, or broad priority.
- `SOURCES.md` explicitly documents an audit of adjacent literature (including Beretta, Ray, and von Spakovsky, *Entropy* 2026, **28**, 772), observing that their Section 4 CSHE1 analysis is restricted to uncorrelated product states and does not repair the correlated composite boundary witness.
- `SOURCES.md` explicitly records: "Absence from those results does not establish priority or novelty. The draft makes no first-discovery claim."
- `README.md` and `CLAIMS.md` explicitly bound the claims to the concrete mathematical statements D1, C1–C13.

#### E. Public Draft, Review, and Formal Certification Labels
- **Labels in `main.tex`:**
  - Date/subtitle: "Manuscript candidate 0.1.0; not formally certified" (line 24).
  - Scope: "A full-manuscript Lean certification plan accompanies the draft; no formal coverage or independent peer review is claimed" (lines 182–183).
  - Disclosure: "OpenAI Codex assisted with derivation, source comparison, drafting and internal verification. This is a preparation-stage candidate" (lines 186–187).
- **Labels in `README.md`:**
  - "**Public manuscript draft; no archival release, DOI, independent human peer review or Lean certification.**" (line 203).
  - Explicitly distinguishes the internal same-agent review from independent provider review.
- **Labels in `.zenodo.json` & `CITATION.cff`:**
  - Type: preprint / publication; message clearly states: "Unpublished manuscript candidate; no DOI has been assigned. Cite only with its preparation-stage status and commit."
  - Description: "Preparation-stage manuscript... No formal certification, general SEA impossibility or physical nonlinear-computing result is claimed."

---

### 3. Severity-Tagged Findings

#### [INFO-01] Exposition / Literature Citation Scope in LaTeX Manuscript
- **Location:** `manuscript/main.tex`, Section 6 & Bibliography (lines 189–196).
- **Finding:** In `SOURCES.md`, the author audits the subsequent paper by G. P. Beretta, R. K. Ray, and M. R. von Spakovsky, *Entropy* **28**, 772 (published 7 July 2026), verifying that its hypoequilibrium product-state construction (CSHE1) does not address or repair the correlated composite boundary failure. However, `main.tex` cites only the foundational 2025 paper (*Entropy* **27**, 1018).
- **Assessment:** Optional exposition. The 2025 paper contains the definitive statement of the composite equation being audited. Mentioning the 2026 follow-up paper in a brief bibliographic remark in `main.tex` (as is already done in `SOURCES.md`) would be informative for readers tracking subsequent developments, but its omission from `main.tex` does not constitute a defect or misattribution.

#### [INFO-02] Verification Diagnostic Scope vs. Analytic Proof
- **Location:** `manuscript/main.tex`, Section 6 (lines 181–183); `README.md` (lines 224–232).
- **Finding:** The repository provides an exact-rational Python script (`tools/run_exact.py`). The manuscript accurately describes this script:
  > "The argument is analytic. A separate exact-rational diagnostic checks the matrix substitutions, constraints, unequal times and repair examples, treating $\ln 3$ as a positive formal factor. It supports arithmetic only."
- **Assessment:** Perfectly qualified. The author avoids attributing the proof to the arithmetic script, correctly maintaining that the proof is analytic while the diagnostic serves purely to catch matrix arithmetic slips.

#### [CONFIRMED-01] Rigorous Boundary and Domain Qualification
- **Location:** `manuscript/main.tex`, Theorem 2, Proposition 4, Section 5, and Section 6.
- **Finding:** The draft repeatedly and explicitly isolates the exact hypotheses under which the obstruction holds: (1) pointwise definition of $\operatorname{Bln}(0) = 0$; (2) uniform metric; (3) normalization and mean-energy constraints; (4) finite positive relaxation times. It expressly denies that the result refutes all SEA models, full-rank dynamics, or alternative boundary completions.
- **Assessment:** Full compliance with non-claims and attribution requirements.

---

### 4. Attempted Falsifiers & Stress Tests

| Falsifier Hypothesis | Stress Test / Analysis | Outcome |
| :--- | :--- | :--- |
| **1. Relaxation times vanish at the boundary** | Could $\tau_J \to \infty$ or $D_J \to 0$ on the boundary to prevent penetration into negative eigenvalues? | **Falsified:** Ray and Beretta assume constant positive relaxation times in Section 10. The manuscript explicitly qualifies Theorem 2 for "every finite positive local relaxation times" and explicitly notes in Section 5 that state-dependent relaxation times would constitute a different hypothesis. |
| **2. Epistemic ensemble interpretation** | Is $\rho_*$ intended to be decomposed into an ensemble of pure states evolved separately? | **Falsified:** Ray and Beretta treat $\rho$ as an intrinsic, homogeneous quantum state, explicitly discuss pure states as special cases, and claim nonnegativity preservation of the overall density operator $\rho$. Section 1 of the manuscript explicitly addresses and delimits this distinction. |
| **3. Off-diagonal Hamiltonian commutator dynamics** | Can off-diagonal elements of $-i[H, \rho_*]$ restore positivity? | **Falsified:** For any positive trajectory $\rho(t)$ with $\rho(0)|11\rangle = 0$, the scalar population $\langle 11|\rho(t)|11\rangle$ must be nonnegative, requiring $\langle 11|\dot{\rho}(0)|11\rangle \ge 0$. The commutator satisfies $\langle 11|[H, \rho_*]|11\rangle = 0$ identically. The negative dissipative rate is uncompensated. |
| **4. Inward boundary limit equivalence** | Can the author be accused of attacking a strawman because the limit from full rank is positive? | **Falsified:** The manuscript itself derives the inward full-rank limit in Section 5, explicitly showing that the limit gives $+\infty$. It accurately attributes $\operatorname{Bln}(0)=0$ to Eq. (19) of Ray and Beretta, demonstrating that the published pointwise vector field is discontinuous at the boundary. |
| **5. Exaggerated metadata or formal proof status** | Do Zenodo or CFF metadata claim peer-reviewed status, accepted Lean proofs, or official DOI? | **Falsified:** All metadata files explicitly classify the artifact as an uncertified, unreviewed preparation-stage manuscript candidate, disclaiming formal proof coverage and archival status. |

---

### 5. Final Disposition

The manuscript candidate is mathematically rigorous, scrupulously attributed, and completely transparent regarding its scope, limitations, and preparation status. 

**Verdict:** **GO-WITH-NOTES** (Proceed with public candidate archiving and three-lens review coordination).
