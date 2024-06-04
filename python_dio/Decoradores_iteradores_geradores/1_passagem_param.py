def mensagem(nome):
    print("executando nome")
    return f'Oi {nome}'

def mensagem_longa(nome):
    print('executando mensagem longa')
    return f'Ola tudo bem com voce {nome}'

def executar(funcao, nome):
    print("executando executar")
    return funcao(nome)

print(executar(mensagem, 'Rafael'))
print(executar(mensagem_longa, 'Rafael'))

