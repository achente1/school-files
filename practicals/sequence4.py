# wap to find the sum of the sequence given including the factorial
number = int(input("enter the number:  "))
power = int(input("enter the power: "))
sum = 0
product = 0
factorial = 1
for i in range(1, power + 1):
    factorial *= i
    sum = number**i / factorial
print(f"sum of the series is {sum}")
