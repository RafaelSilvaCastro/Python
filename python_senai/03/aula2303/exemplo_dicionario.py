#tupla ()
#lista []
#dicionario {}

carros = {
    'uno':'vermelho',
    'gol':'branco',
    'celta':'prata',
    'corsa':'azul',
    'palio':'verde'
}

#adicionar item
carros['celta']='amarelo'
print(carros)

#exibir somente os modelos dos veiculos
print(carros.keys())

#adicionar mais de um item 
# carros2 = {
#     'uno':['vermelho','4 portas']
# }

#exibir as cores dos carros
print(carros.values())

#exibir o dicionario inteiro
print(carros.items())
