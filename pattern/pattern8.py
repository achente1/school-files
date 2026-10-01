# Hollow Diamond Pattern
n = int(input("Enter row size for top half of Diamond (e.g., 5): "))

# 1. Top half of the hollow diamond
for i in range(1, n + 1):
    # Print leading spaces
    for j in range(n - i):
        print(" ", end="")

    # Print stars and inner spaces
    for k in range(1, 2 * i):
        if k == 1 or k == (2 * i - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()

# 2. Bottom half of the hollow diamond
for i in range(n - 1, 0, -1):
    # Print leading spaces
    for j in range(n - i):
        print(" ", end="")

    # Print stars and inner spaces
    for k in range(1, 2 * i):
        if k == 1 or k == (2 * i - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()
