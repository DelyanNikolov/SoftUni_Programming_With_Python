animals = input()    # sheep or wolf

list_of_animals = animals.split(", ")
wolf_position = 0
sheep_number = 0

for index in range(len(list_of_animals)):
    if list_of_animals[index] == "wolf":
        wolf_position = index + 1
        sheep_number = len(list_of_animals) - wolf_position
        if wolf_position == len(list_of_animals):
            print("Please go away and stop eating my sheep")
else:
    if sheep_number >= 1:
        print(f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!")
