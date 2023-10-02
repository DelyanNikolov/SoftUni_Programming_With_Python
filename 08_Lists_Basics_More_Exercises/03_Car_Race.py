race_track = input().split(" ")

finish = len(race_track) // 2
left_side = race_track[:finish]
right_side = race_track[finish + 1:]
right_side = right_side[::-1]

winner = ""
time_winner = 0

total_time_left = 0
total_time_right = 0
for index in range(len(left_side)):
    time_left = int(left_side[index])
    time_right = int(right_side[index])
    total_time_left += time_left
    if int(left_side[index]) == 0:
        total_time_left *= 0.8

    time_right = int(right_side[index])
    total_time_right += time_right
    if int(right_side[index]) == 0:
        total_time_right *= 0.8

if total_time_left < total_time_right:
    winner = "left"
    time_winner = total_time_left
elif total_time_left > total_time_right:
    winner = "right"
    time_winner = total_time_right

print(f"The winner is {winner} with total time: {time_winner:.1f}")
