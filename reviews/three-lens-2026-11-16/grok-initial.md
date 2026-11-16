The audited identities match an independent recomputation. The classification is **GO-WITH-NOTES**. No essential correction to the constants, quantifiers that carry a theorem, or the pointwise-versus-full-rank separation.

**Source SHA-256:** `5ac0dd44c6dc2031576982eb7be2284214ec5a9bb43279a2a9ea985e1fcdd1fb`  
Supplied packet hash. This review did not recompute the digest: the instruction forbade commands.

**Lens.** Complexity and quantitative scope only. No human review, kernel-convention endorsement, or novelty search is asserted. The publisher PDF was not reopened. Extracted source equation (39) has a lost complement mark, and (61) is typographically degraded. Readable anchors are source (18)–(20), (41), (59), and (62).

## Recomputed core

Witness \(\rho_*=\frac13\mathrm{diag}(1,1,1,0)\), \(H=X\otimes I+I\otimes X\), basis \(00,01,10,11\).

- Marginals \(a=b=\mathrm{diag}(2/3,1/3)\), both full rank. \(C=\rho_*-a\otimes b=\mathrm{diag}(-1,1,1,-1)/9\).
- With \(\ell=\ln 3\) and \(\mathrm{Bln}(0)=0\): \(S(\rho_*)=\ell\,\mathrm{diag}(1,1,1,0)\), \(S^A=S^B=\ell\,\mathrm{diag}(1,2/3)\), \(\mathrm{tr}(aS^A)=8\ell/9\), \(\Delta S^J=\ell\,\mathrm{diag}(1/9,-2/9)\).
- \(H^A=H^B=X\), \((H,H)^J=1\), \((H,S)^J=0\), so \(\beta_J=0\). Denominators are exactly 1.
- \(G_J=\dfrac{8\ell}{27\tau_J}\mathrm{diag}(1,-1)\).
- Kernel entry, every finite \(\tau_A,\tau_B>0\):
  \[
  \langle 11|\mathcal F(\rho_*)|11\rangle
  =-\frac{8\ln 3}{81}\Big(\frac1{\tau_A}+\frac1{\tau_B}\Big)<0.
  \]
  The two summands are separately negative. No positive ratio cancels them. \(\langle 11|[H,\rho_*]|11\rangle=0\).
- Equal times: dissipative diagonal \(\dfrac{\ln 3}{81\tau}\mathrm{diag}(32,-8,-8,-16)\), trace 0.
- \(H\) eigenvalues \(\{2,0,0,-2\}\). The shift \(H\mapsto H+2I\) leaves centered covariances, commutators, and \(\mathcal F\) unchanged.
- Trace and locally perceived mean energy of each \(G_J\) are zero.
- Proposition 3: for additive \(H\) and traceless \(G_J\), the dissipative part of \(\dot C\) cancels and \(\dot C=-i[H,C]\). At \(\rho_*\), the product rule on \(a_{11}b_{11}=1/9\) reproduces the same \(-c\).
- Repair constant \(c=\dfrac{8\ln 3}{81}(\tau_A^{-1}+\tau_B^{-1})\). Pinching \(\sum_i|R_{ii}|\le\|R\|_1\) is correct. Trace-free implies \(\tfrac12\|R\|_1\ge c\). Both partial traces zero force the diagonal \((r,-r,-r,r)\) and \(\tfrac12\|R\|_1\ge 2c\). \(R_0=c\,\mathrm{diag}(-1,0,0,1)\) and \(R_1=c\,\mathrm{diag}(1,-1,-1,1)\) meet these with equality. For each finite positive time pair, a short linear step stays positive semidefinite, and conjugation by \(e^{-itH}\) matches \(-\!i[H,\rho_*]+ \mathcal F_{\mathrm{diss}}+R\) at \(t=0\).
- Full-rank family: \(\Delta S^J_{11}=2uv\ln(u/\delta)\) and
  \[
  \langle 11|\mathcal F(\rho_\delta)|11\rangle
  =8uv^3\Big(\frac1{\tau_A}+\frac1{\tau_B}\Big)\ln\frac{u}{\delta}.
  \]
  For \(0<\delta<1/4\) this is positive. As \(\delta\downarrow 0\) the prefactor tends to \(\frac8{81}(\tau_A^{-1}+\tau_B^{-1})\) and the logarithm tends to \(+\infty\). That limit is distinct from the finite negative pointwise value.

Lemma 1 is the standard one-sided tangent test. Theorem 2 is the correct negation: one kernel quadratic form strictly below zero rules out a right-differentiable positive-semidefinite curve with that initial derivative. No existence theorem is required. Shared counters make the displays Lemma 1, Theorem 2, Proposition 3, Proposition 4. The claims table’s pinching location, equation (20), agrees with the LaTeX equation counter.

## Findings

**Essential.** None. The sign, the factor \(8/81\), the equal-time diagonal, both repair constants, and the full-rank prefactor survived direct recalculation.

**[OPTIONAL] Abstract quantifier.** The abstract’s “cannot generate a right-differentiable positive-state trajectory from every density operator” is readable as “not from all,” which matches Theorem 2, and also as a universal no-go. Theorem 2, equation (negative), is the precise statement: failure at this \(\rho_*\), for every finite \(\tau_A,\tau_B>0\).

**[OPTIONAL] Abstract correlation clause.** “Unitary evolution of the connected-correlation operator” is Proposition 3 under an additive Hamiltonian and traceless \(G_J\). The witness Hamiltonian is additive. The abstract sentence does not repeat that hypothesis.

**[OPTIONAL] Sharpness wording in Proposition 4.** The attaining curves stay positive semidefinite with a zero eigenvalue. The short step is positive semidefinite. Lemma 1 already uses that cone. The bounds are instantaneous tangent bounds. The same proof says they are not a globally positive SEA flow, and that the comparison curve need not preserve the marginal dynamics past \(t=0\).

**[OPTIONAL] Section 5 compression.** The displayed identities \(S^J_{00}=L_u\), \(S^J_{11}=2uL_u+vL_\delta\), \(\Delta S^J_{11}=2uv\ln(u/\delta)\), and equation (fullrank) are correct. The sentence “their difference is \(v\ln(u/\delta)\), so \(\Delta S^J_{11}=\ldots\)” skips \(1-2u=v\) and \(\Delta S_{11}=2u(S_{11}-S_{00})\).

**[OPTIONAL] Log notation outside the theorem.** The manuscript uses \(\ln 3\). CLAIMS C3 says natural log. README and CLAIMS C4 write \(\log 3\). The rational coefficient is the same only if that log is natural.

**[OPTIONAL] CLAIMS C3 range.** Equations (9)–(14) are the witness substitutions through \(G_J\). Equation (15), the equal-time diagonal, stands after the proof. C5 already covers it.

**[LIMIT] Source typography.** Correspondence checked from the readable excerpts: kernel value \(\mathrm{Bln}(0)=0\); \(D_J=-2/(k_B\tau_J)[(S)^J-\sum\vartheta_k(C_k)^J]\) with \(\vartheta_2=(H,S)^J/(H,H)^J\); marginal equation (41). With \(k_B=1\), centering puts the trace part into the normalization multiplier and reproduces the manuscript’s \(D_J\) and \(G_J\). The \(k_B\) in \(S\) and the \(k_B\) in the prefactor of (59) cancel, so the state derivative does not retain a hidden \(k_B\). The kernel entry is also independent of the positive factor in front of \(-i[H,\rho]/\hbar\).

**[LIMIT] Diagnostic.** Section 6 limits the exact-rational check to arithmetic, with \(\ln 3\) a positive formal factor, including substitutions, constraints, unequal times, and the repair examples. It does not prove the trace-norm argument, the conjugation derivative, or the full-rank logarithm. This review did not execute that check.

**[LIMIT] Custody and priority.** Repository, receipt, and Lean-plan sentences were not re-checked. SOURCES.md already withholds a first-discovery claim. This review did not search the literature.

## Attempted falsifiers

All of the following were tried against the stated formulas. Each failed to break the scoped claim.

- Unequal times, including \(\tau_A/\tau_B\to\infty\) with both times finite and positive: the kernel entry stays strictly negative.
- Energy-origin shift \(H\mapsto H+2I\): centered field unchanged; lower bound \(-2\) is exact.
- Commutator contribution on \(|11\rangle\): both terms vanish because \(\rho_*|11\rangle=0\).
- Covariance \((H,S)^J\): explicit anticommutator \(\{X,\Delta S\}\) is off-diagonal and has trace zero against a diagonal marginal. \((H,H)^J=1\) exactly, so the example is not a zero-denominator degeneracy. \(\beta=0\) is a computed covariance, and the energy constraint remains in the formula.
- Coherent repair with \(\tfrac12\|R\|_1<c\) at trace zero, or \(<2c\) with both partial traces zero: the diagonal pinching inequality forbids both.
- Replacing the pointwise kernel value by the full-rank approach \(\delta\downarrow 0\): the 11-entry tends to \(+\infty\), which is a different prescription from equation (negative).
- Extending equation (fullrank) past the stated range: at \(\delta=1/4\), \(u=\delta\) and the entry is 0; for \(\delta>1/4\) the algebraic sign flips while the state is still full rank. That does not touch Lemma 1, whose kernel test is vacuous at full rank. The hypothesis \(0<\delta<1/4\) is required for the strict inward sign and is present.
- Product-state reading of “separable”: \(\rho_*\) is a classical mixture of product projectors and \(C\neq 0\). The obstruction uses that correlation. Proposition 3 does not claim the same cancellation for an interacting Hamiltonian.

## Scope that the manuscript keeps in bounds

Theorem 2 is one witness in the displayed pointwise field: uniform metric, normalization and mean energy, finite positive times, \(\mathrm{Bln}(0)=0\). Section 5 treats a full-rank restriction, a non-differentiable boundary completion, another kernel rule, and state-dependent times as different hypotheses. Proposition 4 is an instantaneous trace-norm obligation at \(\rho_*\); \(2c\) is sharp for that tangent problem and is not a global repaired flow.

Section 6, the abstract, CLAIMS.md, README, and the Zenodo description exclude a no-go for every SEA model, a signaling theorem, a physical nonlinear gate, and any complexity-class or simulation result. No such claim appears in the formulas. The pure-projector remark is only that \(\mathrm{Bln}\) vanishes on \(\{0,1\}\), so a rank-one projector is a different boundary point from this rank-three witness.

The theorem statements can stand as written. The optional items are exposition and inventory hygiene before any archival posting.
