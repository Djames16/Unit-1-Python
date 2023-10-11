"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.

"""
from datetime import date
today = date.today()
print("Today's date:", today)
#

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
from datetime import date
da = today.strftime("%m/%d/%y")
print("Today's date:",da)
#
"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
from datetime import datetime

date_str1 = '02/28/2023'
date_str2 = '03/01/2023'
date_obj1 = datetime.strptime(date_str1, "%m/%d/%Y")
date_obj2 = datetime.strptime(date_str2, "%m/%d/%Y")
date_obj3=date_obj2-date_obj1
print(date_obj3)


#
"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
from datetime import datetime
User=input("Please input your birthday like %m/%d/%Y")

print(User)

        Add=input("Enter an item:")

        Todo.append(Add)

        print(Todo)
#