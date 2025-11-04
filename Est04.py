Velocidade = float(input('Qual é a velocidade atual do carro? '))
if Velocidade > 80:
    print ('MULTADO! Você excedeu o limite permitido que é de 80km/h!')
    multa = (Velocidade -  80) * 7
    print ('Você deve pagar uma multa de R$ {:.2f}'.format(multa))
print('Tenha um bom dia e dirija com segurança!')

