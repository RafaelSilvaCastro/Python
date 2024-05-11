# crie um programa em python que contenha uma lista com 5 modelos de veiculos. Exibi-los em ordem.

lista_carro = []
for i in range(5):
    carro = input(f'Digite o nome do {i+1}º carro ')
    lista_carro.append(carro)
    
#for para exibir
for carro in lista_carro:
    sorted_carros = sorted(lista_carro)
print(sorted_carros)