import sympy as sp
import numpy as np

def make_constraint():
    func = '0'
    #横の制約
    for i in range(4):
        func += ' + (1-{}-{}-{}-{})**2'.format('q'+str(4*i), 'q'+str(4*i+1), 'q'+str(4*i+2), 'q'+str(4*i+3))
    #print(func)
    #縦の制約
    for i in range(4):
        func += ' + (1-{}-{}-{}-{})**2'.format('q'+str(i), 'q'+str(i+4), 'q'+str(i+8), 'q'+str(i+12))
    #print(func)

    return func

def calc(x):
    element = x.split('*')
    number1 = 0
    number2 = 0

    print(x)

    if '**' in x:
        # 2 q0 2
        number1 = element[1].split('q')[1]
        number2 = number1
    elif len(element) == 3:
        # 4 q1 q2
        number1 = element[1].split('q')[1]
        number2 = element[2].split('q')[1]
        print('check', number1, element[2].split('q')[1])
    elif len(element) == 2:
        # 2 q1
        number1 = element[1].split('q')[1]
        number2 = number1

    x, y = min(int(number1), int(number2)), max(int(number1), int(number2))
    print('check2',x, y, element[0])
    return x, y, element[0]


for n in range(16):
    exec("q%d = sp.symbols('%s')" % (n, 'q'+str(n)))
    #print("q%d = sp.symbols('%s')" % (n, 'q'+str(n)))

func = make_constraint()

ex_func = sp.expand(func)
#print(ex_func)

ex_func_list = ['+'] + str(ex_func).split(' ')
#print(ex_func_list)

J1 = np.zeros((16, 16))

for i, x in enumerate(ex_func_list):
    if x != '+' and x != '-' and x != '8':
        a, b, item = calc(x)
        if ex_func_list[int(i) - 1] == '-':
            print('-')
            J1[int(a), int(b)] += -1 * int(item)
        else:
            J1[int(a), int(b)] += int(item)

print(J1)
