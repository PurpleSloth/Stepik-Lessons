# -*- coding: utf-8 -*-
"""
Скачайте файл. В нём указан адрес другого файла, который нужно скачать 
с использованием модуля requests и посчитать число строк в нём.

Используйте функцию get для получения файла (имеет смысл вызвать метод strip 
к передаваемому параметру, чтобы убрать пробельные символы по краям).

После получения файла вы можете проверить результат, обратившись к полю text. 
Если результат работы скрипта не принимается, проверьте поле url на 
правильность. Для подсчёта количества строк разбейте текст с помощью 
метода splitlines.

В поле ответа введите одно число или отправьте файл, содержащий одно число.
"""

import requests

with open ('E:\Downloads\dataset_3378_2 (1).txt', "r", encoding='utf-8') as inf:
    file_url = inf.readline().strip()
    
content = requests.get(file_url)
content_lines = content.text.splitlines()

    
print(len(content_lines))
print(content.url)



    