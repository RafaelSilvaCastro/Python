#1.1 Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
numeros = ('um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')
for indice in range(5):
    print(numeros[indice])
    
#1.2 Seu programa deverá ler um número pelo teclado (entre 0 e 10) e mostra-lo por extenso.
num = int(input("Digite um numero de 0 a 10: "))
extenso = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')

if num > 10:
    print('Numero invalido')
else:
    print(extenso[num])
        



    
    