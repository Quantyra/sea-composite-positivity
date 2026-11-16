"""Fixed rational diagnostic, <=4x4 matrices; ln(3) is a formal positive factor.
This checks substitutions, not the analytic tangent/norm/limit theorems.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib,json,time
ROOT=Path(__file__).resolve().parents[1]; start=time.perf_counter(); checks=0
def eq(a,b,label):
 global checks
 checks+=1
 if a!=b: raise AssertionError(f'{label}: {a} != {b}')
def mat(n,f): return [[Q(f(i,j)) for j in range(n)] for i in range(n)]
def diag(v): return mat(len(v),lambda i,j:v[i] if i==j else 0)
def add(a,b): return mat(len(a),lambda i,j:a[i][j]+b[i][j])
def scale(a,c): return mat(len(a),lambda i,j:a[i][j]*c)
def sub(a,b): return add(a,scale(b,-1))
def mul(a,b): return mat(len(a),lambda i,j:sum(a[i][k]*b[k][j] for k in range(len(a))))
def tr(a): return sum(a[i][i] for i in range(len(a)))
def anti(a,b): return add(mul(a,b),mul(b,a))
def kron(a,b):
 n=len(b);return mat(len(a)*n,lambda i,j:a[i//n][j//n]*b[i%n][j%n])
def partial(r,side):
 return mat(2,lambda i,j:sum(r[2*i+k][2*j+k] if side=='A' else r[2*k+i][2*k+j] for k in range(2)))
I=diag([1,1]);X=[[Q(0),Q(1)],[Q(1),Q(0)]]
H=add(kron(X,I),kron(I,X));rho=diag([Q(1,3)]*3+[0]);S=diag([1,1,1,0])
def center(f,r): return sub(f,scale(I,tr(mul(r,f))))
def cov(f,g,r): return tr(mul(r,anti(center(f,r),center(g,r))))/2
def term(r,s,side,tau):
 own=partial(r,side);bar=partial(r,'B' if side=='A' else 'A')
 embedding=kron(I,bar) if side=='A' else kron(bar,I)
 sj=partial(mul(embedding,s),side);hj=partial(mul(embedding,H),side)
 denominator=cov(hj,hj,own);eq(denominator,1,'energy variance')
 numerator=cov(hj,sj,own);eq(numerator,0,'energy entropy covariance')
 g=scale(anti(center(sj,own),own),Q(2)/tau)
 eq(tr(g),0,'local trace');eq(tr(mul(g,hj)),0,'local energy')
 return g,kron(g,bar) if side=='A' else kron(bar,g)
eq(partial(rho,'A'),diag([Q(2,3),Q(1,3)]),'marginal A')
eq(partial(rho,'B'),partial(rho,'A'),'marginal B');eq(tr(rho),1,'trace')
comm=sub(mul(H,rho),mul(rho,H))
eq([comm[i][i] for i in range(4)],[Q(0)]*4,'Hamiltonian diagonal')
rows=[]
for ta,tb in [(1,1),(1,2),(2,1),(2,3)]:
 ga,fa=term(rho,S,'A',Q(ta));gb,fb=term(rho,S,'B',Q(tb));f=add(fa,fb)
 c=Q(8,81)*(Q(1,ta)+Q(1,tb))
 eq(f[3][3],-c,'negative kernel coefficient');eq(tr(f),0,'joint trace')
 eq(tr(mul(H,f)),0,'joint energy');eq(partial(f,'A'),ga,'marginal derivative A');eq(partial(f,'B'),gb,'marginal derivative B')
 for preserve,r in [(False,diag([-c,0,0,c])),(True,diag([c,-c,-c,c]))]:
  eq(add(f,r)[3][3],0,'repaired kernel');eq(tr(r),0,'repair trace')
  eq(sum(abs(r[i][i]) for i in range(4))/2,(2 if preserve else 1)*c,'sharp repair norm')
  eq(tr(mul(H,r)),0,'repair energy')
  if preserve:
   eq(partial(r,'A'),diag([0,0]),'repair A');eq(partial(r,'B'),diag([0,0]),'repair B')
  # Exhibit a positive trace-one linear tangent path for the dissipative part,
  # in units with the formal positive ln(3) factor normalized to one.
  d=add(f,r);t=Q(1,1+6*sum(abs(d[i][i]) for i in range(4)))
  eq(all(rho[i][i]+t*d[i][i]>=0 for i in range(4)),True,'positive tangent example')
 rows.append({'tau_A':ta,'tau_B':tb,'minus_kernel_over_ln3':str(c)})
# Controls: a uniform product state is stationary under the dissipator;
# a pure projector has zero Bln by the prescribed spectral convention.
for r,s,label in [(diag([Q(1,4)]*4),diag([1]*4),'uniform product'),(diag([1,0,0,0]),diag([0]*4),'pure')]:
 ga,fa=term(r,s,'A',Q(1));gb,fb=term(r,s,'B',Q(1))
 eq(add(fa,fb),diag([0]*4),label)
receipt={'status':'pass','scope':'exact finite rational substitutions, not asymptotic proof or formal certification','assertions':checks,'maximum_matrix_dimension':4,'time_pairs':rows,'logarithm':'formal positive factor ln(3); sign and limits proved in manuscript','elapsed_seconds':time.perf_counter()-start,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'verification/exact-check.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt))
