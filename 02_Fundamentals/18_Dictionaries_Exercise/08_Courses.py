courses_dict = {}
command = input()
while not command == "end":
    course_name, student_name = command.split(" : ")
    if course_name not in courses_dict.keys():
        courses_dict[course_name] = [student_name]
    else:
        courses_dict[course_name].append(student_name)
    command = input()
for course_name, students_count in courses_dict.items():
    print(f"{course_name}: {len(students_count)}")
    for student in courses_dict[course_name]:
        print(f"-- {student}")
