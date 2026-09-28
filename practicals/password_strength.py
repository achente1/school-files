# wap a program to find the strength of the password:

password = input("enter a password: ")
upper = 0
lower = 0
digit = 0 
special = 0 
for i in password:
  if i.isupper():
    upper += 1
  elif i.islower():
    lower += 1
  elif i.isdigit():
    digit += 1
  elif i.isalnum() == False:
    special += 1
if lower >= 1 and upper >= 1 and digit >= 1 and special >= 1:
  print("strong password")
else:
  print("weak password")
        
