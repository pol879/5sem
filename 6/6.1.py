class Complex:
    def __init__(self, x, y):
        self.Re=x
        self.Im=y
    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Complex(self.x - other.x, self.y - other.y)
    def __neg__(self):
        return Complex(-self.x, -self.y) 
    def __mul__(self, num):
        '''complex number and real number'''
        return Complex(self.x*other, self.y*other)
    def __matmul__(self, other):
        ''' 2 complex numbers'''
        return Complex(self.x*other.x - self.y*other.y, self.x*other.y+self.y*other.x)
    def conj(self):
        ''' complex conjugate'''
        return Complex(self.x, -self.y)
    def __abs__(self):
        return (self.x**2+self.y**2)**0.5 
    def __truediv__(self, other):
        '''2 complex numbers'''
        return Complex((self@other).Re/abs(other)**2, (self@other).Im/abs(other)**2)
    def __str__(self):
        return '({}+{}i)'.format(self.Re, self.Im)
    def __repr__(self):
        return '({}+{}i)'.format(self.Re, self.Im)
    
#Testing
a=complex(-1,1)
print(a)
b=Complex(-1,1)
print(b)
    