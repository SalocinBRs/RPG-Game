from person import *


from monba import *


import time


from inicio import historia


def salvar_jogo(eu):
    try:
        with open('database.db', 'wb') as arquivo:
            dump(eu, arquivo)
            print("Jogo salvo")
    except Exception as error:
        print("Algum erro ocorreu")
        print(error) 


def carregar_jogo():
        try:
            with open('database.db', 'rb') as arquivo:
                eu = load(arquivo)
                print("Jogo Carregado")
                return eu
        except Exception as error:
            print("Algum erro ocorreu")
            print(error) 


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
            elif resposta == 4:
                salvar_jogo(eu)
            else:
                print("resposta incorreta")
        except ValueError:
            print("resposta incorreta")


#TELA DE INICIO
eu = carregar_jogo()

if not eu:
    name = historia()
    eu = Player(name=name)

    choice_first_monba(eu)

    rival = Enemy("Solenvir", Monbas=[monba.MonbaAnimed("Squirtleto", level=3)])
    eu.figth(rival)
    salvar_jogo(eu)

rival = Enemy("Solenvir", Monbas=[monba.MonbaAnimed("Squirtleto", level=3)])

while True:
    print("~~" * 20)
    print("O que deseja fazer?")
    print("1 - Explorar mapa")
    print("2 - Lutar com um inimigo")
    print("3 - Mostrar Monbas disponíveis")
    print("4 - Salvar Jogo")
    print("5 - Novo jogo")
    print("9 - Sair")

    try:
        resposta = int(input(""))
    except ValueError:
        print("")

    if resposta == 1:
        eu.explore()
    if resposta == 2:
        inimigo = Enemy(name=None)
        eu.figth(inimigo)
    if resposta == 3:
        print("")
        eu.show_Monbas()
    if resposta == 9:
        break
    if resposta == 4:
        salvar_jogo(eu)
        break
    if resposta == 5:
        pass
    else:
        print("")
