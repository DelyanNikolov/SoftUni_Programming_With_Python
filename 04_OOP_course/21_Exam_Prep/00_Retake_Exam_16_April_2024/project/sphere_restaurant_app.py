from typing import List

from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    VALID_WAITER_TYPES = {"FullTimeWaiter": FullTimeWaiter, "HalfTimeWaiter": HalfTimeWaiter}
    VALID_CLIENT_TYPES = {"RegularClient": RegularClient, "VIPClient": VIPClient}

    def __init__(self):
        self.waiters: List[BaseWaiter] = []
        self.clients: List[BaseClient] = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        # creates a new waiter if waiter type is valid
        try:
            new_waiter = self.VALID_WAITER_TYPES[waiter_type](waiter_name, hours_worked)
        except KeyError:
            return f"{waiter_type} is not a recognized waiter type."

        # validates if a waiter with the same name is in the staff if it is returns message
        existing_waiter = next((w for w in self.waiters if w.name == waiter_name), None)
        if existing_waiter is not None:
            return f"{waiter_name} is already on the staff."

        # if the waiter type is valid, and waiter with the same name is not on the staff adds the new water to the list
        # of waiters
        self.waiters.append(new_waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        # creates a new client if waiter type is valid if not returns error msg
        try:
            new_client = self.VALID_CLIENT_TYPES[client_type](client_name)
        except KeyError:
            return f"{client_type} is not a recognized client type."

        # validates if a client with the same name is in the staff if it is returns message
        existing_client = next((c for c in self.clients if c.name == client_name), None)
        if existing_client is not None:
            return f"{client_name} is already a client."

        # if the client type is valid, and client with the same name is not on the clients list adds the new client
        self.clients.append(new_client)
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        # if waiter exists returns shift report if not returns error msg
        try:
            waiter = next(filter(lambda w: w.name == waiter_name, self.waiters))
            return waiter.report_shift()
        except StopIteration:
            return f"No waiter found with the name {waiter_name}."

    def process_client_order(self, client_name: str, order_amount: float):
        # if client exists returns points earned if not returns error msg
        try:
            client = next(filter(lambda c: c.name == client_name, self.clients))
            return f"{client_name} earned {client.earning_points(order_amount)} points from the order."
        except StopIteration:
            return f"{client_name} is not a registered client."

    def apply_discount_to_client(self, client_name: str):
        try:
            client = next(filter(lambda c: c.name == client_name, self.clients))
            discount_percentage, remaining_points = client.apply_discount()
            return f"{client_name} received a {discount_percentage}% discount. Remaining points {remaining_points}"
        except StopIteration:
            return f"{client_name} cannot get a discount because this client is not admitted!"

    def generate_report(self):
        sorted_waiters = sorted(self.waiters, key=lambda w: -w.calculate_earnings())
        total_earnings = sum([w.calculate_earnings() for w in self.waiters])
        total_client_points = sum([c.points for c in self.clients])
        clients_count = len(self.clients)

        result = [
            "$$ Monthly Report $$", f"Total Earnings: ${total_earnings:.2f}",
            f"Total Clients Unused Points: {total_client_points}",
            f"Total Clients Count: {clients_count}", "** Waiter Details **"
        ]
        for item in sorted_waiters:
            result.append(item.__str__())
        return '\n'.join(result)
