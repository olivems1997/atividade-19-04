class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def freiar(self):
        print("")
    def acelerar(self):
        print("")
class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def abrir_porta(self):
        print('Abrir porta')
    
class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def empinar(self):
        print("Empinar...")
    
if __name__== '__main__':
    carro1 = Carro("Renault", "Sandeiro", "Prata")
    moto1 = Moto("Yamara", "XJ6", "600")
    print(f'Marca: {carro1.marca}\n Modelo: {carro1.modelo}\n Cor: {carro1.cor}')
    print(f'Marca: {moto1.marca}\n Modelo: {moto1.modelo}\n Cilindrda: {moto1.cilindrada}')
