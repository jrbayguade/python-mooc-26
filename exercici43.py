score_system = [
    {"min": 0, "max": 14, "grade": 0},
    {"min": 15, "max": 17, "grade": 1},
    {"min": 18, "max": 20, "grade": 2},
    {"min": 21, "max": 23, "grade": 3},
    {"min": 24, "max": 27, "grade": 4},
    {"min": 28, "max": 30, "grade": 5},
]


def capture_data() -> list:
    students = []
    while True:
        text_introduced = input("Exam points and exercises completed: ")
        if text_introduced == "":
            break

        parts = text_introduced.split()
        exam_points = int(parts[0])
        exercises = int(parts[1])

        exercise_points = exercises // 10
        total_points = exam_points + exercise_points

        if exam_points < 10:
            grade = 0
        else:
            grade = 0
            for s in score_system:
                if s["min"] <= total_points <= s["max"]:
                    grade = s["grade"]
                    break

        students.append({"total_points": total_points, "grade": grade})

    return students


def calculate_statistics(students: list):
    if not students:
        return

    total_score = sum(s["total_points"] for s in students)
    points_average = total_score / len(students)

    passed_count = sum(1 for s in students if s["grade"] > 0)
    pass_percentage = (passed_count / len(students)) * 100

    print("Statistics:")
    print(f"Points average: {points_average:.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")
    print("Grade distribution:")

    for g in range(5, -1, -1):
        count = sum(1 for s in students if s["grade"] == g)
        stars = "*" * count
        print(f"  {g}: {stars}")


def main():
    students = capture_data()
    calculate_statistics(students)


main()