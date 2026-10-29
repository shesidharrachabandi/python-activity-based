fee = int(input("Fee paid? (1=yes, 0=no): "))
attendance = int(input("Attendance: "))
marks = int(input("Internal marks: "))

if fee == 0:
    print("Pay fees")
if attendance < 75:
    print("Low attendance")
if marks < 40:
    print("Low marks")

if fee == 1 and attendance >= 75 and marks >= 40:
    print("Eligible for exam")
else:
    print("Not eligible")