# Fibonacci Sequence Calculator
terms = int(input("How many Fibonacci terms to display? "))

# Initial two numbers of the sequence
a = 0
b = 1

count = 0

if terms <= 0:
    print("Please enter a positive integer.")
elif terms == 1:
    print("Fibonacci sequence:")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < terms:
        print(a, end=" ")
        # Calculate next term by swapping variables
        next_term = a + b
        a = b
        b = next_term
        count += 1
    print()  # New line at the end
