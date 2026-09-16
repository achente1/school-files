# program to ckeck the given number if positive and also ckec if it is a single digit, double digit and the triple digit 

number = int(input("enter the desired number : "))
if number > 0:
    print("it is a positive number. ")
    if number > 0 and number < 10:
        print(f'the number {number} is a single digit number.')
    elif number >= 10 and number < 100:
        print(f'the number {number} is a double digit number.')
    elif number >= 100 and number < 1000:
        print(f'the number {number} is a 3 digit number.')
    else:
        print(f'the number {number} is a multi digit number which has more than 3 digits.')

elif number < 0:
    print("it is a negative number. ")
    if number <= -1 and number > -10:
        print(f'the number {number} is a single digit number.')
    elif number <= -10 and number > -100:
        print(f'the number {number} is a double digit number.')
    elif number <= -100 and number > -1000:
        print(f'the number {number} is a 3 digit number.')
    else:
        print(f'the number {number} is a multi digit number which has more than 3 digits.')

else:
    print(f'the number is neither negative nor positive')