# WAP to find the min, max and sum of elements in the list
l = []
e = int(input("enter the number of elements: "))
for i in range(e):
    a = int(input("Enter an element: "))
    l.append(a)
print("the smallest element in the list is", min(l))
print("the largest element in the list is", max(l))
print("the sum of element in the list is", sum(l))
