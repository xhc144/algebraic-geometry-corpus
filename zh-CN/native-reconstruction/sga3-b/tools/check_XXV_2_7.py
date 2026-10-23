#!/usr/bin/env python3
"""Exact rank-one check of the printed XXV2.7 construction; not a numerical test."""
from pathlib import Path
import json
import sympy as S

a=S.symbols('a',nonzero=True)
x,y=S.symbols('x y')
L=lambda z:S.Matrix([[1,0],[z,1]])
U=lambda z:S.Matrix([[1,z],[0,1]])
T=lambda z:S.diag(z,1/z)
w=S.Matrix([[0,1],[-1,0]])
actual=S.simplify(w*L(x)*T(a)*U(y)*w.inv())
printed_d=a**2+x*y
corrected_d=a**-2+x*y
candidate=lambda d:S.simplify(L(-y/d)*T(a*d)*U(-x/d))
printed_residual=S.simplify(candidate(printed_d)-actual)
corrected_residual=S.simplify(candidate(corrected_d)-actual)
assert corrected_residual==S.zeros(2)
assert printed_residual!=S.zeros(2)
point={a:S.Integer(2),x:0,y:0}
result={
 'method':'Exact identities in Q(a,x,y), with a and the Gauss denominator inverted; no floating-point approximation.',
 'root_character':'alpha(T(a))=a^2; alpha_star(z)=diag(z,z^-1)',
 'coordinates':'u=L(x_minusalpha) T(a) U(x_alpha), with x=x_minusalpha,y=x_alpha',
 'w':'p_minusalpha(-1)p_alpha(1)p_minusalpha(-1)=[[0,1],[-1,0]]',
 'actual_conjugate':str(actual),
 'printed_d':str(printed_d),'corrected_d':str(corrected_d),
 'printed_formula_is_identity':False,'corrected_formula_is_identity':True,
 'exact_corrected_residual':str(corrected_residual),
 'counterexample_at_a2_x0_y0':{'actual_conjugate':str(actual.subs(point)),'printed_construction':str(candidate(printed_d).subs(point))},
 'source_comparison':'The same English source, XX3.12 lines2556-2571, explicitly uses alpha(t)^(-1)+XY and t alpha_star(d). French XXV printed271-272 repeats the erroneous plus-alpha(t) expression.',
 'limits':'A rank-one counterexample conclusively refutes the printed formula. The corrected expression also follows from the general elementary-system identity XX3.12; this script alone is not a new proof of every existence-theorem step.'
}
p=Path(__file__).resolve().parents[1]/'review/20261022/XXV_2_7_SYMBOLIC_CHECK.json'
p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
