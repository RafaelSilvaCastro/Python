produtos = [['banana','maca'],[3.50,5.50]]

#qual o preço da banana?
for indice in range(len(produtos[0])):
    if produtos[0][indice] == 'banana':
        print(f'O preco da banana e: R${produtos[1][indice]}')
        break
else:
    print('A banana nao esta disponivel na lista de produtos.')
    
#qual o preço do abacate?
for ind1 in range(len(produtos[0])):
    if produtos[0][ind1] == 'maca':
        print(f'O preco da maca e: R${produtos[1][ind1]}')
        break
else:
    print('O abacate não esta disponivel na lista de produtos.')
