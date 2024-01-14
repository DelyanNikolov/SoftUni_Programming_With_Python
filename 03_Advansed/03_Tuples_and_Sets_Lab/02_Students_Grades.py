students_count = int(input())
students_data = {}
for _ in range(students_count):
    student_name, grade = input().split()
    if student_name not in students_data:
        students_data[student_name] = []
    students_data[student_name].append(float(grade))

for student, data in students_data.items():
    average_grade = sum(data) / len(data)
    grades_as_string = [f"{grade:.2f}" for grade in data]
    print(f"{student} ->", *grades_as_string, f"(avg: {average_grade:.2f})")
