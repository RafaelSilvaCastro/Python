class Passaro:
    def voar(self):
        print("Voando...")
        
    
class Pardal(Passaro):
    def voar(self):
        super().voar()
    

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz nao pode voar")
        
        
class Aviao(Passaro):
    def voar(self):
        print("Avião esta decolando...")
    

def plano_voo(obj):
    obj.voar()
    
    

plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())