import sys
sys.path.append("../common")
from utility_from_pyqubo import *
import dimod


Q = make_qubo(100, flag=False)
print("complete!")
input()
solver = dimod.SimulatedAnnealingSampler()
response = solver.sample_qubo(Q, num_reads=10)
print(response.lowest(atol=0.0, rtol=0.0))
print(return_result(response))
make_hist(response)
