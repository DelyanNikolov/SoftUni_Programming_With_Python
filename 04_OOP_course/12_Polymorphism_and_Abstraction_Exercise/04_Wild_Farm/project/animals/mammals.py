from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    @property
    def gained_weight(self):
        return 0.10

    @property
    def food_that_eats(self):
        return [Vegetable, Fruit]

    def make_sound(self) -> str:
        return "Squeak"


class Dog(Mammal):
    @property
    def gained_weight(self):
        return 0.40

    @property
    def food_that_eats(self):
        return [Meat]

    def make_sound(self) -> str:
        return "Woof!"


class Cat(Mammal):
    @property
    def gained_weight(self):
        return 0.30

    @property
    def food_that_eats(self):
        return [Vegetable, Meat]

    def make_sound(self) -> str:
        return "Meow"


class Tiger(Mammal):
    @property
    def gained_weight(self):
        return 1.00

    @property
    def food_that_eats(self):
        return [Meat]

    def make_sound(self) -> str:
        return "ROAR!!!"


