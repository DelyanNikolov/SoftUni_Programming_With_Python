from math import ceil
people_count = int(input())
elevator_capacity = int(input())

trips = ceil(people_count / elevator_capacity)
print(trips)
