import random


class Monba:

    def __init__(self, especie, name=None, level=None):
        self.especie = especie

        if level:
            self.level = level
        else:
            self.level = random.randint(1,7)

        if name:
            self.name = name
        else:
            self.name = especie


    def __str__(self):
        return f'{self.especie} ({self.level})'


    def attack(self, monba):
        print(f'o {self.especie} atacou o {monba.especie}')

class MonbaAnimal(Monba):
    kind = "Animal"

    def attack(self, monba):
        print(f'{self.especie} scratched {monba.especie}')


class MonbaAnimed(Monba):
    kind = "Animed"

    def attack(self, monba):
        print(f'{self.especie} ??? {monba.especie}')


class MonbaZombie(Monba):
    kind =  "Zombie"

    def attack(self, monba):
        print(f'{self.especie} bit {monba.especie}')

