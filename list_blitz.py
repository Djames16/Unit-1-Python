"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
my_list = ["Ms.M", "Mr.F", "Ms.A" , "Ms.Ma"]
print(my_list) 
# I made a variable for the list. Then set it equal to 4 strings. Then printed the list.
"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
my_list.append("Mr.T")
print(my_list)
# I continued from the variable from the last exercise. I just added append to the variable then the value I wanted to add. Then I printed the list.
"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
my_list.remove("Mr.T")
print(my_list)
# I continued from the last exercise. I just used the variable but added remove and the variable I wanted to delete. Then I printed the list. 
"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
my_list[1] = "Ms.C"
print(my_list)
# I used the last variable. I added it's index number in brackets. Added a new value. Then printed the list.
"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
my_list.append( "Mr.T" )

my_list.append( "Mr.F" )

print( my_list )
# I used the last variable. I appended 2 new strings to the list. Then I printed the list.

"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
del my_list[0]

print(my_list)
# I used the last list. I just deletd the first variable using del then printed the list.

"""
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your "list
Then print out the new variable
"""

my_number=["one", "two", "three"]

print( my_number[0:2] )
#I made a new list then put 0 and 2 in the print to symbolize the position to print.

"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""
my_list1 = ["Mr.J", "Ms.Mi"]

my_list2 = ["Ms.P", "Mr.H"]

my_listings = my_list1 + my_list2

print(my_listings)
# I made 2 lists then added them using a plus and made a new variable for the sum to become then printed the result.
