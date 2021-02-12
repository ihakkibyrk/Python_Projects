age = int(input("Please enter your age : "))

chronic = input("Do you have a severe chronic disease, (Y / N): ").upper()

immune = input("Is your immune system too weak? (Y / N): ").upper()

if age > 75 and chronic == "Y" and immune == "Y":
    print("You are in risky group")
else:
    print("You are not in risky group")