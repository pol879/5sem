#�������, ��� ������ ����� �������� � ���� ������ ����� ������


def answ(f):
    '''decorator'''
    def wrapper():
        res = f()
        if res ==0:
            print('���(')
        elif res > 10:
            print('����� �����')
        else:
            print(res)
    return wrapper

@answ            
def count_even():
    '''������� ��� �������� ������ ����� � ��������� ������ '''
    a=list(map(int, input().split()))
    counter = 0
    for num in a:
        if num%2==0:
            counter+=1
    return counter

count_even()

    