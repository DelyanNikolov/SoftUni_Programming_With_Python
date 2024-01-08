neighborhood = [int(house) for house in input().split("@")]
start_index = 0
current_house_index = 0
while True:
    command = input().split()
    if command[0] == "Love!":
        break
    elif command[0] == "Jump":
        jump = int(command[1])
        current_house_index += jump
        if current_house_index > len(neighborhood) - 1:
            current_house_index = start_index
        if neighborhood[current_house_index] == 0:
            print(f"Place {current_house_index} already had Valentine's day.")
        else:
            neighborhood[current_house_index] -= 2
            if neighborhood[current_house_index] == 0:
                print(f"Place {current_house_index} has Valentine's day.")

print(f"Cupid's last position was {current_house_index}.")
if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    house_count = sum([1 for house in neighborhood if house != 0])
    print(f"Cupid has failed {house_count} places.")
