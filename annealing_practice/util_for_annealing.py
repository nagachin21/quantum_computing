import sys
sys.path.append("./annealing_practice")
import numpy as np
import random
from numerology import *

def make_dis_matrix():
    mat = np.array([
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
    ])

    return mat

def make_rel_matrix():
    person = []
    person.append([1993,9,22])
    person.append([1995,4,7])
    person.append([1985,1,2])
    person.append([1980,12,1])

    for i in range(8):
        person.append([str(1900 + random.randint(0,99)), str(random.randint(1,12)), str(random.randint(1,30))] )
        print(person[i])

    print(len(person))

    mat = np.zeros((12,12))
    for i in range(12):
        for j in range(12):
            if i < j:
                x = divine(*person[i])
                y = divine(*person[j])
                mat[i][j] = affinity(x,y)
    '''
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
    '''

    return mat

def rel_num(x):
    return x // 12

def dis_num(x):
    return x % 12


def make_J2():
    J2 = np.zeros((144,144))
    relation = make_rel_matrix()
    distance = make_dis_matrix()
    #print(relation)
    #print(distance)

    for i in range(144):
        for j in range(144):
            if i < j:
                r1, r2 = min(rel_num(i), rel_num(j)), max(rel_num(i), rel_num(j))
                d1, d2 = min(dis_num(i), dis_num(j)), max(dis_num(i), dis_num(j))
                J2[i][j] = relation[r1][r2] * distance[d1][d2]

    return J2
