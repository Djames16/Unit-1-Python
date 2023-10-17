try:
    age = int(input('Enter your age: '))
    if age <= 21:
        print('You are not allowed to enter, you are too young.')
    else:
        print('Welcome, you are old enough.')
except: 
 print("Age is not correct")

faveNum = int(input('What is your favorite number: '))

try:
 print("Fun Fact! Your age divided by your favorite number is: " , age / faveNum)
except:
  print(" Division is not applicable")

#I put the age and if statement within a try and excpet so that the error in for not putting a valid number would print that it is wrong. Then put another try so that when dividing by 0 it cant be applicable