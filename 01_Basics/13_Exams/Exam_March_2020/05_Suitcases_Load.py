suitcase_count = 0
room_left = True
capacity = float(input())
command = input()
while command != "End":
    volume_of_suitcase = float(command)
    suitcase_count += 1
    if suitcase_count % 3 == 0:
        volume_of_suitcase *= 1.1
    if volume_of_suitcase >= capacity:
        suitcase_count -= 1
        room_left = False
        break
    else:
        capacity -= volume_of_suitcase
    command = input()

if room_left:
    print("Congratulations! All suitcases are loaded!")
else:
    print("No more space!")
print(f"Statistic: {suitcase_count} suitcases loaded.")
