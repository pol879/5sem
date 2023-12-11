def my_zip(a1,a2):
    i=0
    while i<len(a1):
        yield a1[i],a2[i]
        i+=1
        
def my_map(f, iterable):
    for i in iterable:
        yield f(iterable)
def my_enumerate(iterable, start=0):
    for el in iterable:
        yield start, el
        start+=1