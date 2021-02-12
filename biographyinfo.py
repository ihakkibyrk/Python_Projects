# Biography Info

from datetime import date

def date_birth():
    a = int(input("year = "))
    b = int(input("month = "))
    c = int(input("day = "))
    print("- Date of birth: ", date(a, b, c))

name = input("What is your name? ")
date_birth()
address = input("What is your address? ")
person_goal = input("What is your personal gaol? ")

if (name.replace(" ", "")).isalnum():

    print("- Name: ", name)
else:
    print("Please write a valid name")
    name = input("What is your name? ")

if (address.replace(" ", "")).isalnum():
    print("- Address: ", address)
else:
    print("Please write a valid address")
    address = input("What is your address? ")

if (person_goal.replace(" ", "")).isalnum():
    print("- Personal goals: ", person_goal)
else:
    print("Please write a valid input")
    person_goal = input("What is your personal goal? ")


