from collections import deque

fuel_sequence = [int(f) for f in input().split()]
additional_consumption = deque(int(f) for f in input().split())
needed_fuels = deque(int(f) for f in input().split())
counter = 0
reached_altitudes = []
while True:
    initial_fuel = fuel_sequence.pop()
    additional_fuel = additional_consumption.popleft()
    needed_fuel = needed_fuels.popleft()

    calculated_fuel = initial_fuel - additional_fuel

    if calculated_fuel < needed_fuel:
        print(f"John did not reach: Altitude {counter + 1}")
        fuel_sequence.append(initial_fuel)
        additional_consumption.appendleft(additional_fuel)
        needed_fuels.appendleft(needed_fuel)
        break
    else:
        counter += 1
        reached_altitudes.append(f"Altitude {counter}")
        print(f"John has reached: Altitude {counter}")
    if not additional_consumption and not fuel_sequence and not needed_fuels:
        print("John has reached all the altitudes and managed to reach the top!")
        exit()
if reached_altitudes and fuel_sequence:
    print("John failed to reach the top.")
    print(f"Reached altitudes: {', '.join(reached_altitudes)}")
else:
    print(f"John failed to reach the top.\nJohn didn't reach any altitude.")

