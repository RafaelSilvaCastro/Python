carros = ('Gol','Uno','Fiesta','Palio','Celta','Corsa')

#metodo para capturar o tamanho de um elemento
#### len ####
tamanho_tupla = len(carros)
print(tamanho_tupla)

#exibindo corretamente a tupls
for aux in range(tamanho_tupla):
    print(carros[aux])
    
#1 verificar se tem uma kombi
if carros[aux] == "Kombi":
    print("Tem uma Kombi")
else:
    print("Nao tem Kombi")
    
#2 verificar se tem uma kombi
# verificar = False
# for aux in range(tamanho_tupla):
#     if carros[aux] == 'Kombi':
#         verificar = True
# if verificar == True:
#     print('Tem Kombi')
# else:
#     print("Nao tem Kombi")
    
#3 verificar se tem uma kombi 
# if 'Kombi' in carros:
#     print("Tem kombi")
    
#4 verificar se tem uma kombi
# if 'Kombi' not in carros:
#     print('Nao tem Kombi')


