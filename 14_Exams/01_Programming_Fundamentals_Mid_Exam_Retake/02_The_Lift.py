people_on_que = int(input())
wagons_in_lift = [int(man) for man in input().split()]

for wagon_number in range(len(wagons_in_lift)):
    space_in_wagon = wagons_in_lift[wagon_number]
    if space_in_wagon > 4:  # chek if the cart is full, if 4 people are in the cart --> check next wagon
        continue
    else:
        if people_on_que >= 4:                      # chek if people on the que are more of the capacity of the cart
            people_to_board = 4 - space_in_wagon    # if there are more, we calculate how many people can fit
        else:                                       # this check insures that we can't get negative people count in
            people_to_board = people_on_que         # the que
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
