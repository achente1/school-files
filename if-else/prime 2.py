is_prime = True 
a = int(input("enter number : "))
i=0
if a == 1 or a == 0:
    print("not prime")
    pass

else: 
    for i in range(2,a):
        if a % i == 0:
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime:
        print("prime")
    else:
        print("not prime")
