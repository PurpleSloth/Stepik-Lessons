# -*- coding: utf-8 -*-
"""
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя 
следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл 
из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
"""
import requests

with open ('E:\Downloads\dataset_3378_3 (1).txt', "r", encoding='utf-8') as inf:
    file_url = inf.readline().strip()
    print(file_url)

content = requests.get(file_url)
new_url = 'https://stepic.org/media/attachments/course67/3.6.3/'
new_url += content.text

i = 0

while i == 0:
    content = requests.get(new_url).text
    if 'We' not in content:
        new_url = 'https://stepic.org/media/attachments/course67/3.6.3/' + content
        print(new_url)
    else: 
        print(content)
        i = 1
        break

#print(content.text)