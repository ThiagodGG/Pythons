pessoas = {'Nome': 'Iarley', 'Sexo': 'M', 'Idade': 19}
pessoas['Nome'] = 'Thiago'
pessoas['Peso'] = 107.8
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos. ')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = []
estado1 = {'uf': 'Ceara', 'Sigla': 'CE'}
estado2 = {'uf': 'Bahia', 'Sigla': 'BA'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])

estado3 = dict()
brasil3 = list()
for c in range(0, 3):
    estado3['uf'] = str(input('Unidade Federativa: '))
    estado3['sigla'] = str(input('Sigla do Estado: '))
    brasil3.append(estado3.copy())
for e in brasil3:
    for v in e.values():
        print(v, end=' ')
    print()


