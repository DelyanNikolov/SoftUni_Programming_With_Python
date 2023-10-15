number_of_rooms = int(input())
total_free_chairs = 0
total_needed_chairs = 0
for number_of_room in range(1, number_of_rooms + 1):
    chairs, visitors = input().split()
    if len(chairs) < int(visitors):
        needed_chairs_in_room = int(visitors) - int(len(chairs))
        total_needed_chairs += needed_chairs_in_room
        print(f"{needed_chairs_in_room} more chairs needed in room {number_of_room}")
    else:
        total_free_chairs += len(chairs) - int(visitors)

if total_free_chairs >= total_needed_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")
