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

    def __init__(self, name=None, Monbas=[], money=100):
        if name is None:
            self.name = random.choice(NAMES)
        else:
            self.name = name

        self.Monbas = Monbas
        self.money = money

    def __str__(self):
        return f'{self.name}'


    def show_Monbas(self):
        print(f"Monbas de {self.name}")
        for monbinha in self.Monbas:
            print(monbinha)

    
    def choice_monba(self):
        for i, monba in enumerate(self.Monbas):
            print(f"{i + 1} - {monba}")
        while True:
            try:
                choice = int(input("Escolha: "))
                chosen = self.Monbas[choice - 1]
                print(f"eu conjuro voce!!! {(monba.name).upper()}")
                return chosen
            except:
                print("escolha invalida")

    def figth(self, enemy):
        print(f"{self.name} batalha com{ enemy.name}")
        print("~~" * 20)
        
        enemy.show_Monbas()
        my_monba = self.choice_monba()
        enemy_monba = enemy.choice_monba()
        
        while True:
            victory = my_monba.attack(enemy_monba)
            if victory:
                print(f"{self.name} ganhou")
                self.earn_money(20)
                break
            enemy_victory = enemy_monba.attack(my_monba)
            if enemy_victory:
                print(f"{enemy.name} ganhou")
                del my_monba
                break


    def show_money(self):
        print(f"{self.name} tem {self.money} dinheiros")
    

    def earn_money(self, money):
        self.money += money
        print(f"{self.name} ganhou {money} dinheiros")



class Player(Person):
    kind = "Player"

    def __init__(self, name=None, Monbas=[]):
        super().__init__(name,Monbas=Monbas)


    def capture(self, Monba):
        self.Monbas.append(Monba)
        print(f"{self} selou {Monba}!")

    
    def explore(self):
        monba = random.choice(MONBAS)
        chance = random.random()
        if chance >= 0.7:
            print(f"{monba} apareceu")
            choice = input("Selar? [y/n] ")
            if choice == 's':
                if random.random() >= 0.8:
                    self.capture(monba)
                else:
                    print("Monba Fugiu")
        else:
            print("Nada ocorreu")
        print()

    


class Enemy(Person):
    kind = "Enemy"

    def __init__(self, name=None, Monbas=[]):
        super().__init__(name,Monbas=Monbas)
        if not Monbas:
            for i in range(random.randint(1, 6)):
                Monbas.append(random.choice(MONBAS))
            i += 0

    
    def choice_monba(self):
        chosen = random.choice(self.Monbas)
        return chosen
