#4 Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram o números pares.

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
n3 = int(input("Digite um numero: "))
n4 = int(input("Digite um numero: "))

num_tupla = (n1,n2,n3,n4)
print(15*'-')

num_rep = num_tupla.count(9)
print("A quantidade de numeros 9 foi de: ",num_rep)
print(15*'-')

for i in range(len(num_tupla)):
    if num_tupla[i] == 3:
        posicao_num = num_tupla.index(num_tupla[i])
        print('A posicao do numero 3 e: ',posicao_num+1)

for num in num_tupla:
    if num % 2 == 0:
        print("Os numeros pares digitados foram: ",num)








