# -*- coding: utf-8 -*-
"""
В первой строке входных данных содержится целое число n - число классов.

В следующих n строках содержится описание наследования классов. В i-й строке 
указано от каких классов наследуется i-й класс. Обратите внимание, что класс 
может ни от кого не наследоваться. Гарантируется, что класс не наследуется 
сам от себя (прямо или косвенно), что класс не наследуется явно от одного 
класса более одного раза.

В следующей строке содержится число q - количество запросов.

В следующих q строках содержится описание запросов в формате <имя класса 1> 
<имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не 
более 50.

Формат выходных данных
Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 
является предком класса 2, и "No", если не является.
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
    class_pairs += [input().split()]
#print(class_list)
#print(class_pairs)
'''
class_list = {'A': ['B', 'C', 'D', 'G', 'H'], 'B': ['C', 'E', 'G', 'H', 'K', 'L'], 'C': ['E', 'D', 'H', 'K', 'L'], 'E': ['D', 'F', 'K', 'L'], 'D': ['G', 'H'], 'F': ['K'], 'G': ['F'], 'H': ['L'], 'K': ['H', 'L'], 'L': []}
class_pairs = [['K', 'D'], ['D', 'A'], ['G', 'D'], ['H', 'A'], ['E', 'E'], ['H', 'G'], ['E', 'L'], ['B', 'D'], ['D', 'L'], ['D', 'G'], ['D', 'E'], ['A', 'F'], ['A', 'C'], ['K', 'A'], ['A', 'H'], ['K', 'D'], ['H', 'B'], ['K', 'B'], ['D', 'L'], ['G', 'G'], ['A', 'H'], ['K', 'L'], ['G', 'E'], ['B', 'A'], ['C', 'K'], ['K', 'L'], ['C', 'L'], ['G', 'C'], ['D', 'D'], ['C', 'G'], ['E', 'A'], ['F', 'K'], ['B', 'G'], ['H', 'L'], ['L', 'F'], ['H', 'G'], ['D', 'A'], ['H', 'L']]
#class_pairs = [['K', 'D']]
founded = 'No'

def check_parent(x, y):
    global founded
    # is name
    if y not in class_list:
        #print('None this class')
        founded = 'No'
        return
    
    # same name
    if x == y:
        #print('Same name')
        founded = 'Yes'
        return
    
    for k in range(len(class_list[y])):
        #print('I search in parents of', class_list[y][k])
        # check if name in this list
        
        if x in class_list[class_list[y][k]]:
            #print('Yep!', class_list[y][k], class_list[class_list[y][k]])
            #print('Yes')
            founded = 'Yes'
            return
        else:
            #print('I found nothing, go up', class_list[class_list[y][k]])
            check_parent(x, class_list[y][k])

    
for i in range(len(class_pairs)):
    #print('Searching is', class_pairs[i][0], 'parent for', class_pairs[i][1])
    #print()
    check_parent(class_pairs[i][0], class_pairs[i][1]) 
    print(founded) 
    founded = 'No'
    #print()







