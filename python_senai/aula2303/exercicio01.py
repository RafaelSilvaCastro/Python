lista_num = []
import math 
while True:
    num = int(input('Digite um numero: '))
    lista_num.append(num)
    
    resposta = int(input("Deseja sair? digite 0 "))
    if resposta == 0:
        break
minimo = min(lista_num)
maior = max(lista_num)
soma  = sum(lista_num)
mult = math.prod(lista_num)

print(12*'-')
print(f'A lista de numeros foi: {lista_num}')
print(f'A soma dos numeros e: {soma}')
print(f'A multiplicaçao dos numeros e: {mult}')
print(f'O menor numero digitado e: {minimo}')
print(f'O maior numero digitado e: {maior}')
print(12*'-')
    
    