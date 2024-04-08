#Crie um programa em Python que peça para o usuário três notas de um aluno, logo após o programa deve exibir a media do aluno e informar se o mesmo está reprovado ou aprovado. Para ser aprovado a media deve ser maior que 5.
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))


media = (nota1 + nota2 + nota3)/3

print("Sua media e: ",media)

if media > 5:
    print("Voce esta Aprovado")
else:
    print("Voce esta Reprovado")