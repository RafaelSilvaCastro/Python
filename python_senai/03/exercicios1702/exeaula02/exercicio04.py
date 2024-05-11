#Crie um programa em Python que peça para o usuário digitar dois números, logo após o programa deve exibir qual o maior e qual o menor número digitado.
num1 = int(input("Digite um primeiro numero: "))
num2 = int(input("Digite um segundo numero: "))

if num1 > num2:
    print("O Primeiro numero digitado e maior que o segundo numero digitado")
if num1 < num2:
    print("O segundo numero e maior que o primeiro numero digitado")
else:
    print("Os numeros sao iguais")