from typing import List

from project.customer import Customer
from project.dvd import DVD


class MovieWorld:

    def __init__(self, name):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity() -> int:
        return 15

    @staticmethod
    def customer_capacity() -> int:
        return 10

    def add_customer(self, customer: Customer) -> None:
        # add the customer if capacity is not exceeded
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        # add the DVD if capacity is not exceeded
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer = next(filter(lambda c: c.id == customer_id, self.customers))
        dvd = next(filter(lambda d: d.id == dvd_id, self.dvds))

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return "DVD is already rented"

        if dvd.age_restriction > customer.age:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer = next(filter(lambda c: c.id == customer_id, self.customers))
        dvd = next(filter(lambda d: d.id == dvd_id, self.dvds))

        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"

        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        result = []
        result.extend([str(customer) for customer in self.customers])
        result.extend([str(dvd) for dvd in self.dvds])

        return '\n'.join(result)

    # def __repr__(self):
    #     return "\n".join([
    #         *[str(c) for c in self.customers],
    #         *[str(d) for d in self.dvds],
    #     ])
