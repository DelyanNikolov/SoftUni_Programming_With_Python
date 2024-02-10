from collections import deque

available_seats = {s: True for s in input().split(", ")}
first_sequence = deque(int(n) for n in input().split(", "))
second_sequence = deque([int(m) for m in input().split(", ")])

matched_seats = []
taken_seats = 0
rotations = 0

while taken_seats < 3 and rotations < 10:
    first_num = first_sequence.popleft()
    second_num = second_sequence.pop()
    letter = chr(first_num + second_num)

    seats_to_check = [f"{first_num}{letter}", f"{second_num}{letter}"]
    rotations += 1

    match_found = False
    for seat in seats_to_check:
        if seat in available_seats.keys() and available_seats[seat]:
            taken_seats += 1
            match_found = True
            available_seats[seat] = False
            matched_seats.append(seat)
            break
        elif seat in available_seats and not available_seats[seat]:
            break
    if not match_found:
        first_sequence.append(first_num)
        second_sequence.appendleft(second_num)

print(f"Seat matches: {', '.join(matched_seats)}")
print(f"Rotations count: {rotations}")
