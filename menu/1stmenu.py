while True:

    print("menu")
    print(' ')
    print("1. sum of positive numbers")
    print("2. printing 0-5 except 3")
    print("3. factorial program")
    print("4. temperature converter")
    print("5. leap year calculator")
    print("6. triangle")
    print("7. inverse triangle")
    print("0. quit")
    print(' ')

    a = int(input("enter number from the given inputs: "))
    if a == 1:
        sum = 0
        while True:
            a = int(input("enter number : "))
            if a >= 0:
                sum = sum + a 
            else:
                break
        print(sum)
    elif a == 2:
        for i in range(0,6):
            if i != 3:
                print(i)
                continue
            else:
                pass

    elif a == 0:
        print('program ended\n')
        break

    elif a == 3:
        a = int(input("Enter number : "))
        s = 1
        for i in range(1,a+1):
            s = i * s 
        print(s)

    elif a == 4:
        temp = input("enter the tempreature unit to convert from (available options, fahrenheit or celcius) : ")
        if temp == 'fahrenheit' or temp == 'Fahrenheit' or temp == 'F' or temp == 'f':
            f = float(input("enter the tempreature : "))
            c = (f-32)*5/9
            print(f"tempreature in celcius is {c}\n")
        elif temp == 'celcius' or temp == 'Celcius' or temp == 'c' or temp == 'C':
            c = float(input("enter the tempreature : "))
            fa = c*9/5 + 32
            print('the tempreature in fahrenheit is {fa}\n')
        else:
            print("enter a proper unit from the following\n")
            print("program terminated\n")

    elif a == 5:
        year = int(input('enter year: '))
        if year % 400 == 0:
            print(f'{year} is leap year and century\n')
        elif year % 4 == 0 and year % 100 != 0:
            print(f'{year} is a leap year\n')
        else:
            print(f'{year} is not a leap year\n')

    elif a == 6:
        for i in range(0,10,2):
            for j in range(0,i+1,2):
                print(i,end='')
            print('')

    elif a == 7:
        for m in range(8,-1,-2):
            for n in range(m+1,0,-2):
                print(m,end='')
            print('') 

    else:
        print("print a valid number")