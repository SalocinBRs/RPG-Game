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


    def attack(self, Monba):
        print(f'o {self.especie} atacou o {Monba.especie}')
    
class MonbaAnimal(Monba):
    kind = "Animal"

    def attack(self, Monba):
        print(f'{self.especie} scratched {Monba.especie}')


class MonbaAnimed(Monba):
    kind = "Animed"

    def attack(self, Monba):
        print(f'{self.especie} ??? {Monba.especie}')


class MonbaZombie(Monba):
    kind =  "Zombie"

    def attack(self, Monba):
        print(f'{self.especie} bit {Monba.especie}')

