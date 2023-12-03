#Считаем, что список чисел задается в одну строку через пробел


def answ(f):
    '''decorator'''
    def wrapper():
        res = f()
        if res ==0:
            print('Нет(')
        elif res > 10:
            print('Очень много')
        else:
            print(res)
    return wrapper

@answ            
def count_even():
    '''функция для подсчета четных чисел в введенном списке '''
    a=list(map(int, input().split()))
    counter = 0
    for num in a:
        if num%2==0:
            counter+=1
    return counter

count_even()

    