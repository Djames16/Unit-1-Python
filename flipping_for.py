"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""

animals = ["Tiger", "Lion", "Cheetah"]
for x in animals:
  print(x)
# I first made a list with the variable animals and put 3 different animals in the list. Then put a for loop for x then put it in the  variable then printed x.
"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
Number = [7,14]
L = 0
for num in Number :
  L += num
  print(L)
  # I first made 2 different numbers in brackets in a variable. Then set a variable equal to 0. Then put a for loop for num then put it in the variable. Made the variable equal to 0 then added it and set it equal to num. Then printed L.
"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
Biden='He is the president'
Biden=Biden.split(" ")
for p in Biden:
  print(p)
  print(len(p))
  
"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""
random = {
  'eat': 4,
  'beat': 3,
  'treat': 5,
  'feet': 9
}
for r in random:
  print(random)