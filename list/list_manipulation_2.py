# WAP to find the sum of odd and even numbers in a dynamically created list.
a = int(input("enter the number of elements in the list: "))
l = []
for i in range(a):
    e = int(input("enter the number of elements: "))
    l.append(e)
sum_even = 0
sum_odd = 0
for i in l:
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print("the sum of even numbers in the list is", sum_even)
print("The sum of odd numbers in the list is", sum_odd)
