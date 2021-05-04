# -*- coding: utf-8 -*-
"""
Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue﻿).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.

Пример:

<cube color="blue">
  <cube color="red">
    <cube color="green">
    </cube>
  </cube>
  <cube color="red">
  </cube>
</cube>

Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML
документа имеет ценность 1. Кубики, расположенные прямо под ним, имеют ценность 2.
Кубики, расположенные прямо под нижележащими кубиками, имеют ценность 3. И т. д.

Ценность цвета равна сумме ценностей всех кубиков этого цвета.

Выведите через пробел три числа: ценности красного, зеленого и синего цветов.
"""
from xml.etree import ElementTree

#tree = ElementTree.fromstring(input())
tree = ElementTree.fromstring('<cube color="blue"><cube color="red"/><cube color="green"><cube color="green"></cube></cube><cube color="red"><cube color="blue"><cube color="blue"></cube><cube color="red"></cube></cube></cube><cube color="blue"></cube></cube>')
level = 2

list_all = tree.findall('.//cube')
find_str = './cube'
tree.set('level', 1)

def setDepth(tree):
    global level
    global find_str
    if len(list_all) > 0:
        for element in tree.findall(find_str):
            element.set('level', level)
            list_all.remove(element)
        level += 1
        find_str += '/cube'
        setDepth(tree)


setDepth(tree)
red = 0
green = 0
blue = 0

for element in tree.iter('cube'):
    #print(element, element.attrib)
    if element.attrib['color']  == 'red':
        red += element.attrib['level']
    elif element.attrib['color'] == 'green':
        green += element.attrib['level']
    elif element.attrib['color'] == 'blue':
        blue += element.attrib['level']


print(red, green, blue)

