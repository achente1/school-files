# wap to make a armstrong number calculator and also a perfect number calculator

number = int(input("Enter a number: "))
sum = 0
# perfect number calculator
for i in range(1, number):
    if number % i == 0:
        sum += i 
print(sum)

# armstrong number calculator
arm = 0
digit = 0
while number > 0:
    digit = number % 10
    print(arm,digit)
    arm += digit ** 3
    number //= 10
print(arm)