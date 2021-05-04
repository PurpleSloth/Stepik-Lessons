# -*- coding: utf-8 -*-
"""
Недавно мы считали для каждого слова количество его вхождений в строку.
Но на все слова может быть не так интересно смотреть, как, например, 
на наиболее часто используемые.

Напишите программу, которая считывает текст из файла (в файле может 
быть больше одной строки) и выводит самое частое слово в этом тексте 
и через пробел то, сколько раз оно встретилось. 
Если таких слов несколько, вывести лексикографически первое 
(можно использовать оператор < для строк).

В качестве ответа укажите вывод программы, а не саму программу.

Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:
abc a bCd bC AbC BC BCD bcd ABC

Sample Output:
abc 3
"""
s_file = ''

with open ('E:/test.txt') as inf:
    for line in inf:
        line = line
        s_file += line

s_list = s_file.lower().split()    
#print(s_list)

final_dict = {}

for word in s_list:
    if word in final_dict:
        final_dict[word] +=1
    else:    
        final_dict[word] = 1
#print(final_dict)    

result_key = 0


for key in final_dict.keys():
    if final_dict[key] > result_key:
        result_key = final_dict[key]
        print(key, result_key)

