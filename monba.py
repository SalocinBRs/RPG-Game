class Monba:

    def __init__(self, especie, name=None, level=1):
        self.especie = especie
        self.level = level
        if name:
            self.name = name
        else:
            self.name = especie


    def __str__(self):
        return f'{self.especie} ({self.level})'


    def attack(self, pokemon):
        print(f'o {self.especie} atacou o {pokemon.especie}')
    
class MonbaAnimal(Monba):
    kind = "Animal"

    def attack(self, pokemon):
        print(f'{self.especie} scratched {pokemon.especie}')


class MonbaAnimed(Monba):
    kind = "Animed"

    def attack(self, pokemon):
        print(f'{self.especie} ??? {pokemon.especie}')

class MonbaZombie(Monba):
    kind =  "Zombie"
    
    def attack(self, pokemon):
        print(f'{self.especie} bit {pokemon.especie}')

m_teste = MonbaAnimal("animal")
