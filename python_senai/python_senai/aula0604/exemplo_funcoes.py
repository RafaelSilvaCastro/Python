import exemplo_funcoes_externas #importa funções externas 

def somarDoisNumeros(n1,n2):
    soma = n1 + n2
    print(f'Soma = {soma}')
    
def subtrairDoisNumeros(n1,n2):
    subtrair = n1 - n2
    print(f'Subtracao = {subtrair}')

def multDoisNumeros(n1,n2):
    mult = n1 * n2
    print(f'Multiplicação = {mult}')
    
def divDoisNumeros(n1,n2):
    divisao = n1 / n2
    print(f'Divisão = {divisao}')

numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))
    
print(30*'-')
somarDoisNumeros(numero1,numero2)
subtrairDoisNumeros(numero1,numero2)
multDoisNumeros(numero1,numero2)
divDoisNumeros(numero1,numero2)
exemplo_funcoes_externas.calcularRaiz(numero1) #usando uma função externa 

#criar uma função externa que faça a potencia que calcule o valor do numero 2 ao quadrado
exemplo_funcoes_externas.calcularNumeroAoQuadrado(numero2)