

def tip_total():
    total_bill = float(input("What is the total bill for today, please?"))
    inv_person = int(input("please write the number of people involved"))
    vat_rate = int(input("please write the tip rate"))
    tip = total_bill*(100/vat_rate)
    total = round(total_bill + tip)
    print(f"%{vat_rate} tip is ${tip}, which bringss your total to ${total}, it is also per person {total//inv_person} ")


tip_total()
