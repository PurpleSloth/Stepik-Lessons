# -*- coding: utf-8 -*-
"""
Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.

Вам необходимо распаковать этот архив, и затем найти в данной в файловой
структуре все директории, в которых есть хотя бы один файл с расширением ".py".

Ответом на данную задачу будет являться файл со списком таких директорий,
отсортированных в лексикографическом порядке.

Для лучшего понимания формата задачи, ознакомьтесь с примером.

"""

import os

res_list = []
os.chdir('E:\Work\Python\Stepik Lessons\Source for Stepik_course2_12')

for current_dir, dirs, files in os.walk('E:\Work\Python\Stepik Lessons\Source for Stepik_course2_12\main'):
    for filename in files:
        fn = filename.split('.')
        dn = os.path.relpath(current_dir, start='Stepik Lessons')
        if fn[-1] == 'py':
            line = dn[3:].split('\\')
            line = '/'.join(line)
            if line not in res_list:
                res_list += [line]
            print(line)
    #print(current_dir, dirs, files)
res_list.sort()
print(res_list)
with open('E:/result.txt', 'w') as w:
    content = '\n'.join(res_list)
    w.write(content)

