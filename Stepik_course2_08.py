# -*- coding: utf-8 -*-
"""
Алиса владеет интересной информацией, которую хочет заполучить Боб.
Алиса умна, поэтому она хранит свою информацию в зашифрованном файле.
У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде в
текстовом файле.

Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом
с паролями, но он не смог понять какой из паролей ему нужен. Помогите ему
решить эту проблему.

Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
Она представила информацию в виде строки, и затем записала в бинарный файл
результат работы метода simplecrypt.encrypt.

Вам необходимо установить библиотеку simple-crypt, и с помощью метода
simplecrypt.decrypt узнать, какой из паролей служит ключом для расшифровки
файла с интересной информацией.

Ответом для данной задачи служит расшифрованная интересная информация Алисы.
"""
pass_list = []

with open("E:/encrypted.bin", "rb") as inp:
    encrypted = inp.read()
print(encrypted)
print()

with open("E:/passwords.txt", "r") as inp2:
    pass_list += inp2.read().strip().splitlines()
print(pass_list)

from simplecrypt import encrypt, decrypt

def try_pass(pwd):
    try:
        return decrypt(pwd, encrypted).decode('utf8')
    except:
        return False

for password in pass_list:
    if try_pass(password) != False:
        print(try_pass(password))
        break
    else:
        print('Failed for ', password)

