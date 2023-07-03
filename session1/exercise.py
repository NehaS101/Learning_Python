'''
Write a program that prompts the user for their name, age, and favorite color.
Then, display the collected information in the following format:

Your name is {name}, you are {age} years old, and your favorite color is {color}.

Make sure to handle any potential errors, such as invalid input or empty input.
'''
try: 

  name = input('Enter your name : ')
  age = int(input('Enter your age : '))
  color = input('Enter your favorite color : ')
  print(f"Your name is {name}, you are {age} years old, and your favorite color is {color}")
except ValueError:
  print("Invalid input")


'''
Write a program that prompts the user to enter two numbers and displays the sum, difference, product, 
and quotient of those numbers. Make sure to handle any potential errors,
such as if the user enters invalid data or tries to divide by zero.
'''  


try:
    num1 = int(input("enter first number : "))
    num2 = int(input("enter second number :"))
    
    sum = num1+num2
    diff = num1-num2
    prod = num1*num2
    
    if num2!=0:
       quotient = num1/num2
       print(f"sum = {sum}, difference = {diff}, product = {prod}, quotient = {quotient}")
    else:
       print("you are trying to divide by zero")   
    
except ValueError:
    print("invalid input")