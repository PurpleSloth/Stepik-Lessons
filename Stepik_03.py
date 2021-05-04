# -*- coding: utf-8 -*-
"""
Имеется файл с данными по успеваемости абитуриентов. Он представляет
из себя набор строк, где в каждой строке записана следующая
информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.

Напишите программу, которая считывает файл с подобной структурой 
и для каждого абитуриента выводит его среднюю оценку по этим трём 
предметам на отдельной строке, соответствующей этому абитуриенту.

Также в конце файла, на отдельной строке, через пробел запишите 
средние баллы по математике, физике и русскому языку по всем абитуриентам.

В качестве ответа на задание прикрепите полученный файл со 
средними оценками.
"""
students = []
with open ('E:/test.txt', "r", encoding='utf-8') as inf:
    for line in inf:
        line = line.strip().split(';')
        students += [line[1:]]
        
sum4stud = 0
count4stud = 0
sum4pred = 0
ouf = open('E:/result.txt', "w", encoding='utf-8')
for student in students:
    for i in range(len(student)):
        sum4stud += int(student[i])
        count4stud += 1

    mean_student = sum4stud / count4stud
    sum4stud = 0
    count4stud = 0
    #
    
    ouf.write(str(mean_student)+'\n')
    #print(mean_student)


for i in range(len(students[i])):
    for k in range(len(students)):
        #print(students[k][i])
        sum4pred += int(students[k][i])
    ouf.write(str(sum4pred / len(students)) + ' ')
    
    sum4pred = 0
        
ouf.close()
    

        
    


