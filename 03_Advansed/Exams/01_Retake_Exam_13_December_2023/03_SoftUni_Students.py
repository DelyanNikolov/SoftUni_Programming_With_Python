def softuni_students(*student_ids, **course_data):
    result = ""
    successful_students = {}
    invalid_students = []
    for id_, student in student_ids:
        student_username = student
        student_id = id_
        if student_id in course_data:
            successful_students[student_username] = []
            successful_students[student_username].append(course_data[student_id])
        else:
            invalid_students.append(student_username)
    for u_name, subject in sorted(successful_students.items()):
        result += f"*** A student with the username {u_name} has successfully finished the course {subject[0]}!\n"
    if invalid_students:
        result += f"!!! Invalid course students: {', '.join(sorted(invalid_students))}"

    return result


print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))

print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))

print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
