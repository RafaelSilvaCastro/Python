class Peassoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        
      
    @classmethod  
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        # print(cls)
        idade = 2024 - ano
        return cls(nome, idade)   
    
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
    
    
# p = Peassoa("Rafael", 19)
# print(p.nome, p.idade)

p = Peassoa.criar_apartir_data_nascimento(2005, 5, 19, "Rafael")
print(p.nome, p.idade)

print(Peassoa.e_maior_idade(18))
print(Peassoa.e_maior_idade(8))