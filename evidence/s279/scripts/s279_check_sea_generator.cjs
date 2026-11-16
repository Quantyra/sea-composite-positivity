'use strict';
// Fixed preregistered exact arithmetic audit. No trajectories or floating logs.
const fs = require('node:fs');
const started = process.hrtime.bigint();
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b];}return a;}
class Q {
  constructor(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error('zero denominator');if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}
  add(b){b=q(b);return new Q(this.n*b.d+b.n*this.d,this.d*b.d);}
  neg(){return new Q(-this.n,this.d);}
  sub(b){return this.add(q(b).neg());}
  mul(b){b=q(b);return new Q(this.n*b.n,this.d*b.d);}
  div(b){b=q(b);return new Q(this.n*b.d,this.d*b.n);}
  eq(b){b=q(b);return this.n===b.n&&this.d===b.d;}
  toString(){return this.d===1n?`${this.n}`:`${this.n}/${this.d}`;}
}
const q=x=>x instanceof Q?x:new Q(x);
const z=()=>q(0);
const matrix=(n,m,f)=>Array.from({length:n},(_,i)=>Array.from({length:m},(_,j)=>q(f(i,j))));
const diag=v=>matrix(v.length,v.length,(i,j)=>i===j?v[i]:0);
const I=diag([1,1]), X=[[q(0),q(1)],[q(1),q(0)]];
const add=(A,B)=>matrix(A.length,A[0].length,(i,j)=>A[i][j].add(B[i][j]));
const scale=(A,s)=>matrix(A.length,A[0].length,(i,j)=>A[i][j].mul(s));
const sub=(A,B)=>add(A,scale(B,-1));
const mul=(A,B)=>matrix(A.length,B[0].length,(i,j)=>A[i].reduce((a,x,k)=>a.add(x.mul(B[k][j])),z()));
const tr=A=>A.reduce((a,row,i)=>a.add(row[i]),z());
const anti=(A,B)=>add(mul(A,B),mul(B,A));
const kron=(A,B)=>matrix(A.length*B.length,A[0].length*B[0].length,(i,j)=>A[Math.floor(i/B.length)][Math.floor(j/B[0].length)].mul(B[i%B.length][j%B[0].length]));
function partial(R,side){return matrix(2,2,(i,j)=>[0,1].reduce((s,k)=>s.add(side==='A'?R[2*i+k][2*j+k]:R[2*k+i][2*k+j]),z()));}
const lpo=(F,bar,side)=>partial(mul(side==='A'?kron(I,bar):kron(bar,I),F),side);
const center=(F,r)=>sub(F,scale(I,tr(mul(r,F))));
const cov=(A,B,r)=>tr(mul(r,anti(center(A,r),center(B,r)))).div(2);
let assertions=0;
function eq(a,b,label){assertions++;if(!q(a).eq(b))throw Error(`${label}: ${a} != ${b}`);}
function meq(A,B,label){A.forEach((row,i)=>row.forEach((a,j)=>eq(a,B[i][j],`${label}[${i},${j}]`)));}
function zero(A,label){meq(A,matrix(A.length,A[0].length,()=>0),label);}
const R=diag([new Q(1,3),new Q(1,3),new Q(1,3),0]);
const H=add(kron(X,I),kron(I,X));
// Entropy divided by ln(3), k_B=1; Bln(0)=0 from source eq.19.
const S=diag([1,1,1,0]);
const A=partial(R,'A'),B=partial(R,'B');
meq(A,diag([new Q(2,3),new Q(1,3)]),'marginal A');
meq(B,A,'marginal B');eq(tr(R),1,'trace');eq(R[3][3],0,'kernel');
function term(R,S,H,side,tau){
  const own=partial(R,side),bar=partial(R,side==='A'?'B':'A');
  const SJ=lpo(S,bar,side),HJ=lpo(H,bar,side);
  const denominator=cov(HJ,HJ,own),numerator=cov(HJ,SJ,own);
  eq(denominator,1,`${side} nonzero energy denominator`);
  eq(numerator,0,`${side} energy-entropy covariance`);
  const beta=numerator.div(denominator);
  const M=center(sub(SJ,scale(HJ,beta)),own);
  const D=scale(M,new Q(-2).div(tau));
  const G=scale(anti(D,own),-1);
  eq(tr(G),0,`${side} trace constraint`);
  eq(tr(mul(G,HJ)),0,`${side} energy constraint`);
  return {SJ,HJ,D,G,full:side==='A'?kron(G,bar):kron(bar,G)};
}
const receipts=[];
for(const [ta,tb] of [[1,1],[1,2],[2,1],[2,3]]){
  const a=term(R,S,H,'A',ta),b=term(R,S,H,'B',tb),F=add(a.full,b.full);
  meq(a.SJ,diag([1,new Q(2,3)]),'perceived entropy');meq(a.HJ,X,'perceived H');
  meq(a.G,diag([new Q(8,27*ta),new Q(-8,27*ta)]),'local dissipator');
  meq(partial(F,'A'),a.G,'partial global derivative A');
  meq(partial(F,'B'),b.G,'partial global derivative B');
  eq(F[3][3],new Q(-8,81).mul(new Q(1,ta).add(new Q(1,tb))),'negative kernel derivative');
  eq(tr(F),0,'global trace');eq(tr(mul(H,F)),0,'global energy');
  const C=sub(mul(H,R),mul(R,H));eq(C[3][3],0,'Hamiltonian kernel derivative');eq(tr(mul(H,C)),0,'Hamiltonian energy derivative');
  assertions++;if(F[3][3].n>=0n)throw Error('kernel derivative not negative');
  if(ta===1&&tb===1)meq(F,diag([new Q(32,81),new Q(-8,81),new Q(-8,81),new Q(-16,81)]),'complete diagonal');
  receipts.push({tauA:ta,tauB:tb,kernelCoefficientOfLog3:F[3][3].toString()});
}
// Product control with same marginals. Entropy = log(3)*S3 + log(2)*S2.
const P=kron(A,B),S3=scale(diag([1,1,1,1]),2),S2=diag([-2,-1,-1,0]);
const c3a=term(P,S3,H,'A',1),c3b=term(P,S3,H,'B',1);
zero(c3a.G,'product log3 cancels A');zero(c3b.G,'product log3 cancels B');
const c2a=term(P,S2,H,'A',1),c2b=term(P,S2,H,'B',1);
const localG=diag([new Q(-8,9),new Q(8,9)]);
meq(c2a.G,localG,'single-system product gradient A');meq(c2b.G,localG,'single-system product gradient B');
meq(add(c2a.full,c2b.full),add(kron(localG,B),kron(A,localG)),'product rule');
eq(tr(P),1,'product trace');assertions++;if(P.some((row,i)=>row[i].n<=0n))throw Error('control not full rank');
// Pure global state: its entropy operator is identically zero, including null space.
const pure=matrix(4,4,(i,j)=>(i===0||i===3)&&(j===0||j===3)?new Q(1,2):0);
meq(mul(pure,pure),pure,'pure projector');
const pureEntropy=diag([0,0,0,0]);
zero(term(pure,pureEntropy,H,'A',1).G,'pure global dissipation A');
zero(term(pure,pureEntropy,H,'B',1).G,'pure global dissipation B');
const elapsedSeconds=Number(process.hrtime.bigint()-started)/1e9;
const receipt={status:'PASS',assertions,elapsedSeconds,scope:'Exact finite arithmetic only; not external or formal review, physical realization, or trajectory integration',source:'arXiv:2301.11548v5 equations 14-20,39,59-62',fixtures:receipts,productControl:'PASS',pureStateControl:'PASS'};
fs.writeFileSync('artifacts/s279-exact-check.json',JSON.stringify(receipt,null,2)+'\n');
process.stdout.write(JSON.stringify(receipt)+'\n');
