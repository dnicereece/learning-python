# Letter grade calculator with pluses and minuses

score = float(input("Enter the numeric score (0-100): "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 97:
    print("A+")
elif score >= 93:
    print("A")
elif score >= 90:
    print("A-")
elif score >= 87:
    print("B+")
elif score >= 83:
    print("B")
elif score >= 80:
    print("B-")
elif score >= 77:
    print("C+")
elif score >= 73:
    print("C")
elif score >= 70:
    print("C-")
elif score >= 67:
    print("D+")
elif score >= 63:
    print("D")
elif score >= 60:
    print("D-")
else:
    print("F")
    