def conta():
    opc=1
    valores=[]
    while opc != 0:
        prestacao = int(input("Digite o valor da conta a ser paga ou digite 0 para encerrar o programa: "))
        if prestacao == 0:
           break        
        dias = int(input("Digite os dias em atraso: "))   
        juros = prestacao*(0.001 * dias)
        atraso = prestacao*(0.03 * dias)
        total = prestacao+juros+atraso
        print(f"O valor da prestação com juros e atrasos a ser paga é: {total}")
        extrato = [dias,juros,atraso,total]
        valores.append(extrato)
        print(f"Valores calculados: {extrato}")

conta()