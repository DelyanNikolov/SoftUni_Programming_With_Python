from collections import deque


def accommodate_new_pets(capacity, max_weight_limit, *animals):
    result_to_print = []
    pets = deque(animals)
    hotel = {}

    available_capacity = capacity
    while available_capacity and pets:
        animal = pets.popleft()
        animal_type = animal[0]
        animal_weight = float(animal[1])
        if animal_weight > max_weight_limit:
            continue
        if animal_type not in hotel:
            hotel[animal_type] = 0
        hotel[animal_type] += 1
        available_capacity -= 1
    if not pets:
        result_to_print.append(f"All pets are accommodated! Available capacity: {available_capacity}.")
    else:
        result_to_print.append(f"You did not manage to accommodate all pets!")

    result_to_print.append("Accommodated pets:")
    for pet, quantity in sorted(hotel.items()):
        result_to_print.append(f"{pet}: {quantity}")

    return '\n'.join(result_to_print)


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))
print()
print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
print()
print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
