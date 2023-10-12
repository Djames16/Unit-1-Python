# Task 1: Greeting Function
# Write a function `greet(name)` that takes a name as a parameter and prints a greeting message like "Hello, [name]!".
def my_greet(name):
    print("Hello," + name)
my_greet("DJ")
# I put a def and  function and a name in the function then printed hello and name then printed a name.

# Task 2: Sum of Two Numbers
# Write a function `sum_numbers(a, b)` that takes two numbers as parameters and returns their sum.
def my_sum(a,b):
    print(a + b)
my_sum(7, 14)
# I put a def and function and 2 variables in the function then printed the 2 variables when they are added then printed the 2 variables I want to be added.

# Task 3: Calculate Factorial
# Write a function `factorial(n)` that calculates the factorial of a given number `n`.

def fact(n):
    fact = 1
    for f in range(1, n + 1):
        fact = fact * f
    print("Factorial of",n,"is",fact)
fact(3)
# Task 4: Check Even or Odd
# Write a function `is_even(num)` that takes a number as a parameter and returns `True` if the number is even, and `False` otherwise.


# Task 5: Calculate Area of a Rectangle
# Write a function `calculate_area(length, width)` that calculates and returns the area of a rectangle given its length and width.