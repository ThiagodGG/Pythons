def somar (a=0, b=0, c=0):
    """
    Faz a soma de três valores e mostra o resultado na tela
    """
    s = a + b + c
    print(f'A soma vale {s} ')

somar(3, 2)


def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'na função teste, x vale {x}')


#Programa principal
n = 2
x = 5
print(f'No progarama principal, n vale {n}')
teste()
print(f'No programa principal, x vale {x}')


def somar (a=0, b=0, c=0):
    s = a + b + c
    return s


#Programa com 'RETURN'
somar(3,2,5)
r1 = somar (3, 2, 5)
r2 = somar (1, 7)
r3 = somar (4)
print(f'Meus calculos deram {r1}, {r2} e {r3}.')

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n= int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

def par(n=0):
    if n%2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
