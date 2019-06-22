import sympy as sp
import numpy as np

def make_constraint():
    func = '0'
    #横の制約
    for i in range(12):
        func += ' + (1-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{})**2'.format('q'+str(12*i), 'q'+str(12*i+1), 'q'+str(12*i+2), 'q'+str(12*i+3),\
                                                                       'q'+str(12*i+4), 'q'+str(12*i+5), 'q'+str(12*i+6), 'q'+str(12*i+7),\
                                                                       'q'+str(12*i+8), 'q'+str(12*i+9), 'q'+str(12*i+10), 'q'+str(12*i+11))
    #print(func)
    #縦の制約
    for i in range(12):
        func += ' + (1-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{})**2'.format('q'+str(i), 'q'+str(i+12*1), 'q'+str(i+12*2), 'q'+str(i+12*3),\
                                                                       'q'+str(i+12*4), 'q'+str(i+12*5), 'q'+str(i+12*6), 'q'+str(i+12*7),\
                                                                       'q'+str(i+12*8), 'q'+str(i+12*9), 'q'+str(i+12*10), 'q'+str(i+12*11))
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

def make_J1():
    for n in range(144):
        exec("q%d = sp.symbols('%s')" % (n, 'q'+str(n)))
        #print("q%d = sp.symbols('%s')" % (n, 'q'+str(n)))

    func = make_constraint()

    ex_func = sp.expand(func)
    #print(ex_func)

    ex_func_list = ['+'] + str(ex_func).split(' ')
    #print(ex_func_list)

    J1 = np.zeros((144, 144))

    for i, x in enumerate(ex_func_list):
        if x != '+' and x != '-' and x != '24':
            a, b, item = calc(x)
            if ex_func_list[int(i) - 1] == '-':
                #print('-')
                J1[int(a), int(b)] += -1 * int(item)
            else:
                J1[int(a), int(b)] += int(item)

    np.set_printoptions(edgeitems=8)
    #print(J1)
    #print(np.get_printoptions())
    return J1

def return_J2_element(i, j):
    if i >= j:
        result = 0
    else:
        result = 1
    return result

def make_J2(num):

    J2 = np.zeros((num**2, num**2))

    for i in range(num**2):
        for j in range(num**2):
            J2[i, j] = return_J2_element(i, j)

    return J2
