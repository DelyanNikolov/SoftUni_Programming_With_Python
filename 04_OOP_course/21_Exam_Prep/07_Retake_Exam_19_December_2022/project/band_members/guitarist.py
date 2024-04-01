from typing import List

from project.band_members.musician import Musician


class Guitarist(Musician):
    @property
    def available_skills(self) -> List[str]:
        return [
            "play metal",
            "play rock",
            "play jazz"
        ]
