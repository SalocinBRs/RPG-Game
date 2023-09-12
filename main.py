from person import *
from monba import *

def choice_first_monba(player):
    print(f"{player.name} choice your first Monba!")
    first = monba.MonbaAnimal("Pikaro", level=3)
    second = monba.MonbaAnimed("Squirtleto", level=3)
    third = monba.MonbaAnimal("Bulbazaur", level=3)

    print("you have 3 choices")
    print(f"1 - {first}\n2 - {second}\n3 - {third}")

    while True:
        try:
            resposta = int(input("choice one: "))
            if resposta == 1:
                player.capture(first)
                print("~~" * 15)
                break
            elif resposta == 2:
                player.capture(second)
                print("~~" * 15)
                break
            elif resposta == 3:
                player.capture(third)
                print("~~" * 15)
                break
            else:
                print("wrong answer")
        except ValueError:
            print("wrong answer")

eu = Player(name="Nicolas")
choice_first_monba(eu)


inimigo = Enemy(name="Solenvir", Monbas=[monba.MonbaAnimed("Jigglypuffo")])

eu.figth(inimigo)