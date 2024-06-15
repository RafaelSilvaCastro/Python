#01 - Faça um programa que tenha uma função chamada área(), quereceba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(largura,comprimento):
    areaTerreno = largura*comprimento
    return areaTerreno

largura = int(input('Digite a largura do terreno: '))
comprimento = int(input('Digite o comprimento do terreno: '))
print(f'A area do terreno e de: {area(largura,comprimento)}')
    