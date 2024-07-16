class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    # forma correta para acessar um metodo privado
    def mostrar_saldo(self):
        return self._saldo

conta = Conta("1234-5", 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())
