from person import *


from monba import *


import time


from inicio import historia


def choice_first_monba(player):
    print(f"{player.name} Essses são os 3 primeiros Monbas, escolha um para ser seu!")
    first = monba.MonbaAnimal("Pikaro", level=30)
    second = monba.MonbaAnimed("Squirtleto", level=3)
    third = monba.MonbaAnimal("Bulbazaur", level=3)

    print(f"1 - {first}\n2 - {second}\n3 - {third}")

    while True:
        try:
            resposta = int(input("O escolhido: "))
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
                print("resposta incorreta")
        except ValueError:
            print("resposta incorreta")


#TELA DE INICIO
name = historia()
eu = Player(name=name)

choice_first_monba(eu)

rival = Enemy("Solenvir", Monbas=[monba.MonbaAnimed("Squirtleto", level=3)])

eu.show_money()

eu.explore()
'''
inimigo = Enemy(name="Solenvir", Monbas=[monba.MonbaAnimed("Jigglypuffo"),monba.MonbaAnimed("Squirtleto")])
eu.figth(inimigo)
'''