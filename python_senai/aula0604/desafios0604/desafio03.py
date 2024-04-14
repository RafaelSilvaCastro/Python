# 03 Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionario se por acaso o ctps for diferente de zero, o dicionario recebera tambem o ano de contratação e o salario. Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar.

# sabaendo que ele vai se aposentar apos 35 anos de contribuição 

aposentadoria = {}

nome = input('Digite seu nome: ')
ano_nasc = int(input('Digite o ano de nascimento: '))
ano_atual = int(input('Digite o ano Atual: '))
num_carteira = int(input('Digite o numero de sua carteira: '))
idade = ano_atual - ano_nasc
while True:
    if num_carteira !=0:
        ano_contratacao = int(input('Digite seu ano de contratação: '))
        sal = int(input("Digite seu salario: "))
        contibuicao = ano_atual - ano_contratacao
        aposentadoria [nome] = [idade,num_carteira,contibuicao,sal]
        if contibuicao >= 35:
            print('voce e aposentado')
        else:
            ano_falta = 35 - contibuicao
            ano_aposentar = idade + ano_falta
            print(20*"=")
            print(f"Seu salario e de: R${sal}")
            print(f'{nome} voce nao se aposentou ainda, falta {ano_falta} anos!')
            print(f"Você ira se aposentar com {ano_aposentar} anos.")
        break
    else:
        print(f'Escreva um numero de carteira veridico!!')
        num_carteira = int(input('Digite o numero de sua carteira: '))

print(f"O dicionario e: {aposentadoria}")      


