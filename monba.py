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


    def attack(self, enemy):
        damage = int(1.3 * random.random() * self.power)
        enemy.life -= damage
        print(f"{enemy.name} lost {damage} life")

        if enemy.life <= 0:
            print(f"{enemy.name} died")
            return True
        else:
            return False

class MonbaAnimal(Monba):

    def attack(self, monba):
        print(f'{self.especie} scratched {monba.especie}')
        return super().attack(monba)

class MonbaAnimed(Monba):

    def attack(self, monba):
        print(f'{self.especie} ??? {monba.especie}')
        return super().attack(monba)

class MonbaZombie(Monba):

    def attack(self, monba):
        print(f'{self.especie} bit {monba.especie}')
        return super().attack(monba)

