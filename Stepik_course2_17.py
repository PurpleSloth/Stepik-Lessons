# -*- coding: utf-8 -*-
"""
Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют
классам. У каждого JSON-объекта есть поле name, которое содержит имя класса,
и поле parents, которое содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]},
 {"name": "C", "parents": ["A"]}]

﻿Эквивалент на Python:

class A:
    pass

class B(A, C):
    pass

class C(A):
    pass

Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и
что никакой класс не наследуется явно от одного класса более одного раза.

Для каждого класса вычислите предком скольких классов он является и выведите
эту информацию в следующем формате.

<имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.
"""
json_input = '[{"name": "G", "parents": ["ZZZ"]}, {"name": "TH", "parents": ["ZZZ"]}, {"name": "G", "parents": ["ZY"]}, {"name": "G", "parents": ["F"]}, {"name": "A", "parents": []}, {"name": "B", "parents": ["A"]}, {"name": "C", "parents": ["A"]}, {"name": "D", "parents": ["B", "C"]}, {"name": "E", "parents": ["D"]}, {"name": "F", "parents": ["D"]}, {"name": "X", "parents": []}, {"name": "Y", "parents": ["X", "A"]}, {"name": "Z", "parents": ["X"]}, {"name": "V", "parents": ["Z", "Y"]}, {"name": "W", "parents": ["V"]}]'

import json

#json_input = input()
parents = {}
count = {}
python_classes = json.loads(json_input)
result = []

for i in python_classes:
    if i['name'] not in parents:
        parents[i['name']] = []
        count[i['name']] = []
    for k in i['parents']:
        if k not in parents:
            parents[k] = []
            count[k] = []
        parents[i['name']].append(k)

current = ''

def check_parent(parent):
    global current
    for key, value in parents.items():
        if parent in value:
            if key not in count[current]:
                count[current].append(key)
            check_parent(key)


for key in parents:
    current = key
    count[current].append(key)
    check_parent(key)

print(count)

for key in count.keys():
    a = key, ':', len(count[key])
    result.append(a)
result.sort()
for i in result:
    print(*i)


