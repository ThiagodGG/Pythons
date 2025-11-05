def contador(i, f, p):
    """
      --> Faz uma contagem e mostra na tela. 
    : param i : Inicio da contagem
    : param f : Fim da Contagem
    : param p : Passo da contagem
    : return: Sem retorno
    : Função criada por Thiago Barboza
    """
    

    c = i
    while c <= f:
        print(f'{c}', end='')
        c += p 
    print('FIM!')



help(contador)
