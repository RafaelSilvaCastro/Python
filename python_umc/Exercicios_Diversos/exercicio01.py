soma = 0
qtde = 0

while True:
    print("Digite 1 para colocar um numero:")
    print("Digite 2 para somatoria:")
    print("Digite 3 para quantidade de numeros:")
    print("Digite 4 para mostrar a media:")
    print("Digite 5 para sair:")
  
    decisao = int(input("Digite o numero para serviço desejavel: "))  
    
    if decisao == 1:
        num = float(input("Digite um numero: "))
        soma += num
        qtde = qtde + 1
    elif decisao == 2:
        print(f"A somatoria e: {soma}")
    elif decisao == 3:
        print(f"Numeros digitados foram {qtde}")
    elif decisao == 4:
        media = soma / qtde
        print(f"A media e: {media}")
    elif decisao == 5:
        break
