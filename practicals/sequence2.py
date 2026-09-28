# wap to find the sum of a sequence whose even terms are only added

number = int(input("enter a number: "))
power = int(input("enter a power:  "))
negative_sum = 0
positive_sum = 0
total_sum = 0
while True:
    if power % 2 == 0:
        positive_sum += number**power
    else:
        negative_sum += number**power
    power -= 1
    if power < 0:
        break
print(f"the sum is {positive_sum - negative_sum}")
