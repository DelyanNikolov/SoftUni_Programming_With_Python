
students_count = int(input())
fail_students = 0
between_3_and_4 = 0
between_4_and_5 = 0
top_students = 0
sum_of_grades = 0
for _ in range(students_count):
    current_grade = float(input())
    if current_grade < 3:
        fail_students += 1
        sum_of_grades += current_grade
    elif current_grade < 4:
        between_3_and_4 += 1
        sum_of_grades += current_grade
    elif current_grade < 5:
        between_4_and_5 += 1
        sum_of_grades += current_grade
    elif current_grade >= 5:
        top_students += 1
        sum_of_grades += current_grade

top_students_percentage = top_students / students_count * 100
between_4_and_5_percentage = between_4_and_5 / students_count * 100
between_3_and_4_percentage = between_3_and_4 / students_count * 100
fail_students_percentage = fail_students / students_count * 100
average_grade = sum_of_grades / students_count

print(f"Top students: {top_students_percentage:.2f}%")
print(f"Between 4.00 and 4.99: {between_4_and_5_percentage:.2f}%")
print(f"Between 3.00 and 3.99: {between_3_and_4_percentage:.2f}%")
print(f"Fail: {fail_students_percentage:.2f}%")
print(f"Average: {average_grade:.2f}")
