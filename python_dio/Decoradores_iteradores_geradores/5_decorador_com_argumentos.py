def meu_decorador(funcao):
    def envelope(*args, **nwargs):
        print("faz algo antes de executar")
        funcao(*args, **nwargs)
        print("faz algo depois de executar")
        
    return envelope

@meu_decorador # açucar sintatico
def ola_mundo(nome):
    print(f"Ola Mundo {nome}")
    
ola_mundo("Rafael")