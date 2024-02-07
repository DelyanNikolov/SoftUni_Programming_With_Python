from collections import deque

ducks = (
    ("Darth Vader Ducky", [0, 60]),
    ("Thor Ducky", [61, 120]),
    ("Big Blue Rubber Ducky", [121, 180]),
    ("Small Yellow Rubber Ducky", [181, 240])
)

given_ducks = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0
}

times_to_complete_task = deque(int(t) for t in input().split())
number_of_tasks_stack = [int(x) for x in input().split()]

while times_to_complete_task and number_of_tasks_stack:
    programmer_time = times_to_complete_task.popleft()
    task = number_of_tasks_stack.pop()

    calculated_time = programmer_time * task

    for duck_type, interval in ducks:
        if calculated_time in range(interval[0], interval[1] + 1):
            given_ducks[duck_type] += 1

        if calculated_time > 240:
            task -= 2
            number_of_tasks_stack.append(task)
            times_to_complete_task.append(programmer_time)
            break
print(f"Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for duck, count in given_ducks.items():
    print(f"{duck}: {count}")
