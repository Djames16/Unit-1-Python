"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.

"""
from datetime import date
today = date.today()
print("Today's date:", today)
# First I put from datetime import date so that I can recieve the date. Set a variable today equal to date.today so that I can get todays dates. Then printed Todays date.

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
from datetime import date
da = today.strftime("%m/%d/%y")
print("Today's date:",da)
# First I put from datetime import date so that I can recieve the date. Set a variable today equal to today.strftime so that I can get todays dates in / / format. Then printed Todays date.
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


#First I put from datetime import date so that I can recieve the date. Set 2 variables equal to 2 dates and time in / / format. Then subtracted the 2 dates then set it equal to a new variable then printed the difference date.
"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""