from math import ceil
number_of_students = int(input())
total_number_of_lectures = int(input())
additional_bonus = int(input())
max_bonus_points = 0
attendances = 0

for student in range(number_of_students):
    student_attendances = int(input())
    total_bonus = student_attendances / total_number_of_lectures * (5 + additional_bonus)
    if total_bonus > max_bonus_points:
        max_bonus_points = total_bonus
        attendances = student_attendances
print(f"Max Bonus: {ceil(max_bonus_points)}.")
print(f"The student has attended {attendances} lectures.")
