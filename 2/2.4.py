x=1
a=[]
while x<2500:
    sx=x**2
    if str(sx)[-1]=='1':
        a.append(sx)
    x+=1
print(*a)