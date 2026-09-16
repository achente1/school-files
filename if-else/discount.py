# python program to give a discount to customer

amount = int(input("Enter the purchase amount "))
membership_holder = input("Do you have a membership card ? y or N")
if (amount > 5000) and (membership_holder == 'y' or 'Y'):
    discount = amount * 50 / 100
    print(f'You get a discount of {discount} rupees ')
elif (amount > 5000) and (membership_holder == 'N' or 'n'):
    discount = amount * 25 / 100
    print(f'You get a discount of {discount} rupees ')
else:
    discount = amount * 5 / 100
    print(f'You get a discount of {discount} rupees ')
