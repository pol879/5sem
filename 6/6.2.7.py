# coding: utf-8
from vector import Vector
N=int(input())
points=[]
for i in range(N):
    s=input()
    point=Vector(s)
    points.append(point)
area=0
for i in points:
    for j in points:
        for k in points:
            v = i.area_triangle(j,k)
            if v >= area:
                area = v 
print('Наибольшая площадь:{}'.format(area))