import sys
sys.path.append("./annealing_practice")
import numpy as np
from numerology import *

def make_dis_matrix():
    mat = [
    [0,  1,0.5,  3,  2,0.5,  0,  0,  0,  0,  0,  0],
    [0,  0,  2,  1,  3,  1,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,0.5,  1,  3,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  2,0.5,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  2,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  2,0.5,  3,  1,0.5],
    [0,  0,  0,  0,  0,  0,  0,  0,  2,  1,  3,  1],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,0.5,  1,  3],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  3,0.5],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  2],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
    ]

    return mat

def make_rel_matrix():
    A = [1993,9,22]
    B = [1995,4,7]
    C = [1985,1,2]
    D = [1980,12,1]

    A_num = divine(*A)
    B_num = divine(*B)

    #print("A ", A_num)

    mat = [
    [0,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
    [0,  0,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
    [0,  0,  0,  1,  1,  1,  1,  1,  1,  1,  1,  1],
    [0,  0,  0,  0,  1,  1,  1,  1,  1,  1,  1,  1],
    [0,  0,  0,  0,  0,  1,  1,  1,  1,  1,  1,  1],
    [0,  0,  0,  0,  0,  0,  1,  1,  1,  1,  1,  1],
    [0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,  1],
    [0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
    ]

    return mat

def rel_num(x):
    return x // 12

def dis_num(x):
    return x % 12


def make_J2():
    J2 = np.zeros((144,144))
    relation = make_rel_matrix()
    distance = make_dis_matrix()

    for i in range(144):
        for j in range(144):
            if i < j:
                r1, r2 = min(rel_num(i), rel_num(j)), max(rel_num(i), rel_num(j))
                d1, d2 = min(dis_num(i), dis_num(j)), max(dis_num(i), dis_num(j))
                J2[i][j] = relation[r1][r2] * distance[d1][d2]

    return J2

#np.set_printoptions(edgeitems=8)
#print(make_J2())
