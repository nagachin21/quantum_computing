import sys, os
sys.path.append('../annealing_practice')
from utility import *
import neal

# 問題を設定（着席推奨4席）
b = 0.2
J1 = make_J1(4)
J2 = make_J2(4)
H = J1 + b*J2
linear = {}
quadratic = {}

for i, x in enumerate(H):
    for j, y in enumerate(x):
        if i < j:
            quadratic.update( {('q'+str(i), 'q'+str(j)): y} )
        elif i == j:
            linear.update( {'q'+str(i): y} )
solver = neal.SimulatedAnnealingSampler()
response = solver.sample_ising(linear, quadratic, num_reads=5)

for datum in response.data(['sample', 'energy']):
    print(datum.sample, datum.energy)
