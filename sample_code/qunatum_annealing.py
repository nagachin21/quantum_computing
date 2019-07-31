import sys,os
sys.path.append('../annealing_practice')
from utility import *
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import time

b = 0.2
J1 = make_J1(4)
J2 = make_J2(4, random_flag=False)
H = J1 + b*J2
Q = {}

for i, x in enumerate(H):
    for j, y in enumerate(x):
        if i <= j:
            Q.update( {('q'+str(i), 'q'+str(j)): y} )

start_time = time.time()
solver = EmbeddingComposite(DWaveSampler())
response = solver.sample_qubo(Q, num_reads=10000)
end_time = time.time()

print(response.lowest())
print("elapsed time:{0}".format(end_time - start_time) + "[sec]")
make_hist(response.data(fields=['energy']))
