# leap year calculator

year = int(input("Enter year : "))
if year % 400 == 0:
    print(f'year {year} is a leap year and century')
elif (year % 4 == 0) and (year % 100 != 0):
    print(f'year {year} is a leap year')
else:
    print(f'year {year} is not a leap year')
