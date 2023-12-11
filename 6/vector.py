class Vector:
    def __init__(self, s):
        self.x, self.y, self.z=tuple(map(float, s.split(',')))
    def __str__(self):
        return '({},{},{})'.format(self.x, self.y, self.z)
    def __repr__(self):
        return '({},{},{})'.format(self.x, self.y, self.z)
    def __add__(self, other):
        return Vector('{},{},{}'.format(self.x + other.x, self.y + other.y, self.z+other.z))
    def __sub__(self, other):
        return Vector('{},{},{}'.format(self.x - other.x, self.y - other.y,self.z-other.z))
    def __neg__(self):
        return Vector('{},{},{}'.format(-self.x, -self.y, -self.z)) 
    def __mul__(self, other):
        '''Vector and real number'''
        return Vector('{},{},{}'.format(self.x*other, self.y*other, self.z*other))
    def __matmul__(self, other):
        ''' 2 Vectors -- scalar product in orthonormal basis'''
        return Vector('{},{},{}'.format(self.x*other.x, self.y*other.y, self.z*other.z))
    def __abs__(self):
        return (self.x**2+self.y**2+self.z**2)**0.5 
##Testing
#a=Vector('1,1,1')
#b=Vector('0,4,5')

#print(a@b)
#print(a+b)