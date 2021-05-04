# -*- coding: utf-8 -*-
"""
Одним из самых часто используемых классов в Python является класс filter.
Он принимает в конструкторе два аргумента a и f – последовательность и
функцию, и позволяет проитерироваться только по таким элементам x из
последовательности a, что f(x) равно True. Будем говорить, что в этом случае
функция f допускает элемент x, а элемент x является допущенным.

В данной задаче мы просим вас реализовать класс multifilter, который будет
выполнять ту же функцию, что и стандартный класс filter, но будет использовать
не одну функцию, а несколько.

Решение о допуске элемента будет приниматься на основании того, сколько функций
допускают этот элемент, и сколько не допускают. Обозначим эти количества за
pos и neg.

Введем понятие решающей функции – это функция, которая принимает два
аргумента – количества pos и neg, и возвращает True, если элемент допущен,
и False иначе.

"""

class multifilter:
    def judge_half(pos, neg):
        if pos >= neg:
            return True
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        if pos >= 1:
            return True
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        if neg == 0:
            return True
        # допускает элемент, если его допускают все функции (neg == 0)

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        self.iterable = iterable
        # funcs - допускающие функции
        self.funcs = funcs
        # judge - решающая функция
        self.judge = judge
        self.i = 0
        self.pos = 0
        self.neg = 0

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        return self

    def __next__(self):
        self.pos = 0
        self.neg = 0
        if self.i < len(self.iterable):
            self.countRes(self.iterable[self.i], self.funcs)
            self.i += 1
            if self.judge(self.pos, self.neg) == True:
                return self.iterable[self.i - 1]
            else:
                return self.__next__()
        else:
            raise StopIteration

    def countRes(self, x, funcs):
        for k in funcs:
            if k(x) == True:
                self.pos += 1
            else:
                self.neg += 1


#
#
#
#

def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)] # [0, 1, 2, ... , 30]

#print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_any)))

print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]