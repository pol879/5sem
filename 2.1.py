import sys
a=[]
mean=0
qmean=0
s=input()
try:
    s=float(s)
    a.append(s)
    mean+=s
    qmean+=s**2
except ValueError:
    print('Give at least one number')
    sys.exit()
f=True
while f:
    s=input()
    try:
        s=float(s)
        a.append(s)
        mean+=s
        qmean+=s**2        
    except ValueError:
        if s=='End':
            f=False        
        else:
            print('Print \'End\' when finish giving numbers')
            sys.exit()

# implementation of quick sort in python (hoare partition scheme) - using code from previous semester

def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)
        
def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start+=1

        while elements[end] > pivot:
            end-=1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end

mean/=len(a)
qmean/=len(a)

quick_sort(a,0,len(a)-1)
print('max =', a[-1], '\n',
      'min =', a[0], '\n',
      'mean =', mean, '\n',
      'quadratic_mean =', (qmean - mean**2)**0.5)
print('Compare results with numpy below')
#check
import numpy as np
p=np.array(a)
print('max =', np.max(a), '\n',
      'min =', np.min(a), '\n',
      'mean =', np.mean(a), '\n',
      'quadratic_mean =', np.std(a))