from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACIES_TYPES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    VALID_BOOTH_TYPES = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if type_delicacy not in self.VALID_DELICACIES_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        for delicacy in self.delicacies:
            if delicacy.name == name:
                raise Exception(f"{name} already exists!")

        delicacy_to_add = self.VALID_DELICACIES_TYPES[type_delicacy](name, price)
        self.delicacies.append(delicacy_to_add)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.VALID_BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")

        boot_to_add = self.VALID_BOOTH_TYPES[type_booth](booth_number, capacity)
        self.booths.append(boot_to_add)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        available_boot = next((b for b in self.booths if not b.is_reserved and b.capacity >= number_of_people), None)

        if available_boot is None:
            raise Exception(f"No available booth for {number_of_people} people!")

        available_boot.reserve(number_of_people)
        return f"Booth {available_boot.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = next((b for b in self.booths if b.booth_number == booth_number), None)
        delicacy = next((d for d in self.delicacies if d.name == delicacy_name), None)

        if booth is None:
            raise Exception(f"Could not find booth {booth_number}!")

        if delicacy is None:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth_to_leave = next(b for b in self.booths if b.booth_number == booth_number)

        bill = booth_to_leave.price_for_reservation + sum([order.price for order in booth_to_leave.delicacy_orders])

        self.income += bill
        booth_to_leave.delicacy_orders.clear()
        booth_to_leave.is_reserved = False
        booth_to_leave.price_for_reservation = 0
        return f"Booth {booth_to_leave.booth_number}:\n" \
               f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
