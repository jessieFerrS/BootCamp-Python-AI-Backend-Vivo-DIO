
def barrinha(texto):
    print("-" * 60)

    print(texto.center(60))

    print("-" * 60)


def menu():
    barrinha('Menu')

    opcao = '''1.Depositar

2.Sacar

3.Extrato

4.Criar Conta

5.Listar Contas

6.Novo Usuario

7.Finalizar

opcao ->'''

    return input(opcao)


def depositar(saldo, valor, extrato, /):
    if valor > 0:

        saldo += valor

        extrato += f"Depósito:\tR$ {valor:.2f}\n"

        print("Depósito realizado com sucesso!")

    else:

        print("Valor informado Inválido!")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:

        print("Você não tem saldo suficiente!")

    elif excedeu_limite:

        print("O valor do saque excede o limite!")

    elif excedeu_saques:

        print("Número máximo de saques excedido")

    elif valor > 0:

        saldo -= valor

        extrato += f"Saque:\t\tR$ {valor:.2f}\n"

        numero_saques += 1

        print("Saque realizado com sucesso!")

    else:

        print("Valor informado Inválido!")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    barrinha('Extrato')

    print("Não foram realizadas movimentações." if not extrato else extrato)

    print(f"\nSaldo:\t\tR$ {saldo:.2f}")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Usuário já cadastrado!")

        return

    nome = input("Informe o nome completo: ")

    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")

    endereco = input("Informe o endereço (logradouro, numero - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário Cadastrado com Sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]

    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")

        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado, Criação de conta encerrada!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\

            Agência:\t{conta['agencia']}

            C/C:\t\t{conta['numero_conta']}

            Titular:\t{conta['usuario']['nome']}

        """


def main():
    LIMITE_SAQUES = 3

    AGENCIA = "0001"

    saldo = 0

    limite = 500

    extrato = ""

    numero_saques = 0

    usuarios = []

    contas = []

    while True:

        opcao = menu()

        if opcao == "1":

            valor = float(input("Valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":

            valor = float(input("Valor do saque: "))

            saldo, extrato = sacar(

                saldo=saldo,

                valor=valor,

                extrato=extrato,

                limite=limite,

                numero_saques=numero_saques,

                limite_saques=LIMITE_SAQUES,

            )

        elif opcao == "3":

            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":

            criar_usuario(usuarios)

        elif opcao == "5":

            numero_conta = len(contas) + 1

            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":

            listar_contas(contas)

        elif opcao == "7":

            break

        else:

            print("Operação inválida, Selecione novamente a operação desejada.")


main()
