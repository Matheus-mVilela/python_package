import game_sorted_number
import game_forca


def play():
    print("*****************************")
    print("*****Bem vindo ao jogos!*****")
    print("*****************************\n")

    print("Jogo 1 (--Sorted Number--)", "-", "Jogo 2 (--Forca--)")

    game = int(input("Escolha um jogo:"))

    if game == 1:
        game_sorted_number.play()

    elif game == 2:
        game_forca.play()


if __name__ == "__main__":
    play()
