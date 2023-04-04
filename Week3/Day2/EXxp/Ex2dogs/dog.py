class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f"{self.name} won the fight"
        else:
            return f"{other_dog.name} won the fight"


dog1 = Dog("Rex", 5, 30)
dog2 = Dog("Max", 3, 20)
dog3 = Dog("Buddy", 7, 40)

print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog3))
