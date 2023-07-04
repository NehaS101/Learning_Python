'''
Exercise 1:
Write a program that checks if a number is prime. 
Prompt the user to enter a number, and then display whether it is prime or not. 
A prime number is a number greater than 1 that has no divisors other than 1 and itself.
'''
import math
def check(num):
    if num<2:
        return False
    prime=True
    for i in range(2,int(math.sqrt(num))+1) :
        if num%i==0:
            prime=False
            break
    return prime

output=check(5)
if output==True:
    print("Number is prime")
else:
    print("Number is not prime")


'''
Exercise 2:
Write a program that calculates the factorial of a given number. 
Prompt the user to enter a positive integer, and then display its factorial. 
The factorial of a number is the product of all positive integers less than or equal to that number.
'''