people_on_que = int(input())
wagons_in_lift = [int(man) for man in input().split()]

for wagon_number in range(len(wagons_in_lift)):
    space_in_wagon = wagons_in_lift[wagon_number]
    if space_in_wagon > 4:
        continue
    else:
        if people_on_que >= 4:
            people_to_board = 4 - space_in_wagon
        else:
            people_to_board = people_on_que
        wagons_in_lift[wagon_number] += people_to_board
        people_on_que -= people_to_board

if wagons_in_lift[-1] < 4:
    print("The lift has empty spots!")
    print(" ".join(map(str, wagons_in_lift)))
elif people_on_que > 0:
    print(f"There isn't enough space! {people_on_que} people in a queue!")
    print(" ".join(map(str, wagons_in_lift)))
elif people_on_que == 0:
    print(" ".join(map(str, wagons_in_lift)))
