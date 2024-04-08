# 01 Escreva um programa que:
#     leia duas notas de varios alunos e armazena tais notas em um dicionaario, onde a chave e o nome do aluno. A entrada de dados deve terminar quando for lida uma string vazia como nome.
    
#     No final exibir os nomes dos alunos com suas respectivas notas 

notas = {}
while True:
    nome = input('Digite o nome do aluno: ')
    num1 = int(input('Digite a 1 nota: '))
    num2 = int(input('Digite a 2 nota: '))
    notas [nome] = [num1,num2]
    
    res = input("Deseja adicionar mais alunos? S/N ")
    res = res.upper()
    if res == "N":
        break

for a, b in sorted(notas.items()):
    print(f"O aluno(a) {a}, tirou as notas: {b}")