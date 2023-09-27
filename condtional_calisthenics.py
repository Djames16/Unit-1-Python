'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''

number = int(input("Enter a number:"))

if number>10 and number%2==0:
    print("True")
else:
    print("False")

#A variable for the user to input a number is created. Then that is variable must be set higher than 10 and remainder %2 equal to 0. Then print true or false depending on the input.
'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
student = int(input("Enter your age: "))
if student < 18:
    print("You must pay $10 to enter for a ticket")
else:
    print("You must pay $20 to enter for a ticket")

#A variable for the user to input their age is created. Then that is variable must be set less than 18. Then print their ticket price depending on the input.
'''

Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''



fruit = (input("Enter the fruit:"))
fruits = ["apple", "banana","orange","banana","Mango","Coconut"]


if fruit in fruits:
	print("Yes, that fruit is in the list.")
else
     print("No, that fruit is not in the list.")


#I made 2 variables. 1 to represent the list another to represent the user input then if the input is in the list then yes or no will print 
'''
Exercise 4:
Check if a year is a century year and a leap year.
'''
year=input("Enter a year: ")
if int(year)
'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.