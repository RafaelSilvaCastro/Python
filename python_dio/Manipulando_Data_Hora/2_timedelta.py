from datetime import datetime, timedelta

tipo_carro = "G" # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.utcnow()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(days=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto ás {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(days=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto ás {data_estimada}")
else:
    data_estimada = data_atual + timedelta(days=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto ás {data_estimada}")
    
    

resultado = datetime(2024, 6, 12, 12, 10, 30) -  timedelta(hours=1)
print(resultado.time())
