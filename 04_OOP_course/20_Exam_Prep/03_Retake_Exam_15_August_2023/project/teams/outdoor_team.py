from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    BUDGET = 1000.0
    ADVANTAGE_POINTS = 115

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, self.BUDGET)

    def win(self):
        self.advantage += self.ADVANTAGE_POINTS
        self.wins += 1

