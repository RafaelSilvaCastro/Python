def meu_corador(funcao):
    def envelope():
        print("faz algo antes de executar")
        funcao()
        print("faz algo depois de executar")
        
    return envelope


def ola_mundo():
    print("Ola Mundo!")
    
    
ola_mundo = meu_corador(ola_mundo)
ola_mundo()