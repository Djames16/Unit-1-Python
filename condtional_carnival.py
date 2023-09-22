
#TASK 1 Even or Odd
#Determine if a number is even or odd.

number=int(input("Enter a number to see whether or not it is even or odd"))
moderation= number % 2
if moderation > 0:
    print("This is an odd number")
else:
    print("This is an even number")
# I made a variable for the user to input either even or odd. Then put a if and else statement if the number would be even or odd.
#TASK 2 Positive, Negative, or Zero:
#Determine if a number is positive, negative, or zero.



#EXTRA CREDIT: Tell the user if they did not enter a valid number

number=float(input("Enter a number to see whether or not it is positive, negative or zero"))
if number > 0:
    print("This is a postive number")
elif number==0:
    print("Zero")
else:
    print("This is a negative number")
#I made a variable for the user to input either postive, negative or zero. Then put a if, elif and else statement if the number would be postive, negative or zero result.

#TASK 3: Largest of Three
#Find and print the largest of three numbers.

number1=float(input("Enter the first of three numbers"))
number2=float(input("Enter the second of three numbers"))
number3=float(input("Enter the third of three numbers"))

if (number1>=number2) and (number1>=number3):
    largest=number1
elif (number2>=number1) and (number2>=number3):
    largest=number2
else:
    largest = number3
print("The largest number is", largest)
#I made a variable for the user to input 3 numbers to determine the largest number. Then put a if, elif and else statement to determine the largest number.
'''
TASK 4: Leap Year
Determine if a year is a leap year or not.
'''
Leap=int(input("Enter a Year:"))
if (Leap % 400 == 0) and (Leap % 100 ==0):
    print("{0} is a leap year".format(Leap))

elif(Leap % 4 ==0) and (Leap % 100 !=0):
    print("{0} is a leap year".format(Leap))

else:
    print("{0} is not a leap year".format(Leap))


#I made a variable for the user to input a year  to determine the leap year. Then put a if, elif and else statement to determine if it is a leap year.
#TASK 5: Vowel or Consonant:
#Identify if a character is a vowel or consonant.

def vowelOrConsonant(x):
  
    if (x == 'a' or x == 'e' or
        x == 'i' or x == 'o' or x == 'u'):
        print("Vowel")
    else:
        print("Consonant")
  
vowelOrConsonant('a')
vowelOrConsonant('f')
      
#EXTRA CREDIT: Tell the user if they did not enter a valid letter
