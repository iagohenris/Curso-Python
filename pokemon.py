import random


class Pokemon:
    def __init__(self, especie, level=None, nome=None):
        self.especie = especie

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        if nome:
            self.nome = nome
        else:
            self.nome = especie

        self.ataque = self.level * 5
        self.vida = self.level * 10
    def __str__(self):
        return '{} ({})'.format(self.nome, self.level)


    def atacar(self, pokemon):
        ataque_efetivo = int((self.ataque * random.random() * 1.3))
        pokemon.vida -= self.ataque
        print('{} perdeu {} pontos de vida'.format(pokemon, ataque_efetivo))

        if pokemon.vida <= 0:
            print("{} foi derrotado".format(pokemon))
            return True
        else:
            return False

class PokemonAgua(Pokemon):
    tipo = 'Água'

    def atacar(self, pokemon):
        print("{} lançou jato d'água em {}".format(self, pokemon))
        return super().atacar(pokemon)


class PokemonPlanta(Pokemon):
    tipo = 'Planta'

    def atacar(self, pokemon):
        print("{} lançou folhas de navalha em {}".format(self, pokemon))
        return super().atacar(pokemon)

class PokemonEletrico(Pokemon):
    tipo = 'Eletrico'

    def atacar(self, pokemon):
        print("{} lançou raio do trovão em {}".format(self, pokemon))
        return super().atacar(pokemon)

class PokemonFogo(Pokemon):
    tipo = 'Fogo'

    def atacar(self, pokemon):
        print("{} lançou bola de fogo em {}".format(self, pokemon))
        return super().atacar(pokemon)

class Corsola(PokemonAgua):
    tipo2 = 'Pedra'


