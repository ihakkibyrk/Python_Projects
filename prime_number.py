n = int(input("Please write a number : "))

prime_list = []

for number in range(2,n):
    
    if n == 1:
        print("Please write a number bigger than 1")

    elif n > 1:
        if number == 2 or number == 3 or number == 5:
            prime_list.append(number)
        elif number % 2 != 0:
            prime_list.append(number)
            
for i in range(2,n):
    for a in prime_list:
        if a % i == 0 and i != a:
            prime_list.remove(a)

        
                   
print(prime_list)
