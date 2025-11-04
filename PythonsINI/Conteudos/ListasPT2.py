teste = list()
teste.append('Thiago')
teste.append(40)
#print(teste)
galera = list()
galera.append(teste[:])
teste[0] = 'Iarley'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera2 = [ ['João', 19], ['Ana', 20], ['joaquim', 66], ['Maria', 45] ]
print(galera2[1])
for p in galera2:
    print(f'{p[0]} tem {p[1]} anos de idade.')

galera3 = list()
dado = list()
totmai = totmen = 0
for c in range (0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera3.append(dado[:])
    dado.clear()

for p in galera3:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade. ')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade. ')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade. ')
