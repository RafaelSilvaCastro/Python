#usuario e senha 

usuario = 'root'
senha = 1234

usuario_digitado = input('Digite o nome de usuário: ')
senha_digitada = int(input('Digite a sua senha: '))

if usuario_digitado == usuario:
    print('Usuario correto')
    if senha_digitada == senha:
        print('Senha correta')
    else:
        print('Senha Incorreta')
else:
    print('Usuario Incorreto')