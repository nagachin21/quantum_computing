import numpy as np
import wildqat as wq

a = wq.opt()

J1 = np.array([
[-3, 4,-2],
[ 0,-5, 6],
[ 0, 0, 3]
])

a.qubo = J1

result = a.sa()
print(result)
