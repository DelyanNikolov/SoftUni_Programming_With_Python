from collections import deque
from datetime import datetime, timedelta


robots_data = {}
products_que = deque()

robots = input().split(";")
factory_time = datetime.strptime(input(), "%H:%M:%S")

product = input()
while not product == "End":
    products_que.append(product)
    product = input()

for robot in robots:
    robot_name, process_time = robot.split("-")
    if robot_name not in robots_data:
        robots_data[robot_name] = []
    robots_data[robot_name].append(int(process_time))
    robots_data[robot_name].append(0)

while products_que:
    factory_time += timedelta(0, 1)
    current_product = products_que.popleft()

    free_robots = []

    for name, value in robots_data.items():
        if value[1] > 0:
            robots_data[name][1] -= 1
        if value[1] == 0:
            free_robots.append([name, value])

    if not free_robots:
        products_que.append(current_product)
        continue

    robot_name, data = free_robots[0]
    robots_data[robot_name][1] = data[0]

    print(f"{robot_name} - {current_product} [{factory_time.strftime('%H:%M:%S')}]")
