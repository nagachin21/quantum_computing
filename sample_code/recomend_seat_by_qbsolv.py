import sys
sys.path.append('../annealing_practice')
import numpy as np
import sympy as sp
from pprint import pprint
from utility import *
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
from dwave_qbsolv import QBSolv


b = 0.2 # placeholder (PyQUBO)

J1 = make_J1(12)
J2 = make_J2(12)

H = J1 + b*J2
Q = {}

for i, x in enumerate(H):
    for j, y in enumerate(x):
        if i <= j:
            Q.update( {('q'+str(i), 'q'+str(j)): y} )

print("--- start embedding ---")
# サンプラーの設定
sampler = EmbeddingComposite(DWaveSampler())
print("--- end embedding ---")

print("--- start Dwave solver ---")
# 全結合でキメラグラフに設定（最大64量子ビット）
#response = sampler.sample_qubo(Q, num_reads=1)
response = QBSolv().sample_qubo(Q, solver=sampler)
print("--- end Dwave solver ---")

# dwave sampleの解表示法
#print("samples=" + str(list(response.samples())))
#print("energies=" + str(list(response.data_vectors['energy'])))

#min_sol, min_energy, max_occurence = 0, 0, 0
for sample, energy, num in response.data(['sample', 'energy', 'num_occurrences']):
    #print(sample, "Energy: ", energy, "Occurrences: ", num)
    print("Energy: ", energy, "Occurrences: ", num)
#    if num > max_occurence:
#        min_sol, min_energy, max_occurence = sample, energy, num
#print("minimum result:", min_sol, min_energy, max_occurence)
