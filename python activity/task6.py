name = input("Enter student name: ")
maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

total = maths + science + english
percentage = total / 3

if maths >= 40 and science >= 40 and percentage >= 60:
    print("Admission Eligible")
    print("Student:", name)
    print("Percentage:", percentage)
else:
    print("Admission Not Eligible")
