parking_lot = {}

commands_count = int(input())
command = ""
username = ""
license_plate = ""
for _ in range(commands_count):
    line = input().split()
    if line[0] == "register":
        command, username, license_plate = line[0], line[1], line[2]
    elif line[0] == "unregister":
        command, username = line[0], line[1]

    if command == "register":
        if username in parking_lot.keys():
            print(f"ERROR: already registered with plate number {parking_lot[username]}")
        else:
            parking_lot[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
    elif command == "unregister":
        if username not in parking_lot.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking_lot[username]

for username, license_plate in parking_lot.items():
    print(f"{username} => {license_plate}")
