# program to find the discount 20 % if the amount > 3000, discount 10% if the amount is between 1000 and 3000 and the discount otherwise if it is less than 1000

price = float(input("enter the price of the item: "))
quantity = float(input("enter the quantity: "))
amount = price*quantity
print(f"the purchased amount is {amount}")
if amount > 3000 : 
    discount = amount * 20 / 100
    print(f"the discount is {discount}")
elif amount > 1000 and amount <= 3000:
    discount = amount * 10 / 100
    print(f"the discount is {discount}")
else: 
    discount = amount * 5 / 100 
    print(f"the discount is {discount}")
