# -*- coding: utf-8 -*-
"""
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com

Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли
интересный математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный
факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют
числа во входном файле.

Пример запроса к интересному числу:
http://numbersapi.com/31/math?json=true

Пример запроса к скучному числу:
http://numbersapi.com/999/math?json=true
"""
import requests

with open('E://test.txt', 'r') as f:
    for line in f:
        req_url = 'http://numbersapi.com/{}/math?json=true'.format(line.strip())
        num_json = requests.get(req_url)
        if num_json.json()['found']:
            print('Interesting')
        else:
            print('Boring')
