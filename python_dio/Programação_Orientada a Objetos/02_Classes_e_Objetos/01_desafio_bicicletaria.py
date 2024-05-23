# criando uma classe
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, marcha):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        # self.marcha = 1
        
    # metodos  
    def buzinar(self):
        print("Plim plim..")
        
    def parar(self):
        print("Parando bicicleta ...")
        print("Bicicleta parada!")
        
    def correr(self):
        print("Vruuummm ...")
        
    # def trocar_marcha(self, nro_marcha):
    #     print("Trocando marcha")
        
    #     def _trocar_marcha():
    #         if nro_marcha > self.marcha:
    #             print("Marcha trocada ...")
    #         else: 
    #             print("Não foi possivel trocar de marcha ...")
                
        
    # def get_cor(self):
    #    return self.cor
        
    # um jeito melhor de mostrar
    # def __str__(self):
    #     return f"Bicicleta: cor = {self.cor}, modelo = {self.modelo}, ano = {self.ano}, valor = {self.valor}"
    
    # jeito altomatico de mostrar
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
        
b1 = Bicicleta("azul", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2)
# b2.buzinar() # Bicicleta.buzinar(b2)

# print(b2.get_cor())
  
    