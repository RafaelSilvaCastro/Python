#exemplo listas
#criar lista com 4 nomes de alunos

alunos_python = ['Enzo','Raul','Jonathan','Pedro']

#exibir a lista corretamente
for aluno in alunos_python:
    print(aluno)
print(12*'-')

for alu in range(len(alunos_python)):
    print(alunos_python[alu])
print(12*'-')

curso_senai = ['Java','Python','Banco de Dados','JavaScript']
print(curso_senai[2][4])
print(12*'-')

nome_escola = 'Senai'
print(nome_escola[3])
print(12*'-')

#lista de lista
curso_python = [['aula 1','aula 2','aula 3','aula 4'],['Tipos de dados','Condicionais','Laços de repetição','Tuplas']]

print(f'Na {curso_python[0][0]} de python: aprendemos {curso_python[1][0]}')
print(12*'-')

#exibir as todas as aulas e o conteudo dado
for python in range(len(curso_python[0])):
        print(f'Na {curso_python[0][python]}, aprendemos {curso_python[1][python]}')

print(12*'-')