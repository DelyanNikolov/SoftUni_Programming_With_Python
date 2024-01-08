top_students = 0
between_4_00_and_4_99 = 0
between_3_00_and_3_99 = 0
fail = 0
sum_of_grades = 0

students_count = int(input())

for _ in range(students_count):
    current_grade = float(input())
    sum_of_grades += current_grade
    if current_grade < 3:
        fail += 1
    elif current_grade < 4:
        between_3_00_and_3_99 += 1
    elif current_grade < 5:
        between_4_00_and_4_99 += 1
    elif current_grade >= 5:
        top_students += 1

average_grade = sum_of_grades / students_count
percentage_top = top_students / students_count * 100
percentage_4_00_and_4_99 = between_4_00_and_4_99 / students_count * 100
percentage_3_00_and_3_99 = between_3_00_and_3_99 / students_count * 100
percentage_fail = fail / students_count * 100

print(f"Top students: {percentage_top :.2f}%")
print(f"Between 4.00 and 4.99: {percentage_4_00_and_4_99 :.2f}%")
print(f"Between 3.00 and 3.99: {percentage_3_00_and_3_99 :.2f}%")
print(f"Fail: {percentage_fail :.2f}%")
print(f"Average: {average_grade :.2f}")
