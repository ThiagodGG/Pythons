num = [5,9,1,2]
num [2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop(2)
num.insert(2, 2)
num.remove(2)

if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')

print(num)
print(f'essa lista tem {len(num)} elementos. ')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}.', end='')

for c, v in enumerate(valores):
    print(f'\nNa posição {c} encontrei o valor {v}!')

#valores2 = list()
#for cont in range (0, 5):
#    valores2.append(int(input('Digite um valor: ')))

#for c, v in enumerate(valores2):
#    print(f'Na posição {c} encontrei o valor {v}! ')
#print('Fim da lista!')


a = [2,3,4,7]
b = a[:]
b[2]=8
print(f'A lista A: {a}')
print(f'A lista B: {b}')

