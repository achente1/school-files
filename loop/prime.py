# program to find if the number is prime or not

is_prime = True
n = int(input("Enter a number:"))
if n == 1 or n == 0:
    print("Not a prime number")
elif n < 0:
    print("Please put a whole number")
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")
