import sympy

q0, q1, q2, q3, q4, q5, q6, q7, q8, q9 = sympy.symbols('q0, q1, q2, q3, q4, q5, q6, q7, q8, q9')
q10, q11, q12, q13, q14, q15, q16 = sympy.symbols('q10, q11, q12, q13, q14, q15, q16')

func = (1 - q0 - q1 - q2 - q3)**2 + (1 - q4 - q5 - q6 - q7)**2 + (1 - q8 - q9 - q10 - q11)**2 + (1 - q12 - q13 - q14 - q15)**2\
      + (1 - q0 - q4 - q8 - q12)**2 + (1 - q1 - q5 - q9 - q13)**2 + (1 - q2 - q6 - q10 - q14)**2 + (1 - q3 - q7 - q11 - q15)**2

print(sympy.expand(func))
