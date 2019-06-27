import numpy as np
import sympy as sp
import wildqat as wq
from expand_for12_12 import *
from util_for_annealing import *

a = wq.opt()
a.dwavetoken = "DEV-1bc37e85b416b94b19afdd046f774059d756299c"
b = 0.2

J1 = make_J1()
J2 = make_J2()

#print(J1)
#print(J2)
#print(J2.shape)
#print(J1 + b*J2)
#print(J1 - b*J2)

a.qubo = J1 + b*J2
answer = []

for i in range(1):
    result = a.sa()
    #result = a.dw()
    print(result)

    tmp = []
    for i, qbit in enumerate(result):
        if qbit == 1:
            #print(i)
            tmp.append(i)
            #print(tmp)
    answer.append(tmp)

for i in range(len(answer)):
    print(answer[i])
