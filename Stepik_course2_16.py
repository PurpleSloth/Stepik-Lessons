# -*- coding: utf-8 -*-
"""
Вам дана частичная выборка из датасета зафиксированных преступлений,
совершенных в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное
число раз в 2015 году.
"""
import csv
#print(csv.reader.__doc__)
result = {}

with open('E:\Work\Python\Stepik Lessons\Source for Stepik_course2_16\Crimes.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['Primary Type'] not in result:
            result[row['Primary Type']] = 0
        result[row['Primary Type']] += 1

a = 0
b = ''

for key, value in result.items():
    if value > a:
        a = value
        b = key
print(b)


