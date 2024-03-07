from typing import List

from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        # finds the room with that number and tries to accommodate the guests in the room
        room = next(filter(lambda r: r.number == room_number, self.rooms))
        room.take_room(people)
        self.guests += people

    def free_room(self, room_number):
        # finds the room with that number and tries to free it
        room = next(filter(lambda r: r.number == room_number, self.rooms))
        people = room.guests
        room.free_room()
        self.guests -= people

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join([str(room.number) for room in self.rooms if not room.is_taken])}\n" \
               f"Taken rooms: {', '.join([str(room.number) for room in self.rooms if room.is_taken])}"
