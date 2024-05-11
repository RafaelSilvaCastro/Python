# Exercício 3
# Faça um programa que tenha uma função chamada maior(), que
# receba três parâmetros com valores inteiros.

# Seu programa tem que analisar todos os valores e dizer qual deles é
# o maior.

def maior(n1,n2,n3):
    maiorNumero = max(n1,n2,n3)
    return maiorNumero

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
n3 = int(input("Digite um numero: "))

print(maior(n1,n2,n3))
