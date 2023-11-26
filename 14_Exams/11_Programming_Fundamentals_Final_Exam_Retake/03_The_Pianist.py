def collect_piece(song):
    piece_info = song.split("|")
    name = piece_info[0]
    composer = piece_info[1]
    key = piece_info[2]

    for piece_info in list_of_pieces:
        if name in piece_info:
            return  # Piece already exists, no need to collect it again

    return {name: {'composer': composer, 'key': key}}


def add_piece_to_list(name, author, tonality):
    found = False
    for piece_info in list_of_pieces:
        if name in piece_info:
            found = True
    if found:
        print(f"{name} is already in the collection!")
    else:
        print(f"{name} by {author} in {tonality} added to the collection!")
        list_of_pieces.append({name: {'composer': author, 'key': tonality}})


def remove_piece_of_list(name):
    found = False
    for piece_info in list_of_pieces:
        if name in piece_info:
            found = True
            print(f"Successfully removed {name}!")
            index = list_of_pieces.index(piece_info)
            list_of_pieces.pop(index)
            break
    if not found:
        print(f"Invalid operation! {name} does not exist in the collection.")


def change_key_of_piece(name, key):
    found = False
    for piece_info in list_of_pieces:
        if name in piece_info:
            piece_info[name]['key'] = key
            print(f"Changed the key of {name} to {key}!")
            found = True
            break
    if not found:
        print(f"Invalid operation! {name} does not exist in the collection.")


list_of_pieces = []
n = int(input())
for _ in range(n):
    piece = input()
    collected_piece = collect_piece(piece)
    if collected_piece:
        list_of_pieces.append(collected_piece)

while True:
    command = input().split("|")
    if command[0] == "Stop":
        break
    elif command[0] == "Add":
        piece_name = command[1]
        piece_composer = command[2]
        piece_key = command[3]
        add_piece_to_list(piece_name, piece_composer, piece_key)
    elif command[0] == "Remove":
        piece_name = command[1]
        remove_piece_of_list(piece_name)
    elif command[0] == "ChangeKey":
        piece_name = command[1]
        piece_key = command[2]
        change_key_of_piece(piece_name, piece_key)

for info in list_of_pieces:
    for name_song, details in info.items():
        print(f"{name_song} -> Composer: {details['composer']}, Key: {details['key']}")
