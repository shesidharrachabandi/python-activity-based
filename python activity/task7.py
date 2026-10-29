n = int(input("Number of teams: "))

for i in range(n):
    name = input("Team name: ")
    size = int(input("Team size: "))
    score = int(input("Enter score: "))

    if size >= 2 and size <= 4:
        print(name, "Total Score:", score)
    else:
        print("Invalid team size")
