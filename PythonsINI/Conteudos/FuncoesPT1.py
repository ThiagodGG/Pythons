def lin():
    print('-' * 30)


#primeiro programa
lin()
print(' VEGETTA')
lin()
print(' SON GOHAN ')
lin()
print(' SON GOKU ')
lin()


def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


#segundo programa
titulo(' BULMA ')
titulo(' VIDEL ')
titulo(' CHICHI ')


def soma(a , b):
    s = a + b
    print(s)


#terceiro programa
soma(7, 5)
soma(9, 6)
soma(3, 5)


def soma(c, e):
    print(f'C = {c} e E = {e}')
    s = c + e
    print(f'A soma C + E = {s}')


#quarto programa
soma(4, 5)
soma(7, 8)
soma(6, 1)


def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros')


#quinto programa
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 6, 2, 7)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


#Sexto programa
valores = [6, 3, 5, 6, 7, 9]
dobra(valores)
print(valores)


def soma( * valores):
    s = 0
    for num in valores:
        s += num
    print(f'somando os valores {valores} temos {s}')


#Setimo programa
soma(5, 2)
soma(2, 9, 4)
