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

def make_qubo(idx, flag=True):
    x = Array.create('q', idx**2, 'BINARY')
    const1 = 0.0
    const2 = 0.0
    cost = 0.0
    for i in range(idx):
        const1 += (1 - Sum(0,idx, lambda j:x[idx*i+j]))**2
        const2 += (1 - Sum(0,idx, lambda j:x[i+idx*j]))**2
    if flag:
        J2 = make_J2(idx,random_flag=False)
        cost = Sum(0,idx**2, lambda i: from_J2(i, x, J2))

    H = const1 + const2 + 0.2 * cost

    model = H.compile()
    Q, offset = model.to_qubo()
    return model
