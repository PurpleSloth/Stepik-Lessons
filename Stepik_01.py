# -*- coding: utf-8 -*-
"""
На прошлой неделе мы сжимали строки, используя кодирование повторов.
Теперь нашей задачей будет восстановление исходной строки обратно.
Напишите программу, которая считывает из файла строку, 
соответствующую тексту, сжатому с помощью кодирования повторов, 
и производит обратную операцию, получая исходный текст.
Запишите полученный текст в файл и прикрепите его, как ответ на это 
задание.
В исходном тексте не встречаются цифры, так что код однозначно 
интерпретируем.
Примечание. Это первое задание типа Dataset Quiz. 
В таких заданиях после нажатия "Start Quiz" у вас 
появляется ссылка "download your dataset". 
Используйте эту ссылку для того, чтобы загрузить 
файл со входными данными к себе на компьютер. 
Запустите вашу программу, используя этот файл в качестве входных данных. 
Выходной файл, который при этом у вас получится, 
надо отправить в качестве ответа на эту задачу.

Sample Input:
a3b4c2e10b1

Sample Output:
aaabbbbcceeeeeeeeeeb
"""

with open ('E:/test.txt') as inf:
    s1 = inf.readline().strip()
    
numbers = '0123456789'
line_num = ''
cur_count = 0
let_count = 0 #count of current letter
letter = ''
cur_list = []

for i in range(len(s1)):
    if s1[i] not in numbers:
        cur_list = s1[i:]
        letter = cur_list[0]
        while cur_count in range(len(cur_list) - 1):
            cur_count += 1
            if cur_list[cur_count] in numbers:
                let_count += 1
            else:
                break
        to_mult = int(cur_list[1:let_count + 1])
        line_num += letter * to_mult
        let_count = 0
        cur_count = 0
    else:
        letter += s1[i]
    
with open('E:/result.txt', 'w') as inf:
    inf.write(str(line_num))
    