number = str(input("Please write a numeric number : "))

sum_num = 0

if number.isdecimal():
    
    if type(float(number)) == type(1.2):
        for x in range(len(number)):
            sum_num += int(number[x])**len(number)
        if sum_num == int(number):
            print(number, 'is an Armstrong number')
        else:
            print(number, 'is not an Armstrong number')
   
else:
    print(number,'it is an invalid entry. Don\'t use non-numeric, float, or negative values!')







