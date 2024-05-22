# Desafio 01

# Uma empresa de telecomunicações deseja criar uma solução algorítmica que ajude aos seus clientes a escolherem o plano de internet ideal com base em seu consumo mensal de dados. Para a resolução, você pode solicitar ao usuário que insira o seu consumo, sendo este um valor 'float'. Crie uma função chamada recomendar_plano para receber o consumo médio mensal de dados informado pelo cliente, além de utilizar estruturas condicionais para fazer a verificação e retornar o plano adequado.

# Planos Oferecidos:

# - Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB.
# - Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB.
# - Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB.

# Entrada
# Como entrada solicite o consumo médio mensal de dados em GB (float).

# Saída
# Retorne o plano ideal para o cliente de acordo com o consumo informado na entrada.

# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
# TODO: Retorne o plano de internet adequado:
    

# Solicita ao usuário que insira o consumo médio mensal de dados:
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:


def recomendar_plano(consumo):
  
  if consumo < 10:
    print("O plano recomendao e: Plano Essencial Fibra - 50Mbps.")
  elif consumo <= 20:
    print("O plano recomendao e: Plano Prata Fibra - 100Mbps.")
  elif consumo > 20:
    print("O plano recomendao e: Plano Premium Fibra - 300Mbps.")
  
  #return consumo

consumo = float(input("Digite seu consumo: "))

recomendar_plano(consumo)