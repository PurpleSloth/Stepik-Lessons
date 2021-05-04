# -*- coding: utf-8 -*-
"""
Дана квадратная матрица. Найдите определитель данной матрицы.

В первой строке задается число nn (1\le n\le121≤n≤12).

Следующие nn строк содержат n^2n
2
  целых чисел от -5−5 до 55 (по nn чисел в каждой строке) — элементы матрицы.

Выведите одно целое число — определитель данной матрицы.
"""
# mrank = int(input())
# m = []
# firstcheck = 0
# sign = 1
# determinant = 1.0
# for i in range(mrank):
#     m.append(list(map(float, input().split())))
#     firstcheck += abs(m[i][0])

mrank = 4
m = [[-1.0, -1.0, 1.0, 1.0], [1.0, -1.0, 1.0, 0.0], [1.0, 0.0, 0.0, -1.0], [1.0, 0.0, -1.0, 0.0]]
firstcheck = 0
sign = 1
determinant = 1.0
for i in range(mrank):
    firstcheck += abs(m[i][0])

print(m)

def det(m):
    global sign, determinant, mrank, firstcheck
    # zeroes
    for i in range(mrank):
        firstcheck += abs(m[i][0])
    if firstcheck == 0:
        print(int(firstcheck))
        return
    # sort
    print('Lets sort')
    for i in range(mrank):
        if m[i][0] != 0 and mrank > 1:
            if i == 0:
                print('Going further')
                sign = 1
                print('Sign is ', sign)
                break
            else:
                print('Swap strings')
                m[0], m[i] = m[i], m[0]
            if sign == 1:
                sign = -1
                print('Sign is ', sign)
            else:
                sign = 1
                print('Sign is ', sign)
            print('Sorted - ', m)
            print('Sign = ', sign)
            break
    # multiply
    for k in range(1, mrank):
        print('Search ak for {} string - {}'.format(k, m[k]))
        ak = m[k][0] / m[0][0]
        print('ak = {} = {} / {}'.format(ak, m[k][0], m[0][0]))

        for n in range(mrank):
            print('m[{},{}] = {} - ({} * {}) = {}'.format(k, n, m[k][n], ak, m[0][n], m[k][n] - ak * m[0][n]))
            m[k][n] = m[k][n] - (ak * m[0][n])

    print('This is new m - ', m)
    if mrank > 1:
        print('old det {} * m00 {} = {}'.format(determinant, m[0][0], determinant * m[0][0]))
        determinant *= m[0][0]
        print('det =  old det {} * sign {} = {}'.format(determinant, sign, determinant * sign))
        determinant *= sign

        del(m[0])
        for i in range(len(m)):
            del(m[i][0])
        mrank = len(m)
        print('Work with ', m)
        print(m, determinant)
        firstcheck = 0
        det(m)
    else:
        determinant *= m[0][0]
        print(int(round(determinant)))

# check zero
det(m)


