class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return self.cor


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, carregado, cor, placa, numero_rodas):
        super().__init__(cor, placa, numero_rodas)    # INVOCANDO O METODO CONSTRUTOR DA CLASSE PAI
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado!!")


print("----------- MOTO ---------------")
moto = Motocicleta("preta", "abc-1234", 2)
moto.ligar_motor()
print(moto)
print("--" * 20)
print("------------- CARRO ------------")
carro = Carro("cinza", "azd-985", 2)
carro.ligar_motor()
print(carro)
print("--" * 20)
print("---------- CAMINHAO -------------")
caminhao = Caminhao(True, "azul", "def-567", 2)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)
print("--" * 20)
