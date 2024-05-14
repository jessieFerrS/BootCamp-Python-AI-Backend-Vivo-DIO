def faixa(texto):
    """Exibe uma faixa decorativa com texto centralizado"""
    print("-" * 40)
    print(texto.center(40))
    print("-" * 40)


def menu():
    """Exibe o menu principal do sistema."""
    faixa('M E N U  P R I N C I P A L')
    return (f'[1 ou d] Depositar\n'
            f'[2 ou s] Sacar\n'
            f'[3 ou e] Extrato\n'
            f'[0 ou q] Sair ')


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    print(menu())
    opcao = input("Opção: ")

    if opcao == "1" or opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2" or opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("A operação falhou! Saldo Insuficiente.")

        elif excedeu_limite:
            print("A operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("A operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3" or opcao == "e":
        faixa('E X T R A T O')
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print('-' * 40)

    elif opcao == "0" or opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
