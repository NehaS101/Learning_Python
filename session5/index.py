#OOP(object oriented programming)

#_______classes_______#

#class definition
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


#_______encapsulation_______#

#class constructor
class BankAccount:
    def __init__(self,AcNo,Bal):
        self.AcNo=AcNo
        self.Bal=Bal

    def deposit(self,amount):  
        self.Bal += amount

    def withdraw(self,amount):
        if self.Bal >= amount:
            self.Bal -= amount
        else:
            print("Insufficient funds to withdraw")

    def getBalance(self):
        print(self.Bal)

#creating objects instance
account=BankAccount("1234",2000) 

#calling methods
account.deposit(500)
account.withdraw(300)
account.getBalance()


#_______Inheritance_______#

# Parent class
class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print("generic sound")    

# Child class
class Dog(Animal):
    def speak(self):
        print("woof")    

animal = Animal("generic animal")
dog = Dog("Buddy")

print(animal.name)
print(dog.name)
dog.speak()