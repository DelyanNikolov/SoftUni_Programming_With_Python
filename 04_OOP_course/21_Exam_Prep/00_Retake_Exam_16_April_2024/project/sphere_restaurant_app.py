from typing import List

from project.clients.base_client import BaseClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    valid_waiter_types = {"FullTimeWaiter": FullTimeWaiter, "HalfTimeWaiter": HalfTimeWaiter}

    def __init__(self):
        self.waiters: List[BaseWaiter] = []
        self.clients: List[BaseClient] = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        # creates a new waiter if waiter type is valid
        try:
            new_waiter = self.valid_waiter_types[waiter_type](waiter_name, hours_worked)
        except KeyError:
            return f"{waiter_type} is not a recognized waiter type."

        # validates if a waiter with the same name is in the staff if it is returns message
        existing_waiter = (next(filter(lambda w: w.name == waiter_name, self.waiters)), None)
        if existing_waiter is not None:
            return f"{waiter_name} is already on the staff."

        # if the waiter type is valid, and waiter with the same name is not on the staff adds the new water to the list
        # of waiters
        self.waiters.append(new_waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        pass