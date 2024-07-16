# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

    def fazer_chamada(self, destinatario, duracao):
        if not self.plano.verificar_saldo(duracao):
            print("Saldo insuficiente para fazer a chamada.")
            return

        custo = self.plano.custo_chamada(duracao)
        self.plano.deduzir_saldo(custo)

        print(f"Chamada para {destinatario} realizada com sucesso. Saldo: ${self.plano.saldo:.2f}")


    def custo_chamada(self):
        custo = duracao * 0.10
        return custo


class Plano:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def verificar_saldo(self, duracao):
        custo_estimado = duracao * 0.10  # Supondo $0.10 por minuto
        return self.saldo >= custo_estimado

    def custo_chamada(self, duracao):
        # A implementação deste método pode ser a mesma do método da classe UsuarioTelefone
        custo = duracao * 0.10  # Supondo $0.10 por minuto
        return custo

    def deduzir_saldo(self, valor):
        self.saldo -= valor


class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


# Recebendo as informações do usuário:
nome = input()
numero = input()
saldo_inicial = float(input())

# Criando um objeto UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)

# Recebendo o número de destino e a duração da chamada:
destinatario = input()
duracao = int(input())

# Chamando o método fazer_chamada e imprimindo o resultado:
usuario_pre_pago.fazer_chamada(destinatario, duracao)
