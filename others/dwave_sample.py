import wildqat as wq
import numpy as np

a = wq.opt()
a.dwavetoken = "DEV-1bc37e85b416b94b19afdd046f774059d756299c"

a.qubo = np.array([[3,0],[0,-2]])

result = a.dw()
print(result)
