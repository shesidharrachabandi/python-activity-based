name = input("Enter student name: ")
marks = int(input("Enter marks: "))
assessment = int(input("Enter assessment score: "))
attendance = int(input("Enter attendance: "))

if marks >= 60 and assessment >= 50 and attendance >= 75:
    total_score = marks + assessment
    print("Eligible for Internship")
    print("Student Name:", name)
    print("Total Score:", total_score)
else:
    print("Not Eligible for Internship")