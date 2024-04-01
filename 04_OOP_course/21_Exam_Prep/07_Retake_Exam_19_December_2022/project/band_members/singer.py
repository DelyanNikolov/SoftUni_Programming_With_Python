from typing import List

from project.band_members.musician import Musician


class Singer(Musician):
    @property
    def available_skills(self) -> List[str]:
        return [
            "sing high pitch notes",
            "sing low pitch notes"
        ]
