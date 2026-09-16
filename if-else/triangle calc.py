# triangle classification
s1 = int(input("Enter 1st side of the triangle "))
s2 = int(input("Enter 2nd side of the triangle "))
s3 = int(input("Enter 3rd side of the triangle "))

if (s1 + s2 > s3) or (s2 + s3 > s1) or (s3 + s1 > s2):
    if (s1 == s2 == s3):
        print("Equilateral Triangle")
    elif (s1 + s2 > s3) and (s1 == s2 or s2 == s3 or s3 == s1):
        print("Isoceles Triangle")
    elif (s1 + s2 > s3):
        print("Scalene Triangle")
else:
    print("Invalid Triangle")
