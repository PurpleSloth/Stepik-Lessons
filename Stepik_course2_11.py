# -*- coding: utf-8 -*-
"""
Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки
в обратном порядке.

"""
lines = []
with open('E:/test.txt') as f:
    for line in f:
        line = line.strip()
        lines += [line]

#print(lines)

lines.reverse()

print(lines)

with open('E:/result.txt', 'w') as w:
    content = '\n'.join(lines)
    w.write(content)