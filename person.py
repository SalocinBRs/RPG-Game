import monba, random


NAMES = [
    "Alice", "Bob", "Carlos", "Daniela", "Eduardo", 
    "Fernanda", "Gabriel", "Heloísa", "Isabel", "José",
    "Laura", "Miguel", "Natália", "Oliver", "Patrícia",
    "Rafael", "Sofia", "Thiago", "Valentina", "William",
    "Xavier", "Yasmin", "Zacarias", "Amanda", "Bruno",
    "Clara", "Diego", "Elisa", "Felipe", "Giovanna"
]

MONBAS = [
    monba.MonbaAnimal("Pikaro"),
    monba.MonbaAnimed("Squirtleto"),
    monba.MonbaAnimal("Charlanda"),
    monba.MonbaAnimed("Jigglypuffo"),
    monba.MonbaAnimal("Bulbazaur"),
]


class Person:

    def __init__(self, name=None, Monbas=[]):
        if name:
            self.name = name
        else:
            self.name = random.choice(NAMES)

        self.Monbas = Monbas

    def __str__(self):
        return f'{self.name}'

    def show_Monbas(self):
        print("Monbas disponíveis")
        for monbinha in self.Monbas:
            print(monbinha)
    

class Player(Person):
    kind = "Player"

    def __init__(self, name=None, Monbas=[]):
        
        if Monbas:
            self.Monbas = Monbas
        else:
            self.Monbas = Monbas.random.choice(MONBAS)


    def capture(self, Monba):
        self.Monbas.append(Monba)
        print(f"{self} capturou {Monba}")


class Enemy(Person):
    kind = "Enemy"

    def __init__(self, name=None, Monbas=[]):
        if name:
            self.name = name
        else:
            self.name = random.choice(NAMES)
        if Monbas:
            self.Monbas = Monbas
        else:
            self.Monbas = random.choice(MONBAS)


eu = Player()

inimigo = Enemy()

print(inimigo)

eu.show_Monbas()