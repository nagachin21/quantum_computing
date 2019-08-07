import sys
sys.path.append('../common')
import numpy as np
import sympy as sp
from pprint import pprint
from utility import *
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
from dimod import BinaryQuadraticModel
#from dimod import dimod
import hybrid
import time


b = 0.2 # placeholder (PyQUBO)

J1 = make_J1(100)
J2 = make_J2(100, random_flag=False)

H = J1 + b*J2
Q = {}

for i, x in enumerate(H):
    for j, y in enumerate(x):
        if i <= j:
            Q.update( {('q'+str(i), 'q'+str(j)): y} )

# construct BQM
bqm = BinaryQuadraticModel.from_qubo(Q, 200)

# Define the workflow
iteration = hybrid.RacingBranches(
    hybrid.Identity(),
    hybrid.InterruptableTabuSampler(),
    hybrid.EnergyImpactDecomposer(size=2)
    | hybrid.QPUSubproblemAutoEmbeddingSampler()
    | hybrid.SplatComposer()
) | hybrid.ArgMin()
workflow = hybrid.LoopUntilNoImprovement(iteration, convergence=3)
#workflow = hybrid.LoopUntilNoImprovement(iteration)

# Solve the problem
start_time = time.time()
init_state = hybrid.State.from_problem(bqm)
final_state = workflow.run(init_state).result()
end_time = time.time()

# Print results
print("Solution: sample={.samples.first}".format(final_state))
#print(final_state.timing)

print("elapsed time:{0}".format(end_time - start_time) + "[sec]")
'''
return_result(response.lowest(atol=0.0, rtol=0.0))
make_hist(response)
'''
