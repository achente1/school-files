# WAP to search an element in the list and find it's index if there and send an appropriate message if not present
l = []
e = int(input("enter the number of elements: "))
for i in range(e):
    a = int(input("Enter an element: "))
    l.append(a)
f = int(input("Enter element to check if it's in list: "))
if f in l:
    print("yes in list, index is", l.index(f))
else:
    print("not in list.")
