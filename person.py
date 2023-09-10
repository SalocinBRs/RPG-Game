import monba
class Person:

    def __init__(self, name=None, Monbas=[]):
        if name:
            self.name = name
        else:
            self.name = "Anonymous"

        self.Monbas = Monbas

    def __str__(self):
        return f'{self.name}'

    def show_Monbas(self):
        print("Monbas disponíveis")
        for monbinha in self.Monbas:
            print(monbinha)
    

class Player(Person,):
    kind = "Player"

    def capture(self, monba):
        self.Monbas.append(monba)
        print(f"{self} capturou {monba}")


class Enemy(Person):
    kind = "Enemy"


my_monba1 = monba.MonbaAnimal("animal")
my_monba2 = monba.MonbaZombie("zombie")
monba


eu = Player(name="Protagonista",Monbas=[my_monba1, my_monba2])
eu.capture(monba.MonbaAnimal('galileu'))

eu.show_Monbas()