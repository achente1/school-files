n = int(input("Enter number : "))
s = 0
for i in range(1,n+1,2):
    if n%2==0:
        s = s+i
print(s)