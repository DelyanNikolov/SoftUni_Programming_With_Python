searched_book = input()

books_count = 0
found_book = False
command = input()

while command != "No More Books":
    current_book = command
    if current_book == searched_book:
        found_book = True
        break
    books_count += 1
    command = input()
if found_book:
    print(f"You checked {books_count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {books_count} books.")
