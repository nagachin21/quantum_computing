import os.path,sys
sys.path.append('../common')
import numpy as np
import sympy as sp
from pprint import pprint
from utility import *
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
from dimod import BinaryQuadraticModel
from utility_from_pyqubo import *
#from dimod import dimod
import hybrid
import time

if not os.path.exists("../common/qubo/qubo_100.pkl"):
    make_qubo_to_pkl(100, random_flag=False)
    print("pklファイルが存在しないため、作成しました")

Q, offset = load_qubo_from_pkl(100)
print("pklファイルからQUBOをロードしました")

# construct BQM
bqm = BinaryQuadraticModel.from_qubo(Q, offset)

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

input()

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
