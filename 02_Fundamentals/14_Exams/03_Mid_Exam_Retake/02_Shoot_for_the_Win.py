targets = [int(target) for target in input().split()]
shot_target_indexes = []
shot_target_count = 0
command = input()
while not command == "End":
    target_index = int(command)
    if 0 <= target_index < len(targets) and target_index not in shot_target_indexes:
        target_value = targets[target_index]
        targets[target_index] = -1
        shot_target_indexes.append(target_index)
        shot_target_count += 1
        for i in range(len(targets)):
            if 0 <= targets[i] <= target_value:
                targets[i] += target_value
            elif targets[i] != -1 and targets[i] > target_value:
                targets[i] -= target_value
    command = input()
print(f"Shot targets: {shot_target_count} -> {' '.join(map(str, targets))}")
