
def leap_year():
    year = int(input("Write a year : "))
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            print("{} is not a leap year".format(year))
        else:
            print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

            
leap_year()

