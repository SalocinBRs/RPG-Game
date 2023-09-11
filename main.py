import monba
import person

def choice_first_monba(Player):
    print(f"{Player.name} escolha o seu primeiro Monba!")
    first = monba.MonbaAnimal("Pikaro", level=3)
    second = monba.MonbaAnimed("Squirtleto", level=3)
    third = monba.MonbaAnimal("Bulbazaur", level=3)

    print("Você tem 3 escolhas")
    print(f"1 - {first}\n2 - {second}\n3 - {third}")

    while True:
        resposta = input("Qual será: ")
        if resposta == 1:
            Player.capture(first)
            break
        elif resposta == 2:
            Player.capture(second)
            break
        elif resposta == 3:
            Player.capture(third)
            break
        else:
            print("resposta invalida")

eu = monba.Player("nicolas")
print(eu)


