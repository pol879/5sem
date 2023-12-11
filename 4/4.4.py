# coding: utf-8
import time
import os


def log(path):
    def outer(f):
        def wrapper(*args, **kwargs):
            with open(path, 'w') as file:
                start = time.time()
                ans = f(*args,**kwargs)
                end = time.time()
                answ = ans if ans else '-'
                tim = end-start
                args_s=str(args)[1:-1]
                s='''
                Время вызова функции: {s}
                Входящие аргументы:  {arg}
                Ответ return: {answ}
                Время завершения работы функции: {e}
                Время работы функции: {time}'''.format(s=start, answ=answ, arg=args_s, e=end, time=tim)
                file.write(s)
        return wrapper
    return outer
    
    
#Testing
path = os.getcwd()+'\\test.txt'

@log(path)
def f(a,b, res=True):
    '''пробная функция'''
    time.sleep(0.5)
    if res:
        return a+b
    
f(3,2, res=False)