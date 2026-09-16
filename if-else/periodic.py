# python program for exams. 
# leap year 
year = int(input("enter the year : "))
if year % 400 == 0:
    print("it's a leap year and century")
elif year % 4 == 0 and year % 100 != 0:
    print("it's a leap year ")
else:
    print("not a leap year")

