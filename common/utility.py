import numpy as np
import sympy as sp
import random
import matplotlib.pyplot as plt
import matplotlib as mpl
from numerology import *

'''
J1の作成部分
'''
def make_constraint(idx):
    func = '0'

    #横の制約
    for i in range(idx):
        func += '+ (1 '
        for j in range(idx):
            func += '-{}'.format( 'q'+str(idx*i+j) )
        func += ')**2'

    #縦の制約
    for i in range(idx):
        func += '+ (1 '
        for j in range(idx):
            func += '-{}'.format( 'q'+str(i+idx*j) )
        func += ')**2'

    #print(func)

    return func

def calc(x):
    element = x.split('*')
    number1 = 0
    number2 = 0

    #print(x)

    if '**' in x:
        # 2 q0 2
        if len(element) == 4:
            number1 = element[1].split('q')[1]
            number2 = number1
        elif len(element) == 3:
            number1 = element[0].split('q')[1]
            number2 = number1
            element = ['1'] + element
    elif len(element) == 3:
        # 4 q1 q2
        number1 = element[1].split('q')[1]
        number2 = element[2].split('q')[1]
        #print('check', number1, element[2].split('q')[1])
    elif len(element) == 2:
        # 2 q1
        number1 = element[1].split('q')[1]
        number2 = number1

    x, y = min(int(number1), int(number2)), max(int(number1), int(number2))
    #print('check2',x, y, element[0])
    return x, y, element[0]

def make_J1(idx):
    for n in range(idx**2):
        exec("q%d = sp.symbols('%s')" % (n, 'q'+str(n)))
        #print("q%d = sp.symbols('%s')" % (n, 'q'+str(n)))

    func = make_constraint(idx)

    ex_func = sp.expand(func)
    #print(ex_func)

    ex_func_list = ['+'] + str(ex_func).split(' ')
    #print(ex_func_list)

    J1 = np.zeros((idx**2, idx**2))

    for i, x in enumerate(ex_func_list):

        if x != '+' and x != '-' and x != str(idx*2):
            a, b, item = calc(x)
            if ex_func_list[int(i) - 1] == '-':
                J1[int(a), int(b)] += -1 * int(item)
            else:
                J1[int(a), int(b)] += int(item)

    return J1

'''
J2の作成部分
'''
def make_dis_matrix(idx):
    if idx == 12:
        '''
        12x12
        '''
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
    elif idx == 8:
        '''
        8x8
        '''
        mat = np.array([
        [0,  1,  2,  3,  1,1.5,2.5,3.5],
        [0,  0,  1,  2,1.5,  1,1.5,2.5],
        [0,  0,  0,  1,2.5,1.5,  1,1.5],
        [0,  0,  0,  0,3.5,2.5,1.5,  1],
        [0,  0,  0,  0,  0,  1,  2,  3],
        [0,  0,  0,  0,  0,  0,  1,  2],
        [0,  0,  0,  0,  0,  0,  0,  1],
        [0,  0,  0,  0,  0,  0,  0,  0]
        ])
    elif idx == 4:
        '''
        4x4
        '''
        mat = np.array([
        [0,3,2,1],
        [0,0,1,2],
        [0,0,0,3],
        [0,0,0,0]
        ])
    else:
        mat = np.zeros((idx, idx))

    return mat

def make_rel_matrix(idx, random_flag=True):
    person = []
    if random_flag:
        for i in range(idx):
            person.append([str(1900 + random.randint(0,99)), str(random.randint(1,12)), str(random.randint(1,30))] )
    else:
        for i in range(idx):
            person.append([str(1980 + i*5), str(i), str(1+i)])
            #print(person)

    mat = np.zeros((idx,idx))
    for i in range(idx):
        for j in range(idx):
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

def rel_num(x, idx):
    return x // idx

def dis_num(x, idx):
    return x % idx


def make_J2(idx, random_flag=True):
    J2 = np.zeros((idx**2,idx**2))
    relation = make_rel_matrix(idx, random_flag)
    distance = make_dis_matrix(idx)
    #print(relation)
    #print(distance)

    for i in range(idx**2):
        for j in range(idx**2):
            if i < j:
                r1, r2 = min(rel_num(i, idx), rel_num(j, idx)), max(rel_num(i, idx), rel_num(j, idx))
                d1, d2 = min(dis_num(i, idx), dis_num(j, idx)), max(dis_num(i, idx), dis_num(j, idx))
                J2[i][j] = relation[r1][r2] * distance[d1][d2]

    return J2

def make_hist(response):
    list = []
    print(response.info)
    for sample, energy, occurences in response.data(['sample', 'energy', 'num_occurrences']):
        #print(sample, energy, occurences)
        for i in range(occurences):
            list.append(energy)

    plt.title('annealing sampling')
    plt.hist(list)
    plt.show()


def return_result(sampleSet):
    for sample, energy in sampleSet.data(fields=['sample', 'energy']):
        #print(sample, type(sample))
        qubits = []
        for qubit,i in sample.items():
            if i == 1:
                qubits.append(qubit)
        print("sample:{0}, energy:{1}".format(qubits,energy))
