text = input("Please write a sentence/text : " )

count_letter = dict()

for i in text:
    if i in count_letter.keys():
        count_letter[i] += 1
    else:
        count_letter[i] = 1

print(count_letter) 