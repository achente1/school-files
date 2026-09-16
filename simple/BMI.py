# bmi
weight = int(input("enter your weight in kilograms : "))
height = float(input("enter your height in meters : "))
bmi = weight / (height**2)
print(f"your bmi is {bmi}")
if bmi < 18.5:
    print("you are underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("you have a normal weight")
elif bmi >= 25 and bmi <= 29.9:
    print("you are obese")
else:
    print("you are overweight")