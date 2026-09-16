# program to print prime numbers till a limit
n = int(input("Enter a limit that is a positive integer: "))
prime = True
for i in range(2, n+1):
    if i % 2 == 0:
        prime = False
        pass
    else:
        print(i, end=' ')
        pass

# program to be on list for completion, need to check logic and etc.
