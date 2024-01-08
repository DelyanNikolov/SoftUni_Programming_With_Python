from math import floor
biscuits_per_worker = int(input())
workers_count = int(input())
biscuits_to_compete = int(input())
days = 30
biscuits_per_day = biscuits_per_worker * workers_count
biscuits_produced = 0
for day in range(1, days + 1):
    if day % 3 == 0:
        biscuits_produced += floor(0.75 * biscuits_per_day)
    else:
        biscuits_produced += biscuits_per_day

print(f"You have produced {biscuits_produced} biscuits for the past month.")
difference = biscuits_produced - biscuits_to_compete
percentage = abs(difference / biscuits_to_compete * 100)
if difference > 0:
    print(f"You produce {percentage:.2f} percent more biscuits.")
else:
    print(f"You produce {percentage:.2f} percent less biscuits.")

