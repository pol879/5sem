#задача вызвать ошибку в программе
#допустим программа выглядит так..
def func():
    print('Hello...')

class MyException(Exception):
    pass

raise MyException('I want to sleep, bye')
