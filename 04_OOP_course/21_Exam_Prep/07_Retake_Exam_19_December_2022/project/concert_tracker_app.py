from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")

        musician = next((m for m in self.musicians if m.name == name), None)
        if musician is not None:
            raise Exception(f"{name} is already a musician!")

        musician = self.VALID_MUSICIAN_TYPES[musician_type](name, age)
        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band = next((b for b in self.bands if b.name == name), None)
        if band is not None:
            raise Exception(f"{name} band is already created!")
        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = next((c for c in self.concerts if c.place == place), None)
        if concert is not None:
            raise Exception(f"{place} is already registered for {concert.genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = next((m for m in self.musicians if m.name == musician_name), None)
        if musician is None:
            raise Exception(f"{musician_name} isn't a musician!")

        band = next((b for b in self.bands if b.name == band_name), None)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = next((b for b in self.bands if b.name == band_name), None)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        musician = next((m for m in band.members if m.name == musician_name), None)
        if musician is None:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = next(b for b in self.bands if b.name == band_name)
        concert = next(c for c in self.concerts if c.place == concert_place)

        drummers = [d for d in band.members if d.__class__.__name__ == "Drummer"]
        singers = [s for s in band.members if s.__class__.__name__ == "Singer"]
        guitarists = [g for g in band.members if g.__class__.__name__ == "Guitarist"]

        if not drummers or not singers or not guitarists:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == "Rock":
            for musician in band.members:
                if musician.__class__.__name__ == "Drummer" \
                        and "play the drums with drumsticks" not in musician.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if musician.__class__.__name__ == "Singer" \
                        and "sing high pitch notes" not in musician.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if musician.__class__.__name__ == "Guitarist" \
                        and "play rock" not in musician.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == "Metal":
            for musician in band.members:
                if musician.__class__.__name__ == "Drummer" \
                        and "play the drums with drumsticks" not in musician.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if musician.__class__.__name__ == "Singer" \
                        and "sing low pitch notes" not in musician.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if musician.__class__.__name__ == "Guitarist" \
                        and "play metal" not in musician.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == "Jazz":
            for musician in band.members:
                if musician.__class__.__name__ == "Drummer" \
                        and "play the drums with drum brushes" not in musician.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if musician.__class__.__name__ == "Singer" \
                        and ("sing low pitch notes" not in musician.skills
                             or "sing high pitch notes" not in musician.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if musician.__class__.__name__ == "Guitarist" \
                        and "play jazz" not in musician.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
