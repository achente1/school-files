# WAP to remove all odd numbers from a dynamically created list.
l = []
e = int(input("enter the number of elements: "))
for i in range(e):
    a = int(input("Enter an element: "))
    l.append(a)
for i in l:
    if i % 2 == 0:
        continue
    else:
        l.remove(i)
print("the new list is", l)
