import numpy as np
import sympy as sp
from pprint import pprint
from utility import *
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import wildqat as wq

b = 0.2

J1 = make_J1(4)
J2 = make_J2(4, random_flag=False)

H = J1 + b*J2
'''
wildqatでシミュレート
a=wq.opt()
a.qubo = H
print("シミュレート結果", a.run())
input()
'''
print("H shape", H.shape)
Q = {}

for i, x in enumerate(H):
    for j, y in enumerate(x):
        if i <= j:
            Q.update( {('q'+str(i), 'q'+str(j)): y} )
#Q = dict(Q_list)
#pprint(Q)
#print("Q size", len(Q))

print("Pose, if you want continue to solve, push your enter key")
input()

print("--- start embedding ---")
sampler = EmbeddingComposite(DWaveSampler())
print("--- end embedding ---")

print("--- start Dwave solver ---")
response = sampler.sample_qubo(Q, num_reads=10)
#response = DWaveSampler().sample_qubo(Q, num_reads=1)
print("--- end Dwave solver ---")

min_sol, min_energy, max_occurence = 0, 0, 0
for sample, energy, num in response.data(['sample', 'energy', 'num_occurrences']):
    print(sample, "Energy: ", energy, "Occurrences: ", num)
    if num > max_occurence:
        min_sol, min_energy, max_occurence = sample, energy, num
print("minimum result:", min_sol, min_energy, max_occurence)
print("Lowest", response.lowest())
