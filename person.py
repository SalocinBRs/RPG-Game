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
        print("Avalible Monba")
        for monbinha in self.Monbas:
            print(monbinha)
    

class Player(Person):
    kind = "Player"

    def __init__(self, name=None, Monbas=[]):
        super().__init__(name=None,Monbas=Monbas)


    def capture(self, Monba):
        self.Monbas.append(Monba)
        print(f"{self} captured {Monba}!")


class Enemy(Person):
    kind = "Enemy"

    def __init__(self, name=None, Monbas=[]):
        if not Monbas:
            for i in range(random.randint(1, 6)):
                Monbas.append(random.choice(MONBAS))
       

        super().__init__(name=None,Monbas=Monbas)




inimigo = Enemy()
print(inimigo)
inimigo.show_Monbas()
