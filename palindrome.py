# Is a palindrome

def check():
    word = input("Write a word : ")

    if word.casefold() == word[::-1].casefold():
        print("It is a palindrome")
        print("\n")
        check()
    else:
        print("It is not a palindrome")
        print("\n")
        check()

check()

