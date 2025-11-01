# Contador lateral
cont = 1
while cont <= 10:
    print(cont, '->', end='')
    cont += 1
print('Acabou')

# Usnado o "break"  
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vele {}'.format(s))

# FORMATO PYTHON 3.6 f Strings
nome = 'Jose'
idade = 33
salario = 1000.0
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}')
