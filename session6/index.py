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

    