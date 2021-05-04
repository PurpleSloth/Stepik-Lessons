# -*- coding: utf-8 -*-
"""
В этой задаче вам необходимо воспользоваться API сайта artsy.net

API проекта Artsy предоставляет информацию о некоторых деятелях искусства,
их работах, выставках.

В рамках данной задачи вам понадобятся сведения о деятелях искусства
(назовем их, условно, художники).

Вам даны идентификаторы художников в базе Artsy.
Для каждого идентификатора получите информацию о имени художника и годе рождения.
Выведите имена художников в порядке неубывания года рождения. В случае если
у художников одинаковый год рождения, выведите их имена в лексикографическом порядке.
"""
import requests
import json

client_id = '5346eca51118188329c6'
client_secret = 'a80603be08de47e87bc60fb9f8400e4c'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

artist_list = {}

with open('E://test.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        # инициируем запрос с заголовком
        r = requests.get("https://api.artsy.net/api/artists/{}".format(line.strip()), headers=headers)
        # разбираем ответ сервера
        j = json.loads(r.text)
        artist_list[j['sortable_name']] = j['birthday']

#result = sorted(artist_list, key=lambda x: artist_list[x])
result = sorted(artist_list.items(), key=lambda x: (x[1], x[0]))

for i in result:
    print(i[0])