def check_contest_is_valid(name):
    return name in contests


def check_password_is_valid(name, word):
    return contests.get(name) == word


contests = {}
contest_results = {}

# Collect contests and passwords
while True:
    command = input()
    if command == "end of contests":
        break
    contest_name, password_for_contest = command.split(":")
    contests[contest_name] = password_for_contest

# Collect contest results
while True:
    command = input()
    if command == "end of submissions":
        break
    contest, password, username, points = command.split("=>")
    if check_contest_is_valid(contest) and check_password_is_valid(contest, password):
        if username not in contest_results:
            contest_results[username] = {}
        if contest not in contest_results[username] or int(points) > int(contest_results[username][contest]):
            contest_results[username][contest] = points

# Calculate total points and find the best candidate
top_user = max(contest_results, key=lambda k: sum(map(int, contest_results[k].values())))
total_points = sum(map(int, contest_results[top_user].values()))

print(f"Best candidate is {top_user} with total {total_points} points.")
print("Ranking:")

# Print results
for student_name, course_info in sorted(contest_results.items()):
    print(student_name)
    for name_of_course, points in sorted(course_info.items(), key=lambda item: int(item[1]), reverse=True):
        print(f"#  {name_of_course} -> {points}")
