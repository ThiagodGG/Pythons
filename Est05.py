nome = str(input('Qual é o seu nome: '))
if nome == 'Thiago':
    print('Que nome bonito!')
elif nome == 'Iarley' or nome == 'Neuma' or nome == 'Ocelio':
    print ('Seu nome é absolute CINEMA!')
elif nome in 'Raquel Manuella Auri Auricelia':
    print ('Belissimo nome!')
else:
    print('Seu nome é normal!')
print('Tenha um bom dia, {}!'.format(nome))

