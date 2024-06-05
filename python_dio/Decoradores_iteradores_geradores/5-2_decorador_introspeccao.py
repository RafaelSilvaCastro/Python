import functools

def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **nwargs):
        funcao(*args, **nwargs)
    
    return envelope

@meu_decorador # açucar sintatico
def ola_mundo(nome):
    print(f"Ola Mundo {nome}")
    
print(ola_mundo.__name__)