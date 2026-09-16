# python program to calcuate profit and loss

actual_cost = float(input("Please enter the actual product size (positive): "))
sale_amount = float(input("Please enter the sale amount (positive) : "))

if (actual_cost > sale_amount):
    amount = actual_cost - sale_amount
    print(f'the toal loss amount is {amount}')
elif (sale_amount < actual_cost):
    amount = sale_amount - actual_cost
    print(f'the total profit amount is {amount}')
else: 
    print("no profit no loss !!!")