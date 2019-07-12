# this make a comparison between exact sampler, simulated annealing and quantum annealing sampler
import numpy as np
import sympy as sp
from pprint import pprint
from utility import *
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import dimod
import neal

# 問題を設定（着席推奨4席）
b = 0.2
J1 = make_J1(4)
J2 = make_J2(4)
H = J1 + b*J2
Q_list = {}

for i, x in enumerate(H):
    for j, y in enumerate(x):
        if i <= j:
            Q_list.update( {('q'+str(i), 'q'+str(j)): y} )
Q = dict(Q_list)

# exact solver
solver_ex = dimod.ExactSolver()
response = solver_ex.sample_ising(Q)
for datum in response.data(['sample', 'energy']):
    print(datum.sample, datum.energy)

# simulated annealing
solver_nl = neal.SimulatedAnnealingSampler()
response = solver_nl.sample_ising(Q, num_reads=10)
# quantum annealing sampler
print("--- start embedding ---")
sampler = EmbeddingComposite(DWaveSampler())
print("--- end embedding ---")

print("--- start Dwave solver ---")
response = sampler.sample_qubo(Q, num_reads=10)
for datum in response.data(['sampler', 'energy']):
    print(datum.sampler, datum.energy)

#response = DWaveSampler().sample_qubo(Q, num_reads=1)
print("--- end Dwave solver ---")

min_sol, min_energy, max_occurence = 0, 0, 0
for sample, energy, num in response.data(['sample', 'energy', 'num_occurrences']):
    #print(sample, "Energy: ", energy, "Occurrences: ", num)
    if num > max_occurence:
        min_sol, min_energy, max_occurence = sample, energy, num
print("minimum result:", min_sol, min_energy, max_occurence)
