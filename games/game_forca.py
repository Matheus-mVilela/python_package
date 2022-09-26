import random


def play():
    menssgem_abertura()
    palavra = busca_palavra()

    erros = len(palavra)
    letras_escondidas = ["_" for letra in palavra]
    enforcado = False
    acertou = False

    while not enforcado and not acertou:
        print(letras_escondidas)

        chute = input("Digite seu chute:").strip().upper()

        if chute in palavra:
            index = 0
            for letra in palavra:
                if chute == letra:
                    print("Encontrado letra {} na posição {}".format(chute, index))
                    breakpoint()
                    letras_escondidas[index] = letra

                index += 1

        else:
            erros -= 1

        if "_" not in letras_escondidas:
            acertou = True
            print("ACERTOU, GAME WIN")

        if erros == 0:
            enforcado = True
            print("ENFORCADO, GAME OVER")

    print("Fim de Jogo")


def menssgem_abertura():
    print("*******************************************")
    print("*****Bem vindo ao jogo de Forca!*****")
    print("*******************************************")


def busca_palavra():
    lista_palavras_txt = open("./games/lista_palavras.txt", "r")
    lista_palavras_py = []

    for palavra in lista_palavras_txt:
        palavra.strip()
        lista_palavras_py.append(palavra)
    lista_palavras_txt.close()
    palavra = random.choice(lista_palavras_py).upper()

    return palavra


if __name__ == "__main__":
    play()
