students = []
while True:
    command = input()
    if ":" not in command:
        search_course = command
        break
    name, student_id, course = command.split(":")
    students.append({"name": name, "ID": student_id, "course": course})

for student in students:
    if search_course.startswith(student["course"][0:3]):
        print(f"{student['name']} - {student['ID']}")
