wagons_count = int(input())
train = [0] * wagons_count

while True:
    command = input().split()
    if command[0] == "End":
        print(train)
        break
    elif command[0] == "add":
        people = int(command[1])
        train[-1] += people

    elif command[0] == "insert":
        index = int(command[1])
        people = int(command[2])
        train[index] += people
    elif command[0] == "leave":
        index = int(command[1])
        people = int(command[2])
        train[index] -= people
