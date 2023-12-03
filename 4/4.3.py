
def swap(f):
    '''swap unnamed inputs'''
    def wrapper(*args, **kwargs):
        res = f(*tuple(reversed(args)), **kwargs)
    return wrapper

#пример для проверки
@swap
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res

div(2, 4, show=True)