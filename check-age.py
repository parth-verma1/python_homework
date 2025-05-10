age = int(input("Enter the age of the student: "))

if age >= 10:
    if age <= 20:
        print("Student is allowed to enroll")
    else:
        print("Student is too old to enroll")
else:
    print("Student is too young to enroll")
