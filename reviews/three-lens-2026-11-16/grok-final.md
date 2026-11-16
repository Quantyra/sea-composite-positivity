The supplied manuscript hash is **54818f5de35272b76c84e661a2eba0da0767e36b9162cee6b953fe44188eb91a**. Verdict: **GO-WITH-NOTES**. No essential correction. The pointwise kernel constant, quantifiers, repair bounds, and full-rank divergence all recompute as written. Notes below are optional exposition or extraction uncertainty.

The hash was taken from the review packet. No byte recompute, external lookup, or novelty claim was made. This is not human peer review and not a certification of the publisher article.

## Confirmed ranges

The tested object is only the pointwise field (1)–(5): uniform metric, normalization and mean energy, finite \(\tau_J>0\), and \(\operatorname{Bln}(0)=0\). Theorem 2 is an initial tangent obstruction at one witness. Proposition 4 is an instantaneous trace-norm bound. Section 5 is one full-rank family, not a limit of every approach. The abstract matches those three ranges, uses \(\ln\), and states the noninteracting hypothesis for the correlation identity.

| Quantity | Location | Recomputed value |
|---|---|---|
| Marginals | Theorem 2 | \(a=b=\operatorname{diag}(2/3,1/3)\), full rank |
| Separability / spectrum | Theorem 2 | Mixture of \(\lvert00\rangle,\lvert01\rangle,\lvert10\rangle\); eigenvalues \(1/3,1/3,1/3,0\) |
| \((H,H)^J\), \(\beta_J\) | Theorem 2 proof | Denominators \(1\), both \(\beta_J=0\) |
| Kernel entry | (8) | \(-\dfrac{8\ln 3}{81}(\tau_A^{-1}+\tau_B^{-1})<0\) for every finite \(\tau_J>0\) |
| Equal-time dissipator | (15) | \(\dfrac{\ln 3}{81\tau}\operatorname{diag}(32,-8,-8,-16)\), trace \(0\); \(11\)-entry matches (8) |
| Connected correlation | Proposition 3; §3 | \(C=\operatorname{diag}(-1,1,1,-1)/9\); \(\dot C=-i[H,C]\) |
| Repairs | Proposition 4 | \(R_{11,11}\ge c\); trace-free \(\tfrac12\lVert R\rVert_1\ge c\); both partial traces zero \(\Rightarrow\) \(\tfrac12\lVert R\rVert_1\ge 2c\); \(R_0,R_1\) attain them |
| Full-rank family | (24), \(0<\delta<1/4\) | \(8uv^3(\tau_A^{-1}+\tau_B^{-1})\ln(u/\delta)>0\), prefactor \(\to 8/81\,(\tau_A^{-1}+\tau_B^{-1})\), logarithm \(\to+\infty\) |

\(\hbar=k_B=1\) is explicit. Restoring \(k_B\) cancels between \(S=-k_B\operatorname{Bln}\) and the \(1/k_B\) in the source dissipator, so the kernel factor is not an artifact of that normalization. \(H+2I\) leaves centered covariances and \(-i[H,\rho]\) unchanged. \(H\ge -2I\), with spectrum \(\{-2,0,0,2\}\).

Lemma 1 is the correct necessary condition. Equation (8) violates it, so no right-differentiable PSD curve can start at \(\rho_*\) with derivative \(\mathcal F(\rho_*)\). The commutator does not affect that quadratic form: \(\rho_*\lvert11\rangle=0\).

## Attempted falsifiers

These were checked against the displayed formulas and did not break them.

- Direct partial traces, spectral \(\operatorname{Bln}(1/3)=-\ln 3\), perceived entropy \(\ell\operatorname{diag}(1,2/3)\), mean \(8\ell/9\), and \(\Delta S^J=\ell\operatorname{diag}(1/9,-2/9)\).
- Covariance: \(\Delta H^J=X\), \(\tfrac12\operatorname{Tr}(a\{X,X\})=\operatorname{Tr}(aX^2)=1\), and \(\operatorname{Tr}(a\{\Delta S,X\})=0\).
- Dissipator prefactor \(2\): \(G_J=(8\ell/(27\tau_J))\operatorname{diag}(1,-1)\), then \((G_A\otimes b+a\otimes G_B)_{11}=-(G_{A,11}+G_{B,11})/3\).
- Second route to (8): local \(\lvert1\rangle\) populations fall at \(8\ell/(27\tau_J)\), their product falls at rate \(c\) from \(1/9\), and both the dissipative and unitary contributions to \(\dot C_{11}\) vanish.
- Source family (71) and variance (73): the witness is that ansatz with Bloch data \(a=b=(0,0,1/3)\), \(c=(0,0,-1/3)\) and \(h_A=h_B=e_x\). Source (73) also gives \((H,H)^A=1\) and \((H)^A=H_A\).
- An anticommutator with the joint \(\rho\), rather than with the marginal tensor factors in (5), would give a zero \(\lvert11\rangle\) diagonal. The negative sign is due to the complementary-marginal product. Replacing it is a different equation, as Section 1 says.
- Trace-norm evasion: for Hermitian \(R\), \(\sum_i\lvert R_{ii}\rvert\le\lVert R\rVert_1\). Off-diagonal entries cannot undercut the bounds. Partial-trace zero forces the diagonal pattern \((r,-r,-r,r)\) with \(r\ge c\).
- Full-rank sign: \(S_{11}-S_{00}=v\ln(u/\delta)\) and \(1-v=2u\) give \(\Delta S_{11}=2uv\ln(u/\delta)\). The resulting \(11\)-entry is positive for \(\delta<1/4\) and diverges, so it is not the finite negative value (8). At \(\delta=1/4\) the logarithm is zero; the strict cutoff is correct.
- Sharpness curves: \(\rho_*+t(F_{\mathrm{diss}}+R_i)\) stays diagonal and PSD for short \(t\ge 0\), and conjugation by \(e^{-itH}\) installs \(-i[H,\rho_*]\) without leaving the trace-one PSD set. For \(R_1\), both partial traces and \(\operatorname{Tr}(HR_1)\) vanish. This is tangent sharpness only.

## Findings

**Essential.** None.

**Optional exposition.**

- Proposition 3 assumes traceless \(G_J\). Trace preservation uses that hypothesis; the identity \(\dot C=-i[H,C]\) itself follows from the product structure, \(\operatorname{Tr}a=\operatorname{Tr}b=1\), and \(H=H_A\otimes I+I\otimes H_B\). The extra hypothesis does not affect the witness.
- In Section 5, “their difference is \(v\ln(u/\delta)\), so \(\Delta S^J_{11}=2uv\ln(u/\delta)\)” omits the two centering lines \(1-v=2u\) and \(\Delta S_{11}=2u(S_{11}-S_{00})\). Both are correct.
- The Proposition 4 proof says the short corrected step “is positive.” The curve constructed there remains singular. The proposition statement correctly says positive semidefinite, and Lemma 1 is the PSD tangent condition. The abstract’s “positive-state” is the same PSD reading as Section 1, with strictly positive states excluded as a narrower claim.
- Equation (3) sets \(\operatorname{Bln}(0)=0\) and \(\ln\) on \((0,1]\). Source (19) also sets the value \(0\) outside \((0,1]\). Density-operator spectra never use that extra clause.

**Extraction uncertainty (not a manuscript defect).** The transcription of source (39) shows \(\otimes\rho_J\) without a visible complement mark. Source (41) gives the local term \(-\{D_J,\rho_J\}\), which is what (5) partial-traces to if the tensor factors are the complementary marginals. Source (59)–(62) match (4), including the factor \(2\) and \(\beta_J=(H,S)^J/(H,H)^J\). Pages 6–7 and 18 support the ontic reading of mixed states and \(\operatorname{Bln}(\rho)=0\) on a pure projector. The rank-three witness is outside that pure case, as Section 6 says.

Pointwise versus full-rank, and tangent versus global repair, stay separated in the abstract, the end of Proposition 4, and Sections 5–6. No essential change to those claims is indicated.
