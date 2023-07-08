#OOP(object oriented programming)

#classes
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"my name is {self.name} and my age is {self.age}")

#creating objects
person1 = Person("neha",19)        

#calling methods
person1.greet()