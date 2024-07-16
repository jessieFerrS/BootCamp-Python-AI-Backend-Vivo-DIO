def calculadora(operacao):
    def soma(a, b):
        return a + b

    def subtracao(a, b):
        return a - b

    def multiplicacao(a, b):
        return a + b

    def divisao(a, b):
        return a / b

    match operacao:
        case "+":
            return soma
        case "-":
            return subtracao
        case "*":
            return multiplicacao
        case "/":
            return divisao


print(calculadora("+")(2, 3))
print(calculadora("-")(9, 3))
print(calculadora("*")(2, 3))
print(int(calculadora("/")(12, 3)))
