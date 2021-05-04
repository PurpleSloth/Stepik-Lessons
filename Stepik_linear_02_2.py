# -*- coding: utf-8 -*-
"""
С использованием процедуры Грама-Шмидта получите ортонормированный базис из базиса вида

В качестве результата введите через пробел координаты полученных векторов, округленные до третьего знака после запятой.
"""
import math

e3 = [1, 2, 7]
e1 = [1, 1, -2]
e2 = [1, -1, 4]

def vectorOnVector(v1, v2):
    resvector = 0
    for i in range(len(v1)):
        resvector += (v1[i] * v2[i])
    print('Scalar of {} and {} is {}'.format(v1, v2, resvector))
    return resvector

def lenVector(v1):
    lenvector = 0
    for i in range(len(v1)):
        lenvector += (abs(v1[i]) * abs(v1[i]))
    print('Len of {} is {}'.format(v1, math.sqrt(lenvector)))
    return math.sqrt(lenvector)

def operVector(v1, num, op):
    mulvector = []
    for i in range(len(v1)):
        if op == 'mul':
            mulvector.append(v1[i] * num)
        elif op == 'div':
            mulvector.append(v1[i] / num)
    print('{} {} on {} is {}'.format(v1, op, num, mulvector))
    return mulvector

def sumVector(v1, v2):
    sumvector = []
    for i in range(len(v1)):
        sumvector.append(v1[i] + v2[i])
    print('Sum of {} and {} is {}'.format(v1, v2, sumvector))
    return sumvector

#vectorOnVector(f3, f3)
#lenVector(f1)
#operVector(f1, 3, 'div')

x1 = 0.409
x2 = 1.682
vectorOnVector(e1, e3)
vectorOnVector(e2, e3)
vectorOnVector(e1, e1)
vectorOnVector(e1, e2)
vectorOnVector(e2, e2)



print(lenVector([2.091, -1.273, 5.91]))