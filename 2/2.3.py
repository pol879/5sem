#��� ��� � ������� �������� �� ��������, � �����, ��� ��������� �������  - ��� �������� ����� � �������� �������, ������, ��� ������� ��� ��� � ������� dict
##������� � ��������� �����
#d=eval(input())
#keys=list(d.keys())
#values=list(d.values())
#d_rev={a: b for a,b in zip(values,keys)}
#print(d_rev)

#������� � ���� �������, �� ������ ������� ������� d:
d=eval(input('������� ������� � ������� {key1:value1, key2:value2, ...}  '))
print({a:b for a,b in zip(list(d.values()), list(d.keys()))})