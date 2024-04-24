#pedir para o usuario digitar 2 numeros
#exibir o mais e o menor

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

#verificando o maior e o menor numero
if num1 > num2:
    print('o numero ',num1,'e maior que ',num2)
elif num2 > num1:
    print("O numero ",num2,"e maior que",num1)
else:
    print("Os numeoros ",num1," e igual a ",num2)