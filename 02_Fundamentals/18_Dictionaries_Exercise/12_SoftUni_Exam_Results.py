exam_results = {}
submissions_count = {}


def banned(user):
    exam_results.pop(user)


while True:
    command = input()
    if command == "exam finished":
        break
    if "banned" in command:
        username = command.split("-")[0]
        banned(username)
    else:
        submission = command.split("-")
        username = submission[0]
        language = submission[1]
        points = int(submission[2])
        if username not in exam_results.keys():
            exam_results[username] = 0
        if points > exam_results[username]:
            exam_results[username] = points
        if language not in submissions_count.keys():
            submissions_count[language] = 0
        submissions_count[language] += 1

print("Results:")
for student_name, points in exam_results.items():
    print(f"{student_name} | {points}")
print("Submissions:")
for language, submissions in submissions_count.items():
    print(f"{language} - {submissions}")
