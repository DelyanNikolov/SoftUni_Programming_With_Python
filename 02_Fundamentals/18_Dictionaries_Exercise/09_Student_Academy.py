students_grades = {}

students_count = int(input())
for student in range(students_count):
    name = input()
    grade = float(input())
    if name not in students_grades.keys():
        students_grades[name] = []
    students_grades[name].append(grade)


for student, grades in students_grades.items():
    average_grade = sum(grades) / len(grades)
    students_grades[student] = average_grade

for student, average_grade in students_grades.items():
    if average_grade >= 4.5:
        print(f"{student} -> {average_grade:.2f}")
