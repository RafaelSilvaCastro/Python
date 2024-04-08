# 03 Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionario se por acaso o ctps for diferente de zero, o dicionario recebera tambem o ano de contratação e o salario. Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar.

# sabaendo que ele vai se aposentar apos 35 anos de contribuição 

aposentadoria = {}

nome = input('Digite seu nome: ')
ano_nasc = int(input('Digite o ano de nascimento: '))
num_carteira = int(input('Digite o numero de sua carteira: '))
ano_atual = datetime.datetime.now()
idade = ano_atual - ano_nasc

print(idade) 