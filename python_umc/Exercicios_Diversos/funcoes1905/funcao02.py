def calcular_valor_prestacao(valor_prestacao, dias_atraso):
    """Calcula o valor a ser pago considerando a multa e os juros por atraso."""
    if dias_atraso > 0:
        multa = valor_prestacao * 0.03
        juros = valor_prestacao * (0.001 * dias_atraso)
        valor_total = valor_prestacao + multa + juros
    else:
        valor_total = valor_prestacao
    return valor_total

def exibir_relatorio(transacoes):
    """Exibe um relatório das transações realizadas."""
    print("\nRelatório de Transações Realizadas:")
    print("Prestação | Valor Original | Valor Pago | Dias de Atraso")
    for transacao in transacoes:
        prestacao, valor_original, valor_pago, dias_atraso = transacao
        print(f"{prestacao:10} | {valor_original:13.2f} | {valor_pago:10.2f} | {dias_atraso:13}")

def calcular_total_pago(transacoes):
    """Calcula o valor total de todas as prestações pagas."""
    total_pago = sum(transacao[2] for transacao in transacoes)
    return total_pago

def solicitar_prestacao():
    """Solicita ao usuário o valor da prestação e os dias de atraso."""
    while True:
        entrada = input("Digite o valor da prestação ou 'Fim de Programa' para encerrar: ")
        if entrada.lower() == "fim de programa":
            return None, None
        
        try:
            valor_prestacao = float(entrada)
            dias_atraso = int(input("Digite o número de dias em atraso: "))
            return valor_prestacao, dias_atraso
        except ValueError:
            print("Entrada inválida. Tente novamente.")

def main():
    transacoes = []
    
    while True:
        valor_prestacao, dias_atraso = solicitar_prestacao()
        if valor_prestacao is None and dias_atraso is None:
            break
        
        valor_pago = calcular_valor_prestacao(valor_prestacao, dias_atraso)
        transacoes.append((valor_prestacao, valor_prestacao, valor_pago, dias_atraso))
        
        print(f"Valor a ser pago: R${valor_pago:.2f}")
    
    exibir_relatorio(transacoes)
    total_pago = calcular_total_pago(transacoes)
    print(f"\nValor total de prestações pagas: R${total_pago:.2f}")


main()
