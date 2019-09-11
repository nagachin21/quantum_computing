from pyqubo import Constraint, Sum, Array, Placeholder
from pprint import pprint
import sys, os
sys.path.append('../common')
import dimod
from utility import *
import time, pickle

def from_J2(i, x, idx, J2):
    cost = 0.0
    for j in range(idx**2):
        if i < j:
            cost += J2[i][j] * x[i] * x[j]
            print("J2 QUBO作成中: {}, {}".format(i, j))
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

    J2 = make_J2(idx,random_flag=flag)
    cost = Sum(0,idx**2, lambda i: from_J2(i, x, idx, J2))


    H = const1 + const2 + 0.2 * cost

    model = H.compile()
    #Q, offset = model.to_qubo()
    return model

def make_qubo_to_pkl(num, random_flag=False):
    model = make_qubo(num, random_flag)
    file_name = "qubo_{}.pkl".format(num)
    with open("../common/qubo/{}".format(file_name), 'wb') as file:
        pickle.dump(model,file)

def load_qubo_from_pkl(num):
    file_name = "qubo_{}.pkl".format(num)
    with open("../common/qubo/{}".format(file_name), 'rb') as file:
        loaded_model = pickle.load(file)

    Q, offset = loaded_model.to_qubo()
    return Q, offset
