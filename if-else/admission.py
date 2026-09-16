# python program to determine admission to a course 
english = int(input("Enter marks in english : "))
stream = input("what stream are you in ? type A for accountancy, type S for Science : ")

if stream == 'a' or stream == 'A':
    accountancy = int(input("Enter marks in accountancy"))
    if english >= 60 and accountancy >= 60:
        print("Eligible for admission")
    else:
        print("Not eligible for admission")
elif stream == 's' or stream == 'S':
    physics = int(input("enter marks in physics : "))
    chemistry = int(input("enter the marks in chemistry : "))
    if english >= 60 and physics >= 60 and chemistry >= 60:
        print("Eligible for admission")
    else:
        print("Not eligible for admission")
else:
    print("Enter valid stream selection ")
