#medias ultilizando elif
#pedir duas notas para o usuario
#se media for maior que 6, aprovado
#se media for maior que 4, reprovado
#se media entre 4 e 5, recuperaçao

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2

if media > 6:
    print("Aprovado")
elif media < 4:
    print("Reprovado")
else:
    print("Recuperação")
