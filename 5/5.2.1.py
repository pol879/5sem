import math
class Shape():
    def __init__(self, base, height): #base - ширина, height - высота
        self.base=base
        self.height=height    
class Triangle(Shape):
    def area(self, full=False):
        if full:
            print('Площадь треугольника с шириной {}, высотой {}: '.format(self.base,self.height), self.base*self.height/2)
        return self.base*self.height/2
class Rectangle(Shape):
    def area(self, full=False):
        if full:
            print('Площадь прямоугольника с шириной {}, высотой {}: '.format(self.base, self.height), self.base*self.height)
        return self.base*self.height

#Testing
test1=Triangle(10,20)
test1.area(full=True)
test2=Rectangle(10,20)
test2.area(full=True)