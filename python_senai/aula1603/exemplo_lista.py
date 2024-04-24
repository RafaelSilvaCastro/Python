lista_bancos = ['Banco do Brasil','Nubank','Inter']
#exibir lista
print(lista_bancos)
print(20*"-")

for banco in lista_bancos:
    print(banco)
print(20*"-")

for i in range(len(lista_bancos)):
    print(lista_bancos[i])
print(20*"-")

#adicionar elemento a lista
lista_bancos.append('Itau')
lista_bancos.append('C6')
for i in range(len(lista_bancos)):
    print(lista_bancos[i])
print(20*"-")

