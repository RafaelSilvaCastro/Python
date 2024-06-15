#calcular a raiz quadrada de um numero

import math

# print(math.sqrt(25))
def calcularRaiz(numero):
    raizQuadrada = math.sqrt(numero)
    print(f'A raiz quadrada e: {raizQuadrada}')

# calcularRaiz()

def calcularNumeroAoQuadrado(numero):
    potencia = numero * numero
    print(f'O numero ao quadrado e: {potencia}')

calcularRaiz(81)
calcularNumeroAoQuadrado(10)