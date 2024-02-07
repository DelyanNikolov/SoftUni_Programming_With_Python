def gather_credits(credits_needed: int, *course_info):
    result = []
    courses = []
    gathered_credits = 0
    for course in course_info:
        course_name = course[0]
        course_credits = int(course[1])
        if gathered_credits >= credits_needed:
            break
        else:
            if course_name not in courses:
                courses.append(course_name)
                gathered_credits += course_credits

    if gathered_credits >= credits_needed:
        result.append(f"Enrollment finished! Maximum credits: {gathered_credits}.")
        result.append(f"Courses: {', '.join(sorted(courses))}")
    else:
        credits_shortage = credits_needed - gathered_credits
        result.append(f"You need to enroll in more courses! You have to gather {credits_shortage} credits more.")

    return '\n'.join(result)


print(gather_credits(
    80,
    ("Basics", 27),
))
print()
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
print()
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
