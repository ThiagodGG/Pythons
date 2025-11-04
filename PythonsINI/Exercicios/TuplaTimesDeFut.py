times = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Bahia', 'Botafogo',
         'Fluminense', 'São Paulo', 'Vasco da Gama', 'Corinthians', 'Gremio', 'Ceara SC',
         'Atletico MG', 'Bragantino', 'Internacional', 'Santos', 'EC Vitoria', 'Fortaleza',
         'Juventude', 'Sport Recife')

print('-=' * 40)
print('Tabela do Brasileirão\n')
for t in times:
    print(t)
print('-=' * 40)

print(f'Os 5 primeiros times são: {times[0:5]} \n')
print('-=' * 40)

print(f'Os 4 ultimos times são: {times[-4:]} \n')
print('-=' * 40)

print(f'Times em ordem alfabetica {sorted(times)} \n')
print('-=' * 40)

print(f'O time do Vozão esta na {times.index("Ceara SC")+1}° posição \n')
print('-=' * 40)
