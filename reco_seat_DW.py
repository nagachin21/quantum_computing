import numpy as np
from pprint import pprint
#import pprint
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

# wildqat QUBO
J1 = np.array([
[-2,2,2,2,2,0,0,0,2,0,0,0,2,0,0,0],
[0,-2,2,2,0,2,0,0,0,2,0,0,0,2,0,0],
[0,0,-2,2,0,0,2,0,0,0,2,0,0,0,2,0],
[0,0,0,-2,0,0,0,2,0,0,0,2,0,0,0,2],
[0,0,0,0,-2,2,2,2,2,0,0,0,2,0,0,0],
[0,0,0,0,0,-2,2,2,0,2,0,0,0,2,0,0],
[0,0,0,0,0,0,-2,2,0,0,2,0,0,0,2,0],
[0,0,0,0,0,0,0,-2,0,0,0,2,0,0,0,2],
[0,0,0,0,0,0,0,0,-2,2,2,2,2,0,0,0],
[0,0,0,0,0,0,0,0,0,-2,2,2,0,2,0,0],
[0,0,0,0,0,0,0,0,0,0,-2,2,0,0,2,0],
[0,0,0,0,0,0,0,0,0,0,0,-2,0,0,0,2],
[0,0,0,0,0,0,0,0,0,0,0,0,-2,2,2,2],
[0,0,0,0,0,0,0,0,0,0,0,0,0,-2,2,2],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2,2],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2],
])

J2 = np.array([
[0,  0,  0,  0,  0,  3,  2,  1,  0,1.5,  1,0.5,  0,0.3,0.2,0.1],
[0,  0,  0,  0,  3,  0,  1,  2,1.5,  0,0.5,  1,0.3,  0,0.1,0.2],
[0,  0,  0,  0,  2,  1,  0,  3,  1,0.5,  0,1.5,0.2,0.1,  0,0.3],
[0,  0,  0,  0,  1,  2,  3,  0,0.5,  1,1.5,  0,0.1,0.2,0.3,  0],
[0,  0,  0,  0,  0,  0,  0,  0,  0,0.3,0.2,0.1,  0,  3,  2,  1],
[0,  0,  0,  0,  0,  0,  0,  0,0.3,  0,0.1,0.2,  3,  0,0.1,  2],
[0,  0,  0,  0,  0,  0,  0,  0,0.2,0.1,  0,0.3,  2,  1,  0,  3],
[0,  0,  0,  0,  0,  0,  0,  0,0.1,0.2,0.3,  0,  1,  2,  3,  0],
[0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,0.3,0.2,0.1],
[0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,0.3,  0,0.1,0.2],
[0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,0.2,0.1,  0,0.3],
[0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,0.1,0.2,0.3,  0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
])

B = 0.2

H = J1 + B * J2

# initialize solver
# Use a D-Wave system as the sampler
#sampler = DWaveSampler(solver={'qpu': True})  # Some accounts need to replace this line with the next:
sampler = DWaveSampler(solver={'qpu': True})

# set Q for the problem QUBO
#linear = {('q0','q0'):-2}
Q_list = {}

for i, x in enumerate(H):
    for j, y in enumerate(x):
        #print("(q{}, q{}: {})".format(i,j,y))
        if i <= j:
            Q_list.update( {('q'+str(i), 'q'+str(j)): y} )
Q = dict(Q_list)
pprint(Q)
print("Q size", len(Q))
# Minor embed and sample 1000 times on default D-wave system
response = EmbeddingComposite(DWaveSampler()).sample_qubo(Q, num_reads=5)

for sample, energy, num in response.data(['sample', 'energy', 'num_occurrences']):
    #pprint.pprint(sample)
    print(sample, "Energy: ", energy, "Occurrences: ", num)
