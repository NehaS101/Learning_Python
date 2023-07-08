#OOP(object oriented programming)

#classes

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


#encapsulation

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
