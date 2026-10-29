c = int(input("Consultation: "))
d = int(input("Diagnostic: "))
t = int(input("Treatment: "))

total = c + d + t

if total <= 0:
    print("Invalid Bill")
else:
    if total >= 5000:
        total = total - 500

    print("Final Bill:", total)

    if total >= 3000:
        print("High Payment")
    else:
        print("Low Payment")
