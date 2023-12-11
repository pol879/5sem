# coding: utf-8
def fibonaci(n):
    'генератор'
    a, b = 0, 1
    i = 0
    while i < n:
        yield a
        a, b = b, a + b
        i += 1
def fib(n):
    'функция для вывода'
    for i in fibonaci(n):
        print(i, end=' ')