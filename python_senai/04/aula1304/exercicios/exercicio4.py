# Exercício 4
# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar(). A primeira função vai sortear 5 números de 1 a 10 e vai coloca-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.

import random

def sorteio():
    lista_num = []
    for i in range(5):
        num_ale = (random.randint(1,10))
        lista_num.append(num_ale)
    return lista_num
    
def somarPar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    return soma 
        
numeros = sorteio()   
print("Numeros sorteados: ", numeros)
print("Soma dos numeros pares sorteados: ", somarPar(numeros))