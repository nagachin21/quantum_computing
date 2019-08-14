import sys, os
sys.path.append('../common')
import dimod
from utility import *
import time

# 問題を設定（着席推奨4席）
b = 0.2
J1 = make_J1(4)
J2 = make_J2(4, random_flag=False)
#H = J1 + b*J2
H = J1
Q = {}

for i, x in enumerate(H):
    for j, y in enumerate(x):
        if i <= j:
            Q.update( {('q'+str(i), 'q'+str(j)): y} )

start_time = time.time()
solver = dimod.ExactSolver()
response = solver.sample_qubo(Q)
end_time = time.time()

#for datum in response.data(['sample', 'energy']):
    #print(datum.sample, datum.energy)

#print(response)
print(response.lowest(atol=0.0, rtol=0.0))
print("elapsed time:{0}".format(end_time - start_time) + "[sec]")
return_result(response.lowest(atol=0.0, rtol=0.0))


'''
for sample, energy, num in response.data(fields=['sample', 'energy', 'num_occurrences']):
    print(sample, energy, num)
'''
