class Cachorro:
    # constructo que inicia a classe, executado no inicio
    def __init__(self, nome, cor, acordado=True):
        print("Iniciando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        
    # destructor de destroi a execução do objeto, executado no final
    def __del__(self):
        print("Removendo a instancia da classe.")
        
    def falar(self):
        print("auau")
        

def criar_cachorro():
    dog = Cachorro("Luciano", "cinza", False)
    print(dog.nome)

        
dog = Cachorro("Caleri", "marrom")
dog.falar()

# forçar a parada de um objeto
del dog


criar_cachorro()