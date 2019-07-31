import sys, os
sys.path.append('../annealing_practice')
import datetime as dt
from utility import *
import dimod
import time

# 問題を設定（着席推奨4席）
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
solver = dimod.SimulatedAnnealingSampler()
response = solver.sample_qubo(Q)
end_time = time.time()

'''
for datum in response.data(['sample', 'energy']):
    print(datum.sample, datum.energy)
'''
print(response.lowest())
print("elapsed_time:{0}".format(end_time - start_time) + "[sec]")

make_hist(response.data(fields=['energy']))


#service time
#time_format = "%Y-%m-%d %H:%M:%S.%f"
