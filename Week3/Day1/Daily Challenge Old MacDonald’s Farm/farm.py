class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal_type, quantity=1):
        if animal_type in self.animals:
            self.animals[animal_type] += quantity
        else:
            self.animals[animal_type] = quantity

    def get_info(self):
        info = f"{self.name}'s farm\n"
        for animal, quantity in sorted(self.animals.items()):
            info += f"{animal} : {quantity}\n"
        info += "    E-I-E-I-0!"
        return info

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_types = self.get_animal_types()
        animals_str = ", ".join(animal_types[:-1]) + f" and {animal_types[-1]}" if len(animal_types) > 1 else animal_types[0]
        return f"{self.name}'s farm has {animals_str}."
