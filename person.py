import random
import monba



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
        if name is None:
            self.name = random.choice(NAMES)
        else:
            self.name = name

        self.Monbas = Monbas


    def __str__(self):
        return f'{self.name}'


    def show_Monbas(self):
        print("Avalible Monba")
        for monbinha in self.Monbas:
            print(monbinha)

    def choice_monba(self):
        for i, monba in enumerate(self.Monbas):
            print(f"{i + 1} - {monba}")
        while True:
            try:
                choice = int(input("Which: "))
                chosen = self.Monbas[choice - 1]
                return chosen
            except:
                print("escolha invalida")




    def figth(self, enemy):
        print(f"{self.name} battle with {enemy.name}")
        
        enemy.show_Monbas()

        self.choice_monba()


class Player(Person):
    kind = "Player"

    def __init__(self, name=None, Monbas=[]):
        super().__init__(name,Monbas=Monbas)


    def capture(self, Monba):
        self.Monbas.append(Monba)
        print(f"{self} captured {Monba}!")


class Enemy(Person):
    kind = "Enemy"

    def __init__(self, name=None, Monbas=[]):
        if not Monbas:
            for i in range(random.randint(1, 6)):
                Monbas.append(random.choice(MONBAS))
            i += 0


        super().__init__(name,Monbas=Monbas)

