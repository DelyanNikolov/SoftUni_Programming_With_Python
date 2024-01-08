schedule = input().split(", ")
command = input().split(":")
while True:
    if command[0] == "course start":
        break
    if command[0] == "Add":
        lesson_title = command[1]
        if lesson_title not in schedule:
            schedule.append(lesson_title)
    elif command[0] == "Insert":
        lesson_title = command[1]
        insert_index = int(command[2])
        if lesson_title not in schedule:
            schedule.insert(insert_index, lesson_title)
    elif command[0] == "Remove":
        lesson_title = command[1]
        if lesson_title in schedule:
            schedule.remove(lesson_title)
    elif command[0] == "Swap":
        lesson_title_1 = command[1]
        lesson_title_2 = command[2]
        exercise_title_1 = f"{lesson_title_1}-Exercise"
        exercise_title_2 = f"{lesson_title_2}-Exercise"
        if lesson_title_1 in schedule and lesson_title_2 in schedule:
            index_lesson_1 = schedule.index(lesson_title_1)
            index_lesson_2 = schedule.index(lesson_title_2)
            schedule[index_lesson_1], schedule[index_lesson_2] = schedule[index_lesson_2], schedule[index_lesson_1]
            if exercise_title_1 in schedule:
                index_lesson_1 = schedule.index(lesson_title_1)
                to_be_moved = schedule.pop(schedule.index(exercise_title_1))
                schedule.insert(index_lesson_1 + 1, exercise_title_1)
            if exercise_title_2 in schedule:
                index_lesson_2 = schedule.index(lesson_title_2)
                to_be_moved = schedule.pop(schedule.index(exercise_title_2))
                schedule.insert(index_lesson_2 + 1, exercise_title_2)
    elif command[0] == "Exercise":
        lesson_title = command[1]
        exercise_title = f"{lesson_title}-Exercise"
        if lesson_title not in schedule:
            schedule.append(lesson_title)
            schedule.append(exercise_title)
        elif lesson_title in schedule and exercise_title not in schedule:
            index_lesson = schedule.index(lesson_title)
            schedule.insert(index_lesson + 1, exercise_title)

    command = input().split(":")
counter = 1
for item in schedule:
    print(f"{counter}.{item}")
    counter += 1
