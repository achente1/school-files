# bpm program 
bpm = int(input("enter your blood pressure ; "))
if bpm < 60:
    print("your blood pressure is low ")
elif bpm >= 60 and bpm <= 100:
    print("your blood pressure is normal.")
else:
    print('your blood pressure is high')

