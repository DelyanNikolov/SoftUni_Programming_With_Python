def shoot_target(index, shot_power):
    if 0 <= index < len(targets):
        targets[index] -= shot_power
        if targets[index] <= 0:
            targets.pop(index)


def add_target(index, value):
    if 0 <= index < len(targets):
        targets.insert(index, value)
    else:
        print("Invalid placement!")


def strike_target(index, radius):
    if 0 <= index < len(targets) and 0 <= index - radius and index + radius < len(targets):
        targets.pop(index + radius)
        targets.pop(index)
        targets.pop(index - radius)
    else:
        print("Strike missed!")


targets = [int(target) for target in input().split()]

command = input().split()
while not command[0] == "End":
    if command[0] == "Shoot":
        target_index = int(command[1])
        power = int(command[2])
        shoot_target(target_index, power)
    elif command[0] == "Add":
        target_index = int(command[1])
        target_value = int(command[2])
        add_target(target_index, target_value)
    elif command[0] == "Strike":
        target_index = int(command[1])
        shot_radius = int(command[2])
        strike_target(target_index, shot_radius)
    command = input().split()
print("|".join((map(str, targets))))
