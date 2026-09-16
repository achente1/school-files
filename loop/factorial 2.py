#factorial

a = int(input("Enter number : "))
s = 1
for i in range(1,a+1):
    s = i * s 
print(s)