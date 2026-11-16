The source SHA-256 `8176c99fff1fdb723493452a36eef09f25144987dddebbc1f3b81978572c6ee5` is **GO-WITH-NOTES**. No essential mathematical correction remains in the tested claims. Publisher-PDF equation fidelity below uses only the supplied page extracts (notation there can drop bars and determinant layout).

**Essential corrections:** none.

The pointwise witness, quantifiers, kernel convention, correlation identity, repair bounds, and full-rank divergence all check. Theorem 2 is an initial tangent obstruction for this vector field at \(\rho_*\). It is not a global no-go, and the repair proposition does not build a positive SEA flow.

### What was rechecked

Constants at \(\rho_*=\frac13\mathrm{diag}(1,1,1,0)\), \(H=X\otimes I+I\otimes X\), \(\ell=\ln 3\), \(k_B=\hbar=1\):

- Marginals \(\mathrm{diag}(2/3,1/3)\) are full rank. The state is separable and rank three, and it is not a product state. \(C=\mathrm{diag}(-1,1,1,-1)/9\).
- \(\mathrm{Bln}(0)=0\) gives \(S=\ell\,\mathrm{diag}(1,1,1,0)\), \(S^J=\ell\,\mathrm{diag}(1,2/3)\), \(\operatorname{tr}(aS^A)=8\ell/9\), \(\Delta S^J=\ell\,\mathrm{diag}(1/9,-2/9)\).
- \((H,H)^J=1\) and \((H,S)^J=0\), so \(\beta_J=0\). The anticommutator \(\{\Delta S^J,X\}\) is not the zero operator. Its trace against the diagonal marginal is zero, so the covariance claim is the right one.
- \(G_J=\frac{8\ell}{27\tau_J}\mathrm{diag}(1,-1)\). The joint kernel entry is \(-\frac{8\ln 3}{81}(\tau_A^{-1}+\tau_B^{-1})<0\) for every finite \(\tau_A,\tau_B>0\). The factor \(2\) in \(D_J\) matches source (59) in the extract. \(-i[H,\rho_*]\) does not contribute to that entry.
- Equal times: \(\mathcal F_{\mathrm{diss}}=\frac{\ln 3}{81\tau}\mathrm{diag}(32,-8,-8,-16)\), trace zero. \(H\ge -2I\). Adding \(2I\) does not change centered covariances or the field.
- Noninteracting \(H\), trace-one \(\rho\), and traceless \(G_J\) give \(\dot C=-i[H,C]\). Trace one is necessary: without \(\operatorname{tr} b=1\), \(\operatorname{tr}_B(G_A\otimes b)\) is not \(G_A\). At \(\rho_*\), \(\dot{(a_{11}b_{11})}\) equals the kernel entry.
- Repairs: \(R_{11,11}\ge c\). Trace zero forces \(\frac12\|R\|_1\ge c\). Both partial traces zero force the diagonal pattern \((r,-r,-r,r)\) and \(\frac12\|R\|_1\ge 2c\). \(R_0\) and \(R_1\) meet those bounds. The unitary conjugate of a short diagonal step starts at \(\rho_*\), stays trace-one and positive semidefinite, and has the corrected right derivative at \(0\). That is tangent sharpness only.
- Full rank: \(\langle 11|\mathcal F(\rho_\delta)|11\rangle=8uv^3(\tau_A^{-1}+\tau_B^{-1})\ln(u/\delta)>0\) for \(0<\delta<1/4\). The prefactor tends to \(8/81\,(\tau_A^{-1}+\tau_B^{-1})\) and the logarithm goes to \(+\infty\), which is not the finite negative pointwise value.

Abstract and claim ranges match that split: pointwise right-differentiable failure, unitary correlation law under the proposition’s hypotheses, instantaneous trace-norm bounds, and a divergent full-rank limit. Natural \(\ln\) is used. Pure states (\(\mathrm{Bln}=0\)) and full-rank or other boundary laws stay outside Theorem 2. The last paragraph does not classify all repairs.

### Attempted falsifiers that did not hit

Flipping the kernel sign. Treating a nonzero \(\{\Delta S,X\}\) as a nonzero covariance. Dropping trace-one in the correlation cancellation. Using \(\delta\ge 1/4\) inside the strict full-rank formula. Replacing the \(8/81\) prefactor limit by \(-\frac{8\ln 3}{81}\). Lowering \(\frac12\|R\|_1\) below \(c\) or \(2c\) inside the stated constraint sets. Letting the Hamiltonian commutator supply the negative kernel derivative. Reading \(R_0\)/\(R_1\) as a global positive SEA integration.

### Optional exposition (not required)

- **NOTE.** `CLAIMS.md` C3 cites equations (9)–(14). In the TeX numbering, (14) is the equal-time diagonal after the proof, which is C5. C3’s evaluated generator stops at \(G_J\).
- **NOTE.** The abstract names noninteracting Hamiltonians for the correlation law. Trace-one and traceless \(G_J\) are stated on the proposition, not in that sentence.
- **NOTE.** Manuscript \(\mathrm{Bln}\) is defined on \(\{0\}\cup(0,1]\). The extract’s source clause sets every other input to \(0\). On density-operator spectra the two agree.

No formal peer review, kernel acceptance, or exhaustive novelty is claimed or implied.
