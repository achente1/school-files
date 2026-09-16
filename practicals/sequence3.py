# wap to find the sum of sequence along with having a base 

number = int(input("enter a number: "))
power = int(input("enter a power: ")) 
sum = 0
while True:
    sum += (number**power)/power 
    power -= 1
    if power <= 0:
        break
print(f"the sum is {sum}")
