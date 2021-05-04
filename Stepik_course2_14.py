# -*- coding: utf-8 -*-
"""
Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е.
внутри A есть тег <a href="B">, возможно с дополнительными параметрами внутри
тега.
Из A можно перейти в B за два перехода если существует такой документ C, что
из A в C можно перейти за один переход и из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов
A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести
на существующие HTML документы.
"""
import requests
import re

url_a = input()
url_b = input()

new_y = []

def get_urls(text):
    site_a = requests.get(text)
    pattern = r'(<a href=\")(.+?)(\")'
    x = re.findall(pattern, site_a.text)
    new_x = []
    for item in x:
        new_x.append(item[1])
    return new_x

if requests.get(url_a).status_code == 200:
    all_a_links = get_urls(url_a)
else:
    print('No')

for link in all_a_links:
    pattern = r'(<a href=\")(.+?)(\")'
    if requests.get(link).status_code == 200:
        y = re.findall(pattern, requests.get(link).text)
        for item in y:
            new_y.append(item[1])

if url_b in new_y:
    print('Yes')
else:
    print('No')

