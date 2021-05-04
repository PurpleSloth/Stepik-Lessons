# -*- coding: utf-8 -*-
"""
Напишите программу, которая находит наилучшее решение системы линейных
алгебраических уравнений методом наименьших квадратов.

Формат входных данных:

В первой строке задаются два числа: количество уравнений n и количество
неизвестных m. Количество уравнений не меньше количества неизвестных.
Далее идут n строк, каждая из которых содержит m+1 число. Первые m чисел --
это коэффициенты i-го уравнения системы, а последнее, (m+1)-е число --
коэффициент bi, стоящий в правой части i-го уравнения.
Формат выходных данных:
В качестве результата следует вывести решение системы в виде m чисел,
разделенных пробелом.
"""

import numpy as np

dim = input().split()
n = int(dim[0])
m = int(dim[1])
matrix = []
full_matrix = []
f = []

# заполняем данными наши матрицы
for i in range(n):
    line = input().split()
    matrix += [line[:m]]
    full_matrix += [line]
    f += line[-1:]

a = np.array(matrix, dtype='float') # переводим в формат numpy матрицу системы
b = np.array(f, dtype='float') # переводим в формат numpy вектор правых частей

res = np.linalg.lstsq(a, b, rcond=None)
print(*res[0])