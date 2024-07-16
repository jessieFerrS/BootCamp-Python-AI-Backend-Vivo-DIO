from abc import ABC, abstractmethod


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    # @abstractproperty -> depreciado usar no lugar @abstractmethod
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")
        print("LIGADA!")

    def desligar(self):
        print("Desligando a TV...")
        print("DESLIGADA!")

    @property
    def marca(self):
        return "LG"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o AR-CONDICIONADO...")
        print("LIGADO!")

    def desligar(self):
        print("Desligando o AR-CONDICIONADO...")
        print("DESLIGADO!")

    @property
    def marca(self):
        return "LG"

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)
print("--" * 30)
controle1 = ControleArCondicionado()
controle1.ligar()
controle1.desligar()
print(controle1.marca)
