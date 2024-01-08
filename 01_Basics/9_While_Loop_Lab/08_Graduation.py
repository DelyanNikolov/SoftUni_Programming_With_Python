

student_name = input()
current_class = 1
bad_tries = 0
failed = False
sum_of_grades = 0

while current_class <= 12:
    current_grade = float(input())
    if current_grade < 4:
        bad_tries += 1
        if bad_tries > 1:
            failed = True
            break
        continue
    sum_of_grades += current_grade
    current_class += 1
if failed:
    print(f"{student_name} has been excluded at {current_class} grade")
else:
    average_grade = sum_of_grades / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
