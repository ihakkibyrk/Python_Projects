# What is my acronym?

word = input(":").title()

a = list(word.split())

b = []
for i in a:
    b.append(i[0])
    acronym = "".join(b)

    

print(acronym)