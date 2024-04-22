#Crie um programa em Python que peça para o usuário digitar a idade de uma pessoa. Faça com que o programa verifique e exiba se a pessoa e de maior ou não.
idade = 18
idade_digitada = int(input("Digite sua idade: "))

if idade_digitada >= idade:
    print("Usuario e maior de idade")
else:
    print("Usuario menor de idade")
