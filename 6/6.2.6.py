# coding: utf-8
from vector import Vector
N=int(input())
points=[]
for i in range(N):
    s=input()
    point=Vector(s)
    points.append(point)
perim=0
for i in points:
    for j in points:
        for k in points:
            v = i.perim_triangle(j,k)
            if v >= perim:
                perim = v 
print('Наибольший периметр:{}'.format(perim))