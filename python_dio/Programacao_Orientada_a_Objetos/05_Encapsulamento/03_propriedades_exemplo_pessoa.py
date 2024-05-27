class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nacimento = ano_nascimento
        
    
    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nacimento 
    

pessoa = Pessoa("Rafael", 2005)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")