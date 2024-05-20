# salvar informações dos proprietarios de veiculos

#cadastramento
def informacoes():
    pessoas = {
        "OTM 2022": ["MARLON", "NEW CIVIC", 2022],
        "AAA-5551": ["ENZO", "GOLF", 2021],
        "ERM-5431": ["RAUL", "ECLIPSE", 2023],
        "XXX-0000": ["JONATHAN", "LANCER", 2022],
        "HQW-5678": ["GUSTAVO", "NEW BEATLE", 2023]
    }
    return pessoas

# exibir todos os dados do dicionario (um em baixo do outro)
for placa, cadastro in pessoas.items():
    print(f"Placa: {placa} Proprietario: {cadastro[0]} Modelo: {cadastro[1]} Ano Veículo: {cadastro[2]}")
print("="*100)
# exibir todas as placas de veiculos (somente as placas)
for placa, cadastro in pessoas.items():
    print(placa)
print("="*100)

# exibir todos os proprietarios de veiculos(somente os proprietarios)
for placa, cadastro in pessoas.items():
    print(f"{cadastro[0]}") # indice 0 = prprietario, 1 = modelo, 2 = ano veiculo
print("="*100)
