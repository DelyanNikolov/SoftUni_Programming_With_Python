total_coffee = 0
command = input()
while not command == "END":
    coffee_amount = 0
    if command.lower() == "coding"\
            or command.lower() == "dog"\
            or command.lower() == "cat"\
            or command.lower() == "movie":
        if command.islower():
            total_coffee += 1
        else:
            total_coffee += 2

    command = input()

if total_coffee > 5:
    print("You need extra sleep")
else:
    print(total_coffee)
