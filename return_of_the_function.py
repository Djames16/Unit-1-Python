"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
def sq_num(a):
    return a**2
x=sq_num(7)
print(x)
# I put a define of a then return a to the second power then set x equal to 7 then printed the result of 7 squared.

assert sq_num(7)==49
assert sq_num(6)==36
# I put an assert to check to see if the code is right then since it is squaring of 7 and 6. I set it equal to the result. Then the code continued on.
"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""
def area_num(a,b):
    return a*b
x=area_num(7,9)
print(x)
# I put a define of a and b then return a times b then set x equal to 7 and 9 then printed the result of 7 and 9.
assert area_num(7,9)==63
assert area_num(9,9)==81
# I put an assert to check to see if the code is right then since we are finding the are of 7, 9 and 9,9. I set it equal to the result. Then the code continued on.
"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
def temp_num(a):
    return(1.8 * a) + 32
x=temp_num(40)
print(x)
# I put a define of a then return a times 1.8 and added 32 to the result to find fahrenheit then set x equal to 40 then printed the result of the return to convert it to fahrenheit.\
assert temp_num (40)==104.0
assert temp_num (45)==113.0
#I put an assert to check to see if the code is right then since we are multiplying of 40 and 45 to 1.8 and adding 32. I set it equal to the result. Then the code continued on.
"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""
def avg_num(a):
    tot=sum(a)
    return tot/len(a)
a=avg_num([1, 2, 3, 4, 5])
print(a)

assert avg_num ([1, 2, 3, 4, 5])==3.0
assert avg_num ([1, 2, 3, 4, 6])==3.2
#I put an assert to check to see if the code is right then since it is a lisyt a put 2 different lists one including 6 and another including 5 then found the mean.I set it equal to the result. Then the code continued on.