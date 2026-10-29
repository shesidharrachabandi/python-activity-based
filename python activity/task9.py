marks = int(input("Enter original marks: "))

original = marks

if marks >= 35 and marks < 40:
    marks = marks + 5

if marks > 100:
    marks = 100

print("Original Marks:", original)
print("Final Marks:", marks)

if marks >= 40:
    print("Pass")
else:
    print("Fail")