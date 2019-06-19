import numpy as np
import wildqat as wq

a = wq.opt()

J1 = np.array([
[-3, 4],
[ 0,-4]
])

a.qubo = J1

result = a.sa()
print(result)
