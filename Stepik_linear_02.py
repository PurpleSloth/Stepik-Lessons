# -*- coding: utf-8 -*-
"""
С использованием процедуры Грама-Шмидта получите ортонормированный базис из базиса вида

В качестве результата введите через пробел координаты полученных векторов, округленные до третьего знака после запятой.
"""
import math

f1 = [1, 2, 2]
f2 = [1, 3, 1]
f3 = [2, 1, 1]

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
    num = round(num, 3)
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

print('Let e1 = f1')
e1 = f1
print()
print('e1 = ', e1)
le1 = lenVector(e1)
e1 = operVector(e1, le1, 'div')
print()
print('Orto e1 is', e1)
print()


print('Found e2 = f2 - (e1f2 / e1e1)* e1')
print()

e1f2 = vectorOnVector(e1, f2)
be1 = operVector(e1, e1f2, 'mul')
e2 = sumVector(f2, be1)
le2 = lenVector(e2)
e2 = operVector(e2, le2, 'div')
print()
print('Orto e2 is', e2)
print()

print('Found e3 = f3 - (f3e1 / e1e1)*e1 - (f3e2 / e2e2)* e2')
print()

f3e1 = vectorOnVector(f3, e1)
e1e1 = vectorOnVector(e1, e1)
b1e1 = operVector(e1, f3e1 / e1e1, 'mul')
f3e2 = vectorOnVector(f3, e2)
e2e2 = vectorOnVector(e2, e2)
b2e2 = operVector(e2, f3e2 / e2e2, 'mul')
b1e1_min = operVector(b1e1, -1, 'mul')
b2e2_min = operVector(b2e2, -1, 'mul')
f3minb1e1 = sumVector(f3, b1e1_min)
e3 = sumVector(f3minb1e1, b2e2_min)
le3 = lenVector(e3)
e3 = operVector(e3, le3, 'div')
print()

for i in range(len(e1)):
    print(round(e1[i], 3))
for i in range(len(e2)):
    print(round(e2[i], 3))
for i in range(len(e3)):
    print(round(e3[i], 3))