# coding: utf-8
class Animal():
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def description(self):
        return self.get_description()
class Zebra(Animal):
    __h='zebra'
    def get_description(self):
        return '''
        Имя: {}
        Возраст: {}
        Кто я? -{}
        '''.format(self.name, self.age, self.__h)
class Dolphin(Animal):
    __h='dolphin'
    def get_description(self):
        return '''
        Имя: {}
        Возраст: {}
        Кто я? -{}
        '''.format(self.name, self.age, self.__h)
    
test1=Zebra('test1', 1)
print(test1.description())
test2=Dolphin('test2', 2)
print(test2.description())