"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
for x in range(1,11,1):
    print(x)
# Put x in range then 1 so it starts at 1 then 11 so it stops at 10 and 1 so it goes up by 1 every time.
"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
for x in range(900,1001,10):
    print(x)
# Put x in range then 900 so it starts at 900 then 1001 so it stops at 1000 and 10 so it goes up by 10 every time.
"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
for x in range(1,101,9):
    print(x)
# Put x in range then 1 so it starts at 1 then 101 so it stops at 100 and 9 so it goes up by 9 every time.
"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
L = 0
for num in range(1,11,1):
  L += num
  print(L)
# I set a variable equal to 0. Then put a for loop for num then put it in the variable. Then put a range so it starts at 1, ends at 11 and increases by 1. Made the variable equal to 0 then added it and set it equal to num. Then printed L.
"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output

"""

rows = 5 
for i in range(rows):
    for j in range(i + 1):
          print('*', end=' ')
    print()
#First the code calls for 5 rows of code. Then it increases by one every time because of the i+1. Then prints the * for the 5 rows increasing by one in each row.