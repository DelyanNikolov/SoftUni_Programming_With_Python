from collections import deque

water_quantity = int(input())
people = deque()
while True:
    name = input()
    if name == "Start":
        break
    people.append(name)

while True:
    command = input().split()
    if command[0] == "End":
        break
    elif command[0].isdigit():
        water_requested = int(command[0])
        person_name = people.popleft()
        if water_quantity >= water_requested:
            water_quantity -= water_requested
            print(f"{person_name} got water")
        else:
            print(f"{person_name} must wait")
    elif "refill" in command:
        refill_liters = int(command[1])
        water_quantity += refill_liters
print(f"{water_quantity} liters left")
