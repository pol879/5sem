import sys
import argparse

  
def fibonacci(n):
    ''' returns nth Fibonacci number, sequence starts from 1, i.e. 1,1,2,3,5,...'''
    if n<=0:
        print('only positive integers accepted')
        sys.exit()
    if n==1 or n==2:
        return 1
    else:
        a=1
        b=1
        curr_val =b
        curr_n=3
        while curr_n<=n:
            curr_val=a+b
            a=b
            b=curr_val
            curr_n+=1
        return curr_val
    
parser=argparse.ArgumentParser(description='Calculate nth number in Fibonacci sequence')
parser.add_argument('name', nargs='?', type=int, default=-1, help='Number in Fibonacci sequence')
parser.add_argument('-n', type=int, help='Number in Fibonacci sequence')

args=parser.parse_args()

if args.name>0:    
    print(fibonacci(args.name))
else:
    print(fibonacci(args.n))
    
    
#пример вызова программы есть в прикрепленном фото