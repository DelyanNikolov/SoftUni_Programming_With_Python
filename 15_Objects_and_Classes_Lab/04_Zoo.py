class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        Zoo.__animals += 1
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

    def get_info(self, species):
        string_to_print = ""
        if species == "mammal":
            string_to_print += f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            string_to_print += f"Fishes in {self.name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            string_to_print += f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"
        return string_to_print


zoo_name = input()
animals_num = int(input())
zoo = Zoo(zoo_name)
for animal in range(animals_num):
    animal_to_add = input().split()
    species = animal_to_add[0]
    name = animal_to_add[1]
    zoo.add_animal(species, name)

species = input()
print(zoo.get_info(species))
