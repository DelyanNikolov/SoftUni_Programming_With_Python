from abc import ABC, abstractmethod


class Workers(ABC):

    @abstractmethod
    def work(self):
        pass


class Eaters(ABC):
    @abstractmethod
    def eat(self):
        pass


class Worker(Workers, Eaters):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")


class SuperWorker(Worker, Eaters):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")


class Robot(Worker):

    def work(self):
        print("I'm a robot. I'm working....")


class BaseManager(ABC):
    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        pass


class WorkersManager(BaseManager):

    def set_worker(self, worker):
        assert isinstance(worker, Workers), "`worker` must be of type {}".format(Workers)

        self.worker = worker

    def manage(self):
        self.worker.work()


class EatersManager(BaseManager):
    def set_worker(self, worker):
        assert isinstance(worker, Eaters), f"`worker` must be of type {Eaters}"

    def manage(self):
        self.worker.eat()

