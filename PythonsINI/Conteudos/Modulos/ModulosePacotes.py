from Pacote import Numeros

#Programa principal
num = int(input('Digite um valor: '))
fat = Numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {Numeros.dobro(num)}.')
