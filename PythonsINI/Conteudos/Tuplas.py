lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') #Tuplas são imutaveis
print(lanche)

lanche2 = ('Pastel', 'Cajuina', 'Coxinha', 'DinDin') #Usando o FOR normal
for comida in lanche2:
    print(f'Eu vou comer {comida}')
print('To de buxo cheio!\n')

lanche3 = ('Chocolate', 'Batata Frita', 'Bolinha de quiejo', 'Espetinho', 'Tapioca') #Usando o RANGE 
for cont in range(0, len(lanche3)):
    print(f'Eu vou comer {lanche3[cont]}')
print('A comida está uma delicia!\n')

lanche4 = ('Panelada', 'Feijoada', 'Sorvete', 'Sarrabulho') #Mostrando a posição de cada item
for pos, rango in enumerate(lanche4):
    print(f'Eu vou comer  {rango} na posição {pos}')
print('Eu comi demais!\n')

lanche5 = ('Peixe frito', 'Rizole', 'Bolo', 'HotDog', 'Açai', 'Pirulito')  #Itens organizados com o comando "Sorted"
print(sorted(lanche5))

numA = (3,7,9,5,2,1,8)
numB = (8,4,7,10,6,9,5)
numC = numA + numB
print(numC)
print(numC.count(3))
print(numC.index(5))

pessoa = ('Thiago', 19, 'M', 107.5)
print (pessoa)
