class Human():
    def __str__(self):
        return self.description()
class Mother(Human):
    def description(self):
        return 'True'
class Daughter(Mother):
    def description(self):
        return 'Hello!'
    
m=Mother()
print(m)
d=Daughter()
print(d)