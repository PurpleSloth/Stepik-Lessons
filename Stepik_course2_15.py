# -*- coding: utf-8 -*-
"""
Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида
<a ... href="..." ... > и вывести список сайтов, на которые есть ссылка.

Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов.
То есть, это последовательность символов, которая следует сразу после символов
протокола, если он есть, до символов порта или пути, если они есть,
за исключением случаев с относительными ссылками вида
<a href="../some_path/index.html">.

Сайты следует выводить в алфавитном порядке.
Тест №1: http://pastebin.com/raw/2mie4QYa
Тест №2: http://pastebin.com/raw/hfMThaGb
Тест №3: http://pastebin.com/raw/7543p0ns
"""
import requests
import re

url_a = input().strip()

a_site = requests.get(url_a)
a_text = a_site.text
pattern = r"<a.*href=[\"|\'](.*?:\/\/)?(\w[a-zA-Z0-9\.\-_]*)"
x = re.findall(pattern, a_text, re.MULTILINE)
new_x = []
for item in x:
    if item[1] not in new_x:
        new_x.append(item[1])

new_x.sort()
for i in new_x:
    print(i)


# url_b = input()

# new_y = []

# def get_urls(text):
#     site_a = requests.get(text)
#     pattern = r'(<a href=\")(.+?)(\")'
#     x = re.findall(pattern, site_a.text)
#     new_x = []
#     for item in x:
#         new_x.append(item[1])
#     return new_x

# if requests.get(url_a).status_code == 200:
#     all_a_links = get_urls(url_a)
# else:
#     print('No')

# for link in all_a_links:
#     pattern = r'(<a href=\")(.+?)(\")'
#     if requests.get(link).status_code == 200:
#         y = re.findall(pattern, requests.get(link).text)
#         for item in y:
#             new_y.append(item[1])

# if url_b in new_y:
#     print('Yes')
# else:
#     print('No')

