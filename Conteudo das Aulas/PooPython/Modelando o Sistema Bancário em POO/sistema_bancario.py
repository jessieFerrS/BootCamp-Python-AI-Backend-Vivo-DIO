import textwrap
from abc import ABC, abstractmethod, abstractproperty, abstractclassmethod
from datetime import datetime

class Cliente:
    """ CLASSE CLIENTE """

    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        """ ADICIONA CONTA NA LISTA DE CONTAS """
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


class Conta:
    def __init__(self, numero_conta, cliente):
        self._saldo = 0
        self._numero_conta = numero_conta
        self._agencia = "1234-5"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero_conta):
        """ RETORNA UMA INSTANCIA DE CONTA """
        return cls(numero_conta, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero_conta(self):
        return self._numero_conta

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n*** Saldo Insuficiente!!! ***")

        elif valor > 0:
            self._saldo -= valor
            print("\n Saque realizado com sucesso!!!")
            return True

        else:
            print("\n*** Valor Inválido!!! Saque não permitido!! ***")
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n Depósito realizado com sucesso!!!")

        else:
            print("*** Valor Inválido!! Depósito Falhou!! ***")
            return False
        return True


class ContaCorrente(Conta):
    def __init__(self, numero_conta, cliente, limite=500, limite_saques=3):
        super().__init__(numero_conta, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n Valor excede o limite diário!!!")

        elif excedeu_saques:
            print("\n Limite máximo de saques atingido!!")

        else:
            return super().sacar(valor)
        return False

    def __str__(self):
        return f"""\
            Número da Agência: {self.agencia}
            Conta Corrente: {self.numero_conta}
            Titular da Conta: {self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            }
        )

class Transacao(ABC):
    """ CLASSE ABSTRATA """
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        transacao_valida = conta.sacar(self.valor)

        if transacao_valida:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

def faixa(texto):
    """Exibe uma faixa decorativa com texto centralizado"""
    print("-" * 40)
    print(texto.center(40))
    print("-" * 40)


def menu():
    """Exibe o menu principal do sistema."""
    faixa('M E N U  P R I N C I P A L')
    opcao = (f'[1 ou d] Depositar\n'
             f'[2 ou s] Sacar\n'
             f'[3 ou e] Extrato\n'
             f'[4 ou u] Novo Usuário\n'
             f'[5 ou n] Nova Conta\n'
             f'[6 ou l] Listar Contas\n'
             f'[0 ou q] Sair\n'
             f'Opção: ')
    return input(opcao)

def filtrar_clientes(cpf, clientes):
    """Exibe os usuarios da conta por CPF"""
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_corrente(cliente):
    if not cliente.contas:
        print("\n *** Cliente não possui conta! ***")
        return

    return cliente.contas[0]

def depositar(clientes):
    cpf = input("Informe o CPF do Titular da Conta: ")
    cliente = filtrar_clientes(cpf, clientes)

    if not clientes:
        print("\n*** Cliente não encontrado! ***")
        return

    valor = float(input("Informe o valor do Depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_corrente(cliente)
    if not conta:
        return "*** Não há conta a ser recuperada! ***"

    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Informe o CPF do Titular da Conta: ")
    cliente = filtrar_clientes(cpf, clientes)

    if not clientes:
        print("\n*** Cliente não encontrado! ***")
        return

    valor = float(input("Informe o valor do Saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_corrente(cliente)
    if not conta:
        return "*** Não há conta a ser recuperada! ***"

    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do Titular da Conta: ")
    cliente = filtrar_clientes(cpf, clientes)

    if not clientes:
        print("\n*** Cliente não encontrado! ***")
        return

    conta = recuperar_conta_corrente(cliente)
    if not conta:
        return "*** Não há conta a ser recuperada! ***"

    faixa("*** EXTRATO ***")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações até o momento!"
        return extrato
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}: \n\tR$ {transacao['valor']:.2f}"

        print(extrato)
        print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
        print("--" * 40)


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente números): ")
    cliente = filtrar_clientes(cpf, clientes)

    if cliente:
        print("\n*** CPF já Cadastrado!! ***")
        return

    nome = input("Informe o nome do Titular: ")
    data_nascimento = input("Informe a data de nascimento (DD-MM-AAAA): ")
    endereco = input("Informe o endereço(logradouro, numero - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n*** Cliente criado com sucesso! ***")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do Titular: ")
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print("\n*** Cliente não encontrado!! ***")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero_conta=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n*** Conta criada com sucesso! ***")

def listar_contas(contas):
    for conta in contas:
        print("--" * 40)
        print(textwrap.dedent(str(conta)))

def main():
    clientes = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "1" or opcao == "d":
            depositar(clientes)

        elif opcao == "2" or opcao == "s":
            sacar(clientes)

        elif opcao == "3" or opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "4" or opcao == "u":
            criar_cliente(clientes)

        elif opcao == "5" or opcao == "n":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "6" or opcao == "l":
            listar_contas(contas)

        elif opcao == "0" or opcao == "q":
            break

        else:
            print("Opção inválida!! Favor selecionar uma opção válida!")


main()
