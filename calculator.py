number1=float(input("Enter a number "))
number2=float(input("Enter another number "))

print("Select an operation")
print("Addition")
print("Subtraction")
print("Multiplication")
print("Division")
print("Floor Division")
print("Exponential")
print("Remainder")

operation = input("Enter an operation ")

if operation == 'Addition':
    print(number1+number2)
elif operation == 'Subtraction':
    print(number1-number2)
elif operation == 'Multiplication':
    print(number1*number2)
elif operation == 'Division':
    print(number1/number2)
elif operation == 'Floor Division':
    print(number1//number2)
elif operation == 'Exponential':
    print(number1**number2)
elif operation == 'Remainder':
    print(number1%number2)
else:
    print("This is an invalid input try again")

#I put 2 variables for the user to imput 2 different numbers. Then listed out every operation. I gave the user a chance to select a operation. Then user selects a operation that gives a output based on the selction. If anything else is printed it would be told to start over. 