def flights(*data):
    destinations = {}
    for idx in range(len(data)):
        if data[idx] == "Finish":
            break
        if idx % 2 == 0:
            if data[idx] not in destinations:
                destinations[data[idx]] = 0
            destinations[data[idx]] += data[idx + 1]
    return destinations


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print()
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print()
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
