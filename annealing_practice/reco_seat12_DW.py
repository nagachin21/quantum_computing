import numpy as np
import sympy as sp
#import wildqat as wq
from expand_for12_12 import *
from util_for_annealing import *
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

#a = wq.opt()
#a.dwavetoken = "DEV-1bc37e85b416b94b19afdd046f774059d756299c"
b = 0.2

J1 = make_J1()
J2 = make_J2()

H = J1 + b*J2
Q_list = {}

for i, x in enumerate(H):
    for j, y in enumerate(x):
        #print("(q{}, q{}: {})".format(i,j,y))
        if i <= j:
            Q_list.update( {('q'+str(i), 'q'+str(j)): y} )
Q = dict(Q_list)
print("Q size", len(Q))
'''
print("--- start embedding ---")
emb = EmbeddingComposite(DWaveSampler())
print("--- end embedding ---")
'''
print("--- start Dwave solver ---")
#response = emb.sample_qubo(Q, num_reads=1)
response = DWaveSampler().sample_qubo(Q, num_reads=1)
print("--- end Dwave solver ---")

for sample, energy, num in response.data(['sample', 'energy', 'num_occurrences']):
    print(sample, "Energy: ", energy, "Occurrences: ", num)
