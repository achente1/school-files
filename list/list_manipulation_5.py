# making menu driven program for list methods.
l1 = []

while True:
    print("menu\n")
    print("1. create new list")
    print("2. delete list")
    print("3. display new list")
    print("4. search an element in the list")
    print("5. sort a list")
    print("0. quit\n")

    d = int(input("Enter the option in the menu given: "))

    if d == 1:
        q = int(
            input(
                "do you want to add elements, 1 for yes, other number for no elements: "
            )
        )
        if q == 1:
            a = int(input("enter the number of elements in the list: "))
            l1 = []
            for i in range(a):
                e = int(input("enter the number of elements: "))
                l1.append(e)
        else:
            continue

    elif d == 2:
        l1.clear()

    elif d == 3:
        print(l1)

    elif d == 4:
        s = int(input("enter the element you want to search in the list: "))
        if s in l1:
            print("yes, element is in list")
        else:
            print("no, element is not in list")

    elif d == 5:
        q = int(
            input(
                "sort the list in ascending order or desending order: (0 or 1 respectively): "
            )
        )
        while True:
            if q == 0:
                l1.sort()
                print(l1)
                break
            elif q == 1:
                l1.sort(reverse=True)
                print(l1)
                break
            else:
                print("enter a proper number from the given options.")

    elif d == 0:
        print("Program ending...")
        break

    else:
        print("Enter a proper number from the list")
