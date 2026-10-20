marks = float(input("Enter marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks! Marks must be between 0 and 100.")
elif marks >= 90:
    print("Grade: A+ (Outstanding)")
elif marks >= 85:
    print("Grade: A (Excellent)")
elif marks >= 80:
    print("Grade: B+ (Very Good)")
elif marks >= 75:
    print("Grade: B (Good)")
elif marks >= 70:
    print("Grade: C+ (Satisfactory)")
elif marks >= 65:
    print("Grade: C (Above Average)")
elif marks >= 60:
    print("Grade: D+ (Average)")
elif marks >= 50:
    print("Grade: D (Pass)")
else:
    print("Grade: F (Fail)")
