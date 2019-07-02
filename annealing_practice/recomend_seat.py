import numpy as np
import sympy as sp
from pprint import pprint
from utility import *
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import wildqat as wq

b = 0.2

J1 = make_J1(8)
J2 = make_J2(8)

H = J1 + b*J2
'''
wildqatでシミュレート
'''
a=wq.opt()
a.qubo = H
print("シミュレート結果", a.run())
input()
print("H shape", H.shape)
Q_list = {}

for i, x in enumerate(H):
    for j, y in enumerate(x):
        if i <= j:
            Q_list.update( {('q'+str(i), 'q'+str(j)): y} )
Q = dict(Q_list)
pprint(Q)
print("Q size", len(Q))

print("Pose, if you want continue to solve, push your enter key")
input()

print("--- start embedding ---")
emb = EmbeddingComposite(DWaveSampler())
print("--- end embedding ---")

print("--- start Dwave solver ---")
response = emb.sample_qubo(Q, num_reads=5)
#response = DWaveSampler().sample_qubo(Q, num_reads=1)
print("--- end Dwave solver ---")

for sample, energy, num in response.data(['sample', 'energy', 'num_occurrences']):
    print(sample, "Energy: ", energy, "Occurrences: ", num)
