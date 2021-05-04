# -*- coding: utf-8 -*-
"""
В первой строке входных данных содержится целое число n - число классов
исключений.

В следующих n строках содержится описание наследования классов. В i-й строке
указано от каких классов наследуется i-й класс. Обратите внимание, что класс
может ни от кого не наследоваться. Гарантируется, что класс не наследуется
сам от себя (прямо или косвенно), что класс не наследуется явно от одного
класса более одного раза.

В следующей строке содержится число m - количество обрабатываемых исключений.
Следующие m строк содержат имена исключений в том порядке, в каком они были
написаны у Антона в коде.
Гарантируется, что никакое исключение не обрабатывается дважды.

Формат выходных данных
Выведите в отдельной строке имя каждого исключения, обработку которого можно
удалить из кода, не изменив при этом поведение программы. Имена следует
выводить в том же порядке, в котором они идут во входных данных.
"""
'''
count = int(input())
class_list = {}
class_pairs = []
tmp = []
for i in range(count):
    tmp = input().split(' : ')
    if len(tmp) > 1:
        tmp2 = tmp[-1].split()
    else:
        tmp2 = []
    class_list[tmp[0]] = []
    class_list[tmp[0]] += tmp2

count = int(input())
for i in range(count):
    class_pairs += input().split()
#print(class_list)
#print(class_pairs)
'''
class_list = {'BaseException': [], 'Exception': ['BaseException'], 'LookupError': ['Exception'], 'KeyError': ['LookupError']}
class_pairs = ['BaseException', 'KeyError']
#class_list = {'a': [], 'b': ['a'], 'c': ['a'], 'f': ['a'], 'd': ['c', 'b'], 'g': ['d', 'f'], 'i': ['g'], 'm': ['i'], 'n': ['i'], 'z': ['i'], 'e': ['m', 'n'], 'y': ['z'], 'x': ['z'], 'w': ['e', 'y', 'x']}
#class_pairs = ['y', 'm', 'n', 'm', 'd', 'e', 'g', 'a', 'f']
#class_pairs = ['y', 'm', 'n', 'm', 'd', 'e']
checked_exceptions = []
res_list = []
ch_val = ''

def check_parent(x):
    global ch_val
    if x in checked_exceptions:
        return x

    for chk_parent in range(len(checked_exceptions)):
        for k in range(len(class_list[x])):
            if checked_exceptions[chk_parent] == class_list[x][k]:
                if ch_val not in res_list:
                    res_list.append(ch_val)
                return ch_val
            else:
                check_parent(class_list[x][k])

for i in range(len(class_pairs)):
    if checked_exceptions == []:
        checked_exceptions.append(class_pairs[i])
    else:
        ch_val = class_pairs[i]
        check_parent(class_pairs[i])
        if class_pairs[i] not in checked_exceptions:
            checked_exceptions.append(class_pairs[i])
        else:
            print(ch_val)

for w in range(len(res_list)):
    print(res_list[w])








