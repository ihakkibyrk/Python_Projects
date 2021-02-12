# Odd or Even

def check():
    number = input()
    if number.isnumeric():
        if int(number) % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")
    else:
        check()

check()



