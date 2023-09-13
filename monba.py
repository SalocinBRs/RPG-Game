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

        self.power = self.level * 5
        self.life = self.level * 10

    def __str__(self):
        return f'{self.especie} ({self.level})'


    def attack(self, monba):
        print(f'o {self.especie} atacou o {monba.especie}')

class MonbaAnimal(Monba):

    def attack(self, monba):
        print(f'{self.especie} scratched {monba.especie}')


class MonbaAnimed(Monba):

    def attack(self, monba):
        print(f'{self.especie} ??? {monba.especie}')


class MonbaZombie(Monba):

    def attack(self, monba):
        print(f'{self.especie} bit {monba.especie}')

