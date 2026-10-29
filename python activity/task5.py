h = int(input("Enter parking hours: "))
v = input("Enter vehicle (car/bike): ")

if v == "car":
    bill = h * 30
else:
    bill = h * 10

print("Parking Fee:", bill)
