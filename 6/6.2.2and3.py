# coding: utf-8
from vector import Vector
N=int(input())
points=[]
dist_from_zero=[] #will contain distances from zero to points
for i in range(N):
    s=input()
    point=Vector(s)
    points.append(point)
    dist_from_zero.append(abs(point))
    
distances=dict(zip(points, dist_from_zero))
sorted_dict= dict(sorted(distances.items(), key=lambda item: item[1]))
print('Наиболее удаленная точка:{}'.format(list(sorted_dict.keys())[-1]))

# так как массы точек не даны, будем считать, что массы всех точек одинаковы при подсчете центра масс
wh=Vector('0,0,0')
for i in range(N):
    wh+=points[i]
print('Координаты центра масс:{}'.format(wh*(1/N)))

