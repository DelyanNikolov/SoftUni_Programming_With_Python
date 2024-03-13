from typing import List

from project.animals.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif self.__animal_capacity > len(self.animals) and self.__budget < price:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            current_worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(current_worker)
            return f"{current_worker.name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = sum([w.salary for w in self.workers])
        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        costs = sum([a.money_for_care for a in self.animals])
        if self.__budget >= costs:
            self.__budget -= costs
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = []
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]

        result.append(f"You have {len(self.animals)} animals")

        result.append(f"----- {len(lions)} Lions:")
        for l in lions:
            result.append(f"{l}")

        result.append(f"----- {len(tigers)} Tigers:")
        for t in tigers:
            result.append(f"{t}")

        result.append(f"----- {len(cheetahs)} Cheetahs:")
        for ch in cheetahs:
            result.append(f"{ch}")

        return '\n'.join(result)

    def workers_status(self):
        result = []
        keepers = [k for k in self.workers if k.__class__.__name__ == "Keeper"]
        caretakers = [c for c in self.workers if c.__class__.__name__ == "Caretaker"]
        vets = [v for v in self.workers if v.__class__.__name__ == "Vet"]

        result.append(f"You have {len(self.workers)} workers")

        result.append(f"----- {len(keepers)} Keepers:")
        for k in keepers:
            result.append(f"{k}")

        result.append(f"----- {len(caretakers)} Caretakers:")
        for c in caretakers:
            result.append(f"{c}")

        result.append(f"----- {len(vets)} Vets:")
        for v in vets:
            result.append(f"{v}")

        return '\n'.join(result)
