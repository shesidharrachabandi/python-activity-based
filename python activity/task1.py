marks = []

for i in range(3):
    m = int(input("Enter marks: "))

    if m < 35 and m >= 30:
        m = 35
        print("Grace marks added")

    marks.append(m)

total = sum(marks)
percentage = total / 3

print("Total Marks:", total)
print("Percentage:", percentage)

if min(marks) >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")
