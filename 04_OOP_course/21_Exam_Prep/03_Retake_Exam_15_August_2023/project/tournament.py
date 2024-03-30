from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT_TYPES = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    VALID_TEAM_TYPES = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    def add_equipment(self, equipment_type: str):
        """creates equipment of the given type and adds it to the equipment collection"""

        # If the equipment’s type is not valid, raise an Exception with the following message:
        # "Invalid equipment type!"
        if equipment_type not in self.VALID_EQUIPMENT_TYPES:
            raise ValueError("Invalid equipment type!")

        equipment = self.VALID_EQUIPMENT_TYPES[equipment_type]()

        self.equipment.append(equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        """creates a team of the given type and adds it to the teams’ collection"""

        # If the team type is not valid, and if not raise an Exception with the following message:
        # "Invalid team type!"
        if team_type not in self.VALID_TEAM_TYPES:
            raise ValueError("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        team = self.VALID_TEAM_TYPES[team_type](team_name, country, advantage)
        self.teams.append(team)

        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team = next(filter(lambda t: t.name == team_name, self.teams))
        equipment = next(filter(lambda e: e.__class__.__name__ == equipment_type, reversed(self.equipment)))

        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        team.equipment.append(equipment)
        team.budget -= equipment.price
        self.equipment.remove(equipment)

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = next((t for t in self.teams if t.name == team_name), None)

        if team is None:
            raise Exception("No such team!")

        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):

        number_of_changed_equipment = 0
        for equipment_change in self.equipment:
            if equipment_change.__class__.__name__ == equipment_type:
                equipment_change.increase_price()
                number_of_changed_equipment += 1

        return f"Successfully changed {number_of_changed_equipment}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team_1 = next(filter(lambda t: t.name == team_name1, self.teams))
        team_2 = next(filter(lambda t: t.name == team_name2, self.teams))

        if team_1.__class__.__name__ != team_2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        points_team_1 = team_1.advantage + sum([e.protection for e in team_1.equipment])
        points_team_2 = team_2.advantage + sum([e.protection for e in team_2.equipment])

        if points_team_1 == points_team_2:
            return "No winner in this game."
        elif points_team_1 > points_team_2:
            team_1.win()
            return f"The winner is {team_1.name}."
        elif points_team_1 < points_team_2:
            team_2.win()
            return f"The winner is {team_2.name}."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)
        result = [f"""Tournament: {self.name}
Number of Teams: {len(self.teams)}
Teams:"""]
        [result.append(t.get_statistics()) for t in sorted_teams]
        return '\n'.join(result)
