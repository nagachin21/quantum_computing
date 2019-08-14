from pyqubo import Constraint, Sum, Array, Placeholder
from pprint import pprint
import sys, os
sys.path.append('../common')
import dimod
from utility import *
import time

def from_J2(i, x, J2):
    cost = 0.0
    for j in range(16):
        if i < j:
            cost += J2[i][j] * x[i] * x[j]
    #pprint(cost)
    return cost


x = Array.create('q', 16, 'BINARY')
const1 = 0.0
const2 = 0.0
for i in range(4):
    const1 += (1 - Sum(0,4, lambda j:x[4*i+j]))**2
    const2 += (1 - Sum(0,4, lambda j:x[i+4*j]))**2
J2 = make_J2(4,random_flag=False)
print(J2)
cost = Sum(0,16, lambda i: from_J2(i, x, J2))

#pprint(cost.compile().to_qubo())
#pprint(const2.compile().to_qubo())

#B = Placeholder('B')
H = const1 + const2 + 0.2 * cost

model = H.compile()
Q, offset = model.to_qubo()
#pprint(Q)

#start_time = time.time()
solver = dimod.ExactSolver()
response = solver.sample_qubo(Q)
#end_time = time.time()

print(response.lowest(atol=0.0, rtol=0.0))
#print("elapsed time:{0}".format(end_time - start_time) + "[sec]")
return_result(response.lowest(atol=0.0, rtol=0.0))
