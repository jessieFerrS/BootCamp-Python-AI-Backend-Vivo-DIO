class Bicicleta:
    def __init__(self, cor, modelo, ano, valor_bicicleta):
        """Metodo construtor"""
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor_bicicleta = valor_bicicleta

    def buzinar(self):
        print('Plim plim...')

    def parar(self):
        print("Parando a bicicleta...Bicicleta Parada!")

    def correr(self):
        print('Vrummmmmm....')

    def __str__(self):
        """Retorna todos os atributos da classe"""
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


bic = Bicicleta("Vermelha", "Caloi", 2022, 900)
bic.buzinar()
bic.correr()
bic.parar()
print(bic.__str__())
