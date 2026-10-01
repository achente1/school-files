# Equilateral Triangle Pattern
rows = int(input("Enter number of rows for Equilateral Triangle: "))

for i in range(1, rows + 1):
    # Print leading spaces to center the stars
    for j in range(rows - i):
        print(" ", end="")

    # Print stars with a space after each
    for k in range(i):
        print("* ", end="")

    print()  # Move to the next line
