#Hnadling exceptions

try:
    result=2/0
except ZeroDivisionError:
    print("can't divide by zero")    

#Handling mutiple exceptions

try:
    res=int("str")
except ValueError:
    print("invalid value")
except ZeroDivisionError:
    print("can't divide by zero")        

#Raising custom exceptions

def validate_age(age):
    if age<0:
        raise ValueError("age can't be negative")
    elif age>100:
        raise ValueError("age is too high")
    
try:
    age=110
    validate_age(age)
except ValueError as e: 
    print(e) 

#"finally" block

try:
    file=open("data.txt","r")
    content= file.read()
    print(content)
except FileNotFoundError:
    print("File not found")
finally:
    file.close()                  