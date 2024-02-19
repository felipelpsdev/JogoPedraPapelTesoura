import random
import os

while True:

    vitorias = 0
    derrotas = 0
    empates = 0

    opcoes = {1: 'PEDRA', 2: 'PAPEL', 3: 'TESOURA'}


    print("============|PEDRA| |PAPEL| |TESOURA| ============")
    nome = input("DIGITE O NOME DO JOGADOR: ")
    if nome == 'sair':
        break

    rodadas = int(input('DIGITE A QUANTIDADE DE RODADAS: '))
    os.system('cls')
    for i in range(rodadas):
        print('====== JOGO ======')
        print('1 - PEDRA')
        print('2 - PAPEL')
        print('3 - TESOURA')
        jogada = int(input('SUA JOGADA: '))

        computador = random.randint(1, 3)
        print("Você escolheu:", opcoes[jogada])
        print("Computador escolheu:", opcoes[computador])
        
        if jogada == computador:
            print("EMPATE")
            empates += 1
        elif (jogada == 1 and computador == 3):
            print(nome, "VENCEU !") #felIpe venceu
            vitorias += 1
        elif (jogada == 2 and computador == 1):
            print(nome, "VENCEU !") #felIpe venceu
            vitorias += 1
        elif (jogada == 3 and computador == 2):
            print(nome, "VENCEU !") #felIpe venceu
            vitorias += 1
        else:
            print("COMPUTADOR VENCEU!")
            derrotas += 1
            
    print("======== RESULTADO FINAL =========")
    print(nome, ":", vitorias, "vitórias")
    print("Computador: ", derrotas,"vitórias")
    print("Empates: ", empates)
    
    input("Pressione Enter para continuar...")
    os.system('cls')
print(":::::::: Jogo encerrado. Até mais!! :::::::::::")
