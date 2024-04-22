#crie uma lista que leia do teclado 3 nomes de carros 
#logo apos, exiba corretamente os carro digitado

#for para criar
lista_carro = []
for i in range(3):
    carro = input(f'Digite o nome do {i+1}º carro ')
    lista_carro.append(carro)
    
#for para exibir
for carro in lista_carro:
    print(carro)