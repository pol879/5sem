# coding: utf-8
#так как в задании подробно не написано, я думаю, что обращение словаря  - это поменять ключи и значения местами, считая, что словарь уже дан в формате dict
##решение в несколько строк
#d=eval(input())
#keys=list(d.keys())
#values=list(d.values())
#d_rev={a: b for a,b in zip(values,keys)}
#print(d_rev)

#РЕШЕНИЕ В ОДНУ СТРОЧКУ, не считая импорта словаря d:
d=eval(input('Введите словарь в формате {key1:value1, key2:value2, ...}  '))
print({a:b for a,b in zip(list(d.values()), list(d.keys()))})