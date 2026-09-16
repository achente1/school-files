# python program to calcualte parkin charges 
time = int(input("Enter the time you've parked your car : "))
if time > 5:
    print("Amount of parking charge is 100 Rs")
elif time > 2 and time <= 5:
    print("Amount of parking charge is 50 Rs")
else:
    print("Amount of parking charge is 20 Rs")