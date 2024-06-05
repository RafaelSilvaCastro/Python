def meu_decorador(funcao):
    def envelope(*args, **nwargs):
        print("faz algo antes de executar")
        resultado = funcao(*args, **nwargs)
        print("faz algo depois de executar")
        return resultado
    
    return envelope

@meu_decorador # açucar sintatico
def ola_mundo(nome):
    print(f"Ola Mundo {nome}")
    return nome.upper()
    
resultado = ola_mundo("Rafael")
print(resultado)