import wildqat as wq
import numpy as np

def make_J2():
    J2 = np.zeros((16,16))
    rel_mat =[
    [0,  1,0.5,0.1],
    [0,  0,0.1,  1],
    [0,  0,  0,0.1],
    [0,  0,  0,  0]
    ]

    dis_mat =[
    [0,3,2,1],
    [0,0,1,2],
    [0,0,0,3],
    [0,0,0,0]
    ]

    for i in range(16):
        for j in range(16):
            if i < j:
                r1, r2 = min(i//4, j//4), max(i//4, j//4)
                d1, d2 = min(i%4, j%4), max(i%4, j%4)
                #print(r1, r2)
                #print(d1, d2)
                #print("relation: ", rel_mat[r1][r2],"r1: ", r1, "r2: ", r2)
                J2[i][j] = rel_mat[r1][r2] * dis_mat[d1][d2]
    return J2

a = wq.opt()

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

B = -0.2

a.qubo = J1 + B * J2
result = a.sa()
print(result)
#test_J2 = make_J2()
#print(test_J2)
#print(J2 == test_J2)
