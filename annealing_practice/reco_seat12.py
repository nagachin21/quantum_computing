import numpy as np
import sympy as sp
import wildqat as wq
from expand_for12_12 import *
from util_for_annealing import *

a = wq.opt()
b = - 0.2

J1 = make_J1()
J2 = make_J2()

print(J1)
print(J2)

a.qubo = J1 + b*J2
result = a.sa()
print(result)

for i, qbit in enumerate(result):
    if qbit == 1:
        print(i)
