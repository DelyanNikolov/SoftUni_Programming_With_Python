def students_credits(*data):
    string_to_print = []
    courses_results = {}
    total_credits = 0
    for course in data:
        course_info = course.split("-")
        name = course_info[0]
        credits = int(course_info[1])
        max_test_pints = int(course_info[2])
        points_earned = int(course_info[3])
        percentage = points_earned/max_test_pints
        credits_for_current_course = credits * percentage
        total_credits += credits_for_current_course
        courses_results[name] = credits_for_current_course
    if total_credits < 240:
        string_to_print.append(f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.")
    else:
        string_to_print.append(f"Diyan gets a diploma with {total_credits:.1f} credits.")
    for cource, points in sorted(courses_results.items(), key=lambda x: -x[1]):
        string_to_print.append(f"{cource} - {points:.1f}")

    return "\n".join(string_to_print)

print(students_credits("Computer Science-12-300-250", "Basic Algebra-15-400-200", "Algorithms-25-500-490"))
