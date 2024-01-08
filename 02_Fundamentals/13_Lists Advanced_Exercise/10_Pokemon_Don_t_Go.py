distances = [int(num) for num in input().split()]
total_sum_of_caught = 0
while distances:
    index = int(input())
    if index < 0:
        caught = distances.pop(0)
        distances.insert(0, distances[-1])
        total_sum_of_caught += caught
        for i in range(len(distances)):
            if distances[i] <= caught:
                distances[i] += caught
            else:
                distances[i] -= caught
    elif index > len(distances) - 1:
        caught = distances.pop(-1)
        distances.append(distances[0])
        total_sum_of_caught += caught
        for i in range(len(distances)):
            if distances[i] <= caught:
                distances[i] += caught
            else:
                distances[i] -= caught
    else:
        caught = distances.pop(index)
        total_sum_of_caught += caught
        for i in range(len(distances)):
            if distances[i] <= caught:
                distances[i] += caught
            else:
                distances[i] -= caught

print(total_sum_of_caught)
