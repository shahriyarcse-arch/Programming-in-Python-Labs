students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]]
]

def calculate_average(marks):
    if len(marks) == 0:
        return 0
    return sum(marks) / len(marks)

def classify_performance(average):
    if average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"

def display_report(records):
    print(f"{'ID':<6} {'Name':<10} {'Average':<10} {'Performance'}")
    print("-" * 42)
    for student in records:
        student_id = student[0]
        name = student[1]
        marks = student[2]

        avg = calculate_average(marks)
        status = classify_performance(avg)
        print(f"{student_id:<6} {name:<10} {avg:<10.2f} {status}")

display_report(students)
