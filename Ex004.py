N1 = int(input('Um valor: '))
N2 = int(input('Outro valor: '))
s = N1+N2
m = N1*N2
d = N1/N2
di = N1//N2
e = N1**N2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s,m,d), end=' ')
print('Divisão inteira {} e potencia {}'.format(di,e))


