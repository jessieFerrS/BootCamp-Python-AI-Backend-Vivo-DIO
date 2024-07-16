import textwrap

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


def depositar(saldo, valor, extrato, /):
    """Realiza deposito na conta"""
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\tR${valor:.2f}\n'
        print("\n*** Depósito Realizado com Sucesso!! ***")
    else:
        print("\n### Operação Falhou! O Valor informado é inválido! ###")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """Realizar saque da conta"""
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print(" Saque Falhou! Saldo Insuficiente!")

    elif excedeu_limite:
        print("Saque Falhou! Limite Execido!!!")

    elif excedeu_saques:
        print("Saque Falho! Número máximo de saques já foi atingido!")

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\t\tR$ {valor:.2f}\n'
        numero_saques += 1
        print("\n **** Saque realizado com sucesso!! ****")
    else:
        print("\n### Saque Falhou! O Valor informado é Inválido! ###")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    """Exibe o extrato bancario"""
    faixa('E X T R A T O')
    print("Não foram realizadas movimentações na conta até o momento." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print('-' * 40)

def criar_usuario(usuarios):
    """Cria o usuario/cliente da conta"""
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n Esse CPF já possui usuário cadastrado!! ")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print(" **** Usuário criado com sucesso! **** ")


def filtrar_usuarios(cpf, usuarios):
    """Exibe os usuarios da conta por CPF"""
    usuarios_filtrados = []
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuarios_filtrados.append(usuario)
    if usuarios_filtrados:
        return usuarios_filtrados[0]
    return None


def criar_conta_corrente(agencia, numero_conta, usuarios):
    """Cria a conta corrente com base em um CPF cadastrado"""
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n *** Conta criada com sucesso! *** ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    return f"\n ### Usuário não encontrado! Processo de Criação de conta falhou! ###"

def listar_contas(contas):
    """Exibe as contas cadastradas"""
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            Conta Corrente:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("-" * 100)
        print(textwrap.dedent(linha))

def main():
    """Função Principal"""
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:

        opcao = menu()

        if opcao == "1" or opcao == "d":
            valor = float(input("Informe o valor do Depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2" or opcao == "s":
            valor = float(input("Informe o valor do Saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3" or opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4" or opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "5" or opcao == "n":
            # numero_conta = len(contas) + 1
            conta = criar_conta_corrente(AGENCIA, numero_conta, usuarios)
            numero_conta += 1

            if conta:
                contas.append(conta)

        elif opcao == "6" or opcao == "l":
            listar_contas(contas)

        elif opcao == "0" or opcao == "q":
            break

        else:
            print("Opção inválida!! Favor selecionar uma opção válida!")


main()
