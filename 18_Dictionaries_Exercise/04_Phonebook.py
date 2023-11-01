phone_book = {}
while True:
    command = input()
    if command.isdigit():
        searches_count = int(command)
        break
    info = command.split("-")
    name = info[0]
    number = info[1]
    phone_book[name] = number

for search in range(searches_count):
    name_to_search = input()
    if name_to_search in phone_book:
        name = name_to_search
        number = phone_book[name_to_search]
        print(f"{name} -> {number}")
    else:
        print(f"Contact {name_to_search} does not exist.")
