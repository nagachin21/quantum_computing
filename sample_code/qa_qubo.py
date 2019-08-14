import sys
sys.path.append("../common")
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import time
from utility_from_pyqubo import *
import hybrid
from dimod import BinaryQuadraticModel

time1 = time.time()
#Q, offset = make_qubo(100, flag=False)
Q, offset = make_qubo(4,flag=False)
time2 = time.time()
print("completed making qubo", time2-time1)

bqm = BinaryQuadraticModel.from_qubo(Q, offset)

iteration = hybrid.RacingBranches(
                hybrid.Identity(),
                hybrid.InterruptableTabuSampler(),
                hybrid.EnergyImpactDecomposer(size=2)
                | hybrid.QPUSubproblemAutoEmbeddingSampler()
                | hybrid.SplatComposer()
) | hybrid.ArgMin()

workflow = hybrid.LoopUntilNoImprovement(iteration, convergence=3)

time3 = time.time()
init_state  = hybrid.State.from_problem(bqm)
final_state = workflow.run(init_state).result()
time4 = time.time()
print("finish", time4-time3)
print(final_state)
