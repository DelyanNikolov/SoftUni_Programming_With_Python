apartment_width = int(input())
apartment_length = int(input())
apartment_height = int(input())

apartment_space = apartment_length * apartment_width * apartment_height

room_left = apartment_space

while True:
    command = input()
    if command == "Done":
        break

    current_boxes = int(command)
    room_left -= current_boxes
    if room_left <= 0:
        break

if room_left > 0:
    print(f"{room_left} Cubic meters left.")
else:
    print(f"No more free space! You need {-room_left} Cubic meters more.")
