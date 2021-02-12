from random import choice

def guess_num():
    # numbers = list(range(1, 51))
    guess = int(input("Guess the number: "))
    computer = 12 #  int(choice(numbers))

    if guess in range(1, 51):
        if guess == computer:

            print("Congratulations!")
            print("\n")
            guess_num()
        else:
            answer = input("Would like to guess more? Yes/No : ")
            if answer.upper() == "YES":
                guess_num()
            else:
                print("Thanks for playing!")
    else:
        print("Enter a valid number between 1 and 50")
        print("\n")
        guess_num()

guess_num()




