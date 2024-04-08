#2 Crie uma tupla preenchida com os 16 times da Tabela do Campeonato Paulista Serie A de Futebol, na ordem de colocação. Depois mostre:

#A) Apenas os 3 primeiros colocados.
#B) Os últimos 3 colocados da tabela.
#C) Uma lista com os times em ordem alfabética.
#D) Em que posição na tabela está o time do São Paulo.

tabela = ('Palmeiras','Santos','Bragantino','Sao Paulo','Novorizontino','Sao Bernardo','Inter de Limeira','Ponte Preta','Agua Santa','Mirassol','Corinthians','Botafogo-SP','Portuguesa','Guarani','Ituano','Santo Andre')

for i in range(len(tabela)):
    print(tabela[i])
print(15*'-')

for i in range(0,3):
    print(tabela[i])
print(15*'-')

for i in range(13,16):
    print(tabela[i])
print(15*'-')

sorted_tabela = sorted(tabela)
for i in range(len(sorted_tabela)):
    print(sorted_tabela[i])
print(15*'-')

for i in range(0,len(tabela)):
    if tabela[i] == 'Sao Paulo':
        posicao_sp = tabela.index(tabela[i])
        print('A posicao do Sao Paulo e o',posicao_sp,"lugar")
print(15*'-')
