
floors_count = int(input())
rooms_count = int(input())
floor_type = ""
for floor in range(floors_count, 0, -1):
    if floor == floors_count:
        floor_type = "L"
    elif floor % 2 == 0:
        floor_type = "O"
    else:
        floor_type = "A"
    for room in range(rooms_count):
        print(f"{floor_type}{floor}{room}", end=" ")
    print()
