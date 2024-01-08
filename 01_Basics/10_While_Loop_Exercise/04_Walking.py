steps_goal = 10000
daily_steps = 0
while True:
    command = input()
    if command == "Going home":
        current_steps = int(input())
        daily_steps += current_steps
        break

    current_steps = int(command)
    daily_steps += current_steps
    if daily_steps >= steps_goal:
        break

if daily_steps >= steps_goal:
    diff_steps = abs(steps_goal - daily_steps)
    print("Goal reached! Good job!")
    print(f"{diff_steps} steps over the goal!")
else:
    diff_steps = abs(steps_goal - daily_steps)
    print(f"{diff_steps} more steps to reach goal.")
