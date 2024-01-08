#
# fail_count = int(input())
# attempt = 0
# number_of_problems = 0
# last_problem = ""
# has_failed = True
# sum_of_score = 0
# while attempt < fail_count:
#     task_name = input()
#     if task_name == "Enough":
#         has_failed = False
#         break
#     score = int(input())
#     if score <= 4:
#         attempt += 1
#     number_of_problems += 1
#     sum_of_score += score
#     last_problem = task_name
# if has_failed == True:
#     print(f"You need a break, {attempt} poor grades.")
# else:
#     average_score = sum_of_score / number_of_problems
#     print(f"Average score: {average_score:.2f}")
#     print(f"Number of problems: {number_of_problems}")
#     print(f"Last problem: {last_problem}")
COMMAND_FOR_END = "Enough"
NOT_GOOD_THRESHOLD = 4

total_grades = 0
count_grades = 0
count_not_good_grades = 0
last_problem_name = ""

not_good_grades_count_threshold = int(input())

is_failed = False
while True:
    command = input()
    if command == COMMAND_FOR_END:
        break

    last_problem_name = command
    problem_grade = int(input())
    total_grades += problem_grade
    count_grades += 1

    if problem_grade <= NOT_GOOD_THRESHOLD:
        count_not_good_grades += 1
        if count_not_good_grades >= not_good_grades_count_threshold:
            is_failed = True
            break


avg_grade = total_grades / count_grades

if not is_failed:
    print(f"Average score: {avg_grade :.2f}")
    print(f"Number of problems: {count_grades}")
    print(f"Last problem: {last_problem_name}")
else:
    print(f"You need a break, {count_not_good_grades} poor grades.")