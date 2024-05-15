menu = """
------- Menu -------
Digite
1 - Depositar
2 - Sacar
3 - Visualizar extrato
0 - Para sair
--------------------
"""

lembrete_saque = """
----------------------------------------
Lembretes:
E permitido realizar 3 saques diarios;
O limite maximo por saque e de R$500,00.
----------------------------------------
"""

saldo = 0
limite = 500
extrato = []
numero_saques = 0

while True:
    print(menu)
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1: # depositar
        valor = float(input("Digite a quantia que deseja depositar: "))
        saldo += valor
        extrato.append(valor)
        
        if valor < 0:
            print("Apenas aceitamos valores positivos!!!")
            
    elif opcao == 2: # sacar
        print(lembrete_saque)
        valor_saque = float(input("Digite o valor que deseja sacar: "))
        numero_saques += 1
        extrato.append(-valor_saque)
        
        if numero_saques > 3:
            print("Sua cota diaria de 3 saques foi ultrapassada!!!")  
        
        elif valor_saque <= 500:
            saldo -= valor_saque
            
        else:
            print("Valor não permitido pra saque!!!")
            
    elif opcao == 3:
        print(f"O saldo atual e: R${saldo:.2f}")
        print("Exibindo o extrato:")   
        for val in extrato:
            if val > 0:
                print(f"Entrada: R${val:.2f}")
            elif val < 0:
                print(f"Saida: R${val:.2f}")
        
    elif opcao > 3:
        print("Escolha uma opção valida!!!")
   
    elif opcao == 0:
        break
    
    
    