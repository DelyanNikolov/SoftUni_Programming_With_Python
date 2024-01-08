
while True:
    command = input()
    if command == "Welcome!":
        break
    elif command == "Voldemort":
        print("You must not speak of that name!")
        break
    name = command
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")
if not command == "Voldemort":
    print("Welcome to Hogwarts.")
