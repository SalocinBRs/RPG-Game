class Monba:

    def __init__(self, type_, especie, name=None, level=1):
        self.type_ = type_
        self.especie = especie
        self.level = level
        if name:
            self.name = name
        else:
            self.name = especie


    def __str__(self):
        return f'{self.especie} ({self.level})'


    def atacar(self, pokemon):
        print(f'o {self.especie} atacou o {pokemon.especie}')

my_monba = Monba('animal', 'Baran')
solenvir_monba = Monba('planta', 'Fryrt')
my_monba.atacar(solenvir_monba)
print(f"{my_monba}")
print(f"{solenvir_monba}")
