# Author: John Asare
# Date: 09/4/2018

""" Creating a code to ask the user for their age"""

user = input("What is your name: ")
print("Hello %s" % user)

age = int(input("what is your age?: "))
question = input("Have you had a birthday this year?: ")

if question == "no":
    age = age - 1

x = 2018 - age

print("You were born in %d" % x)





