import random


def play():
    print("*******************************************")
    print("*****Bem vindo ao jogo de ADIVINHAÇÃO!*****")
    print("*******************************************\n")
    print("Pense em um nḿero de 1 a 20 para responder!\n")

    num = random.randint(1, 20)
    rodadas = 1
    tentativas_por_rodada = 0

    print(num)

    print("Nivel de dificuldade!\n")
    print("Nivel 1 facil!")
    print("Nivel 2 medio!")
    print("Nivel 3 dificil!\n")

    nivel = int(input("Escolha o nivel: "))

    if nivel == 1:
        tentativas_por_rodada = 20
    if nivel == 2:
        tentativas_por_rodada = 10
    if nivel == 3:
        tentativas_por_rodada = 5

    while rodadas <= tentativas_por_rodada:
        resp = input("Digite sua resposta:")

        if not resp:
            print("Resposta não ceita digite um número!\n")
            continue

        intresp = int(resp)

        if num < intresp:
            print("Resposta maior que número secreto!\n")
        if num > intresp:
            print("Resposta menor que número secreto!\n")

        acertou = num == intresp
        errou = num != intresp

        if acertou:
            print("Você ACERTOU parabéns!\n")
            break
        elif errou:
            print("Você ERROU! Tente novamente!\n")

        rodadas += 1


if __name__ == "__main__":
    play()
