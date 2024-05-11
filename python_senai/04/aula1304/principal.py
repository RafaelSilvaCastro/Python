import revisao_funcoes


numero = int(input("Digite um numero para saber sua raiz quadrada: "))

calculoRaiz = revisao_funcoes.raizQuadrada(numero)

print(f"A raiz do numero {numero} e {calculoRaiz}")

primeira_nota = int(input('Digite a 1 nota do aluno: '))
segunda_nota = int(input('Digite a 2 nota do aluno: '))

media_nota = revisao_funcoes.mediaNotas(primeira_nota,segunda_nota)

print(f'A media de nota do aluno e {media_nota}')