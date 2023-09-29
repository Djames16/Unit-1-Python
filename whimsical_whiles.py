"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
i=1
while i < 11:
  print(i)
  i += 1
#I made a variable and set it equal to 1.I made a while and set the variable i less than 11. Then printed the variable. Lastly made the variable add 1 after every iteration.
"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
i=10
while i > 0:
  print(i)
  i -= 1
#I made a variable and set it equal to 10. I made a while and set the variable i greater than 0. Then printed the variable. Lastly made the variable subtract 1 after every iteration.
"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
num=int(input("Enter a number:"))
Product= 1
while num > 0:
  Product *=num
  num -= 1
  print(Product)
  #A variable for the user to input a number is created. I made a variable and set it equal to 1. I made a while and set the input num greater than 0. Put the product and the num to multiply by each other. Lastly made the variable subtract 1 after every iteration. Then printed the product variable.
"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""

Pass ='Mango'
ans= input("Guess any password:")
while ans != Pass:
  print("Try again")
  ans= input("Guess any password:")
else:
 print("Mango is indeed the password. Good job!")

"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""
sum = 0
numb = 1
while numb > 0:
   numb = int(input('Enter a number:'))
   if numb>0:
    sum=sum+numb
   print("This is", sum)
  elif numb == 0:
       print("The end")
      break

"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""