#Task 1
sales = dict(cost_price = 31.87, sell_price = 45.00, inventory = 1000 )

total_profit = (sales["sell_price"] - sales["cost_price"])*sales["inventory"]

print(round(total_profit))

#Task 2

given_amt = input("please write amount =")

print("$ %.2f" % (float(given_amt)))