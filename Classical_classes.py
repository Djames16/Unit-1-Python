"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.
Create a new object using this new class, and call the method you created.
"""
class Person:
    species='human'

    def __init__ (self, name, age):
       self.name=name
       self.age=age

    def hello(self):
       print("Hi my name is " + self.name + " I am " + str(self.age))

Daeon = Person("Daeon", 17)
Daeon.hello()
# I made a class with person and put every that stays consistent in the attribute and everything that varies in the init which assigns variables which would be the name and ages then set them equal to a self.Then I set a method so that I can print the name and age. I then put the values for the class person/values for name and age. Then I printed the statement with my name and age.
"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
class Animal:
    def speak(self):
        print("")
class Cat:
    role="pet"
    def speak(self):
        print("Meow")
Cat="Lazy"
class Dog:
    role="pet"
    def speak(self):
        print("Ruff")
Dog="Energetic"

# I made a class with animal and put self in speak so I can access variables at anytime in the attribute and everything that varies in the Cat class so that I can identify what it is which is a pet then a speak and self to identify that it meows then I added it was lazy.Then printed the meow.I did the same for dog everything that varies in the dog class so that I can identify what it is which is a pet then a speak and self to identify that it ruffs then I added it was energetic.Then printed the ruff.
"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""
class Account:
    def __init__(self,balance,holder):
        self.balance=balance
        self.holder=holder
def balance(self):
    print("Your current balance is",self.balance)
def depositing(self,deposit):
    self.balance=self.balance+deposit
    print("Your new balance is", self.balance)
def withdrawing(self,withdraw):
    self.balance=self.balance-withdraw
    print("Your new balance is", self.balance)
Owner=Account(50,"Owner")
Owner.balance()
Owner.deposit(50)
Owner.withdraw(25)
# I made a class with Account and put init so I can assign variables which would be the balance and holder then set them equal to a self.Then I set the 3 methods of depositing,withdrawing, and balance then used either subtraction or addition on the balance to represent a deposit or withdrawl. I then put the values for the class person/values for name and age. Then I printed the statement with my name and age. Then put all the values for these transactions.