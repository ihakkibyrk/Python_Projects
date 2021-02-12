
from random import choice

def rock_paper_scissors():

    items = ["Rock", "Paper", "Scissors"]

    selection = input("Please choose Rock, Paper or Scissors : ")

    computer = choice(items)

    if selection.capitalize() == "Rock" and computer.capitalize() == "Rock":
        print("It is a tie")
        print("Do you want to play again?: (Y/N) ")
        answer = input(": ")
        if answer.upper() == "Y": 
            rock_paper_scissors()
        else:
            print("Thanks for playing with us!")
    elif selection.capitalize() == "Paper" and computer.capitalize() == "Paper":
        print("It is a tie")
        print("Do you want to play again?: (Y/N) ")
        answer = input(": ")
        if answer.upper() == "Y": 
            rock_paper_scissors()
        else:
            print("Thanks for playing with us!")
    elif selection.capitalize() == "Scissors" and computer.capitalize() == "Scissors":
        print("It is a tie")
        print("Do you want to play again?: (Y/N) ")
        answer = input(": ")
        if answer.upper() == "Y": 
            rock_paper_scissors()
        else:
            print("Thanks for playing with us!")
    elif selection.capitalize() == "Rock" and computer.capitalize() == "Paper":
        print("Computer is the winner!")
        print("Do you want to play again?: (Y/N) ")
        answer = input(": ")
        if answer.upper() == "Y": 
            rock_paper_scissors()
        else:
            print("Thanks for playing with us!")
    elif selection.capitalize() == "Rock" and computer.capitalize() == "Scissors":
        print("User is the winner!")
        print("Do you want to play again?: (Y/N) ")
        answer = input(": ")
        if answer.upper() == "Y": 
            rock_paper_scissors()
        else:
            print("Thanks for playing with us!")
    elif selection.capitalize() == "Paper" and computer.capitalize() == "Rock":
        print("User is the winner!")
        print("Do you want to play again?: (Y/N) ")
        answer = input(": ")
        if answer.upper() == "Y": 
            rock_paper_scissors()
        else:
            print("Thanks for playing with us!")
    elif selection.capitalize() == "Paper" and computer.capitalize() == "Scissors":
        print("Computer is the winner!")
        print("Do you want to play again?: (Y/N) ")
        answer = input(": ")
        if answer.upper() == "Y": 
            rock_paper_scissors()
        else:
            print("Thanks for playing with us!")
    elif selection.capitalize() == "Scissors" and computer.capitalize() == "Rock":
        print("Computer is the winner!")
        print("Do you want to play again?: (Y/N) ")
        answer = input(": ")
        if answer.upper() == "Y": 
            rock_paper_scissors()
        else:
            print("Thanks for playing with us!")
    elif selection.capitalize() == "Scissors" and computer.capitalize() == "Paper":
        print("User is the winner!")
        print("Do you want to play again?: (Y/N) ")
        answer = input(": ")
        if answer.upper() == "Y": 
            rock_paper_scissors()
        else:
            print("Thanks for playing with us!")
    else:
        print("Opps, something is wrong!")
        
rock_paper_scissors()