# coding: utf-8
from vector import Vector
a=Vector(input())
b=Vector(input())
c=Vector(input())
print('Объем параллелепипеда:{}'.format(abs(a.triple_prod(b,c))))