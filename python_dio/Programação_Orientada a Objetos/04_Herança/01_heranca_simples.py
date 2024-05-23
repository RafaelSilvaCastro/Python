class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        
    def ligar_motor(self):
        print("Ligando o motor")

# classes herdeiras
class Motocicleta(Veiculo):
    pass



class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    pass


moto = Motocicleta("preta", "abc-1234", 2)
print(moto)
