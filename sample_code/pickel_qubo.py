import sys
sys.path.append("../common")
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import time, pickle
from utility_from_pyqubo import *
from dimod import BinaryQuadraticModel

'''
model = make_qubo(4, flag=False)

with open('qubo.pkl', 'wb') as file:
    pickle.dump(model,file)
'''
with open('qubo.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

Q, offset = loaded_model.to_qubo()
bqm = BinaryQuadraticModel.from_qubo(Q)
print(bqm)
