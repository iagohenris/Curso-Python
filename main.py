import pickle
import random
from pokemon import *
from pessoa import *

def escolher_pokemon_inicial(player):

    print('Olá {}, você poderá escolher agora qual Pokémon que irá lhe acompanhar nessa jornada!'.format(player))

    bulbasaur = PokemonPlanta('Bulbasaur', level=1)
    squirtle = PokemonAgua('Squirtle', level=1)
    charmander = PokemonFogo('Charmander', level=1)

    print('Você possui 3 opções: ')
    print('1 - ', bulbasaur)
    print('2 - ', squirtle)
    print('3 - ', charmander)

    while True:
        escolha = input("Escolha o seu Pokémon: ")

        if escolha == '1':
            player.capturar(bulbasaur)
            break
        elif escolha == '2':
            player.capturar(squirtle)
            break
        elif escolha == '3':
            player.capturar(charmander)
            break
        else:
            print('Escolha Inválida!')

def salvar_jogo(player):
    try:
        with open("database.db", "wb") as arquivo:
            pickle.dump(player, arquivo)
            print("Jogo Salvo com Sucesso!")
    except Exception as error:
        print("Erro ao salvar jogo!")
        print(error)

def carregar_jogo():
    try:
        with open("database.db", "rb") as arquivo:
            player = pickle.load(arquivo)
            print("Jogo carregado com Sucesso!")
            return player
    except Exception as error:
        print("Save não encontrado!")



if __name__=="__main__":
    print("------------------")
    print("Bem-vindo ao mundo pokémon")
    print("------------------")

    player = carregar_jogo()

    if not player:

        nome = input("Olá, qual o seu nome: ")
        player = Player(nome)
        print("{} esse é o mundo pokémon, "
              "a partir de agora sua missão é se tornar um Mestre Pokémon!".format(player))
        print("Capture o máximo de pokémons que conseguir e lute contra seus inimigos")
        player.mostrar_dinheiro()

        if player.pokemons:
            print("Já vi que você tem alguns pokémons")
            player.mostrar_pokemons()
        else:
            print("Você não tem nenhum pokémon, portanto precisa escolher um")
            escolher_pokemon_inicial(player)

        print("Agora que você possui seu pokémon, enfrente seu arqui-inimigo Gary ")
        gary = Inimigo(nome='Gary', pokemons=[PokemonFogo('Charmander', level=1)])
        player.batalhar(gary)
        salvar_jogo(player)

    while True:
        print("------------------")
        print("O que deseja fazer? ")
        print("1 - Explorar o mundo pokémon")
        print("2 - Enfrentar um inimigo")
        print("3 - Mostrar Pokeagenda")
        print("0 - Sair do jogo")
        escolha = input("Sua escolha: ")

        if escolha == "0":
            print("Fechando o jogo")
            break
        elif escolha == "1":
            player.explorar()
            salvar_jogo(player)
        elif escolha == "2":
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)
        elif escolha == "3":
            player.mostrar_pokemons()
            player.mostrar_dinheiro()
        else:
            print("Escolha inválida")


