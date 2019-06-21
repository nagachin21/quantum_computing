import numpy as np
import sympy as sp
import wildqat as wq
from expand_for12_12 import *

a = wq.opt()

J1 = make_J1()

print(J1)

a.qubo = J1
result = a.sa()
print(result)

for i, qbit in enumerate(result):
    if qbit == 1:
        print(i)
