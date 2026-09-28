# wap to find the sum of a sequence
number = int(input("enter a number: "))
power = int(input("enter the power: "))
sum = 0
while True:
    sum += number**power
    power -= 1
    if power < 0:
        break
print(f"the sum is {sum}")
