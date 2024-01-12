from collections import deque

pumps_count = int(input())
petrol_pumps = deque([[int(x) for x in input().split()] for _ in range(pumps_count)])
pump_index = 0
fuel_in_tank = 0
pumps_data = petrol_pumps.copy()
while pumps_data:
    petrol, distance = pumps_data.popleft()
    fuel_in_tank += petrol
    if fuel_in_tank >= distance:
        fuel_in_tank -= distance

    else:
        fuel_in_tank = 0
        pump_index += 1
        petrol_pumps.rotate(-1)
        pumps_data = petrol_pumps.copy()

print(pump_index)
