from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

cars_count = 0
cars_que = deque()

command = input()
while command != "END":
    if command != "green":
        cars_que.append(command)
    else:
        green = green_light_duration
        window = free_window_duration
        while green > 0 and cars_que:
            time = green + window
            current_car = cars_que.popleft()
            if len(current_car) > time:
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[time]}.")
                exit()
            green -= len(current_car)
            cars_count += 1
    command = input()
print(f"Everyone is safe.\n{cars_count} total cars passed the crossroads.")
