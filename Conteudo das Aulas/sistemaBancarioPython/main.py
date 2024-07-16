menu = """
[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
def menu():
  """Exibe o menu principal do sistema."""
  print(menu)

def obter_valor(mensagem):
  """Obtém um valor float do usuário com base na mensagem informada."""
  while True:
    try:
      valor = float(input(mensagem))
      if valor > 0:
        return valor
      else:
        print("Valor inválido. Digite um valor positivo.")
    except ValueError:
      print("Valor inválido. Digite um número.")

def realizar_deposito():
  """Realiza a operação de depósito em conta."""
  valor_deposito = obter_valor("Informe o valor do Depósito: ")
  saldo += valor_deposito
  extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
  print("Depósito realizado com sucesso!")

def realizar_saque():
  """Realiza a operação de saque em conta."""
  valor_saque = obter_valor("Informe o valor do Saque: ")

  excedeu_saldo = valor_saque > saldo
  excedeu_limite = valor_saque > limite
  excedeu_saques = numero_saques >= LIMITE_SAQUES

  if excedeu_saldo:
    print("Operação falhou! Saldo insuficiente.")
  elif excedeu_limite:
    print("Operação falhou! Limite de saque excedido.")
  elif excedeu_saques:
    print("Operação falhou! Número máximo de saques por dia excedido.")
  elif valor_saque > 0:
    saldo -= valor_saque
    extrato += f"Saque: R$ {valor_saque:.2f}\n"
    numero_saques += 1
    print("Saque realizado com sucesso!")
  else:
    print("Operação falhou! Valor inválido.")

def mostrar_extrato():
  """Exibe o extrato da conta."""
  print("\n================ EXTRATO ================")
  print("Não foram realizadas movimentações." if not extrato else extrato)
  print(f"\nSaldo: R$ {saldo:.2f}")
  print("==========================================")


while True:
  mostrar_menu()
  opcao = input("=> ")

  if opcao == "1" or opcao == "d":
    realizar_deposito()
  elif opcao == "2" or opcao == "s":
    realizar_saque()
  elif opcao == "3" or opcao == "e":
    mostrar_extrato()
  elif opcao == "0" or opcao == "q":
    break
  else:
    print("Operação inválida. Digite novamente.")
