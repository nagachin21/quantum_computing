
def divine(birthy,birthm,birthd):
    list = []
    year  = digit(birthy)
    month = digit(birthm)
    day   = digit(birthd)

    list = year + month + day
    res = sum(list)

    while res // 10 != 0:
        if res == 11:
            return 1
        elif res == 22:
            return 2
        elif res == 33:
            return 3
        elif res >= 10 and res != 11 and res !=22 and res!=33:
            list = digit(res)
            res = sum(list)

    return res

def affinity(x,y):
    if x == 1:
        if y == 5 or y == 6:
            return 1.0
        elif y == 3 or y == 4:
            return 0.1
        else:
            return 0.5
    elif x == 2:
        if y == 2 or y == 4:
            return 1.0
        elif y == 5 or y == 7 or y == 9:
            return 0.1
        else:
            return 0.5
    elif x == 3:
        if y == 8 or y == 9:
            return 1.0
        elif y == 1:
            return 0.1
        else:
            return 0.5
    elif x == 4:
        if y == 2 or y == 6:
            return 1.0
        elif y == 1 or y == 3 or y == 7:
            return 0.1
        else:
            return 0.5
    elif x == 5:
        if y == 1 or y == 3:
            return 1.0
        elif y == 2 or y == 6 or y == 9:
            return 0.1
        else:
            return 0.5
    elif x == 6:
        if y == 1 or y == 4 or y == 8:
            return 1.0
        elif y == 5 or y == 7:
            return 0.1
        else:
            return 0.5
    elif x == 7:
        if y == 4 or y == 9:
            return 1.0
        elif y == 2 or y == 6:
            return 0.1
        else:
            return 0.5
    elif x == 8:
        if y == 3 or y == 6:
            return 1.0
        elif y == 8 or y == 9:
            return 0.1
        else:
            return 0.5
    elif x == 9:
        if y == 3 or y == 7:
            return 1.0
        elif y == 2 or y == 5 or y == 8:
            return 0.1
        else:
            return 0.5


def digit(i):
    lst = []
    while i > 0:
        lst.append(i%10)
        i //= 10
    lst.reverse()
    return lst

def sum(list):
    sum = 0
    for num in list:
        sum += num
    return sum
