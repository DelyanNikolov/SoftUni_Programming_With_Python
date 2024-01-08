import math

world_record = float(input())
distance = float(input())
time_per_meter = float(input())

SWIM_DELAY_PER_METER = 12.5

slow_count = math.floor(distance / 15)

swimmer_time = (distance * time_per_meter) + (slow_count * SWIM_DELAY_PER_METER)

if swimmer_time < world_record:
    print(f" Yes, he succeeded! The new world record is {swimmer_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {(swimmer_time - world_record):.2f} seconds slower.")
