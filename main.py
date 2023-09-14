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
'''
name = historia()
'''

name = 'Nicolas'
eu = Player(name=name)

choice_first_monba(eu)

rival = Enemy("Solenvir", Monbas=[monba.MonbaAnimed("Squirtleto", level=3)])
eu.figth(rival)

while True:
    print("~~" * 20)
    print("O que deseja fazer?")
    print("1 - Explorar mapa")
    print("2 = Lutar com um inimigo")
    print("9 - Sair")

    try:
        resposta = int(input(""))
    except ValueError:
        print("Resposta invalida")

    if resposta == 1:
        eu.explore()
    if resposta == 2:
        inimigo = Enemy(name=None)
        eu.figth(inimigo)
    if resposta == 9:
        break
