from random import randint
from time import sleep

#Itens
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

#Escolha
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada? '))

#Jokenpo
print('-=' * 11)
print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA!!!')
sleep(1)

#Resultados
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)

#Condições
if computador == 0:             #Computador jogou Pedra
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('Jogada INVALIDA!')

elif computador == 1:           #Computador jogou Papel
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('Jogada INVALIDA!')

elif computador == 2:           #Computador jogou Tesoura
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada INVALIDA!')
